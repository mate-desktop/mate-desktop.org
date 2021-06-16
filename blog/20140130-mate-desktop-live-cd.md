<!-- 
.. link: 
.. description: 
.. tags: LiveCD,Arch Linux,News
.. date: 2014/01/30 00:17:32
.. title: MATE desktop Live CD
.. slug: 2014-01-30-mate-desktop-live-cd
.. author: Martin Wimpress
-->

The MATE team have made a Live CD that boots into a full MATE desktop.

<div class="alert alert-info"><strong>Update</strong> The LiveCD was updated to MATE 1.8 on March 10th 2014.</div>

This Live CD was created so that potential new users can evaluate the MATE 
desktop in a non-destructive fashion. The image can be burned to a DVD, 
mounted as an ISO file, or be directly written to a USB stick using a utility 
like `dd`. [Linux Luddites](https://luddites.latenightlinux.com/) beware, `unetbootin` is
not supported. You can download it below:

### BitTorrent download (recommended)

If you can spare the bytes, please leave the client open after your download 
is finished, so you can seed it back to others. *A web-seed capable client is 
recommended for fastest download speeds.*

  * [matelivecd-14.069.1449.iso.torrent]

### HTTP direct download

In addition to the BitTorrent link above, the Live CD .iso can also be
downloaded via HTTP. Please ensure the downloaded file matches the SHA1
checksum.

  * [matelivecd-14.069.1449.iso] [ ~964MB ]
    * SHA1: `12b529d17d1ecef39d9b0e1122fb5271e0534c0a`

## Compatibility

The Live CD is built using [Arch Linux](https://www.archlinux.org) and MATE 
1.8. The Live CD is 32-bit so should work on any i686 or x86_64 computer
with at least 512MB RAM. Xorg drivers are included for Intel (`i915`),
AMD/ATI (`radeon`) and nvidia (`nouveau`) with a fall back to VESA.
Drivers for Virtual Box and VMware are also included so that evaluation
using these virtualization solutions is simple.

All common file systems, including [ZFS](http://open-zfs.org), are supported 
and some data recovery and backup tools are included. If you plug in your 
mobile device it will most likely be recognised and you'll be able to access 
the data on it. NetworkManager is included along with all the VPN clients it 
supports.

## Usernames and passwords

The MATE Desktop Live CD has the following accounts configured.

  * `root` - password is `livecd`.
  * `mate` - password is `livecd`.

The `root` account is obviously `root`. The `mate` account it a regular user 
that has with full password-less `sudo` rights. The Live CD will auto-login 
using the `mate` account.

## Applications

The Live CD is primarily designed to showcase the MATE desktop, however we've 
included some additional applications that are not part of the MATE desktop in 
order to make the LiveCD a little more useful and enjoyable.

  * [Firefox](https://www.mozilla.org/firefox/)   - Standalone web browser from mozilla.org
  * [GParted](https://gparted.sourceforge.io/)   - A Partition Magic clone, frontend to GNU Parted
  * [HardInfo](https://www.berlios.de/software/hardinfo/)  - A system information and benchmark tool
  * [HexChat](https://hexchat.github.io/)   - IRC client configured to auto-connect to [#mate@libera](https://web.libera.chat/?#mate)
  * [Onboard](https://www.gnome.org/projects/orca)      - Screen reader for individuals who are blind or visually impaired
  * [Orca](https://www.gnome.org/projects/orca)      - On-screen keyboard useful for mobility impaired individuals
  * [Pidgin](https://pidgin.im/)    - Multi-protocol instant messaging client
  * [Xnoise](http://www.xnoise-media-player.com/)    - Media player with a slick GUI, great speed and lots of features

## Creative Commons content

We have bundled the following Creative Commons licensed content.

  * [Think Python](https://www.greenteapress.com/thinkpython/)                        - To read with Atril

## Changing language

Be default the Live CD is configured to use the `en_US` locale but if you want 
to activate another language here is how to do it. In the example below, we 
will enable Italian.

Edit `/etc/locale.gen` an uncomment your locale, in this case `it_IT.UTF-8 UTF-8`
and rebuild the locales.

    sudo locale-gen

Edit `/etc/locale.conf` and change the `LANG=` to reflect your locale, in this 
case `LANG=it_IT.UTF-8`. Finally restart the display manager and you will be 
logged back into a MATE session using your prefered language.

    sudo systemctl restart lightdm

## Linux Action Show Feature

The MATE Desktop LiveCD and MATE itself we featured on the [Linux Action 
Show](https://www.jupiterbroadcasting.com/show/linuxactionshow/) in the [CuBox 
Linux Review](https://www.jupiterbroadcasting.com/50842/cubox-linux-review-las-s30e08/) 
episode. Two clips are embedded below, the first a quick look at the MATE 
Desktop LiveCD the second is a review of the CuBox i4 which is running MATE.

### MATE Desktop LiveCD

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=608" frameborder="0" allowfullscreen></iframe>

### CuBox i4 Pro Review

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=1925" frameborder="0" allowfullscreen></iframe>

## Feedback

We hope you give the Live CD a test drive and enjoy the speed and simplicity 
the MATE Desktop provides. Once you've taken the MATE Desktop Live CD for a 
spin let us know what you think in the comments or use the Live CD to join us 
in the [#mate IRC channel](https://webchat.freenode.net/?channels=#mate).

