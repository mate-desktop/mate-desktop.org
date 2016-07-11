<!-- 
.. link: 
.. description: MATE Desktop collaborates with Blueman project.
.. tags: Blueman,BlueZ,Bluetooth,News
.. date: 2014/03/11 07:45:00
.. title: MATE Desktop singing the BlueZ
.. slug: 2014-03-11-mate-desktop-singing-the-bluez
.. author: Martin Wimpress
-->

The MATE team are delighted to announce that we are collaborating with the
[Blueman project](https://github.com/blueman-project/blueman) and helping to
update Blueman to BlueZ 5.x.

## Why ditch mate-bluetooth?

`mate-bluetooth` supports BlueZ 4.x which has been discontinued and many
distributions have, or are about to, replace BlueZ 4.x with BlueZ 5.x in their
respective package repositories. Migrating `mate-bluetooth` to BlueZ 5.x was
shaping up to be a lot of work and doesn't provide the range of features
available in Blueman.

## Why Blueman? Isn't it dead?

While the original Blueman project has stagnated, [Christopher Schramm](https://github.com/cschramm)
has reignited the development and started porting Blueman to BlueZ 5.x. While
there is also some effort in updating Blueman to support BlueZ 5.x we feel it
will provide a far better Bluetooth interface for MATE.

## When will the updated Blueman be ready?

The observant among you may have noticed that the [MATE 1.8 release announcement](/blog/2014-03-04-mate-1-8-released/)
already mentioned that `mate-bluetooth` has been replaced with Blueman and the
even more observant will also have noticed that a fresh version of Blueman has
not yet been released. Yeah, we suck! Sorry about that.

While we acknowledge that we suck, we are actively contributing to the effort of
porting Blueman to BlueZ 5.x and GObject introspection. We are hoping to have it
ready in time for MATE 1.8.1 which is primarily intended as a bug fix
release.

## Can't you do it faster, damn it?!

Yes. Anyone familiar with BlueZ 4.x/5.x, dbus, PyGObject and PyGTK is encouraged
to contribute via the [Blueman GitHub repository](https://github.com/blueman-project/blueman).
