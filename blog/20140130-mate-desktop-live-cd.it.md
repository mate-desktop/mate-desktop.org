<!-- 
.. link: 
.. description: 
.. tags: LiveCD,Arch Linux,News
.. date: 2014/01/30 00:17:32
.. title: Live CD del Desktop MATE
.. slug: 2014-01-30-mate-desktop-live-cd
.. author: Martin Wimpress
-->

Il team MATE ha realizzato un live CD che avvia un desktop MATE completo.

<div class="alert alert-info"><strong>Update</strong> Il LiveCD è stato aggiornato a MATE 1.8 il 10 Marzo 2014.</div>

Questo Live CD è stato creato in modo che i potenziali nuovi utenti possano provare il desktop MATE
in modo non distruttivo. L'immagine può essere masterizzata su un DVD,
montata come file ISO, o scritta direttamente su una penna USB utilizzando una utility come `dd`. [Linux Luddites](https://luddites.latenightlinux.com/) fate attenzione,  `unetbootin` non è supportato. Potete scaricarlo dal link qui sotto:

### download via BitTorrent (raccomandato)

Se potete, per favore lasciate il client aperto
dopo che è terminato il download, in modo da renderlo disponibile ad altri. *Si raccomanda un client capace di web-seed
per velocità di download più elevate.*

  * [matelivecd-14.069.1449.iso.torrent]

### download diretto HTTP

Oltre al link BitTorrent dato prima, il file iso Live CD può essere scaricato anche via HTTP. Per favore assicuratevi che il file scaricato corrisponda al
checksum SHA1.

  * [matelivecd-14.069.1449.iso] [ ~964MB ]
    * SHA1: `12b529d17d1ecef39d9b0e1122fb5271e0534c0a`

## Compatibilità

Il Live CD è realizzato utilizzando [Arch Linux](https://www.archlinux.org) e MATE 1.8. Il Live CD è a 32 bit e dovrebbe quindi funzionare su ogni computer i686 o x86_64
con almeno 512MB RAM. I driver xorg sono inclusi per Intel (`i915`),
AMD/ATI (`radeon`) e nvidia (`nouveau`) con fallback a VESA.
I driver per Virtual Box e VMware sono anch'essi inclusi in modo che sia semplice anche la valutazione utilizzando queste soluzioni di virtualizzazione.

Sono supportati tutti i filesystem comuni, incluso [ZFS](http://open-zfs.org),
e sono compresi alcuni strumenti per il recupero dei dati ed il backup. Se collegate il vostro
dispositivo mobile, questo sarà molto probabilmente riconosciuto e sarete in grado di accedere
ai dati in esso contenuti. È presente NetworkManager assieme a tutti i client VPN che esso
supporta.

## Nomi utenti e password

IL CD Live del Desktop MATE ha i seguenti account preconfigurati.

  * `root` - la password è `livecd`.
  * `mate` - la password è `livecd`.

L'account `root` è ovviamente `root`. L'account `mate` è un utente regolare
che possiede pieni diritti `sudo` senza password. Il Live CD eseguirà il login automatico
utilizzando l'account `mate`.

## Applicazioni

Il live CD è pensato principalmente per mostrare il desktop MATE, tuttavia abbiamo
incluso alcune applicazioni aggiuntive che non fanno parte del desktop MATE
per rendere il Live CD più utile e piacevole.

  * [Firefox](https://www.mozilla.org/firefox/)   - Browser web autonomo da mozilla.org
  * [GParted](https://gparted.sourceforge.io/)   - Un clone di Partition Magic, frontend per GNU Parted
  * [HardInfo](https://www.berlios.de/software/hardinfo/)  - Uno strumento per le informazioni di sistema ed il benchmark. 
  * [HexChat](https://hexchat.github.io/)   - Client IRC configurato per auto-connettersi a [#mate@libera](https://web.libera.chat/?#mate)
  * [Onboard](https://www.gnome.org/projects/orca)      - Lettore dello schermo per individui che sono ciechi o con limitazioni visive
  * [Orca](https://www.gnome.org/projects/orca)      - Tastiera sullo schermo utile per individui con difficoltà motorie
  * [Pidgin](https://pidgin.im/)    - Client di messaggistica istantanea multi-protocollo
  * [Xnoise](http://www.xnoise-media-player.com/)    - Media player con una GUI semplice, grande velocità e diverse funzionalità

## Creative Commons content

Abbiamo incluso i seguenti contenuti sotto la licenza Creative Commons.

  * [Think Python](https://www.greenteapress.com/thinkpython/)                        - Da leggere con Atril

## Modificare la lingua

Per impostazione predefinita, il Live CD è configurato per utilizzare il locale `en_US`, ma se lo si desidera
per attivare un'altra lingua ecco come fare. Nell'esempio che segue
abiliteremo l'Italiano.

Modificate `/etc/locale.gen` e decommentate la riga con la vostra localizzazione, in questo caso `it_IT.UTF-8 UTF-8`
quindi fate il rebuild delle localizzazioni.

    sudo locale-gen

Modificate `/etc/locale.conf` e impostate `LANG=` per esprimere la vostra localizzazione, in questo caso
`LANG=it_IT.UTF-8`In fine riavviate il display manager e sarete loggati nella sessione MATE che utilizza la vostra lingua preferita.

    sudo systemctl restart lightdm

## Linux Action Show

Il LiveCD del desktop MATE e MATE stesso sono stati presentati nel [Linux Action 
Show](https://www.jupiterbroadcasting.com/show/linuxactionshow/) nell'episodio [CuBox 
Linux Review](https://www.jupiterbroadcasting.com/50842/cubox-linux-review-las-s30e08/) .
Due clip sono riportate qui sotto, la prima è un rapido sguardo al LiveCD MATE Desktop
e la seconda è una recensione di CuBox i4 su cui gira MATE.

### MATE Desktop LiveCD

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=608" frameborder="0" allowfullscreen></iframe>

### CuBox i4 Pro Review

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=1925" frameborder="0" allowfullscreen></iframe>

## Feedback

Ci auguriamo che facciate un test con il Live CD e che vi piaccia la velocità e la semplicità 
del desktop MATE. Una volta che avrete provato il Live CD del Desktop MATE
fateci sapere cosa ne pensate nei commenti o usate il Live CD per unirvi a noi 
nel [canale IRC #mate](https://webchat.freenode.net/?channels=#mate).

