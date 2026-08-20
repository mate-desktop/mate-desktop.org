---
title: GTK Development
weight: 5
---

MATE uses **GTK 3**. GTK builds on top of GObject and GLib — make sure you have read [C, GLib & GObject](../c-and-gobject) first.

## Widget hierarchy

Every visible element is a `GtkWidget`. Widgets are arranged in a tree: container widgets (boxes, grids, notebooks) hold child widgets. The root of the tree is always a `GtkWindow` (or a subclass like `GtkApplicationWindow`).

```
GtkWindow
  └─ GtkBox (vertical)
       ├─ GtkMenuBar
       ├─ GtkScrolledWindow
       │    └─ GtkTreeView
       └─ GtkStatusBar
```

## Building UI with GtkBuilder

Rather than constructing widgets in C, MATE components often define their UI in `.ui` XML files processed by GtkBuilder:

```xml
<!-- my-window.ui -->
<interface>
  <object class="GtkWindow" id="main_window">
    <property name="title">My App</property>
    <child>
      <object class="GtkButton" id="ok_button">
        <property name="label">OK</property>
        <signal name="clicked" handler="on_ok_clicked"/>
      </object>
    </child>
  </object>
</interface>
```

Load it in C:

```c
GtkBuilder *builder = gtk_builder_new_from_file ("my-window.ui");
GtkWidget  *window  = GTK_WIDGET (gtk_builder_get_object (builder, "main_window"));
gtk_builder_connect_signals (builder, NULL);
g_object_unref (builder);
```

Use [Glade](https://glade.gnome.org/) to edit `.ui` files visually.

## Signals and callbacks

GTK signals follow the same GObject mechanism. The callback signature must match the signal:

```c
static void
on_button_clicked (GtkButton *button, gpointer user_data)
{
    MyWindow *win = MY_WINDOW (user_data);
    /* ... */
}

g_signal_connect (button, "clicked", G_CALLBACK (on_button_clicked), win);
```

A common pattern to avoid signal feedback loops:

```c
g_signal_handlers_block_by_func (widget, handler, data);
gtk_toggle_button_set_active (...);
g_signal_handlers_unblock_by_func (widget, handler, data);
```

## GtkAction and menus

Most existing MATE components use the older `GtkUIManager` + `GtkActionGroup` menu system. New code should prefer `GAction` + `GMenu`:

```c
/* GAction (modern) */
GSimpleAction *action = g_simple_action_new ("quit", NULL);
g_signal_connect (action, "activate", G_CALLBACK (quit_cb), app);
g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (action));
```

Menu XML for GMenu:

```xml
<menu id="app-menu">
  <section>
    <item>
      <attribute name="label">Quit</attribute>
      <attribute name="action">app.quit</attribute>
    </item>
  </section>
</menu>
```

## CSS theming

GTK 3 uses CSS for theming. You can apply custom CSS in code — useful when experimenting with widget appearance:

```c
GtkCssProvider *provider = gtk_css_provider_new ();
gtk_css_provider_load_from_data (provider,
    "button { background: red; }", -1, NULL);
gtk_style_context_add_provider_for_screen (
    gdk_screen_get_default (),
    GTK_STYLE_PROVIDER (provider),
    GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);
```

To inspect and live-edit CSS on a running app, use the [GTK Inspector](../debugging#gtk-inspector).

## Useful patterns

**Idle callbacks** — run code after the current event is processed:

```c
g_idle_add ((GSourceFunc) my_idle_func, data);
```

**Timeouts:**

```c
g_timeout_add (500, (GSourceFunc) my_timeout_cb, data);  /* ms */
```

**Accessing the display:**

```c
GdkDisplay *display = gdk_display_get_default ();
GdkScreen  *screen  = gdk_display_get_default_screen (display);
```

## Further reading

- [GTK 3 Reference](https://docs.gtk.org/gtk3/)
- [GTK Tutorial (C)](https://docs.gtk.org/gtk3/getting_started.html)
- [GNOME HIG 2.2.1](https://mbkma.github.io/gnome-2-hig-book/)