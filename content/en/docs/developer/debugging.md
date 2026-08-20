---
title: Debugging
weight: 7
---

## GLib logging

GLib provides a family of logging macros. Prefer these over `printf` — they respect log level filters and can be redirected:

| Macro | When to use |
|-------|-------------|
| `g_debug ("...")` | Verbose tracing, disabled in release builds |
| `g_message ("...")` | General informational messages |
| `g_warning ("...")` | Recoverable problems |
| `g_critical ("...")` | Programming errors (wrong API usage) |
| `g_error ("...")` | Fatal, unrecoverable — aborts the program |

Control which levels are printed:

```bash
G_MESSAGES_DEBUG=all ./my-mate-app          # all levels including debug
G_MESSAGES_DEBUG=MyApp ./my-mate-app        # debug for a specific domain only
```

Set the log domain at the top of each source file:

```c
#define G_LOG_DOMAIN "MyApp"
```

Turn warnings and criticals into hard crashes during development to catch them early:

```bash
G_DEBUG=fatal-warnings ./my-mate-app
```

## GDB

Build with debug symbols first:

```bash
./autogen.sh --prefix=/usr CFLAGS="-g -O0"
make
```

Then run under GDB:

```bash
gdb ./src/my-mate-app
(gdb) run
# After a crash:
(gdb) backtrace
(gdb) frame 3
(gdb) print variable_name
```

### GLib/GObject helpers for GDB

Load the GLib pretty-printers to display GLib types readably:

```
# In GDB or ~/.gdbinit:
python
import sys
sys.path.insert(0, '/usr/share/glib-2.0/gdb')
import glib_gobject_helper
end
```

After loading, `print` on a `GObject *` shows its type name and ref count.

Useful GDB commands for GObject code:

```
(gdb) call g_type_name(G_TYPE_FROM_INSTANCE(obj))
(gdb) call g_object_get_data(obj, "key")
(gdb) watch obj->ref_count
```

### Catching GLib criticals

```
(gdb) break g_log_default_handler
(gdb) run
```

This stops execution at every `g_warning` / `g_critical`, letting you inspect the call stack.

## GTK Inspector

GTK Inspector is an interactive debugger built into GTK 3. Launch it with:

```bash
GTK_DEBUG=interactive ./my-mate-app
```

Or press **Ctrl+Shift+I** inside a running app. Capabilities:

- **Widget tree** — browse and select any live widget to see its properties and CSS
- **CSS editor** — write and preview CSS changes immediately
- **Signal recorder** — log every signal emission
- **Object statistics** — count live GObject instances by type (useful for leak hunting)

## Valgrind — memory leak detection

{{< callout type="info" >}}
Build with `-g -O0` before running Valgrind. Optimisation inlines code and makes traces hard to read.
{{< /callout >}}

```bash
valgrind --leak-check=full \
         --show-leak-kinds=definite,indirect \
         --num-callers=30 \
         ./src/my-mate-app
```

Suppress known GLib/GTK false positives:

```bash
valgrind --suppressions=/usr/share/glib-2.0/valgrind/glib.supp \
         --leak-check=full ./src/my-mate-app
```

Key output to look for:

- **definitely lost** — real leaks you own
- **indirectly lost** — leaked through a pointer in a directly-lost block
- **still reachable** — held in globals at exit (often intentional in GTK apps)

## AddressSanitizer (ASan)

Faster than Valgrind for catching heap corruption, use-after-free, and buffer overflows:

```bash
./autogen.sh --prefix=/usr CFLAGS="-g -O1 -fsanitize=address" \
             LDFLAGS="-fsanitize=address"
make
./src/my-mate-app
```

ASan reports are printed to stderr with a full stack trace.

## Core dumps

```bash
ulimit -c unlimited
./src/my-mate-app          # let it crash
gdb ./src/my-mate-app core
(gdb) backtrace
```

On systems using systemd-coredump:

```bash
coredumpctl list
coredumpctl gdb my-mate-app
```

## Environment variable reference

| Variable | Effect |
|----------|--------|
| `G_DEBUG=fatal-warnings` | Crash on `g_warning` / `g_critical` |
| `G_MESSAGES_DEBUG=all` | Show all `g_debug` output |
| `G_MESSAGES_DEBUG=<domain>` | Show debug for one log domain |
| `GTK_DEBUG=interactive` | Open GTK Inspector on startup |
| `GTK_DEBUG=geometry` | Log window geometry changes |
| `GTK_THEME=Adwaita` | Force a specific GTK theme |
| `GOBJECT_DEBUG=instance-count` | Print live GObject counts on exit |
| `MALLOC_CHECK_=3` | Glibc heap consistency checking |
