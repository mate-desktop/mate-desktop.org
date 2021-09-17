<!--
.. link:
.. description:
.. tags: Releases
.. date: 2015-06-11 22:40:40
.. title: Rilasciato MATE 1.10
.. slug: 2015-06-11-mate-1-10-released
.. author: Martin Wimpress
-->

Dopo 15 mesi di sviluppo i team MATE Desktop sono orgogliosi di annunciare
il rilascio di MATE Desktop 1.10. Vorremmo ringraziare ogni collaboratore ed ogni utente MATE.

![about](/assets/img/blog/about-mate-1.10.png)

## Cosa c'è di nuovo in MATE 1.10

I principali cambiamenti in MATE 1.10 sono:

  * Ogni componente di MATE può essere compilato con GTK2 o GTK3.
    * Il supporto a GTK3 è ancora considerato *sperimentale*
    * ArchLinux e Fedora al momento offrono build GTK3 alternative 
  * [GSoC 2014] Caja ha adesso un gestore per le estensioni così i plugin possono essere abilitati/disabilitati con Caja in esecuzione.
  * [GSoC 2014] Atril adesso supporta [ePub](https://en.wikipedia.org/wiki/EPUB).
  * [GSoC 2014] È stata introdotta `libmatemixer`, una libreria mixer audio per il desktop MATE.
    * Fornisce una API astratta che consente l'accesso alle funzionalità mixer disponibili
    nei sistemi audio PulseAudio, ALSA e OSS.
  * L'analisi statica del codice ha evidenziato molti memory leak che sono stati corretti.
  * Il supporto dei temi è stato esteso da GTK versione 3.8 a GTK versione 3.16 inclusi il CSD e il supporto per il pop-over.

I vari componenti di MATE 1.10 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.10/>

## Screenshots

  * [MATE 1.10 Screenshots](/gallery/1.10/)

## Changelog

Segue una analisi più dettagliata di ciò che è cambiato.

### mate-common

  * Aggiunto il supporto per `automake` 1.15
  * Aggiunto il supporto per `lcov` 1.11
  * Migrato a `glib-gettexize` se si usa GLib `gettext`
  * Effettuata la verifica della presenza di `appdata-xml.m4` con `APPDATA_XML`.

### mate-desktop

  * Migrati `MateRRScreen`, `GnomeRRConfig` e `GnomeOutputInfo` a GObject.
  * Aggiunta l'introspezione GObject
  * Aggiunta la chiave automatic-mnemonics per GTK `xsetting`
  * Aggiunta la classe `MateAboutDialog` per avere la tradizionale finestra di dialogo about con GTK3
  * Aggiunta la classe `MateColorButton` per avere la tradizionale finestra di dialogo della selezione dei colori con GTK3
  * Aggiunto lo schema GSettings `org.mate.debug`
  * Uso di `GDK_WINDOW_XID` per la compatibilità inter-GTK
  * Aggiornato `mpaste` per la modifica del sito web
  * Aggiornate le traduzioni
  * Rimosso desktop-docs
  * Rimossa la guida dell'utente
  * Rimossa la dipendenza opzionale `libunique`.
  * Vari bug fix in RANDR

### libmatekbd

  * Aggiornate le traduzioni
  * Vari bug eliminati

### libmatemixer

`libmatemixer` è una nuova libreria mixer per MATE desktop. Fornisce una API astratta
che consente di accedere alle funzionalità mixer disponibili
nei sistemi audio PulseAudio, ALSA ed OSS.

  * Rilascio iniziale

### libmateweather

  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-icon-theme

  * Aggiunte più icone
  * Aggiunte nuove icone simboliche

### Caja

  * Aggiunta la gestione dei plugin per abilitare/disabilitare i plugin con Caja in esecuzione
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-polkit

  * Aggiornate le traduzioni

### Marco

  * Uso di `zenity` invece di `mate-dialogs`
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-settings-daemon 

  * Migrazione ai cambiamenti nella API `MateRR*`
  * Migrato media-keys plugin a `libmatemixer`
  * Aggiornate le traduzioni
  * Rimosso GStreamer e resi `libmatemixer`, `libcanberra` and PulseAudio dipendenze opzionali

### mate-session-manager

  * Disabilitato il supporto `upower` come servizio predefinito, usare `--enable-upower` se se ne ha ha bisogno.
  * Aggiornate le traduzioni

### mate-menus

  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-panel

  * Corretta la dimensione dell'icona `showdesktop`.
  * Risolto l'utilizzo dell'API puntatore di GDK deprecata (GTK3)
  * Migrati tutti i `GtkStyle` a `GtkStyleContext` (GTK3)
  * Migrato `gtk_rc_parse_string` a `GtkCssProvider` (GTK3)
  * `GDK_KEY_*` è usato anche in Gtk+ 2.24.x
  * Rimosso il vbox da `panel-addto` perché è deprecato
  * Aggiornate le traduzioni
  * Vari bug eliminati
    * Controllo delle dimensioni allocate prima di creare il pixbuf dell'ombra nell'orologio.
    * Disconnect mostra e disattiva i segnali di menù prima di distruggere l'applet menù
    * Gestione di `SYSTEM_TRAY_CANCEL_MESSAGE`
    * Corretta la dichiarazione implicita della funzione di `gdk_x11_set_sm_client_id`
    * Aggiunta una gtkimage con il corrente pixbuf al button-widget
    * Utilizzo della cache per le icone gtk invece di una personalizzata

### mate-backgrounds

  * Aggiunti gli sfondi Ubuntu senza marchi
  * Aggiunti i nuovi sfondi MATE-Stripes-Dark.png, MATE-Stripes-Light.png

### mate-themes

  * Aggiunto il supporto per GTK 3.16, 3.14, 3.12, 3.10 and 3.8.
  * Aggiunti molti miglioramenti per le applicazioni MATE GTK3
  * Aggiunti effetti di transizione ai pulsanti e agli oggetti del menù quando si utilizza GTK3
  * Aggiunto il supporto per le applicazioni CSD
  * Aggiunto il supporto per popovers
  * Abilitata l'ombra delle finestre per le applicazioni CSD
  * Abilitate le icone regolari per i controlli delle finestre
  * Disabilitato l'utilizzo delle icone simboliche
  * Utilizzato il logo MATE per l'animazione spinner
  * Rielaborato GreenLaguna
  * Rielaborati i temi ContrastHigh
  * TraditionalOKTest è installabile con i normali flag configure
  * Molti altri ritocchi e rifininiture

### mate-notification-daemon

  * Vari bug eliminati
  * Aggiornate le traduzioni

### mate-control-center

  * Aggiunta una opzione per configurare la disposizione dei pulsanti della barra del titolo
  * Aggiunto il suporto per `metacity-theme-2.xml`
  * Aggiunto il supporto per le applicazioni di ufficio in Applicazioni Preferite
  * Migrazione ai cambiamenti nella API `MateRR*`
  * Aggiornate le traduzioni

### mate-screensaver

  * Migrazione ai cambiamenti nella API `MateRR*`
  * Aggiornate le traduzioni

### mate-menus

  * Rimosse le dipendenze di PulseAudio
  * Rimossi `gst-mixer` e `gst-mixer-applet`
  * Aggiorntato mate-volume-control:
    * Migratto da PulseAudio a `libmatemixer`
    * Permessa la selezione dei connettori di input e output
    * Il widget per il test degli altoparlanti adesso possiede un pulsante Chiudi
    * Gli elenchi dei dispositivi e degli stream adesso sono ordinati
    * Non vengono mostrate le icone su un pannello verticale
    * Consentito il clic su una finestra di popup
  * Aggiornate le traduzioni

### mate-power-manager

  * Aggiunto il supporto per `upower` 0.99+
  * Aggiornate le traduzioni
  * Rimossa la dipendenza da `udisks`

### mate-system-monitor

  * Introdotti i miglioramenti da GNOME System Monitor
  * Aggiornate le traduzioni
  * Vari bug eliminati

### Atril 

  * Aggiunto il supporto ePub
  * Aggiunto il supporto per la compressione xz
  * Aggiunta la rotazione con CTRL+Freccia Sinistra e CTRL+Freccia Destra nella modalità presentazione
  * Aggiunto il supporto per `bsdtar` al backend del formato per fumetti.
  * Aggiunto il supporto ai file `pdf.xz` al beckend PDF.
  * Aggiunto il supporto per i collegamenti esterni a  EvViewPresentation
  * Aggiunto EvBookmarks per gestire i segnalibri all'interno dei documenti
  * Aggiunto il supporto per le azioni OCG State al beckend PDF
  * aggiunto il salvataggio del fattore di zoom nelle impostazioni predefinite quando il ridimensionamento è libero
  * Aggiunta l'estensione `png` quando si salva un'immagine utilizzando il drag and drop
  * Aggiunto un parametro timesamp a SyncView
  * Aggiunto il file ini per Caja estension
  * Aggiunto il file appdata
  * Implementato `document_links_find_link_page()` nel backend PDF
  * implementato `document_links_find_link_page()` nel backend djvu
  * Migrato a `find_link_page()` invece di `find_link_dest()` in `get_dest_page()`
  * Corretta la memorizzazione della pagina corrente quando il documento è ricaricato in modalità presentazione
  * Corretta la risoluzione delle destinazioni con nome nel backend PDF
  * Corretto il problema di sidebar-thumbnails di connettersi al segnale di lavoro finito prima dello scheduling del lavoro
  * Corretta la visualizzazione dei glifi con trasparenza nel backend DVI
  * Corretti diversi problemi di sicurezza nel backend DVI
  * Corretti diversi problemi di accessibilità
  * Risolti vari segfault e molti memory leak
  * Aggiornato ai cambiamenti dell'API `poppler` 0.16.0
  * Migrato a `MateAboutDialog` da `libmate-desktop`
  * Aggiornate le traduzioni
  * Vari bug eliminati

### caja-extensions

  * Aggiunta la nuova estensione 'Imposta come sfondo'
  * Reintrodotta l'opzione per selezionare i plugin `send-to` da compilare
  * Aggiornate le traduzioni

### Engrampa

  * Aggiunte la compressione delle immagini iso e degli archivi tar dal manù di Caja
  * Aggiunta la finestra di dialogo di conferma della sovrascrittura quando si estraggono file con il drag & drop
  * Aggiunta la chiave keywords al file `.desktop`
  * Aggiunto il file ini per l'estensione di Caja
  * Aggiunto `engrampa.appdata.xml`
  * Corretta l'apertura di un file RAR all'interno di un file RAR
  * Corretti gli errori di apertura con alcuni file protetti da password
  * Coretto il caricamento degli archivi RAR multi-volume con 7zip
  * Eliminato il crash quando si preme Annulla in Aggiungi file
  * Risolto il problema  hyphen-as-minus-sign per la pagina man di `engrampa.1`
  * Risolti i memomy leak
  * Rimosso il supporto per Gtk+ < 2.24
  * Rimosso il supporto per Glib < 2.32
  * Utilizzo opzionale dello schema GSettings di Caja
  * Uso di `g_get_user_config_dir` ivece dell'hardcoded `~/.config/mate`
  * Uso di `GtkRecentAction objects` per creare il selettore dei file recenti
  * Non impostare la app selezionata come predefinita del sistema
  * Non impostare la finestra di dialogo "last output" come modale per permettere che l'utente lo possa ridimensionare 
  * Aggiornate le traduzioni
  * Vari bug eliminati

### Eye of MATE

  * Introdotti miglioramenti da Eye of GNOME
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-applets

  * Migrato a `MateAboutDialog` da `libmate-desktop`
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-netbook

  * Risolto  il problema dell'applet Window Picker che modifica forzatamente le impostazioni di Maximus
  * Migrato a `MateAboutDialog` da `libmate-desktop`
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-netspeed

  * Aggiunto il grafico del carico di rete e reso simile ai grafici di MATE System Monitor
  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-sensors-applet

  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-terminal

  * Migrato a funzioni comuni in `libmate-desktop`
  * Aggiornate le traduzioni

### mate-user-share

  * Aggiornate le traduzioni
  * Vari bug eliminati

### mate-utils

  * Aggiornate le traduzioni
  * Vari bug eliminati

### Mozo

  * Aggiornate le traduzioni

### Pluma

  * Migrato a `MateAboutDialog` da `libmate-desktop`
  * Aggiornate le traduzioni
  * Vari bug eliminati

### python-caja

  * Aggiunto il pulsante About Extensions alla scheda Extensions di Caja
  * Vari bug eliminati


<br/><br/>

