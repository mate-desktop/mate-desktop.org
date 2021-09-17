<!--
.. link:
.. description:
.. tags: Releases
.. date: 2016-09-21 21:00:00
.. title: Rilasciato MATE 1.16
.. slug: 2016-09-21-mate-1-16-released
.. author: Martin Wimpress
-->

Dopo 6 mesi di sviluppo il team di MATE Desktop è orgoglioso di annunciare
il rilascio di MATE Desktop 1.16. Vorremmo ringraziare ogni collaboratore MATE per il suo aiuto nell'aver reso possibile questo rilascio.

![about](/assets/img/blog/about-mate-1.16.png)

## Cosa c'è di nuovo in MATE 1.16

Questa release è centrata sul miglioramento della compatibilità GTK3+, sulla migrazione dei componenti alle librerie più nuove, eliminando bug e migliorando il codice.
I principali cambiamenti di MATE Desktop 1.16 sono:

  * Supporto a GTK+3 migliorato in tutto il Desktop MATE.
  * Supporto ai temi e alle applicazioni per GTK+ 3.22.
  * Accresciuto il numero di applicazioni compilate esclusivamente contro GTK+3
    * Engrampa
    * MATE Notification Daemon
    * MATE PolKit
    * MATE Session Manager
    * MATE Terminal
  * Alcune applicazioni sono state disaccoppiate da `libmate-desktop`:
    * Engrampa
    * MATE Applets
    * MATE Netbook
    * MATE Power Manager
    * MATE Terminal
    * Pluma
  * È iniziato il lavoro per portare le applicazioni a GApplication o GtkApplication:
    * Engrampa
    * MATE Applets
    * MATE Netbook
    * MATE User Share
  * Molti bug e parecchio codice deprecato sono stati corretti.
  * Le traduzioni sono state aggiornate. *Grazie al nostro team di traduttori!*

I vari componenti di MATE 1.16 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.16/>

## Changelog

Segue una analisi più dettagliata di ciò che è cambiato.

### mate-common

  * Verificare solo per `autoreconf` in `mate-autogen` come `autoconf`, `automake`,
    `libtool`, `gettext` sono già verificati da `autoreconf`

### mate-desktop

  * mate-bg: rimossa l'inutile proprietà ignore-pending-change (non più necessaria dalla correzione del colore del font in Caja 1.14)
  * GTK+3: Corrette varie deprecazioni
  * distcheck: utilizzo esplicito della versione GTK+ correntemente selezionata
  * Alcune ripuliture minori
  * Aggiornate le traduzioni

### libmatekbd

  * Richiesto libxklavier 5.2 e l'utilizzo della sua introspezione
  * GTK+3: Corrette alcune deprecazioni
  * distcheck: utilizzo esplicito della versione GTK+ correntemente selezionata
  * Aggiornate le traduzioni

### libmatemixer

  * Aggiornate le traduzioni

### libmateweather

  * Località: aggiornato il codice ICAO per Quito, Ecuador
  * Località: corrette le coordinate dell'aeroporto di Minsk (codice UMMS)
  * Aggiornate le traduzioni

### mate-icon-theme

  * Aggiornate le traduzioni

### Caja

  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Pathbar: mostrata sempre il pulsante freccia destra
  * Corretto il problema del cambiamento di icona della barra delle applicazioni quando si passa tra schede con icone diverse
  * Corretti un gran numero di warning quando si compila la documentazione per `libcaja-extension`
  * GTK+3: aggiunte classi di stile per gli elementi della barra delle posizioni
  * GTK+3: Corretta la visualizzazione e la modifica dello sfondo del desktop con le versioni >= 3.21
  * GTK+3: Corretto un gran numero di deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-polkit

  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Aggiornate le traduzioni

### Marco

  * Aggiornate le traduzioni
  * Fatto in modo che distcheck utilizzi la versione di GTK+ correntemente selezionata

### mate-settings-daemon 

  * Modificato lo stile predefinito per i suggerimenti a 'hintslight'
  * Utilizzo dell'antialiasing 'rgba' (LCD subpixel) come predefinito
  * GTK+3: aggiunta la possibilità dei temi via css per OSD  (MsdOsdWindow) al posto dei colori inseriti direttamente nel codice
  * GTK+3: Corretta la visualizzazione e la modifica dello sfondo del desktop con le versioni >= 3.21
  * GTK+3: Corrette diverse deprecazioni
  * Corretti alcuni warning di compilazione
  * Aggiornate le traduzioni

### mate-session-manager

  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Aggiornate le traduzioni

### mate-menus

  * Aggiornate le traduzioni

### mate-panel

  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * GTK+3: uso di GtkColorButton/GtkColorChooser nella finestra di dialogo delle proprietà
  * GTK+3: Corrette molte deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-backgrounds

  * Aggiornate le traduzioni

### mate-themes

  * Completo supporto a GTK+ 3.20 e 3.22.

### mate-notification-daemon

  * Compilazione: uso della directory `m4` invece delle `macros` per le macro m4, come negli altri progetti.
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Aggiunto il supporto a GNotification
  * Corrette le sequenze di escape dei caratteri speciali
  * Corrette alcune deprecazioni di GTK+
  * Aggiornate le traduzioni

### mate-control-center

  * Compilazione: eliminata la compatibilità a dconf 0.10
  * Aspetto: modificato lo stile predefinito dei suggerimenti a slight e renderizzato l'antialising dei campioni utilizzando quello stile
  * Aspetto: renderizzati i campioni di suggerimento utilizzando l'antialising RGBA
  * Aspetto: posizionato il nome del tema sotto l'anteprima del tema nella build GTK+3 come avviene con quella GTK+2
  * Aspetto: centrato il nome del tema nella build GTK+3 come avviene con quella GTK+2
  * Aspetto: nascosta la scheda Colori nella finestra di dialogo Personalizza Tema nella build GTK+3 perché il cambiamento dei colori del tema non funziona in GTK+3
  * GTK+3: risolta la compilazione con il supporto appindicator abilitato
  * GTK+3: risolta la visualizzazione del monitor nelle proprietà del display con glib 2.49.6
  * GTK+3: Corrette varie deprecazioni
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mate-screensaver

  * Corretto il blocco quando lo screensaver è già attivo
  * GTK+3: Corretto lo sfondo e il blocco nel setup multi-monitor
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni
  * Fatto in modo che distcheck utilizzi la versione di GTK+ correntemente selezionata

### mate-media

  * Aggiornate le traduzioni

### mate-power-manager

  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Eliminata la dipendenza da `libmate-desktop`
  * Mostra il tempo rimanente del dispositivo primario come prima voce del menu contestuale
  * Non mostrare un warning sulla console se le batterie del laptop sono scariche
  * GTK+3: port da libunique a GtkApplication
  * GTK+3: aggiunta la capacità di modificare il tema via css per OSD (MsdOsdWindow)
  * GTK+3: Corretto lo spazio vuoto nella barra delle applicazioni quando il sistema non ha la batteria
  * GTK+3: Corrette molte deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni
  * Fatto in modo che distcheck utilizzi la versione di GTK+ correntemente selezionata

### mate-system-monitor

  * Aggiornate le traduzioni

### Atril 

  * compilazione: richiesto poppler 0.18.0
  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Rimossa la dipendenza da `libmate-desktop` e l'opzione di compilazione `--without-matedesktop`
  * Aggiornato `toolbar-editor` da `libegg`
  * Aggiornato synctex a 1.18
  * Divisa l'opzione dual mode in dual mode con pagine dispari e pari sulla sinistra
  * Aggiunta la combinazione di tasti Ctrl+ Freccia in Alto/ Freccia in Basso per il risultato delle ricerca precedente/successiva
  * Aggiunto a `caja-sendto` il supporto per inviare il documento corrente via email, ad un dispositivo mobile, etc.
  * Migliorato il supporto alle destinazioni con nome mediante l'argomento della linea di comando `--named-dest` e il supporto dbus
  * [dvi] Utilizzo dei file di mappatura del font t1
  * GTK+3: aggiunta la classe di stile per la visualizzazione
  * GTK+3: Corretto un possibile crash quando si compila con l'introspezione abilitata
  * GTK+3: Corrette molte deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### caja-extensions

  * open-terminal:
    * Risolta l'apertura di un terminale in una cartella remota con virgolette singole o doppie nel suo nome
    * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### Engrampa

  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Port a GTKApplication
  * Utilizzo dell'ordinamento naturale quando si ordina secondo il nome del file
  * Utilizzo della finestra di dialogo app chooser di GTK+ per il comando "Open With" invece di usare codice personalizzato
  * Resa l'opzione "encrypt header" insensibile se non è specificata alcuna password
  * Data la priorità a unrar invece di p7zip quando si decomprimono archivi RAR
  * 7z: aggiunto il supporto per p7zip-rar >= 15.14
  * 7z: corretto il problema dei file con prefisso '@'
  * Corrette alcune deprecazioni di GTK+3
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### Eye of MATE

 * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
 * Corretta la possibile scrittura out-of-bounds nell'area dei messaggi di errore
 * Alcune rifiniture al codice
 * Aggiornate le traduzioni

### mate-applets

  * Compilazione: richiede polkit 0.97
  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  - Netspeed: utilizzati GtkColorButton/GtkColorChooser
  - Eliminata la dipendenza da `libmate-desktop`
  - GTK+3: Corrette varie deprecazioni
  - Alcune rifiniture al codice
  - Aggiornate le traduzioni

### mate-indicator-applet

  * Compilazione: corretto il controllo per il supporto dei nuovi indicatori di stile
  * Aggiornate le traduzioni

### mate-netbook

  * Applet Window Picker: utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Applet Window Picker: eliminati possibili crash
  * mate-maximus: port da libunique a GtkApplication
  * Eliminata la dipendenza da `libmate-desktop`
  * Aggiornate le traduzioni

### mate-sensors-applet

  * Fatto in modo che distcheck utilizzi la versione di GTK+ correntemente selezionata
  * Aggiornate le traduzioni

### mate-terminal

  * Migrato a GTK+3, richiesto GTK+ 3.14 e VTE 0.38 (API 2,91)
  * Rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Copiati gli helper dconf e gsetting da `libmate-desktop` ed eliminata la dipendenza da `libmate-desktop`
  * Risposta alla variazione di WM solo su X11
  * Corrette molte deprecazioni di GTK+
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-user-share

  * Compilazione: uso della directory `m4` invece delle `macros`, come negli altri progetti.
  * GTK+3: port da libunique a GtkApplication
  * Fatto in modo che distcheck utilizzi la versione di GTK+ correntemente selezionata
  * Aggiornate le traduzioni

### mate-polkit

  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Aggiornate le traduzioni

### mate-utils

  * Aggiunta l'opzione della riga di comando `--version` a `mate-screenshot`
  * GTK+3: Risolto un segfault di mate-dictionary con >= 3.21
  * GTK+3: Corrette molte deprecazioni in tutte le app
  * Aggiornate le traduzioni

### Mozo

  * Aggiunti i pulsanti Proprietà e Cancella
  * Risolti diversi problemi nel drag-and-drop
  * Fissato il crash quando il file `.desktop` ha una slash nel nome
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### Pluma

  * Utilizzo di `GtkAboutDialog()` al posto di `MateAboutDialog()`
  * Rimossa la dipendenza da `libmate-desktop` e l'opzione di compilazione `--without-matedesktop`
  * GTK+3: Corrette molte deprecazioni
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### caja-dropbox

  * Alcune rifiniture al codice

### python-caja

  * Esempi: risolto un crash di Caja caricando l'estensione dell'immagine di sfondo
  * Esempi:correzioni varie
  * Aggiornate le traduzioni
