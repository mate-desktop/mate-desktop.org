<!--
.. link:
.. description:
.. tags: Releases,Fedora
.. date: 2015-06-11 22:30:30
.. title: MATE 1.10 with GTK3 for Fedora 21 and 22
.. slug: 2015-06-11-mate-1-10-with-gtk3-for-fedora-21-22
.. author: Wolfgang Ulbrich
-->

The MATE Desktop maintainers for Fedora are pleased to announce that experimental
GTK3 builds are available for testing on Fedora 21 and Fedora 22. These GTK3 build
do work but have some minor rendering issues, we'd value your feedback.

## Installation

Install the repo file and do a `yum update`.

### Fedora 22

    wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-22/raveit65-Mate-GTK3-fedora-22.repo
    sudo cp raveit65-Mate-GTK3-fedora-22.repo /etc/yum.repos.d/
    sudo yum update

### Fedora 21

    wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-21/raveit65-Mate-GTK3-fedora-21.repo
    sudo cp raveit65-Mate-GTK3-fedora-21.repo /etc/yum.repos.d/
    sudo yum update

Or use `dnf` command:

    sudo dnf copr enable raveit65/Mate-GTK3
    sudo dnf update

## Reporting issues

Please use the MATE Desktop issue tracker on GitHub and include 'GTK3 and Fedora'
in subject.

  * https://github.com/mate-desktop

Some notes:

  * Compiz will only work with `emerald` as window-decorator.
  * Do not use use a mix of GTK2 packages from Fedora stable and GTK3 packages from the
  repo above.
  * Do not use the following MATE applications with a GTK3 build of MATE; they aren't ported to GTK3:
    * mintMenu and MATE Menu
    * mate-applet-streamer
    * mate-applet-lockkeys
    * mate-applet-softupd
    * caja-terminal
