<!--
.. link:
.. description:
.. tags: Releases
.. date: 2020-02-10 09:00:00
.. title: Rilasciato MATE 1.24
.. slug: 2020-02-10-mate-1-24-released
.. author: Wolfgang Ulbrich
-->

Dopo circa un anno di sviluppo il Team di MATE Desktop ha finalmente rilasciato MATE 1.24. Un grosso ringraziamento a tutti i collaboratori che hanno aiutato a renderlo possibile.

![MATE About dialog](/assets/img/blog/about-mate-1.24.png){ width=50% }

## Cosa c'è di nuovo in MATE 1.24

Questo rilascio contiene una gran quantità di nuove funzionalità, correzioni e miglioramenti generali. Alcuni dei più evidenti cambiamenti includono:

* Lo abbiamo fatto ancora, l'utilizzo dell'ambiente desktop MATE è più semplice di prima, una volta che l'utente avvia la sessione. Volete nascondere l'avvio delle applicazioni? Adesso potete impostare quali applicazioni mostrare all'avvio.
* **Engrampa** adesso ha il supporto per una manciata di formati aggiuntivi, assieme al supporto fisso per le password ed i caratteri unicode in alcuni di essi.
* **Eye of MATE** adesso ha il supporto per [Wayland](https://wayland.freedesktop.org/) e abbiamo aggiunto il supporto per i profili di colore integrati.
    * La generazione delle miniature è stata rivista e corretta in diversi punti.
    * Aggiunto il supporto per i file webp.
* Il nostro gestore delle finestre, **marco**, ha ricevuto una serie di modifiche:
    * Abbiamo reintrodotto una serie di decorazioni per le finestre per saziare la vostra nostalgia.
    * Abbiamo finalmente aggiunto i bordi per il ridimensionamento delle finestre trasparenti. Non occorre più sforzarsi per afferrare un bordo con il mouse!
    * Tutti i pulsanti della finestra (minimizza, massimizza, chiudi) adesso sono renderizzati in HiDPI.
    * I popup Alt+Tab ed il selettore degli spazi di lavoro sono stati _interamente_ riscritti. Adesso sono rappresentati in un meraviglioso stile OSD, sono più configurabili, e possono rispondere ai tasti freccia.
    * Affiancare le finestre da tastiera adesso consente di scorrere tra diverse dimensioni. Non c'è più bisogno di sentirsi costretti alla sola metà dello schermo.
* L'applet **Monitor di Sistema** ora ha il supporto per i dispositivi NVMe.
* La **Calcolatrice** adesso supporta l'utilizzo di "pi" o "π".
    * La notazione scientifica è stata migliorata.
    * Abbiamo apportato alcune correzioni per il supporto delle costanti fisiche predefinite.
* Il **Centro di Controllo** adesso mostra correttamente le sue icone sugli schermi HiDPI.
* È stato aggiunto un nuovo **Gestore dell'Orario e della Data**.
* L'app **Mouse** adesso supporta i profili di accelerazione.
* L'app **Applicazioni Preferite** è stata migliorata per l'accessibilità ed offre un maggiore supporto per l'integrazione con i client IM.
* L'**Applet Indicatore** ha una interazione leggermente migliorata con le icone dalle dimensioni non-ordinarie.
* Parlando di icone, quelle dell'applet network manager nei nostri temi sono state completamente ridisegnate e possono essere ammirate a pieno sui display HiDPI.
* Se siete il tipo di persone a cui non piace essere disturbati quando siete occupati, o state effettuando una presentazione, o magari state guardando un film, sarete lieti di sapere che il **demone delle notifiche** adesso supporta una modalità Non-Disturbare.
* Il **pannello di MATE** aveva diversi bug che causavano crash quando si cambiava la disposizione. Questi adesso sono stati corretti!
    * Il supporto per la compatibilità a [Wayland](https://wayland.freedesktop.org/) è stato considerevolmente migliorato. 
    * Le icone di stato (note come **area di notifica**, o **system tray**) hanno il supporto per i display HiDPI.
    * **Wanda il Pesce** ha subito un rifacimento e adesso può essere apprezzata nella pienezza di HiDPI
    * L'applet **elenco delle finestre** adesso supporta le miniature delle finestre al passaggio del mouse.
    * Diversi miglioramenti all'accessibilità attraverso il pannello e le sue applet essenziali.
* Se il vostro sistema non supporta [systemd](https://freedesktop.org/wiki/Software/systemd/) potreste essere interessati nel sapere che abbiamo aggiunto il supporto per [elogind](https://github.com/elogind/elogind)  sia a **MATE Screensaver** che a **MATE Session**.
* Abbiamo anche aggiunto una utility nuova di zecca: **MATE Disk Image Mounter**.
* **Mozo**, l'editor di menù, adesso supporta le azioni Annulla e Ripeti.
* I plugin di **Pluma** sono stati portati a Python 3.
* **Pluma** non deve più invidiare nulla dagli altri editor di testo complessi, perché adesso può mostrare i simboli di formattazione.
* i18n: tutte le applicazioni sono state migrate da intltools a gettext.



I vari componenti di MATE 1.24 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.24/>

## Maggiori dettagli

Seguono maggiori truculenti dettagli.

### atril
* Corretto l'alto consumo di memoria quando si esegue lo zoom
* Corretto il memory leak quando si creano le miniature e si annotano i testi
* Drag and Drop: Resettata l'azione `pressed_button` all'inizio dell'operazione di trascinamento
* Aggiunti più acceleratori sugli elementi del menù
* Rimossa la compilazione interna della libreria 'synctex', si utilizza solo la versione esterna fornita dai rivenditori software
* Corretta la Guida Utente in Greco che impedisce il completamento della compilazione del target
* Tiff backend: corretto il fallimento da TIFFReadRGBAImageOriented
* Tiff backend: Corretto un buffer overflow in tiff-document.c
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Migrazione a Python 3 per i test
* Richiesta GLib 2.54.0 o successiva
* Richiesta WebKitGTK-4.0 2.6.0 o successiva
* Richiesta Cairo 1.14.0 o successiva
* Eliminato il supporto a WebKitGTK-3.0
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/atril/commits/master/>

### caja
* Pronto per l'utilizzo di gcc 10
* fm-properties: Rimosso l'utilizzo dell'helper mate-desktop-thumbnail 
* Non inserire il simbolo hyphen nei nomi dei file
* Aggiunta una nuova interfaccia di estensione: l'API CajaWidgetViewProvider
* Aggiunto un nuovo oggetto: FmWidgetView
* Corretto un errore di grammatica riportato dai traduttori
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretto un crash di Caja quando si spostano file nella localizzazione per la lingua Coreana
* Utilizzo dell'opzione Mostra icone nella scheda visualizzazioni
* Aggiunta una opzione di configurazione per nascondere le icone nella visualizzazione ad elenco
* Aggiunte le icone mancanti a diversi elementi del menù
* Mostrate le miniature nella visualizzazione ad elenco
* Renderizzate più icone come cairo_surfaces per un miglior supporto HiDPI
* Riscritto il caricamento di CSS personalizzati in una funzione separata
* Aggiunto il supporto per verificare l'accessibilità dei file UI  utilizzando gla11y
* Ripristinato lo sfondo trasparente sulle etichette della vista ad icone
* Aggiunta la possibilità di scorrere le schede con la rotella del mouse per le proprietà del File e per le finestre delle preferenze di caja
* desktop: Forzata l'assenza del bordo sugli elementi del desktop come impostazione predefinita
* Modificati i prefissi degli URL da http a https
* caja-progress-info: aggiunti i suggerimenti alla finestra di dialogo trasferimento file
* Aggiunti nomi accessibili per i pulsanti nella finestra di dialogo per le operazioni di trasferimento
* eel: Rimosse le funzioni di data e orario
* caja-file: Corretta la finestra di dialogo per la sostituzione dei file che era incompleta
* caja-file-operations: Aggiunto un commento con avviso di falso positivo
* Corretti diversi memory leak un po' dappertutto
* i18n: Consentita la traduzione di più elementi dell'interfaccia grafica
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja/commits/master/>

### caja-dropbox
* Utilizzata CAJA_EXTENSION_DIR_SYS per memorizzare e mostrare la directory di sistema delle estensioni caja
* Mostrato il percorso completo di caja-extension-dir

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja-dropbox/commits/master/>

### caja-extensions
* caja-wallpaper-extension: corretto un memory leak
* image-converter: Riscritto da zero caja-image-resize.ui eliminando le deprecazioni
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Compilazione con gupnp 1.0 o 1.2.
* image-converter: non più utilizzate le icone inesistenti nei menù contestuali
* i18n image-converter: consentita la traduzione di seleziona un angolo nell'elenco a tendina
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja-extensions/commits/master/>

### engrampa
* Pronto per l'utilizzo di gcc 10
* fr-command-rpm: Utilizzato il file binario rpm2cpio fornito con il pacchetto rpm
* Aggiunta la sorgente rpm ai tipi-mime supportati
* 7z: Non impostare la cartella di lavoro, cioè utilizzare una directory temporanea
* Corretta la logica UI della pausa localizzata
* Zstandard: aggiornato il tipo MIME
* Ar: Aggiornato il tipo MIME ed aggiunti i numeri magici
* LHA: Corretto il tipo di dispositivo internet
* dlg-package-installer: mostrate le icone sui pulsanti della finestra di dialogo di errore 
* unace 2.5: non viene più mostrato il sommario dell'archivio nell'elenco dei file
* java-utils: rimossi gli spazi bianchi prima di leggere il nome di un pacchetto
* Aggiunto il supporto zcompress
* fr-command-unarchiver: Viene richiesta la password qualora fosse necessaria
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* Aggiornato il manuale a docbook 5.0
* Supportato il formato di pacchetto .udeb
* Mostrata la versione dell'applicazione sulla linea di comando
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/engrampa/commits/master/>

### eom
* Aggiunto eom-thumbnailer per i file webp
* thumbnail: Rimosso l'utilizzo dell'helper mate-desktop-thumbnail
* Abilitato il supporto a Wayland
* EomPrintPreview: Corretta la miniatura di anteprima sui display HiDPI
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Consentita la correzione del colore delle immagini con canale alpha
* Richiesta GLib 2.52 o successiva
* store: Aggiungere qualsiasi file immagine nella directory corrente allo store
* Aggiornato il manuale a docbook 5.0
* Utilizzata l'impostazione di pagine persistente
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/eom/commits/master/>

### libmatekbd
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Utilizzato gresources per i file UI
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmatekbd/commits/master/>

### libmatemixer
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmatemixer/commits/master/>

### libmateweather
* Locations: Aggiunta la stazione meteo di  Lleida–Alguaire Airport
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* locations: Modificata la stazione meteo per Rostov-on-Don, Russia
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmateweather/commits/master/>

### marco
* theme: Corretto il rendering hidpi del controllo della finestra per tutti i temi
* tabpopup: Completa riscrittura
* window: Aggiunta la possibilità opzionale di alternare tra più dimensioni di affiancamento
* Aggiunti più temi di decorazione delle finestre: Aggiunti  Atlanta, Esco, Gorilla, Motif, Raleigh
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretto l'utilizzo di RBGA visual in frame.c quando il compositing non è in uso
* Corretto lo spostamento delle finestre sui bordi per funzionare con i client CSD.
* Aggiunto il supporto per il sistema di compilazione meson
* Rese configurabili le colonne massime di alt+tab e considerata la larghezza dell'etichetta della finestra
* Aggiunto il bordo invisibile
* theme: corretto lo stato della finestra quando la si affianca dalla massimizzazione
* constraints: corretto un memory leak in meta_window_constrain()
* alt+tab popup: completa riscrittura
* Consentito l'utilizzo dei tasti freccia sù/freccia giù nel popup alt+tab 
* Corretti diversi memory leak
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/marco/commits/master/>

### mate-applets
* Pronto per l'utilizzo di gcc 10
* Utilizzata ${datadir}/dbus-1/system.d come directory di configurazione predefinita di D-Bus
* La cartella di dbus è stata resa configurabile
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Le build di cpufreq sono state rese indipendenti dalla versione degli header del kernel.
* geyes: Evitato un memory leak
* multiload: Supportati i dispositivi NVMe
* Fatto in modo che la command applet esegua i comandi in maniera asincrona
* Reso traducibile documenters nella finestra di dialogo informazioni
* Rese traducibili le note di copyright nella finestra di dialogo informazioni
* Ci siamo assicurati della corretta traduzione del titolo della finestra di dialogo informazioni 
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-applets/commits/master/>

### mate-backgrounds
* Abilitato il supporto per il sistema di compilazione meson
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-backgrounds/commits/master/>

### mate-calc

* Corretta la presentazione scientifica dei numeri complessi
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* mp-equation: Aggiornati i valori dalle costanti fisiche per farli corrispondere ai valori dei tooltip sui pulsanti matematici
* Aggiunti i tooltip delle unità alle costanti fisiche
* non ottenere il focus con il clic
* mp-equation: Aggiunte le costanti fisiche predefinite
* Utilizzato gresources per i file UI
* mp: corretto il risultato del calcolo ln(e^(i*π))
* mostrati piccoli numeri nella modalità scientifica
* mate-calc: Corretto un memory leak
* Aggiunto il supporto per "pi" oltre che per "π"
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-calc/commits/master/>

### mate-common
* Aggiornata la macro MATE_CXX_WARNINGS
* Impostati i flag di debug del compilatore in  MATE_DEBUG_CHECK
* Verificato che if AX_APPEND_FLAG e AX_CHECK_COMPILE_FLAG siano disponibili
* Aggiornata la macro mate-compiler-flags

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-common/commits/master/>

### mate-control-center
* Ricerca dei temi di sistema nelle cartelle dei dati di sistema
* display: abilitato il pulsante di aiuto
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Diverse icone sono state corrette per i display HiDPI
* font-viewer: Aggiunto font/collection ai tipi mime supportati
* font-viewer: Aggiunti i tipi mime font/ttf e font/otf
* Corretti i memory leak in diverse applicazioni
* mouse: Aggiunto il supporto ai Profili di Accelerazione
* at-properties: Migrazione da dbus-glib a gdbus
* Supportato lightdm-gtk-greeter-settings come programma per le preferenze di login
* Eliminata la dipendenza libXxf86
* Utilizzato python3 per gla11y
* Aggiunte le schede che possono essere alternate con la rotellina del mouse in diverse capplet
* Aggiunto il supporto per verificare l'accessibilità dei file UI  utilizzando gla11y
* Aggiunta una nuova applicazione per la gestione dell'orario
* Aggiunte le associazioni dei tasti del programma di messaggistica istantanea in mate-keybinding-properties
* default-applications: aggiunto un widget per un programma di messaggistica
* capplets: Utilizzato gresources per i file UI
* Migrazione da dbus-glib a GDBus
* Utilizzata le directory dei dati di sistema per localizzare le associazioni di tasti
* default-applications: Migliorata l'accessibilità dell'interfaccia grafica
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-control-center/commits/master/>

### mate-desktop
* Eliminata mate_desktop_thumbnail_scale_down_pixbuf()
* Aumentata la dimensione delle miniature a 256
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Gli schemi periferici rimanenti sono stati spostati in mate-settings-daemon
* schema: gli schemi del mouse sono stati spostati in mate-settings-daemon
* schemas: Definito lo schema per un programma di messaggistica predefinito
* Aggiunto del codice di prova per mate-languages.
* Aggiunto il supporto per il sistema di compilazione meson
* Corretti alcuni memory leak
* Implementazione di MateHSV (fork di GtkHSV)
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-desktop/commits/master/>

### mate-icon-theme
* Aggiunte le icone di stato per le connessioni di rete dei dispositivi mobili
* Rielaborate le icone per volume-status
* Aggiunte le icone per lo stato della rete vpn
* Aggiornate le icone dello stato della rete
* Aggiunte le icone per dropbox-status
* Aggiunta l'immagine mate/256x256/actions/mail-send.png
* Corretta l'immagine mate/22x22/devices/printer.png
* Aumentate le dimensioni delle icone 22x22px a 24x24px aggiungendo 1px ai bordi
* Utilizato un gradiente radiale (Sfocatura 13.9%, Opacità 73.4%) per l'ombra del logo MATE
* Aggiunta l'icona mancante per preferences-system-time
* Mostrata sui pannelli l'icona dello stato del volume con un contrasto migliorato
* Generate le icone dei tipi mime png dal tema Mate paper-sheets.svg 
* Generata preferences-system-time.png dal sorgente
* Generate le icone png dai sorgenti - tema di Mate, appliczioni, categorie e dispositivi
* Aggiornate le icone del terminale per il tema mate
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-icon-theme/commits/master/>

### mate-indicator-applet
* Ridimensionate le icone dell'indicatore per adattarsi al pannello
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-indicator-applet/commits/master/>

### mate-media
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* gvc applet: Aggiunte le traduzioni mancanti (i18n)
* Il volume scorre in incrementi configurabili come è possibile fare con i tasti multimediali
* Aggiunta l'interfaccia di scorrimento utilizzando la rotellina del mouse
* Consentito dissociare la statusicon o il panelapplet
* Abilitato un elemento di menù per il mute dell'output
* Aggiunta una nova vera applet di pannello
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-media/commits/master/>

### mate-menus
* Utilizzate datadir e libdir quando si installano i file gir
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-menus/commits/master/>

### mate-netbook
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Aggiunta una opzione per disabilitare il grassetto del titolo della finestra in una applet
* Resa nuovamente funzionante la caratteristica 'show-home-title'
* Modificata l'etichetta delle preferenze per la finestra dell'applet window picker, ed è stato aggiunto un tooltip
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-netbook/commits/master/>

### mate-notification-daemon
* Utilizzato gresource per mate-notification-properties.ui
* mate-notification-properties: Aggiunta la funzionalità non disturbare
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-notification-daemon/commits/master/>

### mate-panel
* Evitata la doppia descrizione a11y sui toplevel del pannello
* clock applet: aggiunta una chiamata a ATK per fornire l'orario attualmente visualizzato
* status-notifier: Migliorato il supporto HiDPI
* fish: Utilizzata un'immagine a risoluzione maggiore per Wanda the Fish
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* panel-toplevel: Corretta la disposizione delle applet sul pannello verticale esteso
* [clock-applet] Aggiunta l'interfaccia di scorrimento delle schede con la rotella del mouse
* Ulteriori miglioramenti per il supporto a Wayland
* Reso system-tray esclusivamente X11 
* Reso panel-struts esclusivamente X11 
* Reso panel-multimonitor pronto per Wayland
* Reso panel-background pronto per Wayland
* Reso panel-background-monitor esclusivamente X11
* Caricato e memorizzato quali piattaforme supportano le applet
* panel-addto supporta la disabilitazione delle applet
* Panel addto supporto a Wayland
* Corretto il caricamento della disposizione predefinita dopo il reset del pannello
* Corretti crash casuali quando si resetta il pannello
* window-list: mostrata la preview della finestra al passaggio del mouse
* Corretta la focus trap della tastiera per l'applet del pannello
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-panel/commits/master/>

### mate-polkit
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Migrazione da GSimpleAsyncResult a GTask
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-polkit/commits/master/>

### mate-power-manager
* icons: Aggiunte icone a risoluzione più alta
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Richiesto upower-0.99.8 o successivo
* Utilizzata up_client_get_devices2()
* Utilizzato gresources per i file UI
* Aggiunta l'interfaccia di scorrimento delle schede con la rotella del mouse
* Aggiunto una opzione di configurazione per disabilitare gli avvisi del mouse in scaricamento
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-power-manager/commits/master/>

### mate-screensaver
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Ci siamo assicurati che si blocchi alla sospensione e si sblocchi al resume
* Utilizzato gresources per i file UI
* Eliminata la dipendenza libXxf86
* Aggiunto il supporto ELOGIND
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-screensaver/commits/master/>

### mate-sensors-applet
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-sensors-applet/commits/master/>

### mate-session-manager
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretto il timeout con gnome-keyring 3.34
* Rimosso GNOME_KEYRING_LIFETIME_FD
* Corretta la scalatura verticale di mate-session-properties
* test-inhibit: Migrazione a gdbus
* Aggiunte la checkbox Show hidden e il flag gsettings.
* Nascoste le App da Non Visualizzare nelle applicazioni di avvio
* Corretti diversi memory leak
* Aggiunto il file hardware-compatibility
* Corretta l'impossibilità di recuperare la proprietà org.gnome.SessionManager.Renderer
* Aggiunti gli helper mate_session_check_accelerated
* Aggiunto il supporto ELOGIND
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-session-manager/commits/master/>

### mate-settings-daemon
* Richiesto DBUS 1.10.0 o successivo
* DBUS_SYS_DIR ha per valore predefinito ${datadir}/dbus-1/system.d
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* xrandr: Aggiunte icone più grandi per l'applet del vassoio
* Nascondi MATE Settings Daemon dal capplet Applicazioni di Avvio
* Aggiunti gli schemi periferici rimanenti da mate-desktop
* mouse: Aggiunto il supporto ai profili di accelerazione
* Modificato da 6 a 5 il passo del volume dei tasti multimediali  in gschema
* Eliminata la dipendenza libXxf86
* manutenzione dei plugin: Ottimizzazione del codice
* media-keys: Eseguire l'applicazione di messaggistica istantanea di default definita da schema
* locate-pointer: Non afferrare il pulsante del puntatore quando si cerca di individuarlo
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-settings-daemon/commits/master/>

### mate-system-monitor

* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Richiesta GLib 2.56.0 o successiva
* Migliorato il supporto a HiDPI
* Aggiunte le informazioni di I/O del disco nelle sezioni uso e preferenze
* Corretti alcuni memory leak
* Aggiunto l'IO del disco alle informazioni sul processo
* Mostrate le informazioni sulla GPU sulla scheda Sistema
* Supportati fino a 32 CPU
* Mostrato lo spazio disponibile sul disco in ZFS
* Mostrate la release di OpenIndiana e le informazioni sul kernel nella scheda Sistema
* Mostrati il sysname, il rilascio e la versione di FreeBSD nella scheda Sistema
* Corrette le informazioni della rolling release openSUSE Tumbleweed
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-system-monitor/commits/master/>

### mate-terminal
* Pronto per l'utilizzo di gcc 10
* Corretti diversi memory leak
* terminal-screen: corretto il warning quando si chiude la finestra
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Reso configurabile "evidenzia ciò che è sotto il puntatore del mouse" 
* Mostra la finestra di dialogo di conferma se, alla chiusura, ci sono più schede aperte
* Aggiornato il manuale a docbook 5.0
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-terminal/commits/master/>

### mate-user-guide
* Aggiornata la sezione come riportare un malfunzionamento
* Rimossa la sezione custom-command-options e gestita la sintassi
* Aggiornata la sezione applicazioni preferite
* Sostituiti i link docbook con xref e corretto un attributo linkend (#30)
* Aggiornato il manuale a docbook 5.0
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-user-guide/commits/master/>

### mate-user-share
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretta la notifica di configurazione di HTTPD
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-user-share/commits/master/>

### mate-utils
* Pronto per l'utilizzo di gcc 10
* Utilizzato gresources per i file UI
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Aggiunta l'utility MATE Disk Image Mounter
* logview: Utilizzata la rappresentazione di data e ora preferita per il locale corrente
* Aggiunte le schede che possono essere alternate con la rotellina del mouse
* Resi opzionali inkscape e rsvg-convert
* Corretti alcuni memory leak
* Rigenerate le icone png dai file svg
* Aggiornato documenters nella finestra di dialogo informazioni
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-utils/commits/master/>

### mozo
* Aggiunti i pulsanti Annulla e Ripeti
* Corretto il drag and drop creando delle copie di un oggetto, corretto l'annullamento e la ripetizione e un crash quando si aggiorna la visualizzazione
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Aggiunto il supporto per il sistema di compilazione meson
* Corretta la creazione di nuovi menù ed elementi del menù
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mozo/commits/master/>

### pluma
* Aggiunta la capacità di mostrare i caratteri non stampabili (spazio/tab/newline)
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* window: non sovrascrivere GdkWindowStatere
* Corretti alcuni memory leak
* Corretta la compilazione con GtkSourceView 3.22
* spell-checker plugin: Aggiunta una traduzione mancante (i18n)
* Aggiunto il supporto per verificare l'accessibilità dei file UI  utilizzando gla11y
* Aggiunto uno snippet per aggiungere o rimuovere un commento
* pluma-print-preview: Corretto un warning: espressione identica
* Conversione a Python 3
* Manual: Aggiornato come si può aprire pluma dal menù
* Aggiornato il manuale a docbook 5.0
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/pluma/commits/master/>

### python-caja
* Pronto per l'utilizzo di gcc 10
* Eliminato il supporto per Python 2
* Aggiunto il supporto per compilare utilizzando Python 3.9
* i18n: Migrazione da intltools a gettext
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/python-caja/commits/master/>
