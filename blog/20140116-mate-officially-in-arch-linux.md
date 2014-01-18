<!-- 
.. link: 
.. description: 
.. tags: Arch Linux,Raspberry Pi,News
.. date: 2014/01/16 22:22:22
.. title: MATE is officially available in Arch Linux
.. slug: 2014-01-16-mate-officially-in-arch-linux
.. author: Martin Wimpress
-->

MATE has finally found it's way home.

As some of you may know MATE was created by an [Arch Linux](http://www.archlinux.org)
user, Perberos. It is somewhat ironic then that MATE has never featured
in the official Arch Linux package repository until now. That's right,
MATE is finally available in the Arch Linux `[community]` package
repository!

You can find out everything you need to know about installing MATE
on Arch Linux from the following wiki pages:

  * <http://wiki.mate-desktop.org/archlinux_custom_repo>
  * <https://wiki.archlinux.org/index.php/MATE>  

It is also worth noting that the now obsolete unofficial MATE package
repository will be removed once all the Arch Linux mirrors are synced.
So go and update `/etc/pacman.conf` and remove the `[mate]` package
repository.

The other advantage of getting MATE into the official Arch Linux package
repository is that MATE will now also feature in the [Arch Linux ARM](http://archlinuxarm.org/)
package repository. I can finally retire my Raspberry Pi (armv6h) and
Cubox Pro (armv7h) build *"servers"*. I'm not sure how long it will take
for all the MATE packages to appear in the Arch Linux ARM package
repository but I have already seen that some packages are built.

MATE runs really well on the Raspberry Pi Model B with 512MB RAM, so if
you have a Pi and a spare SDCARD, give it a whirl. I'll be writing a
blog post about how install Arch Linux and MATE on the Raspberry Pi with
some useful performance tweaks in the near future.

<div class="alert alert-success">
<strong>Discussion</strong> <a href="http://forums.mate-desktop.org/viewtopic.php?f=20&t=2904" class="alert-link">Comments</a>
</div>
