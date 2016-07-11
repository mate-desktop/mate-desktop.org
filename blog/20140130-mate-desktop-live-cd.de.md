<!-- 
.. link: 
.. description: 
.. tags: LiveCD,Arch Linux,News
.. date: 2014/01/30 00:17:32
.. title: MATE-Desktop Live-CD
.. slug: 2014-01-30-mate-desktop-live-cd
.. author: Martin Wimpress
-->

Das MATE-Team hat eine Live-CD erstellt, die einen vollständigen MATE-Desktop bootet.

<div class="alert alert-info"><strong>Update</strong>Die Live-CD wurde am 10. März 2014 auf MATE 1.8 aktualisiert.</div>

Diese Live-CD wurde erstellt, damit potentielle neue Nutzer den MATE-Desktop 
ausprobieren können, ohne Änderungen an Ihrem System vornehmen zu müssen.
Das Image kann auf eine DVD gebrannt, als ISO eingehangen oder
direkt auf einen USB-Stick (mittels eines Utilitys wie `dd`) geschrieben werden.
[Linux Luddites](http://linuxluddites.com/) aufgepasst: `unetbootin` wird nicht unterstützt.

Sie können es wie folgt herunterladen:

### BitTorrent-Download (empfohlen)

Wenn Sie die zusätzlichen Bytes verschmerzen können, lassen Sie bitte den Client geöffnet,
nachdem der Download beendet ist, damit Sie es an andere zurück "seeden" können.
*Für höchste Download-Geschwindigkeit wird ein "web-seed-fähiger" Client empfohlen.

  * [matelivecd-14.069.1449.iso.torrent](http://repo.mate-desktop.org/livecd/matelivecd-14.069.1449.iso.torrent)

### Direkter HTTP-Download

Zusätzlich zu dem BitTorrent-Link oben, kann das ".iso" der Live-CD auch
über HTTP heruntergeladen werden. Bitte vergewissern Sie sich, dass die heruntergeladene
Datei zu der SHA1-Checksum passt.

  * [matelivecd-14.069.1449.iso](http://repo.mate-desktop.org/livecd/matelivecd-14.069.1449.iso) [ ~964MB ]
    * SHA1: `12b529d17d1ecef39d9b0e1122fb5271e0534c0a`

## Kompatibilität

Die Live-CD wurde mit [Arch Linux](http://www.archlinux.org) und MATE 1.8 gebaut. 
Die Live-CD ist 32-Bit und sollte daher auf jedem i686- oder x86_64-Rechner mit
mindestens 512MB RAM laufen. X.Org-Treiber sind enthalten für Intel (`i915`),
AMD/ATI (`radeon`) und nvidia (`nouveau`) mit einer Ausweichlösung mittels VESA.
Treiber für Virtual Box und VMware sind ebenso enthalten, damit das Ausprobieren
auf diesen Virtualisierungs-Lösungen einfach ist.

Alle gängigen Dateisysteme, inclusive [ZFS](http://open-zfs.org), werden 
unterstützt, und einige Tools zur Datenrettung und zum Backup sind auch dabei.
Wenn Sie Ihr mobiles Endgerät anstecken, wird es mit großer Wahrscheinlichkeit erkannt,
und Sie werden in der Lage sein, auf die sich darauf befindlichen Daten zuzugreifen.
NetworkManager gehört auch zum Lieferumfang, zusammen mit all den unterstützten VPN-Clients.

## Nutzernamen und Passwörter

Auf der MATE-Desktop-Live-CD sind die folgenden Accounts konfiguriert.

  * `root` - Das Passwort ist `livecd`.
  * `mate` - Das Passwort ist `livecd`.

Der `root`-Account entspricht offensichtlich `root`. Der `mate`-Account
ist ein regulärer Benutzer, der volle passwortlose `sudo`-Rechte besitzt. 
Die Live-CD loggt automatisch mit dem `mate`-Account ein.

## Anwendungen

Die Live-CD wurde in erster Linie als Demonstration des MATE-Desktops erstellt,
aber wir haben einige zusätzliche nicht zum MATE-Desktop gehörenden Anwendungen aufgenommen,
um die Live-CD ein wenig nützlicher und unterhaltsamer zu machen.

  * [Firefox](https://www.mozilla.org/firefox/)   - Stand-Alone Web-Browser von mozilla.org
  * [GParted](http://gparted.sourceforge.net)   - Ein Klon von Partition Magic, Front-End für GNU Parted
  * [HardInfo](http://hardinfo.berlios.de/wiki/index.php/Main_Page)  - Ein System-Informations- und Benchmark-Tool
  * [Hexchat](http://hexchat.github.io/)   - IRC-Client, konfiguriert für die automatischen Verbindung zu [#mate@freenode](https://webchat.freenode.net/?channels=#mate)
  * [Onboard](http://www.gnome.org/projects/orca)      - Screen-Reader für blinde bzw. sehbeinträchtigte Personen
  * [Orca](http://www.gnome.org/projects/orca)      - On-Screen-Keyboard, nützlich für motorisch eingeschränkte Personen
  * [Pidgin](http://pidgin.im/)    - Multi-Protokoll Instant-Messaging Client
  * [Truecrypt](http://www.truecrypt.org/) - Freie, quelloffene, cross-plattform Festplatten-Verschlüsselungs-Software
  * [Xnoise](http://www.xnoise-media-player.com/)    - Medien-Player mit einer schicken GUI, hoher Geschwindigkeit und vielen Features

## Creative-Commons-Inhalte

Wir haben die folgenden Inhalte, lizensiert unter Creative-Commons, hinzugepackt:

  * [Think Python](http://www.greenteapress.com/thinkpython/)                        - Zum Lesen mit Atril
  * [Nine in Nails Ghosts I - IV](http://ghosts.nin.com/main/home) Ein Album - Zum Hören mit Xnoise
  * [Nine in Nails Ghosts I - IV](http://ghosts.nin.com/main/home) Photos  - Zum Betrachten mit "Eye of MATE"

## Die Sprache ändern

Standardmäßig ist bei der Live-CD das `en_US`-Locale (Gebietsschema) eingestellt, aber falls
Sie eine andere Sprache aktivierten möchten, erklären wir hier, wie es geht.
Im untenstehenden Beispiel aktivieren wir Deutsch.

Editieren Sie `/etc/locale.gen`, entfernen Sie bei Ihrem Gebietsschema (in diesem Fall`de_DE.UTF-8 UTF-8`) 
die Kommentarzeichen (#) und veranlassen Sie einen Rebuild der Gebietsschemata mit:

    sudo locale-gen

Editieren Sie `/etc/locale.conf` und ändern Sie `LANG=` dahingehend, 
dass die Zeile ihrer Sprachwahl entspricht -- in diesem Fall `LANG=de_DE.UTF-8`.
Zum Schluss starten Sie den DisplayManager wie folgt neu, damit Sie neu eingeloggt werden
in Ihre MATE-Session, die nun Ihre bevorzugte Sprache verwendet:

    sudo systemctl restart lightdm

## Vorstellung in der Linux-Action-Show

Die MATE-Desktop-Live-CD und MATE selbst haben wir
auf der [Linux Action Show](http://www.jupiterbroadcasting.com/show/linuxactionshow/) vorgestellt
in der [CuBox-Linux-Review](http://www.jupiterbroadcasting.com/50842/cubox-linux-review-las-s30e08/)-Episode.
Zwei Videos sind unten eingebettet. Das erste bietet einen kurzen Einblick in die MATE-Desktop-Live-CD,
das zweite eine Besprechung der CuBox i4, auf der MATE läuft.

### MATE-Desktop Live-CD

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=608" frameborder="0" allowfullscreen></iframe>

### CuBox i4 Pro Review

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=1925" frameborder="0" allowfullscreen></iframe>

## Feedback

Wir hoffen, Sie lassen sich auf eine Testfahrt mit der Live-CD ein und mögen
die Geschwindigkeit und Einfachheit, die der MATE-Desktop bietet. Sobald
Sie zurück sind, lassen Sie uns wissen, was Sie darüber denken. Benutzen
Sie dazu bitte die Kommentarfunktion oder treffen Sie uns im 
[#mate IRC channel](https://webchat.freenode.net/?channels=#mate).
