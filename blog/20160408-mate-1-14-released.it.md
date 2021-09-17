<!--
.. link:
.. description:
.. tags: Releases
.. date: 2016-04-08 15:00:00
.. title: Rilasciato MATE 1.14
.. slug: 2016-04-08-mate-1-14-released
.. author: Martin Wimpress
-->

Dopo 5 mesi di sviluppo il team di MATE Desktop è orgoglioso di annunciare
il rilascio di MATE Desktop 1.14. Vorremmo ringraziare ogni collaboratore ed ogni utente MATE.

![about](/assets/img/blog/about-mate-1.14.png)

## Cosa c'è di nuovo in MATE 1.14

I principali cambiamenti in MATE 1.14 sono:

  * Supporto a GTK+3 migliorato in tutto il Desktop MATE.
  * Supporto completo a GTK 3.20 in tutti i temi di MATE
  * Le applicazioni Decorate dal Lato Client adesso vengono renderizzate correttamente in tutti i temi.
  * Portate le applicazioni MATE System Monitor e Mozo all'uso esclusivo di GTK+3.
  * La configurazione del touchpad adesso supporta in modo indipendente lo scorrimento dal bordo e con le due dita.
  * Le estensioni Python in Caja possono adesso essere gestite separatamente.
  * Sono selezionabili tutti e tre i metodi di focus delle finestre.
  * MATE Panel adesso ha la possibilità di modificare la dimensione delle icone della barra dei menù e degli elementi dei menù.
  * L'applet MATE NetSpeed è stata incorporata nel pacchetto MATE Applets.
  * MATE Terminal supporta l'API VTE 2.91 quando viene compilata per GTK+3.
  * Gli elementi OSD per il Volume e la Luminosità possono essere attivati/disattivati.
  * Le traduzioni sono state aggiornate. Grazie al nostro team di traduttori!

I vari componenti di MATE 1.14 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.14/>

## Screenshots

  * [MATE 1.14 Screenshots](/gallery/1.14/)

## Changelog

Segue una analisi più dettagliata di ciò che è cambiato.

### mate-common

  * Rimossi i riferimenti a componenti MATE obsoleti

### mate-desktop

  * Eliminati lo script di migrazione MateConf ed il vecchio strumento `mate-conf-import`
  * Corretto l'utilizzo deprecato di `GtkHBox` e `GtkVBox` compilando con GTK+3

### libmatekbd

  * Rimosso lo script di migrazione MateConf
  * Ridotti i warning di compilazione introspettiva
  * Corrette alcune deprecazioni di GTK+3
  * Aggiustamenti e pulizie varie

### libmatemixer

  * Richiesto PulseAudio 2.0 o successiva
  * Migliorato il controllo degli errori in molte parti
  * Risolti i limiti del volume in PulseAudio
  * Alcuni altri aggiustamenti su PulseAudio
  * Alcune correzioni e migliorie nei backend `alsa` e `oss`
  * Correzioni varie e pulizia

### libmateweather

  * Rimossi i flag di compilazione obsoleti
  * Piccolo fix nello schema

### mate-icon-theme

  * Aggiunte le icone `system-config-keyboard`

### Caja

  * Rimosso lo script di migrazione MateConf
  * Consentita la chiusura delle schede col clic del tasto centrale del mouse
  * Elencate le estensioni Python separatamente nell'elenco delle estensioni
  * GTK+3: aggiunte diverse classi di stile per semplificare l'applicazione dei temi
  * GTK+3: corretto il problema del lampeggiamento del desktop
  * GTK+3: diverse correzioni di codice deprecato
  * Correzioni varie e pulizia

### mate-polkit

  * GTK+3:Corrette diverse deprecazioni

### Marco

  * Rimosso lo script di migrazione MateConf
  * Risolti i problemi visualizzati dopo l'aver demassimizzato la finestra di Chromium
  * Corretta la descrizione della chiave GSettings compositing-fast-alt-tab (si menziona che essa disabilita le miniature)
  * Aggiornamento del sover di libmarco-private per la compilazione GTK+3
  * GTK+3: riaggiunta la possibilità di mostrare le miniature in alt-tab quando il compositor è attivo
  * GTK+3: Corrette diverse deprecazioni

### mate-settings-daemon 

  * Rimosso lo script di migrazione MateConf
  * media-keys: aggiunta l'impostazione per attivare/disattivare l'OSD
  * touchpad: supporto per lo scorrimento laterale e a due dita in modo indipendente (si utilizzano due chiavi GSettings indipendenti)
  * xsettings: aggiunte le impostazioni per modificare il tema e la dimensione del cursore
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### mate-session-manager

  * Rimosso lo script di migrazione MateConf
  * GTK+3: Corrette alcune deprecazioni
  * Correzioni varie e pulizia

### mate-menus

  * Spostato `mate-preferences-categories.menu` fuori da `mate-control-center`.

Questo file può essere pacchettizzato separatamente in modo che gli utenti possano decidere se preferiscono avere le categorie nel menù delle preferenze o no.

### mate-panel

  * Rimosso lo script di migrazione MateConf
  * Aggiunto un pulsante "Cancella" nella finestra di dialogo per ricaricare l'applet, e fatto in modo che il pulsante "Non Ricaricare" faccia ciò che dice (adesso non cancella l'applet in modo permanente)
  * Impostato come configurabile il numero massimo di segnalibri in un menù (prima che venga creato un sottomenù) mediante una chiave GSettings
  * Resa la dimensione delle icone degli elementi del menù configurabile mediante una chiave GSettings
  * Modificata la dimensione predefinita dell'icona della barra dei menù a 22 pixel
  * Eliminata *"Ubuntu hacks"* (l'opzione di compilazione `--enable-ubuntu`) poiché Ubuntu lo ha fatto molto tempo fa
  * GTK+3: aggiunte diverse classi di stile
  * GTK+3: aggiunti diversi nomi css per 3.20
  * GTK+3: Corretta la renderizzazione degli sfondi personalizzati con 3.18 e successive 
  * GTK+3: Corrette molte deprecazioni
  * Correzioni varie e pulizia

### mate-themes

  * Pieno supporto per GTK 3.20.
  * Le applicazioni Decorate dal Lato Client adesso vengono renderizzate correttamente in tutti i temi.
  * Migliorie e rifiniture varie per tutti i temi

### mate-notification-daemon

  * Rimosso lo script di migrazione MateConf
  * GTK+3: wrap del testo di notifica esplicito a 50 caratteri
  * GTK+3: stop al commutare i colori di primo piano/sfondo sul tema degli slider (utilizzare i colori
    dal tema corrente GTK+ così come è)
  * GTK+3: alcune ulteriori correzioni per il tema degli slider
  * GTK+3: Corrette alcune deprecazioni

### mate-control-center

  * Rimosso lo script di migrazione MateConf
  * Eliminata *"Ubuntu hacks"* (l'opzione di compilazione `--enable-ubuntu`) poiché Ubuntu lo ha fatto molto tempo fa
  * Spostato mate-preferences-categories.menu in mate-menus
  * Configurazione del touchpad: supporta in modo indipendente lo scorrimento dal bordo e con le due dita.
  * Proprietà delle finestre: resi selezionabili tutti e tre i metodi di focus delle finestre
  * GTK+3: corretta la preview del tema in mate-appearance-properties
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### mate-screensaver

  * Rimosso lo script di migrazione MateConf
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### mate-media

  * GTK+3: aggiunto il nome css `GvcMixerDialog` per 3.20
  * GTK+3: Corrette diverse deprecazioni

### mate-power-manager

 - Rimosso lo script di migrazione MateConf
 - Risolto un possibile crash quando fallisce una chiamata di funzione Xorg
 - GTK+3: corrette le deprecazioni nell'applet luminosità
 - Correzioni varie e pulizia

### mate-system-monitor

  * migrazione a GTK+3, rimosso il codice GTK+2 e l'opzione di compilazione `--with-gtk`
  * Impostata la versione minima di GTK+3 a 3.14, rimosso codice deprecato
  * Esegue il binario `gksu` invece che caricare `libgksu2.so` (che è solo per GTK+2)
  * Rimosso lo script di migrazione MateConf
  * Finestra principale: salva lo stato massimizzato in gsettings all'uscita e lo carica all'avvio
  * Dischi: aggiunto il salvataggio e il caricamento dell'ampiezza e della visibilità delle colonne
  * Proprietà dei processi: mostrato cgroups
  * Proprietà dei procssi: mostra N/A quando cgroups o selinux non è impostato
  * Tabella dei processi: viene mostrato lo stato di esecuzione quando il tempo della CPU varia
  * Cambiati i colori e i motivi delle linee griglia del grafico
  * Disegnato lo sfondo dei grafici esplicitamente per evitare problemi con GTK 3.20
  * Corrette alcune icone inesatte per alcune applicazioni come marco e vino
  * Correzioni varie e pulizia

### Atril

 * Rimosso lo script di migrazione MateConf
 * Aggiornato il copyright e si menziona il team MATE in Caja extensions
 * Uso del nome DBUS `org.gnome.SessionManager` per inibire lo screensaver
 * GTK+3: aggiunta la classe di stile atril-window al top level
 * GTK+3: aggiunto il nome css EggToolbarEditor per la versione 3.20
 * Correzioni varie e pulizia

### caja-extensions

  * Rimosso lo script di migrazione MateConf
  * GTK+3: Corrette alcune deprecazioni
  * Correzioni varie e pulizia

### Engrampa

  * Rimosso lo script di migrazione MateConf
  * risolto il crash casuale nella finestra di dialogo "apri come"
  * 7z: Risolto il problema con il carattere '?' nei nomi dei file
  * 7z: corretto il controllo per p7zip 15.09+
  * rar: Evitato il messaggio "Nessun file da estrarre" quando si disabilita la sovrascrizione dei file esistenti
  * tar: consentita la modifica dei contenuti dei file .txz (così come lo è per i file tar.xz)
  * unrar: Risolto il problema con il carattere '?' nei nomi dei file

### Eye of MATE

  * Rimosso lo script di migrazione MateConf
  * Uso del nome DBUS `org.gnome.SessionManager` per inibire lo screensaver
  * Caricamento automatico delle immagini non modificate se è cambiato il loro file
  * GTK+3: aggiunta la classe di stile eom-window al top level
  * GTK+3: aggiunto il nome css EggToolbarEditor per la versione 3.20
  * GTK+3: risolta la renderizzazione del formato SVG
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### mate-applets

  * Rimosso lo script di migrazione MateConf
  * Rimosso `null_applet` che oggi giorno non è neppure compilabile
  * Re-licenziate le applet command e timer sotto GPL-2+
  * Incorporata l'applet netspeed dal progetto mate-netspeed (e cessato lo sviluppo per quest'ultima)
  * GTK+3: corretta la renderizzazione dell'applet cpufreq
  * GTK+3: corretta l'impostazione dei colori di primo piano/sfondo ed il tipo di carattere nell'applet note adesive
  * GTK+3: Corrette diverse deprecazioni
  * Aggiustamenti e pulizie varie

### mate-netbook

  * Rimosso lo script di migrazione MateConf
  * GTK+3: Corrette alcune deprecazioni
  * Aggiustamenti e pulizie varie

### mate-netspeed

  * È stato inglobato al pachetto `mate-applets`.

### mate-sensors-applet

  * Aggiustamenti e pulizie varie

### mate-terminal

  * Supporto per l'API VTE 2.91 nella compilazione GTK+3
  * Compilate le espressioni regolari dingu con l'opzione MULTILINE
  * Corretto l'ordinamento errato di COLS e ROWS nella descrizione dell'opzione dalla riga di comando e nella pagina man
  * GTK+3: aggiunta la classe di stile mate-terminal
  * GTK+3: corrette le dimensioni della finestra per la versione 3.20
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### mate-user-share

  * Rimosso lo script di migrazione MateConf
  * Non tradotto il campo Keywords nei file .desktop
  * GTK+3: Corrette alcune deprecazioni

### mate-utils

  * Rimosso lo script di migrazione MateConf
  * Disabilitati gli effetti e le opzioni di ritardo nell'interfaccia utente di mate-screenshot quando viene lanciato con l'argomento -ai dalla riga di comando 
  * Utilizzato per impostazione predefinita il trattino al posto dei due punti nei nomi file degli screenshot
  * GTK+3: risolte molte deprecazioni e qualche problema all'interfaccia grafica
  * Non è più utilizzato il flag `-Werror` nella compilazione
  * Correzioni varie e pulizia

### Mozo

  * Portato a GTK+3 e GObject Introspection, abbandonato il vecchio codice relativo a PyGTK.

### Pluma

  * Rimosso lo script di migrazione MateConf
  * Implementata la chiusura delle schede con il tasto centrale del mouse
  * Aggiunta una nuova finestra di dialogo Configura per il plugin Controllo Ortografico
  * Reso funzionante lo strumento `switch-c` negli strumenti esterni
  * Corretta una potenziale iniezione di shell-code
  * GTK+3: aggiunte le classi di stile pluma-window e pluma-print-preview
  * GTK+3: Corrette diverse deprecazioni
  * Correzioni varie e pulizia

### caja-dropbox

  * Rifiniture minori
