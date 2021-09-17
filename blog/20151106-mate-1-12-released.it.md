<!--
.. link:
.. description:
.. tags: Releases
.. date: 2015-11-05 20:00:00
.. title: Rilasciato MATE 1.12
.. slug: 2015-11-05-mate-1-12-released
.. author: Martin Wimpress
-->

Dopo 5 mesi di sviluppo il team di MATE Desktop è orgoglioso di annunciare
il rilascio di MATE Desktop 1.12. Vorremmo ringraziare ogni collaboratore ed ogni utente MATE.

![about](/assets/img/blog/about-mate-1.12.png)

## Cosa c'è di nuovo in MATE 1.12

I principali cambiamenti in MATE 1.12 sono:

  * Correzioni e miglioramenti per il supporto di GTK3 su tutto il Desktop MATE, incluso il supporto per GTK 3.18.
  * Il supporto al touchpad è significativamente migliorato e adesso supporta i tocchi multipli e lo scorrimento naturale.
  * Il supporto per più monitor è stato migliorato così le impostazioni del display utilizzano nomi in uscita e l'Interfaccia Utente consente di scegliere il monitor principale.
  * L'applet power adesso mostra informazioni sul modello e il venditore ed è quindi possibile distinguere tra più dispositivi alimentati a batteria.
  * Migliorata la gestione della sessione che adesso comprende l'inibizione dello screensaver mentre si riproducono elementi multimediali.
    * MATE adesso ascolta il namespace `org.gnome.SessionManager`.
  * Esteso il supporto a systemd.
  * Corretti bug di vecchia data assieme a molte piccole imperfezioni.
    * Ad esempio, le applet del pannello non sono più riordinate quando si cambia risoluzione dello schermo.
  * Traduzioni aggiornate e un certo numero di componenti adesso recuperano le stringhe di testo direttamente da `gschema` (richiede intltool 0.50.1).
  * Abbandonato il supporto per `win32` and `osx`.

I vari componenti di MATE 1.12 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.12/>

## Screenshots

  * [MATE 1.12 Screenshots](/gallery/1.12/)

## Changelog

Segue una analisi più dettagliata di ciò che è cambiato.

### mate-common

  * Supporto per `lcov` 1.12
  * Aggiornata la documentazione e gli esempi

### mate-desktop

  * Richiede `dconf` 0.13.4 e `xrandr` 1.3
  * Aggiunta una chiave `gsettings` per commutare lo scorrimento di sovrapposizione in GTK+3
  * Aggiunte alcune icone per correggere quelle mancanti in GTK+3 con tema di icone personalizzato
  * Mouse schema: abilitata l'emulazione del clic centrale come impostazione di default
  * RR: implementata la funzione mancante mate_rr_output_get_possible_crtcs
  * RR: risolta l'identificazione del laptop dal nome in output
  * RR: mostra il nome in output in aggiunta al nome visualizzato
  * Spostata la guida utente docbook in un progetto separato
  * Eliminata la dipendenza su yelp (non più necessaria dopo la rimozione della guida utente)

### libmatekbd

  * Aggiunta l'introspezione GObject
  * Layout della finestra di dialogo visualizza/stampa: rimosso il pulsante inutilizzato Aiuto
  * Layout della finestra di dialogo visualizza/stampa: alcuni miglioramenti sull'interfaccia utente

### libmatemixer

  * oss: Usare il contatore di modifica per il polling solo su Linux, è rotto sulle BSD
  * alsa: Corretto FTBFS con le vecchie versioni di ALSA
  * alsa: Corretta la dissolvenza

### libmateweather

  * Aggiornati i fusi orari per le località

### mate-icon-theme

  * Non compilare un file `pkgconfig`

### Caja

  * Finestra di dialogo connetti al server: aggiunto il supporto per AFP
  * Migliorato il supporto multi-monitor

### mate-polkit

  * Aggiunto il supporto per gli indicatori delle applicazioni GTK3

### Marco

  * Aggiunto il manuale e il piazzamento della finestra col puntatore
  * Uso di Alt-`per cambiare tra più finestre della stessa applicazione

### mate-settings-daemon 

  * Aggiunto una nuova combinazione di tasti per il logout (vuota per impostazione predefinita)
  * Impostazioni del touchpad: Aggiunti il supporto per lo scorrimento naturale, clic con 2 e con 3 dita
  * Mouse: utilizzo di `syndaemon -K` per ignorare Ctrl+C o altre combinazioni
  * GTK+3: fatto in modo che l'applet di tray xrandr supporti temi di pannello personalizzati

### mate-session-manager

  * Aggiunto il supporto per una Dock opzionale, come per esempio Plank
  * Aggiunto il supporto per la nuova `libsystemd` in aggiunta a quella esistente `libsystemd-login`
  * Attendere massimo 1 secondo per il logout o lo spegnimento
  * Attivare/disattivare lo scorrimento di sovrapposizione GTK+3 all'avvio utilizzando la nuova chiave gsettings

### mate-menus

  * Utilizzo di `pkg-config` per verificare python (richiede python 2.7)

### mate-panel

  * Richiede `xrandr` 1.3
  * Aggiunta l'opzione per mostrare/nascondere i numeri della settimana nel calendario
  * Risolto il posizionamento delle applet bloccate al cambio di risoluzione dello schermo
  * GTK+3: aggiunta una classe di stile perché le applet seguano `panel-menu-bar`

### mate-themes

  * Per tutti i temi GTK3: restyle dell'applet slider volume/luminosità
  * Migliorie e rifiniture varie per tutti i temi, in modo particolare per GTK 3.18.

### mate-notification-daemon

  * Corrette l'altezza e la visibilità dei temi in gtk3
  * Diverse correzioni ai temi

### mate-control-center

  * Aspetto: ripristinata la scheda Interfaccia
  * Display: aggiunto il supporto per impostare lo schermo primario
  * Display: mostrare i nomi di output oltre a quelli dei display
  * Combinazione di tasti: aggiunta combinazione per il logout
  * Impostazioni del touchpad: aggiunta l'opzione per attivare/disattivare il touchpad
  * Impostazioni del touchpad: Aggiunti il supporto per lo scorrimento naturale, clic con 2 e con 3 dita
  * Migliorata la categorizzazione
  * GTK+3: risolto il problema della visualizzazione del tipo di carattere in Aspetto e mate-font-viewer

### mate-screensaver

  * Aggiunto il supporto per `libsystemd` in aggiunta a quello esistente per `libsystemd-login`
  * Non sfumare al nero quando si blocca lo schermo
  * Corretta la gestione degli eventi di `systemd`

### mate-media

  * Molteplici correzioni nelle pagine man
  * GTK+3: aggiunte classi di stile per lo slider e il menù dell'applet del volume
  * GTK+3: Risolta la mancanza di alcune icone con un tema di icone personalizzato

### mate-power-manager

  * Richiede `xrandr` 1.3
  * Mostrare le informazioni di venditore/modello dei dispositivi hardware
  * Risolta la regolazione della retroilluminazione del Macbook Pro
  * GTK+3: supporto per i temi personalizzati
  * GTK+3: corretto il comportamento dell'applet della luminosità

### mate-system-monitor

  * SysInfo: Aggiunta la corretta identificazione per LinuxMint e LMDE
  * SysInfo: Concesso alle distribuzioni di definire una icona laterale personalizzata
  * Interfaccia: aggiunto il bordo a notebook
  * Aggiunto il supporto per `libsystemd` in aggiunta a quello esistente per `libsystemd-login`
  * Supporto per la compilazione con C++11
  * Rimossa la dipendenza da mate-icon-theme
  * Rimosso il supporto a C89

### Atril 

  * Abbandonato il supporto per `win32` and `osx` e `hildon`.
  * Rimossa la dipendenza inutile `mate-icon-theme`
  * Eliminato l'integrato MathJax in favore dell'utilizzo di una versione pacchettizzata per la distribuzione
  * Reso `smclient` obbligatorio

### caja-extensions

  * Corrette alcune stringhe di testo

### Engrampa

  * Corretto l'utilizzo di `ngettext` nella finestra di dialogo avanzamento
  * Fatto funzionare l'estrazione di archivi multipli in una cartella separata
  * Corretto il controllo di sovrascrittura quando i file da estrarre sono dentro ad una cartella

### Eye of MATE

  * Vari bug eliminati

### mate-applets

  * Accessx-status, geyes: hanno lo sfondo delle applet disegnato automaticamente
  * Cpufreq: reso cpupower la libreria predefinita
  * Rimossa l'inutile dipendenza da `mate-icon-theme`
  * GTK+3: Risolta la mancanza di alcune icone con un tema di icone personalizzato
  * GTK+3: cpufreq, charpick e drivemount suppotano temi di pannello personalizzati

### mate-netbook

  * Window Picker Applet: ha lo sfondo disegnato automaticamente

### mate-netspeed

  * Lo sfondo delle applet è disegnato automaticamente
  * Aggiunge regole silenziose

### mate-sensors-applet

  * Aggiunto il supporto per i sensori nvidia thermal e cooler (richiede libxnvctrl >= 256.25)
  * Aggiunto il plugin `mbmon`
  * Il plugin `udisks` interroga e cerca nuovi valori

### mate-terminal

  * Risolta l'opzione --tab che è stata rotta in 1.10.0
  * Abilitate le silent rules per impostazione predefinita
  * Abbandonato il supporto per `win32` and `osx`.

### mate-user-share

  * Eliminata la dipendenza inutile da `dbus-1`
  * Rimosso il supporto per Apache 2.0

### mate-utils

  * Aggiunta l'icona dell'applicazione a mate-system-log
  * Aggiunto il timestamp al posto del nome della finestra ai nomi predefiniti degli screenshot
  * Lo sfondo dell'applet dizionario è disegnato automaticamente
  * Corrette le traduzioni per gli schemi `gsettings`

### Mozo

  * Abilitate le notifiche all'avvio
  * Aggiunte regole silenziose

### Pluma

  * Aggiunta l'opzione `--enable-tests` per abilitare/disabilitare l'esecuzione di test durante la compilazione
  * Aggiunto un plugin per rimuovere gli spazi iniziali quando si salva
  * Riportato l'elenco dei plugin attivi nello script bugreport
  * Abbandonato il supporto per `win32` and `osx` e il plugin checkupdate
  * Convertito in lettera iniziale maiuscola Pluma nei titoli delle finestre e nel file desktop
  * GTK3: risolta l'anteprima di stampa
  * Corrette alcune annotazioni

### caja-dropbox

  * Aggiustata la directory predefinita di Caja extensions
  * incluso autogen.sh nei tarball

<br/><br/>

