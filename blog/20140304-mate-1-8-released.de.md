<!--
.. link:
.. description:
.. tags: Releases
.. date: 2014-03-04 21:39:36
.. title: MATE 1.8 freigegeben
.. slug: 2014-03-04-mate-1-8-released
.. author: Stefano Karapetsas
-->

Es erfüllt das Team mit Stolz, das Release des MATE-Desktops 1.8 bekanntzugeben.
Wir möchten jedem Mitwirkenden und jedem MATE-Nutzer danken.

![about](/assets/img/blog/about-mate-1.8.png)

Die wesentlichen Änderungen in 1.8 sind:

**Caja (Datei-Manager)**

  * Option hinzugefügt, um IEC-Einheiten anstatt von SI-Einheiten zu verwenden
  * Option “Übergeordneten Ort öffnen” im Kontextmenü der Suchansicht hinzugefügt

**Marco (Window-Manager)**

  * Side-by-Side-Tiling hinzugefügt (Fenster-Einrastung)

**Panel**

  * Unterstützung für Metacity-Tastaturbelegung im "Start"-Dialog und Hauptmenü hinzugefügt
  * Hinzufügen eines Fortschrittsbalkens zum Logout-Dialog

**Kontrollcenter**

  * Hinzufügen der Unterstützung zum Verwenden von Metacity als Window-Manager

**MATE-Desktop-Bibliothek**

  * MATE-Bedienungsanleitung hinzugefügt

**Eye Of MATE (Bildbetrachter)**

  * Shuffle-Modus zur Slideshow hinzugefügt

**Engrampa (Datei-Packprogramm)**

  * Das “Extrahieren nach”-Kontextmenu erscheint nun immer in Caja.

**Bildschirmschoner**

  * Anzeigen des Datums und der Uhrzeit im Sperr-Dialog

**Applets**

  * Undo-Funktionalität zum StickyNote-Applet hinzugefügt
  * Neues “command”-Applet hinzugefügt, das die Ausgabe eines Befehls anzeigt
  * “timer”-Applet neu in C implementiert
  * Das Klicken mit der mittleren Maustaste auf das Volume-Applet (de-)aktiviert die Stummschaltung.

**Entfernte Pakete**

  * Ersetzen der `mate-doc-utils` durch `yelp-tools`
  * Ersetzen von `libmatekeyring` und `mate-keyring` durch `libsecret` und `gnome-keyring`
  * Ersetzen von `libmatewnck` durch `libwnck`
  * Ersetzen von `mucharmap` durch `gucharmap`
  * Ersetzen von `mate-bluetooth` durch [blueman](https://github.com/blueman-project/blueman)
  * Mergen aller Caja-Extensions in ein einzelnes Paket
  * Entfernen des ModemLights-Applet, da das Netspeed-Applet eine ähnliche Funktionalität bietet

**Sonstige Verbesserungen**

  * Beseitigen einer Menge veralteten Codes
  * Beseitigen einer Menge Bugs
  * Verbesserung des Build-Systems
  * Hinzufügen und Verbessern einer Menge Übersetzungen

<br/><br/>

Wie gewöhlich fragten wir Mitarbeiter von Distributionen, die MATE anbieten, 
was sie von unserer Desktop-Umgebung halten.

**Mike Gabriel**, [Debian](https://www.debian.org/) Entwickler und MATE-Maintainer:

> I forsee MATE being one of the most used desktop environments in Debian Jessie (and beyond).

**Tom Wijsman**, [Gentoo](https://www.gentoo.org) Entwickler und MATE-Maintainer:

> Some of our users express that they want to stay with GNOME 2; because they
like how things used to be, they run older hardware or they want a more
lightweight desktop. Given that GNOME 2 became unsupported and will eventually
be removed from our meta distribution due to various maintenance, regression and
security issues; MATE brings back all the glory with an active development team.
Their continuation of GNOME 2's development fixes outstanding issues, brings new
and useful features and keeps the good old experience alive and kicking.

**Willy Sudiarto Raharjo**, Co-Entwickler des [MATE-SlackBuilds-Projekts](https://mateslackbuilds.github.io/):

> MATE shared the same basic philosophies of Slackware, such as simplicity,
stability, and no fixed release schedule. It will be released when it's ready
and preserving the same metaphor which is proven to be working well. MATE is
also easy to be maintained and integrated on top of Slackware since Patrick
Volkerding has given a solid foundation as the base layer in which MATE could
fill the need of GNOME-based Desktop Environment which Slackware lack of since
2005. I'm looking forward for the evolutionary changes that MATE developers
will integrate for the next major release of MATE.

**Chess Griffin**, Co-Entwickler des [MATE-SlackBuilds-Projekts](https://mateslackbuilds.github.io/):

> MATE is a great desktop environment for those who like the old GNOME 2
experience.  I greatly appreciate all the hard work that is put into MATE
to keep it stable and mature yet at the same time incorporating new bits
where appropriate.  The effort to keep MATE agnostic in terms of the user's
operating system or distribution is also to be applauded.  I enjoy being a
part of the MATE SlackBuilds project, which aims to bring the MATE desktop
to the Slackware Linux community.  Thanks to the entire MATE team!

**Benjamin Denisart**, [openSUSE](https://www.opensuse.org/) MATE-Maintainer:

> The openSUSE team wants to thank the MATE developers for their efforts in
providing this new version and is proud to announce the availability
of `gnome-main-menu`, which will please users attracted by a traditional and
easy to use desktop. It's a pleasure for us to work with the MATE team and we
want to send them our congratulations.

**Clement Lefebvre**, [Linux Mint](https://www.linuxmint.com/)-Gründer und Projektleiter:

> MATE proudly carries the colors of GNOME 2 and continues where the project
left off. In many ways and for many people MATE just feels like home.
It's simple, stable and full featured. While more recent desktops experiment
with new concepts, MATE provides an environment which works exactly as you'd
expect it. It's popular with our users and it's the desktop on top of which
Linux Mint built its technology and identity since 2006. We're very proud
and very happy to support MATE and delighted with each and every new release.

**Wolfgang Ulbrich**, MATE-Maintainer in [Fedora](https://fedoraproject.org/): 

> During the Fedora 15/16 releases I was very dissatisfied with the desktop
solutions on offer. After 10 months of using XFCE I discovered MATE and decided
to build my own desktop for Fedora in December 2011. This work resulted in the
first external MATE Desktop repository for Fedora and was used by many users
worldwide, including Fedora spins based on my packages in Russia, Latvia and
Indonesia. The corollary to this work was to bring the MATE Desktop
inside official Fedora together with Dan Mashal for Fedora 18. Two releases
later we have a stable and usable MATE 1.6 desktop solution in Fedora 20. MATE
1.8 is currently in Fedora rawhide and will be released with Fedora 21 in the
summer of 2014.

**Martin Wimpress**, MATE-Maintainer für [Arch Linux](https://www.archlinux.org/):

> MATE was originally created by an Arch Linux user and I am delighted that MATE
is now available in the official Arch Linux and Arch Linux ARM package
repositories. MATE provides a complete, fully integrated, responsive traditional
desktop experience and consistent work flow on my [Raspberry Pi](www.raspberrypi.org),
[CuBox Pro](https://www.solid-run.com/cubox), laptop and desktop. Brilliant!

<br/><br/>

MATE 1.8 ist das Resultat von elf Monaten intensiver Entwicklungsarbeit und enhält 1845
Beiträge von 57 Personen sowie 291 Übersetzern.

  * [MATE 1.8-Screenshots](/gallery/1.8/)

<br/><br/>
