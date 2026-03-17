#!/usr/bin/env python3
import re
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path("content")  # Hugo content root

# regex to fix glued URLs
url_glue_pattern = re.compile(r'(\S)(https?://)')

# match Nikola comment block at top
nikola_block_pattern = re.compile(r'^<!--\s*(.*?)\s*-->\s*', re.DOTALL)

# match Nikola metadata fields
field_pattern = re.compile(r'\.\.\s*(\w+):\s*(.*)')

def parse_date_to_rfc3339(date_str):
    """Convert Nikola date strings to RFC3339 for Hugo"""
    if not date_str:
        return ""
    # remove UTC if present
    date_clean = date_str.replace(" UTC", "").strip()
    # normalize slashes to dashes
    date_clean = date_clean.replace("/", "-")
    formats = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]  # datetime, or date-only
    for fmt in formats:
        try:
            dt = datetime.strptime(date_clean, fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue
    print(f"⚠️  Could not parse date: {date_str}")
    return ""

def convert_nikola_to_hugo(meta_text):
    data = {}
    for line in meta_text.splitlines():
        m = field_pattern.match(line.strip())
        if m:
            key = m.group(1).lower()
            value = m.group(2).strip()
            data[key] = value

    title = data.get("title", "")
    date = parse_date_to_rfc3339(data.get("date", ""))
    slug = data.get("slug", "")
    tags = data.get("tags", "")
    author = data.get("author", "")
    description = data.get("description", "")

    toml = ["+++"]
    if title:
        toml.append(f'title = "{title}"')
    if date:
        toml.append(f'date = "{date}"')
    if slug:
        toml.append(f'slug = "{slug}"')
    if tags:
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        if tag_list:
            toml.append("tags = [" + ", ".join(f'"{t}"' for t in tag_list) + "]")
    if author:
        toml.append(f'author = "{author}"')
    if description:
        toml.append(f'description = "{description}"')
    toml.append("+++")
    toml.append("")
    return "\n".join(toml)

def process_files(reset=False):
    changed = []

    for md in ROOT.rglob("*.md"):
        backup = md.with_suffix(md.suffix + ".bak")

        if reset:
            if backup.exists():
                if md.exists():
                    md.unlink()
                backup.rename(md)
                changed.append(md)
            continue

        text = md.read_text(encoding="utf-8")
        original = text

        # fix glued URLs
        text = url_glue_pattern.sub(r'\1 \2', text)

        # convert Nikola metadata at top
        m = nikola_block_pattern.match(text)
        if m:
            hugo = convert_nikola_to_hugo(m.group(1))
            if hugo:
                text = hugo + text[m.end():]

        if text != original:
            backup.write_text(original, encoding="utf-8")
            md.write_text(text, encoding="utf-8")
            changed.append(md)

    if not changed:
        print("✅ nothing changed")
    else:
        if reset:
            print("✅ restored files from backup:")
        else:
            print("✅ fixed files (backups saved as *.bak):")
        for f in changed:
            print("  ", f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fix Hugo content and Nikola metadata")
    parser.add_argument("--reset", action="store_true", help="Restore files from .bak and delete modified files")
    args = parser.parse_args()
    process_files(reset=args.reset)