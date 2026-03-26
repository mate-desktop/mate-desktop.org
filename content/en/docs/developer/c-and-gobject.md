---
title: C, GLib & GObject
weight: 4
---

MATE is written almost entirely in C using [GLib](https://docs.gtk.org/glib/) and the [GObject type system](https://docs.gtk.org/gobject/). Understanding these layers is the most important step to reading and writing MATE source code.

## GLib fundamental types

GLib defines portable types you will see everywhere:

| GLib type   | C equivalent    | Notes                          |
|-------------|-----------------|--------------------------------|
| `gint`      | `int`           |                                |
| `guint`     | `unsigned int`  |                                |
| `gboolean`  | `int`           | use `TRUE` / `FALSE`           |
| `gchar`     | `char`          |                                |
| `gpointer`  | `void *`        | generic pointer                |
| `gsize`     | `size_t`        | unsigned                       |
| `gssize`    | `ssize_t`       | signed                         |

Prefer GLib types in code that interfaces with GLib/GTK APIs.

## Memory management

GLib provides its own allocator that aborts on failure — no NULL-check boilerplate needed:

```c
gchar *buf = g_malloc (size);
gchar *str = g_strdup ("hello");
g_free (buf);
g_free (str);
```

String utilities worth knowing:

```c
gchar *s = g_strdup_printf ("value = %d", n);
gchar *joined = g_strjoin (", ", "a", "b", "c", NULL);
g_free (s);
g_free (joined);
```

## GObject type system

Every MATE widget and object is a GObject. The minimal boilerplate for a new type uses the convenience macro:

```c
/* In the header (.h) */
G_DECLARE_FINAL_TYPE (MyObject, my_object, MY, OBJECT, GObject)

/* In the source (.c) */
G_DEFINE_TYPE (MyObject, my_object, G_TYPE_OBJECT)

static void
my_object_class_init (MyObjectClass *klass)
{
}

static void
my_object_init (MyObject *self)
{
}
```

`G_DECLARE_FINAL_TYPE` generates the cast macros (`MY_OBJECT()`), the instance/class struct forward declarations, and the `_get_type()` function declaration.

Use `G_DECLARE_DERIVABLE_TYPE` when the type needs to be subclassed.

## Reference counting

GObject uses reference counting. Every `g_object_new()` starts with a ref-count of 1:

```c
MyObject *obj = g_object_new (MY_TYPE_OBJECT, NULL);
g_object_ref (obj);    /* increment */
g_object_unref (obj);  /* decrement — frees when it reaches 0 */
```

`g_clear_object (&obj)` unrefs and sets the pointer to NULL — use this in `dispose` vfuncs and cleanup paths.

## Signals

Signals let objects emit events that other objects can respond to:

```c
/* Connecting to a signal */
g_signal_connect (widget, "clicked", G_CALLBACK (on_clicked), user_data);

/* Disconnecting */
g_signal_handlers_disconnect_by_func (widget, on_clicked, user_data);
```

Define a custom signal in `class_init`:

```c
static guint signals[N_SIGNALS];

signals[SIGNAL_CHANGED] =
    g_signal_new ("changed",
                  G_TYPE_FROM_CLASS (klass),
                  G_SIGNAL_RUN_LAST,
                  0, NULL, NULL,
                  NULL,
                  G_TYPE_NONE, 0);
```

Emit it:

```c
g_signal_emit (self, signals[SIGNAL_CHANGED], 0);
```

## Properties

Properties expose object state through a standard get/set interface used by data binding and GObject introspection:

```c
/* In class_init */
g_object_class_install_property (
    G_OBJECT_CLASS (klass),
    PROP_LABEL,
    g_param_spec_string ("label", "Label", "The label text",
                         NULL,
                         G_PARAM_READWRITE | G_PARAM_STATIC_STRINGS));
```

Implement `get_property` and `set_property` vfuncs on the class.

## Error handling with GError

Functions that can fail take a `GError **` output parameter:

```c
GError *error = NULL;
if (!do_something (&error)) {
    g_warning ("Failed: %s", error->message);
    g_error_free (error);
    return;
}
```

Never pass an already-set `GError **` to a function — always start with NULL.

## Containers

| Type         | Description                        |
|--------------|------------------------------------|
| `GList`      | doubly linked list                 |
| `GSList`     | singly linked list                 |
| `GPtrArray`  | dynamic array of pointers          |
| `GHashTable` | hash map (any key/value types)     |
| `GArray`     | dynamic array of fixed-size items  |

```c
GList *list = NULL;
list = g_list_append (list, item);
g_list_free (list);         /* free list only */
g_list_free_full (list, g_object_unref);  /* free list + items */
```

## Inspecting GObject types at runtime

To find the registered type name of any live object:

```c
g_print ("%s\n", G_OBJECT_TYPE_NAME (obj));
```

From GDB:

```
(gdb) call g_type_name(G_TYPE_FROM_INSTANCE(obj))
```

To list all GTypes registered during a run:

```bash
GOBJECT_DEBUG=instance-count ./my-mate-app
```

## Further reading

- [GLib Reference Manual](https://docs.gtk.org/glib/)
- [GObject Reference Manual](https://docs.gtk.org/gobject/)
- [GObject Tutorial](https://docs.gtk.org/gobject/tutorial.html)
