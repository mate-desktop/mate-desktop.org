<!-- 
.. link: 
.. description: 
.. tags: Arch Linux,Raspberry Pi,News
.. date: 2014/01/16 22:22:22
.. title: MATE è disponibile ufficialmente su Arch Linux
.. slug: 2014-01-16-mate-officially-in-arch-linux
.. author: Martin Wimpress
-->

MATE ha finalmente trovato la strada di casa.

Come qualcuno di voi potrebbe sapere, MATE è stato creato da un utente[Arch Linux](https://www.archlinux.org),
Perberos. È piuttosto ironico il fatto che MATE non sia stato fornito nei repository ufficiali di Arch Linux fino ad oggi. Esatto,
MATE è finalmente disponibile nel repository di pacchetti `[community]` di Arch Linux!.

Potete trovare ogni informazione necessaria ad installare MATE
su Arch Linux dalle pagine wiki seguenti:

  * <https://wiki.archlinux.org/index.php/MATE>

Vale la pena di notare che il repository di pacchetti non ufficiali di MATE sarà rimosso una volta che i mirror Arch Linux saranno sincronizzati.
Pertanto andate ad aggiornare `/etc/pacman.conf` e rimuovete il
repository di pacchetti `[mate]`.

L'altro vantaggio di mettere MATE nei repository dei pacchetti di Arch Linux ufficiali
è che MATE sarà anche sui repository di pacchetti [Arch Linux ARM](https://archlinuxarm.org/).
Posso quindi finalmente ritirare i build *"server"* per Raspberry Pi (armv6h) e
Cubox Pro (armv7h). Non sono sicuro di quanto ci vorrà
perché tutti i pacchetti MATE siano presenti sul repository di pacchetti Arch Linux ARM, ma ho già visto che alcuni pacchetti sono stati costruiti.

MATE viene eseguito bene sul Modello B di Raspberry Pi con 512MB di RAM, quindi se avete una Pi e vi avanza una SDCARD, provatelo. Scriverò a breve
un post sul blog su come installare Arch Linux e MATE sulla Raspberry Pi con alcuni utili tweak sulla performance.
