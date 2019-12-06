<!-- 
.. link: 
.. description: 
.. tags: Arch Linux,Raspberry Pi,News
.. date: 2014/01/16 22:22:22
.. title: MATE offiziell in Arch Linux verfügbar
.. slug: 2014-01-16-mate-officially-in-arch-linux
.. author: Martin Wimpress
-->

MATE ist endlich zuhause angekommen.

Wie manche von Ihnen wohl wissen, wurde MATE von einem [Arch-Linux](https://www.archlinux.org)-Nutzer
erstellt, Perberos. Es entbehrt daher nicht einer gewissen Ironie, dass MATE
in den offiziellen Arch-Linux-Paketrepositorien nie angeboten wurde -- bis jetzt.
Richtig gelesen, MATE ist endlich in den Arch-Linux-`[community]`-Paketrepositorien verfügbar!

Sie erfahren alles, was Sie über die Installation von MATE auf Arch Linux wissen müssen,
auf den folgenden Wiki-Seiten:

  * <https://wiki.archlinux.org/index.php/MATE>

Es sollte auch nicht unerwähnt bleiben, dass das nun überflüssige
MATE-Repositorium entfernt werden wird, sobald alle Arch-Linux-Mirror
synchronisiert wurden. Updaten Sie daher `/etc/pacman.conf`,
und entfernen Sie das `[mate]`-Paket-Repositorium.

Ein weiterer Vorteil der Aufnahme MATEs in das offizielle Arch-Linux-Paketrepositorium
ist, dass MATE nun auch im [Arch-Linux-ARM](https://archlinuxarm.org/)-Repositorium
erscheinen wird. Ich kann endlich meine Build-*"Server"* für Raspberry Pi (armv6h) und
Cubox Pro (armv7h) in den Ruhestand schicken. Ich bin nicht sicher, wie lange es dauern
wird, bis alle MATE-Pakete im Arch-Linux-ARM-Paketrepositorium erscheinen werden, habe aber
gesehen, dass einige Pakete bereits gebaut wurden.

MATE läuft ziemlich ordentlich auf dem Raspberry Pi Model B mit 512MB RAM.
Falls Sie also einen "Pi" und eine SDCARD rumliegen haben, probieren Sie's aus. Ich werde
einen Blog-Beitrag schreiben, wie man Arch Linux und MATE auf dem Raspberry Pi 
mit einigen nützlichen Performance-Tricks installiert.

