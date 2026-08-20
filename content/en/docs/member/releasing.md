---
title: Releasing a New Version
weight: 20
---

This guide covers cutting a release for any single MATE component (e.g. `atril`, `caja`, `mate-panel`). A MATE release cycle typically bumps all components at once; run through this checklist for each repository.

{{< callout type="warning" >}}
**Do not release unilaterally.** All releases must go through a pull request so other MATE members can review the version bump and `NEWS` entry before the tag is pushed. Open a PR, wait for at least one approval, then merge and tag. Pushing a tag directly to `master` without team agreement is not acceptable.
{{< /callout >}}

## Prerequisites

- Commit access to the repository on GitHub.
- A local clone of the repository on the `master` branch (or the release branch if one exists), fully up to date.
- The repository builds cleanly and all tests pass.

```bash
git checkout master
git pull --ff-only
make -j$(nproc) && make -j$(nproc) check
```

## 1. Decide the version number

MATE follows a `MAJOR.MINOR.MICRO` scheme:

| Segment | When it changes |
|---------|-----------------|
| `MAJOR` | Significant architectural changes (rare) |
| `MINOR` | New feature cycle (e.g. 1.28 -> 1.30) |
| `MICRO` | Bug-fix / maintenance release (e.g. 1.28.0 -> 1.28.1) |

Even `MINOR` numbers (1.28, 1.30 ...) are stable releases; odd numbers (1.27, 1.29 ...) are development snapshots.

## 2. Update the version in the build files

{{< tabs >}}
  {{< tab name="Autotools" >}}
Open `configure.ac` and change the version in the `AC_INIT` line:

```diff
-AC_INIT([atril], [1.28.1], [https://github.com/mate-desktop/atril/issues])
+AC_INIT([atril], [1.28.2], [https://github.com/mate-desktop/atril/issues])
```
  {{< /tab >}}
  {{< tab name="Meson" >}}
Open `meson.build` and change the `version:` field in the top-level `project()` call:

```diff
-project('atril', ['c', 'cpp'], version: '1.28.1', ...)
+project('atril', ['c', 'cpp'], version: '1.28.2', ...)
```
  {{< /tab >}}
{{< /tabs >}}

## 3. Update the `NEWS` file

Add a new section at the top of `NEWS` for the release. Follow the existing format used in the file. Mention:

- Fixed bugs (reference GitHub issue numbers where possible).
- New features (minor releases only).
- Translation updates.

```
### atril 1.28.2

  * Fix crash when saving a signed PDF (gh#123)
  * Several translation updates
```

## 4. Commit the version bump

Push the branch and open a pull request against `master`:

```bash
git checkout -b release/1.28.2
git add configure.ac NEWS        # adjust for meson.build if needed
git commit -m "Release 1.28.2"
git push origin release/1.28.2
```

Do **not** squash this commit with anything else - it should stand alone so the tag points to a clean, identifiable state.

Then open the PR on GitHub (the push output will print a direct URL). In the PR description include:

- The highlights from your `NEWS` entry.
- A note on what changed since the previous release (link to the compare URL: `https://github.com/mate-desktop/<repo>/compare/v1.28.1...release/1.28.2`).

Wait for **at least one approval** from another MATE member before merging.

## 5. Merge and tag the release

Once the PR is approved and merged, pull the updated `master` and create an annotated tag. The tag **must** start with `v` - this is what triggers the release workflow.

```bash
git checkout master
git pull --ff-only
git tag -a "v1.28.2" -m "Release 1.28.2"
```

{{< callout type="warning" >}}
Double-check the tag name before pushing. Correcting a pushed tag requires deleting it on GitHub and re-running the release workflow.
{{< /callout >}}

## 6. Push the tag - this triggers the automated release

```bash
git push origin "v1.28.2"
```

Pushing a `v*.*.*` tag starts the **Release Version** workflow, which:

1. Installs build dependencies.
2. Builds the source and runs `make distcheck` to produce a `.tar.xz` tarball.
3. Creates a GitHub release named after the tag, attaches the tarball, and auto-generates release notes from merged pull requests and commits since the previous tag.

Monitor the workflow run under **Actions** in the repository. If it fails, fix the problem, delete the tag locally and from GitHub, then re-tag after the fix.

## 7. Announce the release

- Post on the [MATE Desktop blog](https://mate-desktop.org/blog/) for minor (feature) releases.
- For micro (bug-fix) releases a short note on the [community channels](/community) is sufficient.
- Update the [download page](/download) if the stable version number changes.