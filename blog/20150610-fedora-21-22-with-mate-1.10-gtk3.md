
Mate-1.10 desktop compiled with GTK3 for f22/21.

Do not use use a mix of GTK2 packages from fedora stable, and GTK3 packages from this repo.

Installation instructions:

Install the repo file and do a 'yum update'.

f22:

    wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-22/raveit65-Mate-GTK3-fedora-22.repo
    sudo cp raveit65-Mate-GTK3-fedora-22.repo /etc/yum.repos.d/
    sudo yum update

f21:

    wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-21/raveit65-Mate-GTK3-fedora-21.repo
    sudo cp raveit65-Mate-GTK3-fedora-21.repo /etc/yum.repos.d/
    sudo yum update

Or use dnf command:

    sudo dnf copr enable raveit65/Mate-GTK3
    sudo yum update




Bug reporting:

https://github.com/mate-desktop

Please include GTK3 and fedora in topic header.

Some notes:

- compiz will only work with emerald as window-decorator
- Do not use those mate applications, they aren't ready for GTK3:
- mintmenu
- mate-applet-streamer
- mate-applet-lockkeys
- mate-applet-softupd
- caja-terminal

Not shure about 3rd-party applications
