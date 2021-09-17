<!--
.. link:
.. description:
.. tags: Releases
.. date: 2014-03-04 21:39:36
.. title: Rilasciato MATE 1.8
.. slug: 2014-03-04-mate-1-8-released
.. author: Stefano Karapetsas
-->

Il team è orgoglioso di annunciare il rilascio di MATE Desktop 1.8. Vorremmo 
ringraziare ogni collaboratore ed ogni utente MATE.

![about](/assets/img/blog/about-mate-1.8.png)

I cambiamenti principali in 1.8 sono:

**Caja (file manager)**

  * Aggiunta una opzione per utilizzare le unità IEC anziché quelle SI
  * Aggiunta l'opzione "Apri posizione genitrice" nel menù contestuale della visualizzazione di ricerca

**Marco (gestore delle finestre)**

  * Aggiunto il tiling fianco a fianco (agganciamento delle finestre)

**Pannello**

  * Aggiunto il supporto per il keybinding di Metacity nel dialogo esegui e nel menù principale
  * Aggiunta una barra di progresso alla finestra di dialogo logout

**Centro di controllo**

  * Aggiunto il supporto per utilizzare Metacity come gestore delle finestre

**MATE Desktop library**

  * Aggiunta la Guida Utente di MATE

**Eye Of MATE (visualizzatore di immagini)**

  * Aggiunta la modalità shuffle alla presentazione

**Engrampa (archiviatore di file)**

  * Mostra sempre il menù contestuale "Estrai in" in Caja

**Screensaver**

  * Mostra la data e l'orario nella finestra di blocco

**Applet**

  * Aggiunta la funzionalità Annulla all'applet note adesive
  * Aggiunta una nuova applet "comando" per mostrare l'output di un comando
  * Riscritta l'applet "timer" in C
  * Facendo clic col pulsante centrale del mouse sull'applet volume si attiva/disattiva la funzionalità escludi audio

**Pacchetti eliminati**

  * Sostituito  `mate-doc-utils` con `yelp-tools`
  * Sostituiti `libmatekeyring` e `mate-keyring` con `libsecret` e `gnome-keyring`
  * Sostituito`libmatewnck` con `libwnck`
  * Sostituito `mucharmap` con `gucharmap`
  * Sostituito `mate-bluetooth` con [blueman](https://github.com/blueman-project/blueman)
  * Unite tutte le estensioni di Caja in un solo pacchetto
  * Rimossa l'applet luci del modem, poiché l'applet netspeed offre una funzionalità simile

**Altri miglioramenti**

  * Corrette molte linee di codice deprecato
  * Eliminati molti bug
  * Migliorato il sistema di compilazione
  * Aggiunte e migliorate molte traduzioni

<br/><br/>

Come sempre, abbiamo chiesto agli utenti delle distribuzioni che offrono MATE cosa pensano del
nostro Ambiente Desktop

**Mike Gabriel**, [Debian](https://www.debian.org/) sviluppatore e manutentore MATE:

> Prevedo che MATE sarà uno degli ambienti desktop più utilizzati in Debian Jessie (e successivi).

**Tom Wijsman**, [Gentoo](https://www.gentoo.org) sviluppatore e manutentore MATE:

> Alcuni dei nostri utenti affermano di voler rimanere con GNOME 2; perché
gli piacciono le cose come erano solite essere, eseguono vecchi hardware o vogliono
un desktop più leggero. Dato che GNOME 2 non è più supportato e sarà eventualmente
rimosso dalla nostra meta distribuzione a causa di vari problemi legati alla manutenzione, regressioni e
problemi di sicurezza; MATE riporta in auge una vecchia gloria con un team di sviluppo attivo.
La loro prosecuzione dello sviluppo di GNOME 2 risolve problemi evidenti, introduce funzionalità nuove
ed utili e mantiene viva e vegeta la buona vecchia esperienza.

**Willy Sudiarto Raharjo**, Co-sviuppatore del [Progetto MATE SlackBuilds](https://mateslackbuilds.github.io/):

> MATE ha condiviso la stessa filosofia alla base di Slackware, come la semplicità,
la stabilità, e i rilasci senza scadenza prefissata. Viene rilasciato quando è pronto
e mantiene la stessa metafora  che si è dimostrata funzionare bene. MATE è
anche semplice da mantenere e da integrare su Slackware da quando Patrick
Volkerding ha dato una solida base come substrato su cui MATE potrebbe colmare il bisogno di Ambienti Desktop basati su GNOME che Slackware non possiede più dal 2005. Aspetto con trepidazione le modifiche evolutive che gli sviluppatori MATE
integreranno nella successiva major-release di MATE.

**Chess Griffin**, Co-sviluppatorfe del [Progetto MATE SlackBuilds](https://mateslackbuilds.github.io/):

> MATE è un ottimo ambiente desktop per coloro che amano la vecchia esperienza GNOME 2. 
Apprezzo molto tutto il duro lavoro che viene messo in MATE
per mantenerlo stabile e maturo e allo stesso tempo incorporare nuovi pezzi
dove opportuno. Lo sforzo di mantenere MATE agnostico in termini di sistema operativo o distribuzione dell'utente
è anch'esso da applaudire. Mi piace essere
parte del progetto MATE SlackBuilds, che mira a portare il desktop MATE
alla comunità Slackware Linux. Grazie a tutto il team di MATE!

**Benjamin Denisart**, [openSUSE](https://www.opensuse.org/) manutentore MATE:

> Il team openSUSE vuole ringraziare gli sviluppatori di MATE per i loro sforzi nel
fornire questa nuova versione ed è orgoglioso di annunciare la disponibilità
di `gnome-main-menu`, che farà piacere agli utenti attratti da un desktop tradizionale e
facile da usare. È un piacere per noi lavorare con il team di MATE e vogliamo
inviare loro le nostre congratulazioni.

**Clement Lefebvre**, fondatore e capo progetto di [Linux Mint](https://www.linuxmint.com/):

> MATE porta con orgoglio i colori di GNOME 2 e continua da dove il progetto
era stato lasciato. In molti modi e per molta gente MATE li fa sentire come a casa.
È semplice, stabile e completo. Mentre i desktop più recenti sperimentano
con nuovi concetti, MATE fornisce un ambiente che funziona esattamente come ci si
aspetta. È popolare tra i nostri utenti ed è il desktop su cui
Linux Mint ha costruito la sua tecnologia ed identità dal 2006. Siamo molto orgogliosi
e molto felici di supportare MATE e deliziati ad ogni nuovo rilascio.

**Wolfgang Ulbrich**, manutentore MATE in [Fedora](https://fedoraproject.org/): 

> Durante i rilasci di Fedora 15/16 sono rimasto molto insoddisfatto delle soluzioni desktop
proposte. Dopo 10 mesi di utilizzo di XFCE ho scoperto MATE e ho deciso
di costruire il mio desktop per Fedora nel dicembre 2011. Questo lavoro ha portato al
primo repository esterno del desktop MATE per Fedora ed è stato usato da molti utenti
in tutto il mondo, comprese le spin Fedora basate sui miei pacchetti in Russia, Lettonia e
Indonesia. Il corollario di questo lavoro è stato portare il Desktop MATE
all'interno di Fedora ufficiale insieme a Dan Mashal per Fedora 18. Due versioni
dopo abbiamo una soluzione desktop MATE 1.6 stabile e utilizzabile in Fedora 20. MATE
1.8 è attualmente in Fedora rawhide e sarà rilasciato con Fedora 21
nell'estate del 2014.

**Martin Wimpress**, manutentore MATE per [Arch Linux](https://www.archlinux.org/):

> MATE è stato originariamente creato da un utente di Arch Linux e sono lieto che MATE sia
adesso disponibile nei repository ufficiali dei pacchetti Arch Linux e Arch Linux ARM. MATE fornisce un'esperienza desktop completa, completamente integrata e reattiva
tradizionale e fornisce un flusso di lavoro coerente sul mio [Raspberry Pi](www.raspberrypi.org),
[CuBox Pro](https://www.solid-run.com/cubox), laptop e desktop. Geniale!

<br/><br/>

MATE 1.8 è il risultato di 11 mesi di intenso sviluppo e contiene 1845
contribuzioni da 57 persone, e più di 291 traduttori.

  * [MATE 1.8 Screenshots](/gallery/1.8/)

<br/><br/>
