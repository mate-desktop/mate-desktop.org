---
title: Panel Applets
weight: 10
---

The MATE panel hosts small interactive widgets called **applets** — the clock, workspace switcher, notification area, volume control, and so on. Understanding the architecture of applets is essential for writing or debugging them.

## In-process vs out-of-process applets

MATE panel supports two execution models for applets. The choice has significant implications for both stability and development workflow.

### In-process applets

An **in-process** applet is loaded as a shared library (`.so`) directly into the panel process. The applet code runs in the same address space as the panel itself.

```
┌──────────────────────────────────────────────┐
│  mate-panel (process)                         │
│                                               │
│  ┌────────────┐  ┌────────────┐  ┌─────────┐ │
│  │  Clock     │  │  Workspace │  │  My     │ │
│  │  applet.so │  │  applet.so │  │  applet │ │
│  └────────────┘  └────────────┘  └─────────┘ │
└──────────────────────────────────────────────┘
```

**Advantages:**
- Lowest overhead — no inter-process communication
- Direct access to the panel's GDK/GTK context
- Fastest rendering

**Drawbacks:**
- A crash or memory corruption in the applet **takes down the entire panel**
- Harder to restart without killing the panel
- Symbol conflicts between applets loaded into the same process

In-process loading is controlled by the `--oaf-activate-iid` activation flags. In practice, almost no modern MATE applet uses this mode — it is kept for legacy compatibility.

### Out-of-process applets

An **out-of-process** applet runs in a **separate child process**. It communicates with the panel over **D-Bus** using the `org.mate.panel.applet` interface. The applet creates a `MateApplet` widget, which the panel then **socket-embeds** into its own window using GTK's `GtkSocket`/`GtkPlug` mechanism.

```
┌─────────────────────┐          D-Bus          ┌───────────────────────┐
│  mate-panel         │ ◄────────────────────── │  my-applet (process)  │
│                     │   factory activation &  │                       │
│  ┌───────────────┐  │   widget embedding      │  MateApplet widget    │
│  │ GtkSocket     │◄─┼─────────────────────────┼─ GtkPlug              │
│  │ (plug area)   │  │   XEmbed protocol       │                       │
└──┴───────────────┴──┘                          └───────────────────────┘
```

**Advantages:**
- Crash isolation — if the applet dies, the panel restarts it automatically
- Independent restart and update of individual applets
- Memory leaks in the applet don't grow the panel's footprint indefinitely
- Easier to debug (attach GDB to just the applet process)

**Drawbacks:**
- Slightly higher latency for rendering (XEmbed round-trips)
- More boilerplate: D-Bus activation, factory binary, `.service` file

All first-party MATE applets (clock, workspace switcher, window list, etc.) run out-of-process. This is the **recommended model** for any new applet.

## Applet definition files

Two metadata files describe an out-of-process applet to the panel.

### `.mate-panel-applet` file

Lives in `$PREFIX/share/mate-panel/applets/`. Describes the applet identity to the panel's applet browser:

```ini
[Applet Factory]
Id=MyAppletFactory
InProcess=false
Location=/usr/local/lib/mate-panel/applets/my-applet
Name=My Applet Factory
Description=Factory for My Applet

[Applet]
Id=MyApplet
Factory=MyAppletFactory
Name=My Applet
Description=A sample MATE panel applet
Icon=my-applet-icon
```

`Location` is the path to the **factory executable** — the binary that is launched when the panel needs a new instance of this applet.

### D-Bus service file

Lives in `$PREFIX/share/dbus-1/services/`. Allows D-Bus to auto-start the factory when the panel requests an applet:

```ini
[D-BUS Service]
Name=org.mate.panel.applet.MyAppletFactory
Exec=/usr/local/lib/mate-panel/applets/my-applet
```

The `Name` must match the factory ID prefixed with `org.mate.panel.applet.`.

{{< callout type="warning" >}}
When installing into a custom prefix (`/usr/local`), D-Bus only searches for service files in `/usr/share/dbus-1/services/` by default. You must either install there or set `DBUS_SESSION_BUS_ADDRESS` / add the prefix to D-Bus's service search path:

```bash
export XDG_DATA_DIRS="/usr/local/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
```

The session D-Bus daemon uses `XDG_DATA_DIRS` to build its service search list.
{{< /callout >}}

## Minimal applet example (C)

```c
#include <mate-panel-applet.h>

static gboolean
my_applet_factory (MatePanelApplet *applet,
                   const gchar     *iid,
                   gpointer         data)
{
    GtkWidget *label;

    if (g_strcmp0 (iid, "MyApplet") != 0)
        return FALSE;

    label = gtk_label_new ("Hello, MATE!");
    gtk_container_add (GTK_CONTAINER (applet), label);
    gtk_widget_show_all (GTK_WIDGET (applet));

    return TRUE;
}

MATE_PANEL_APPLET_OUT_PROCESS_FACTORY (
    "MyAppletFactory",
    PANEL_TYPE_APPLET,
    my_applet_factory,
    NULL
)
```

`MATE_PANEL_APPLET_OUT_PROCESS_FACTORY` expands into a `main()` function that:
1. Registers the D-Bus factory service
2. Waits for the panel to call `CreateApplet`
3. Your callback is invoked; populate the `MatePanelApplet` widget and return `TRUE`

Compile and link against the panel applet library:

```bash
gcc -o my-applet my-applet.c \
    $(pkg-config --cflags --libs libmatepanelapplet-4.0 gtk+-3.0)
```

Check the library is available:

```bash
pkg-config --modversion libmatepanelapplet-4.0
```

## Debugging an out-of-process applet

Because the factory runs in a separate process you can attach GDB to it independently:

```bash
# Find the running applet process
pgrep -a my-applet

# Attach GDB
gdb -p $(pgrep my-applet)
(gdb) continue
```

Or run the factory manually so GDB starts it from scratch — useful before the applet has been added to the panel:

```bash
gdb /usr/local/lib/mate-panel/applets/my-applet
(gdb) run --oaf-activate-iid=OAFIID:MyAppletFactory
```

Enable verbose GLib/GObject logging:

```bash
G_MESSAGES_DEBUG=all /usr/local/lib/mate-panel/applets/my-applet
```

To force the panel to reload an applet without restarting the whole panel:

1. Right-click the applet → **Remove from Panel**
2. Right-click the panel → **Add to Panel** → find your applet
3. The factory process is re-launched automatically

## Checking applet registration

```bash
# Is the .mate-panel-applet file installed?
ls /usr/local/share/mate-panel/applets/

# Is the D-Bus service file installed?
ls /usr/local/share/dbus-1/services/ | grep MyApplet

# Can D-Bus see the service?
dbus-send --session --print-reply \
    --dest=org.freedesktop.DBus \
    /org/freedesktop/DBus \
    org.freedesktop.DBus.ListActivatableNames | grep MyApplet
```

## Further reading

- [libmatepanelapplet-4.0 API](https://github.com/mate-desktop/mate-panel/tree/master/libmate-panel-applet) — source of the applet library
- [mate-applets](https://github.com/mate-desktop/mate-applets) — reference implementations of all first-party applets
- GTK `GtkSocket` / `GtkPlug` documentation for the XEmbed embedding mechanism
