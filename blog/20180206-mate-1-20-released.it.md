<!--
.. link:
.. description:
.. tags: Releases
.. date: 2018-02-07 09:00:00
.. title: Rilasciato MATE 1.20
.. slug: 2018-02-07-mate-1-20-released
.. author: Martin Wimpress
-->

Dopo 11 mesi di sviluppo il team di MATE Desktop è soddisfatto di annunciare
il rilascio di MATE Desktop 1.20. Vorremmo ringraziare ogni collaboratore MATE per il suo aiuto nel rendere possibile questo rilascio.

![about](/assets/img/blog/about-mate-1.20.png)

## Cosa c'è di nuovo in MATE 1.20

Il tema di questo rilascio è stato stabilizzare il Desktop MATE sostituendo
il codice deprecato e modernizzando ampie sezioni del codice base. Abbiamo anche
migliorato il nostro gestore delle finestre (Marco) e aggiunto il supporto per HiDPI. In tutto ciò
abbiamo eliminato centinaia di bug. Li abbiamo schiacciati!

I principali cambiamenti in MATE Desktop 1.20 sono:

  * **MATE Desktop 1.20 supporta gli schermi HiDPI con rilevamento e scalatura dinamici.**
    * Gli hint HiDPI per le applicazioni Qt sono anche portati sull'ambiente per migliorare l'integrazione tra i toolkit.
    * Alternando le modalità HiDPI attiva il ridimensionamento e lo dinamici. Non occorre eseguire il log out/in
  * **Marco adesso supporta [DRI3 and XPresent](https://lwn.net/Articles/569701/)**, se disponibile.
     * I frame rate utilizzando Marco sono significativamente accresciuti.
  * Marco adesso supporta **l'affiancamento con trascinamento al quadrante**, i tasti cursore possono essere utilizzati per spostarsi nel selettore <kbd>Alt</kbd> + <kbd>Tab</kbd> e sono state aggiunte scorciatoie da tastiera per spostare le finestre su un altro monitor.
  * È stato aggiunto il **supporto per i provider Global Menu** come [vala-panel-appmenu](https://github.com/rilian-la-te/vala-panel-appmenu).
  * MATE Panel ha molto migliorato il supporto per gli [elementi notificatori di stato (SNI)](https://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/)
  * **I Bookmark adesso supportano le posizioni GTK3+**.
  * Il Terminale di MATE adesso supporta le immagini di sfondo, aggiunge temi solarizzati e combinazioni di tasti per navigare tra le schede.
  * **Atril, il visualizzatore di documenti, ha subito una massiccia revisione** ed è migliorato in ogni singolo aspetto. Sì, in ogni modo. Migliore!
    * In particolare è stato considerevolmente migliorato il supporto per gli utenti con limitazioni visive.
    * È stata aggiunta la navigazione con il cursore.
  * L'**applet Invest è stata rimossa** da MATE Applets.
    * L'API, fornit da Yahoo, non è più attiva e no c'è un candidato valido per la sua sostituzione.
  * Le applet del Pannello adesso si ridimensionano in modo corretto in base alle unità mostrate e molti grafici sono riproporzionati in modo dinamico.
  * **I temi di MATE hanno visto significativi miglioramenti** per implementare completamente tutte le classi di stile esposte da GTK 3.22
  * Engrampa, il visualizzatore di archivi, ha migliorato il supporto agli archivi 7z cifrati.
  * MATE Sensors Applet (finalmente) supporta udisks2.
  * L'autenticazione OpenBSD è supportata in MATE Screensaver, e minizip in Atril supporta più varianti BSD.
  * Le traduzioni sono state aggiornate. *Grazie al nostro team di traduttori!*
  * E per i manutentori delle distribuzioni abbiamo aumentato i requisiti minimi di GTK3+ e GLib.
    * Sono richiesti GTK 3.22 e GLib 2.50 o successivi per compilare il Desktop MATE 1.20.
  * Potreste trovare qualche riferimento a Wayland nel changelog più oltre, non eccitatevi troppo. Non è quello che credete `:-)`

I vari componenti di MATE 1.20 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.20/>

## Changelog

Ecco tutti i dettagli raccapriccianti.

### mate-desktop 1.20.0

  * Aggiunto gsettings per il fattore di ridimensionamento della finestra
  * eliminati alcuni controlli aggiuntivi per la versione minima di GLib
  * rimosse le porzioni di codice < gtk+-3.22 e spinta la versione gtk+ richiesta
  * schema: eliminata la chiave can-change-accels, non funzionerà con GTK+3
  * Implementazione di WidthOfScreen e HeightOfScreen
  * eliminato `MateAboutDialog`
  * mate-about: rimossi le rimanenze dei riferimenti libunique
  * mate-about: passaggio a `GtkAboutDialog`
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor` functions:
  * evitata la deprecata `gdk_screen_get_width/height`
  * mate-desktop-item: mate-about: evitata la deprecata `gtk_show_uri`
  * mate-about: evitata la deprecata  `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_n_monitors`
  * evitata la deprecata `gdk_screen_make_display_name`
  * evitata la deprecata `gdk_screen_get_number`
  * Corrette piccole imprecisioni in `man mate-about`
  * Fissato il cursore di fallback rotto in `mate-colorsel.c`
  * mate-colorsel: non usata la deprecata `GTK_STOCK_COLOR_PICKER`
  * Aggiunto il supporto al Global Menu
  * Aggiornate le traduzioni

### mate-user-guide 1.20.0

  * Aggiornate le traduzioni

### libmatekbd 1.20.0

  * rimosse le porzioni di codice < gtk+-3.22 e spinta la versione gtk+ richiesta
  * Implementazione di WidthOfScreen e HeightOfScreen
  * matekbd-status: risolto il warning  Gdk-CRITICAL quando si crea l'icona nella barra di stato
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor` functions:
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_get_number`
  * matekbd-indicator: non espandere
  * matekbd-indicator: non utilizzata la deprecata `gdk_cairo_create`
  * Corretto lo strano comportamento di GtkIconInfo
  * matekbd-indicator: non utilizzata la deprecata GtkAlignment
  * keyboard-drawing: impostato il nome css matekbd-keyboard-drawing
  * Leggermente incrementata la dimensione del carattere per le etichette dei tasti
  * matekbd-keyboard-drawing: non disabilitare il double buffering
  * matekbd-keyboard-drawing: gestita la funzione `XkbGetKeyboard()` che fallisce
  * matekbd-keyboard-drawing: Evitato che keynav perda il focus
  * Risolti alcuni warning di introspezione
  * show-layout.ui: non utilizzati widget deprecati
  * UI: espansa la kbddraw vertical
  * Aggiornate le traduzioni

### libmateweather 1.20.0

  * Località: aggiunta Radom, Polonia
  * Località: aggiunto l'aeroporto Zhukovsky (Mosca, Russia)
  * Locations: corretto il nome dell'aeroporto Sheremetyevo (Mosca, Russia)
  * Aggiunto il timeout, invalidare effettivamente la sessione in weather_info_abort
  * Iniziato a ridurre lo spam meteo creando un taglio iniziale della funzione `weather_info_equal()`
    che aiuterà le app a determinare se due istanze WeatherInfo sono 'la stessa'
    da non preoccupare con una notifica
  * Rimosso il warning su bsun non utilizzato controllandone il valore
  * Risolto il warnng di deprecazione `soup_session_async_new()`
  * Aggiunte le città mancanti Polacche con gli aeroporti
  * Corretta la fascia oraria di Novosibirsk
  * Aggiunto Ceiba in Porto Rico
  * doc: eliminati i vecchi riferimenti a MateConf e qualche altro aggiustamento
  * Aggiornate le città del Kazakistan.
  * controllato il valore della variabile `$GIO_REQUIRED`
  * Aggiornate le traduzioni

### mate-icon-theme 1.20.0

  * Sostituite alcune flag rotte
  * Aggiornate le traduzioni

### caja 1.20.0

  * eliminato il CSS per GTK+ 3.14
  * Risolto il cambio dell'icona di tasklist quando si apre una nuova scheda
  * Inclusi i file locali con "" invece che con <>
  * `search_dispose` e `search_finilize` non possono essere eseguiti dopo la fine di una ricerca
  * Aggiunta l'icona della finestra mancante alla finestra di dialogo Informazioni delle estensioni
  * spostato libegg in cima a srcdir ed eliminati alcune rimanenze
  * Implementazione di WidthOfScreen e HeightOfScreen
  * caja-places-sidebar: risolto il problema del rifiuto all'unmount quando la barra laterale è ampia
  * caja-places-sidebar: disabilitata la barra di scorrimento di sovrimpressione
  * Risolto: cattivo comportamento col tasto "invio" quando restano file nella vista ad elenco
  * Aprire una cartella in una nuova finestra: <kbd>ctrl</kbd> + <kbd>shift</kbd> +<kbd>w</kbd>
  * zoom-control: è possibile modificare l'ingrandimento con la rotellina del mouse sul pulsante
  * Visualizza -> Colonne visibili: risolta l'espansione verticale del contenuto della finestra di dialogo
  * Riformulata un po' la descrizione della colonna Dimensione su Disco
  * Risolto: il comportamento sbagliato di <kbd>shift</kbd> + <kbd>canc</kbd> mentre rimangono dei file
  * icon.dnd: rimossa la cornice di evidenziazione hardcoded
  * Risolto: alto utilizzo del cpu quando si carica l'immagine di sfondo
  * vista ad elenco: risolto il problema dei margini delle icone larghe quando si esegue lo zoom out
  * Fatto in modo che il ridimensionamento dello sfondo del desktop funzioni in tutti i monitor
  * rimosso l'attributo bizzarro +x da un file sorgente
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor` functions:
  * Aggiunte colonne autoridimensionanti
  * Fatto in modo che tutte le colonne alla variazione dello zoom si aggiornino
  * Forzato il ridisegnamento dei widget grafici quando si zooma
  * barra del percorso: abilitato lo scorrimento con la rotellina del mouse come avveniva con GTK+2
  * libcaja-private: rimosso il collegamento errato dal README interno
  * privato: Assicurarci che si consenta di lanciare i file .desktop da symlink fidati
  * Risolto: il ridimensionamento dello sfondo del desktop non funziona
  * open-with-dialog: impostato max-char-width per una etichetta
  * Risolto il problema con la finestra di dialogo "Apri con" il testo del pulsante non era ben allineato
  * evitata la deprecata `gdk_screen_width/height`
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_make_display_name`
  * libegg: sostituita la deprecata `gtk_drag_begin`
  * eggsmclient: risolto un warning in compilazione a causa di -Wcomment
  * Non più utilizzata la dedprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * Risolto l'esplorazione/autorun di un dispositivo al suo inserimento
  * risolto lo scorrimento verticale nella Vista compatta in `fm_icon_view_scroll_event()`
  * property-browser: aggiunta una classe di stile cornice a scrolledwindows
  * Risolto l'errore off-by-one in `caja-pathbar.c`
  * funzionalità aggiunta: presentare la dimensione su disco dei file quando si mostra la dimensione del file
  * ripristinata l'inizializzazione dell'interfaccia DBus
  * CSS: caricare un caja-desktop.css differente con GTK 3.14
  * Utilizzo della posizione dei bookmark gtk+-3
  * finestra Apri con: forzata la dimensione dell'icona
  * file: fatto in kmodo che `caja_file_get_gicon` restituisca anche le icone personalizate
  * Espansa l'ampiezza della grigia al canvas
  * utilizzo di `atk_component_get_extents` invece di `atk_component_get_position`
  * non analizzare manualmente i file .hidden - GIO lo fa sin dalla 2.36
  * Non si controlla più la variabile di ambiente `MATE22_USER_DIR`
  * Non si controlla più l'inesistente directory `~/.mate2`
  * eel-accessibility: rimossi il codice inutilizzato e i commenti obsoleti
  * mostrato il corretto menù di tasto destro dopo aver effettuato una selezione
  * eel: La Coda si ridimensiona sulla canvas quando gli elementi cambiano visibilità
  * Aggiunto size_request a IconContainer per gestire il riposizionamento non necessario.
  * IconCanvasItem: risolta la sovrapposizione dei filename al passaggio del mouse
  * eel: rimosso l'#include con condizione non necessario
  * eel: rimosso del codice non utilizzato da eel-gdk-pixbuf-extensions
  * risolto un warning di compilazione (lì non è necessario const )
  * risolta la compilazione con gcc 4.9.2 (sembra che sia in modalità c89 per default)
  * ricerca: aggiunto il supporto dei tag (xattr::xdg.tags).
  * Risolta la rinominazione dei file nella vista ad elenco selezionando la cella del nome del file. 
  * property-browser: aggiunta una classe di stile cornice a scrolledwindows
  * caja-application.c: c'era una variabile non inizializzata
  * Aggiornate le traduzioni

### mate-polkit 1.20.0

  * eliminata la libreria polkitgtkmate e la sua documentazione
  * Risolto mostra/nascondi l'icona con statusnotifier
  * status-icons: non utilizzare le icone di stock
  * polkitmateauthenticationdialog: evitato il deprecato GtkAlignment
  * polkitmateauthenticationdialog: sostituita una deprecazione GTK_STOCK
  * Aggiornate le traduzioni

### marco 1.20.0

  * compilazione: eliminata la richiesta non necessaria pangoxft
  * Piccolo bugfix per move_to_X keybinds
  * Eliminato un bug per monitor di diverse dimensioni
  * Ristrutturate le associazioni di tasti del monitor ed aggiustato `save_rect`
  * Implementata una sorciatoia da tastiera per spostare la finestra su un altro monitor
  * schema: eliminato un errore di battitura
  * compositor: non disegna più una finestra che non è visibile
  * risolto un risultato sbagliato in `meta_window_titlebar_is_onscreen()` per le finestre senza cornice
  * Aggiunto il supporto per l'evento gtk3 `_GTK_SHOW_WINDOW_MENU` 
  * Elaborata una soluzione più elegante per gestire le nuove associazioni di tasti per move-to-workspace
  * Implementata una impostazione per disabilitare l'affiancamento verticale
  * Implementato un tabpopup quando si muove una finestra in spazi di lavoro differenti
  * keybindings.c: Risolto un warning di compilazione:
  * Resettare tile_rsized a falso quando si è a schermo intero
  * Risolte le finestre che non vanno a `save_rect` quando si demassimizzano
  * Consentito il ridimensionamento orizzontale e verticale quando si utilizza l'affiancamento angolare
  * Risolto il problema della finestra che viene reimpostata a saved_rect quando si esce dall'affiancamento angolare
  * Aggiunte associazione di tasti per l'affiancamento agli angoli
  * Implementato l'affiancamento agli angoli con il trascinamento del mouse
  * Implementazione di WidthOfScreen e HeightOfScreen
  * Le regioni XFIXES trapelano durante la fase paint_windows
  * Aggiunta una logica più stringente per l'esecuzione senza il supporto di XPresent
  * Reso XPresent opzionale
  * aggiunti alcuni cambiamenti da xfwm4
  * Annullato il flag present_pending in caso di erroring out
  * Supporto all'estensione XPresent
  * Memorizzato un flag quando l'utente ridimensiona dall'affiancamento
  * Consentito il ridimensionamento orizzontale delle finestre affiancate
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * evitata la deprecata `gdk_screen_width/height`
  * evitata la deprecata `gdk_screen_get_width`
  * display: non utilizzare la deprecata `GDK_DEVICE_MANAGER`
  * tools: rimossi marco-mag e marco-grayscaletools
  * risolto un problema nella finestra riassuntiva dei associazioni di tasti/button-grab
  * Forzato il fattore di scala 1 per il gestore delle finestre anziché quello predefinito o configurato dall'utente.
  * Evitata la deprecata `gdk_display_get_screen`
  * evitata la deprecata `gdk_screen_get_number`
  * Alt/tab - definiti i codici dei tasti freccia + frecce sul tastierino numerico
  * Consentito l'utilizzo delle frecce quando si è nel popup <kbd>Alt</kbd> + <kbd>Tab</kbd>
  * UI: Risolta la costruzione dell'oggetto non valido nelle cornici
  * README: corretti i nomi delle chiavi GSettings
  * associazione di tasti: rimosso il carattere maiuscolo dal "spazio di lavoro corrente"
  * Aggiunti tasti chiave per rinominare lo spazio di lavoro corrente
  * risolte alcune deprecazioni nel codice
  * Aggiornate le traduzioni

### mate-settings-daemon 1.20.0

  * HiDPI: Caricamento di xsettings durante la fase di inizializzazione
  * Aggiunta la configurazione di HiDPI in XSettings
  * Aggiunto il supporto ai monitor HiDPI
  * plugin: `G_GNUC_UNUSED` messo tra le variabili inutilizzate ma necessarie
  * xsettings: eliminato can-change-accels, che non funzionerà con GTK+3
  * msd-datetime-mechanism.c: risolti i warning di compilazione:
  * msd-mpris-manager.c: risolti i warning di compilazione:
  * configure.ac: eliminato `GLIB_VERSION_MAX_ALLOWED`
  * Aggiornate le traduzioni

### mate-session-manager 1.20.0

  * gsm-manager.c: risolti i warning di compilazione:
  * non far perdere il focus quando si mostrano le finestre di dialogo di disconnessione o di arresto
  * aggiunta la classe di stile `logout-dialog`
  * Evitata a deprecata `gdk_screen_make_display_name`
  * non più utilizzata la deprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * systemd user-session è stato aggiornato per ottenere tutti gli ambienti definiti dall'utente all'avvio della sessione.
  * dbus è stato aggiornato per ottenere tutti gli ambienti definiti dall'utente all'avvio della sessione.
  * Aggiornate le traduzioni

### mate-menus 1.20.0

  * spinto gio alla versione 2.50.0
  * Fatto il collegamento simbolico mate-applications-merged
  * Aggiornate le traduzioni

### mate-panel 1.20.0

  * Supporto per l'auto ridimensionamento del pannello per display HiDPI
  * innalzato il requisito minimo per libwnck a 3.4.6
  * status-notifier: non va in crash quando il tooltip ha il tipo sbagliato
  * status-notifier: non va in crash quando il layout del menù ha il tipo sbagliato
  * Risolto il rendering dei pulsanti radio nel notificatore di stato
  * panel-run-dialog: risolto un segfault quando l'elenco dei programmi è abilitato
  * ottiene il focus quando viene mostrata la finestra di dialogo "applet rotta"
  * Aggiornata la finestra di dialogo delle proprietà del selettore degli spazi di lavoro
  * semplificato del codice
  * rielaborato il processo di cancellare l'operazione per il cambio dello sfondo
  * status-notifier: gestito corrttamente il caso NULL per gli elementi
  * status-notifier: gestita le icone dalle dimensioni errate chiamate per percorso
  * status-notifier: caricamento delle icone specificate dal percorso
  * Risolti i problemi di caricamento delle icone quando l'applicazione chiama un percorso e non un nome di icona
  * Risolto un warning di compilazione: `toplevel_configure_event` definito ma non utilizzato
  * Risolto un warning di compilazione: ridefinito `GLIB_VERSION_MIN_REQUIRED` 
  * status-notifier: risolto il problema di mostrare l'icona per un'icona mancante
  * implementazione di WidthOfScreen e HeightOfScreen
  * panel-toplevel: rimosso il controllo dei confini del puntatore in `panel_toplevel_queue_auto_hide()`
  * rimossi vecchi residui di gnome-panel
  * mantenute le icone corrette sul fondo quando la risoluzione diventa più larga
  * wncklet: scollegare i segnali dai dati alla distruzione
  * clock: disconnettere uno o più gestori di segnali alla distruzione
  * panel-applet-frame-dbus-c: commentate la nuova variabile non utilizzata
  * Clock: non verificare che siano < 0 quelle variabili che non possono mai essere < 0
  * panel-applet-frame-dbus.c: commentato un blocco di codice mai utilizzato
  * panel-toplevel: rimosso blocco break duplicato
  * status-notifier: rimosso controllo duplicato trovato da cppcheck
  * status-notifier: nascondere l'icona mate-polkit se è passivo
  * Applicata una correzione sulla posizione del popup per GTK 3.20 e precedenti
  * GTK 3.22 status notifier: riposizionato il menù quando cambia la dimensione
  * GTK 3.22/status-notifer: Corretta la posizione del menù se la dimensione è cambiata dall'ultima volta che è stato mostrato
  * Fermato il collasso verso sinistra all'aggiunta di certe applet fuori-processo
  * resi nuovamnte funzionanti i lanciatori di file/cartelle
  * panel-context-menu: Aggiunto un dialogo di conferma all'opzione di reset del pannello
  * Aggiunta l'opzione di resettare il pannello al menù contestuale
  * clock: disconnettere i gestori di segnali alla distruzione
  * Risolto un crash quando si spostano/rimuovono le applet con glib 2.53.4 o successiva
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * Aggiunta una ciave gsettings per abilitare/disabilitare il Supporto SNI
  * wncklet: eliminati i segfault e i warning sulla rimozione dello switcher in esecuzione, window-list
  * fish: risolta l'aggiunta dello sfondo dopo la rimozione
  * Fish: eliminati tutti i warning sulla rimozione quando viene costruito in esecuzione
  * clock:  corretti i warning di rimozione quando una applet in-esecuzione viene rimossa
  * clock: eliminato il segfault rimuovendo una applet quando viene costruita in esecuzione
  * libmate-panel-applet: corretti degli errori di battitura nel rinominare id->factory_id
  * libmate-panel-applet: dichiarare `_panel_applet_shlib_factory()` solo quando occorre
  * libmate-panel-applet: corretto un errore nel deregistrare  l'oggetto dbus
  * libmate-panel-applet: corretto n warning di compilazione
  * libmate-panel-applet: corretta l'introspezione
  * libmate-panel-applet: nome del bus non posseduto deregistrazione dell'oggetto dbus
  * libmate-panel-applet GTK 3.14/3.16 risolto lo sfondo personalizzato con alpha
  * libmate-panel-applet: aggiunta una variabile dummy in factory per certe applet
  * libmate-panel-applet: risolta la renderizzazione dello sfondo per le applet in esecuzione
  * libpanel-applet/panel-applet.h: rinominato  id in `factory_id` per factory
  * limatepanel-applet: aggiunto panel-applet-private.h
  * non più utilizzata GtkPlug/GtkSocket per le applet in esecuzione
  * reso possibile ottenere il widget dell'applet
  * libpanel-applet: aggiunto `panel_applet_factory_get_applet_widget`
  * libpanel-applet: ritornato il tipo di processo e l'uid dell'applet
  * libpanel-applet: memorizzate le factory in hash-table
  * libpanel-applet: ritardata la creazione di GtkPlug
  * libpanel-applet: aggiunto il tipo di processo ai dati privati
  * libpanel-applet: rimosso `out_process` da `panel_applet_factory_main()`
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_get_n_monitors`
  * fish: risolta l'apertura come linea sottile quando viene costruito in processo
  * Forzato il fattore di scala 1 per il gestore delle finestre anziché quello predefinito o configurato dall'utente.
  * evitata la deprecata `gdk_screen_make_display_name`
  * Evitata la deprecata `gdk_display_get_screen`
  * non utilizzare la deprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * corretti i crash delle applet su sfondi del pannello trasparenti personalizzati
  * system tray: corrette le icone nascoste su un colore di sfondo  immagine/trasparente
  * Risolto il supporto dell'immagine di sfondo del tema GTK sul pannello verticale
  * Reso nuovamente funzionante lo sfondo dell'immagine del pannello nel tema GTK
  * clock: risolto il passaggio del mouse sopra il testo di una fascia oraria che provocava la scalatura del pannello oltre i limiti dello schermo
  * GTK 3.18+ risolto lo sfondo del pannello trasparente di default
  * menù: ripristinato il focus dopo aver trascinato con il drag and drop un oggetto del menù all'esterno
  * menù: ripristinato il focus dopo aver chiuso il menù a popup di un oggetto del menù
  * Risolto: la barra dei menù/pulsane del menù incapace di lanciare mozo
  * menù: rimosso il codice errato dal menù a popup di un oggetto del menù
  * status-notifier: segue lo stesso tema del menù come il resto del pannello
  * risolto il movimento delle applet tra i pannelli
  * menù: eliminato il crash quando qualche file .desktop ha un campo Icona vuoto
  * clock: gestita correttamente la visibilità del pulsante Modifica
  * clock: eliminata la deprecata `gtk_size_group_set_ignore_hidden`
  * clock: spostato GtkButton in un altro GtkBox orizzontale genitore
  * clock.c: eliminata la deprecata `gtk_size_group_set_ignore_hidden`
  * tradotti il nome dell'applicazione e la sua descrizione
  * menu-button: disconnessione da GSettings quando l'applet viene rimossa
  * action-button: disconnessione da GSettings quando l'applet viene rimossa
  * rimosso un controllo glib inutile
  * status-notifier: risolto un crash sul nome di un segnale sconosciuto
  * utilizzo dei segnalibri di GTK+3 per il menù Posizioni
  * doc: rimossi alcuni riferimenti a materiale inesistente
  * risolta la compilazione con gcc 4.9.2 (sembra che sia in modalità c89 per default)
  * finestra di dialogo Esegui: Aggiunta l'opzione per invertire l'ordine dello storico
  * finestra di dialogo Esegui: Risolta la lunghezza massima della cronologia. Era impostata ad 1 
  * finestra di dialogo Esegui: consentito di modificare la dimensione della cronologia
  * doc: eliminati i vecchi riferimenti a MateConf
  * finestra di dialogo Esegui: Risolto l'ordine errato della cronologia
  * status-notifier: non nasconde più gli elementi passivi
  * panel-menu-bar: eliminati un warning di compilazione e corretti alcuni spazi bianchi
  * adattato in modo corretto il pannello esteso a dimensioni dello schermo più piccole
  * system-tray: propagati correttamente i mutamenti di orientamento
  * notification-area: corretto l'orientamento dell'elemento
  * workspace switcher: gestione di `GDK_SCROLL_SMOOTH` ed eliminato un warning di compilazione
  * Riattivato il wrapping dello spazio di lavoro
  * versione pre-potenziamento
  * status-notifier: corretta la gestione dello stile della proprietà icon-padding 
  * Semplificata la descrizione del pannello mostrata quando si alternano i pannelli con il Window Manager
  * status-notifier: chiuso un memory leak
  * rimosso l'header `sys/timeb.h` perchè inutilizzato
  * status-notifier-watcher: consentita la ri-registrazione degli elementi registrati
  * impostate le icone personalizzate
  * status-notifier: chiuso un memory leak
  * notification area: risolto un memory leak quando si ordinano gli elementi
  * Aggiornate le traduzioni

### mate-backgrounds 1.20.0

   * Eliminati vecchi residui gnome
   * Aggiornate le traduzioni

### mate-themes da 3.22.8 a 3.22.15

  * Temi Sottomarini: rimosso un box-shadow alla barra degli strumenti di engrampa 
  * Temi Sottomarini: rimosso il padding dalla vista ad albero della barra laterale di caja
  * tutti i temi caja: rimosso il bordo destro da scrolledwindow.frame
  * Tema Menta metacity: rimossi i bordi sinistro e destro per le finestre massimizzate
  * BlackMATE: tracciare il bordo sulla barra di scorrimento
  * tutti i temi: rimosso il bordo destro da scrolledwindow.frame
  * Temi Sottomarini: corretto il colore di primo piano di button.suggested-action nelle barre di intestazione
  * BlackMATE: Aggirato un problema con le barre di scorrimento di Yelp/Lireoffice/Firefox
  * Ripristinare "Gtk+-3.20 tutti i temi: fissato un problema di redraw con yelp"
  * TOK/TG: sliders: mantenere la dimensione originale
  * Gtk+-3.20 Sottomarini: ridurre il raggio del bordo per  treeview.selected/hover nelle barre laterali
  * Gtk+-3.20 Sottomarini: impostare il colore del carattere per il valore degli spinbutton
  * Gtk+-3.20 temi Sottomarini: correggere un pulsante saltellante nella barra di intestazione di gitg
  * Gtk+-3.20 Temi Sottomarini: impostare drag-n-drop per caja-icon-view
  * Gtk+-3.20 Temi T. :correggere il doppio bordo in mate-volume-control dei notebook
  * Gtk+-3.20 Temi Sottomarini: corretto lo stato del focus di pluma-statusbar-button
  * Gtk+-3.20 Molti temi: ridisegnato l'acceleratore hover di un oggetto del menù
  * Tutti i temi: modificata la sintassi per il caricamento dell'immagine del panel-grid per mate-1.20
  * Gtk+-3.20 Temi Sottomarini: impostato il raggio del bordo superiore per .titlebar > headerbar
  * Gtk+-3.20 Molti temi: corretto il padding dell'immagine primaria/secondaria in GtkEntry
  * Gtk+-3.20 Tema TRAD: corretto il colore delle frecce grigie nei menù
  * TOK/TG: aggiunto il menuitem radio misto
  * TOK/TG menuitems: ridisegnati i checkbox e i pulsanti radio
  * Gtk+-3.20 most themes: corretta la selezione con il mouse sugli slider GtkScale se lo slider è fuori intervallo
  * Gtk+-3.20 tutti i temi: fissato un problema di redraw con yelp
  * Gtk+-3.20 GreenLaguna: alcuni aggiustamenti al menù
  * Gtk+-3.20 Temi Menta: aggiunto un effetto transizione per le frecce del menù
  * Gtk+-3.20 temi Menta: eliminate le impostazioni per il menù di firefox
  * Gtk+-3.20 temi Sottomarini: eliminati gli effetti di transizione dalle etichette
  * Aggiunto il file index.theme per il tema gtk+ Alto Contrasto
  * Gtk+-3.20 Molti temi: impostato il bordo per clockmap nell'applet orologio
  * Gtk+-3.20 Temi Sottomarini: alcune correzioni per l'applet orologio
  * Gtk+-3.20 BlackMate: alcune correzioni all'orologio del pannello
  * TOK/TG: caja: colore tinta unita al bordo dell'intestazione del notebook
  * Gtk+-3.20 temi Menta: utilizzato un colore hardcoded per lo sfondo dei tooltip
  * BlackMATE: CSD headerbar noncomposita di apps-match per squadrare il bordo della finestra
  * BlackMATE: altri aggiustamenti alle app CSD
  * Correzioni di BlackMATE per le app CSD
  * Gtk+-3.20 temi Menta: cambiato il colore per i pulsanti delle applet del pannello
  * Gtk+-3.20 Temi Menta: modificato il timing di transizione per un oggetto del menù della barra dei menù
  * Gtk+-3.20 temi Menta: utilizzato lo styiling normale per gli oggetti del menù della barra dei menù per il pannello
  * Gtk+-3.20 temi Menta: rimosso l'effetto di transizione dagli oggetti del menù
  * TOK/TG: mate-terminal: colore tinta unita al bordo dell'intestazione del notebook
  * Gtk+-3.20 BlackMATE: corretto il colore del carattere nella barra degli indirizzi di google chrome
  * Gtk+-3.20 BlackMATE: modificato il colore del carattere per l'acceleratore dell'oggetto del menù
  * TOK/TG: xfce4-terminal: colore tinta unita al bordo dell'intestazione del notebook
  * TOK/TG: Rimossa la sfumatura di colore dall'intestazione del notebook
  * cursore: aggiunto color-picker al file make
  * Gtk+-3.20 temi Sottomarini: migliorata la barra laterale di pluma
  * Gtk+-3.20 temi Sottomarini: corretto il colore di sfondo nelle finestre di dialogo di errore di pluma
  * BlackMATE: completamente con lo stile monocomposito m-s-d OSD
  * BlackMATE: supportata la nuova classe di stile msd-osd-window-solid per il caso di OSD non-composito
  * BlackMATE: rese le etichette di rinominazione in caja più leggibili
  * ContrastHighInverse: corrette le etichette di rinominazione in caja quando il tema viene applicato
  * cursore: aggiunta l'immagine del cursore color-picker
  * GTK+-3.20 temi Sottomarini: migliorati mate-menu e mint-menu
  * Gtk+-3.20 temi Menta: correzioni a mate-menu e mint-menu
  * Gtk+-3.20 temi Tradizionali: migliorate alcune finestre di dialogo
  * temi Tradizionali: non più disegnato uno sfondo per mate-indicator-applet
  * Gtk+-3.20 molti temi: corretto il colore di sfondo nella vista ad elenco del pannello inattivo di caja
  * Gtk+-3.20 tutti i temi: aggiunto il nuovo nome css matekbd-keyboard-drawing
  * temi metacity sottomarini: corretto il bordo interno se viene utilizzato metacity o il gestore delle finestre compiz
  * TOK/TG: xfce4-terminal: colore sfumato per il bordo dell'intestazione del notebook
  * TOK/TG: reso il padding nelle schede notebook 2 pixel più ampio
  * correzione-menta: la battitura errata "{{" corrompe il file gtk-widgets.css 
  * Tutti i temi: correzione: le rappresentazioni della carta nella finestra di dialogo stampa non comparivano in modo corretto
  * Gtk+-3.20 temi Menta: non si fa più alcuna differenza tra lo sfondo e lo stato normale
  * Gtk+-3.20 molti temi: mate-panel nasconde la modifica del pulsante
  * TOK/TG: caja: impostata una sfumatura per il bordo dell'intestazione del notebook
  * Gtk+-3.20 temi Sottomarini: mate-panel nasconde le modifiche del pulsante
  * TOK/TG: Corretti i bordi in xfce4-terminal e altre applicazioni
  * Gtk+-3.20 tutti i temi: migliorie per mate-menu
  * Gtk+-3.20 tutti i temi: miglior modo per rappresentare le disposizioni delle tastiere
  * TOK/TG: mate-terminal: impostato un colore sfumato per il bordo dell'intestazione del notebook
  * Gtk+-3.20 Traditionale: impostato un colore per il bordo dell'intestazione del notebook in mate-terminal
  * Gtk+-3.20 temi Menta: ordinato mate-applications.css
  * temi Menta: impostare il colore per il bordo dell'intestazione del notebook
  * TOK/TG: Nuovi colori nella griglia del pannello
  * Gtk+-3.20 tutti i temi: creato lo stile per mate-keyboard-layout-viewer
  * temi Tradizionali: utilizzati i gestori delle applet da Menta
  * TOK/TG: mate-terminal: utilizzato il bordo nella scheda di intestazione piuttosto che sul notebook
  * Gtk+-3.20 ContrastHighInverse: aggiunti gli asset mancanti per evitare un warning in esecuzione
  * temi Menta: eliminato il border-color errato nella schermata di blocco
  * Gtk+-3.20 Sottomarini: eliminato il border-color errato nella schermata di blocco
  * GreenLaguna: corretti i bordi delle schede notebook in mate-terminal
  * Temi Sottomarini: corretti i bordi delle schede notebook in mate-terminal
  * Gtk+-3.20 temi Menta: corretti i bordi dell'intestazione del notebook in mate-terminal
  * temi Tradizionali: eliminate alcune linee in mate-terminal per un miglior aspetto
  * Gtk+-3.20 Molti temi: Non più utilizzato un bordo per il notebook del terminale 
  * temi Tradizionali: migliorie alla finestra di dialogo di stampa
  * temi Tradizionali: impostare i bordi del notebook per pavu-control (migliorare la correzione)
  * temi Tradizionali: impostare i bordi del notebook per pavu-control
  * Gtk+-3.20 GreenLaguna: disegnata la giunzione della barra di scorrimento
  * Gtk+-3.20: aggiunto un noioso wildcard per firefox
  * Gtk+-3.20 GreenLaguna: alcuni aggiustamenti ai bordi per la barra laterale di caja
  * Gtk+-3.20 GreenLaguna: cambiato il colore del bordo di GtkSwitch
  * Gtk+-3.20 GreenLaguna: cambiato il colore del bordo per le barre di scorrimento
  * GTK+-3.20 GreenLaguna: modificato insensitive_bg_color
  * Gtk+-3.20 GreenLaguna: migliorati i notebook
  * temi Tradizionali: eliminate le due linee inutilizzate nel notebook
  * Gtk+-3.20 GreenLaguna: re-implementato i bordi delle cornici ed altri miglioramenti
  * GreenLaguna metacity: aumentata la dimensione del bordo
  * Metacity Sottomarini: aumentata la dimensione del bordo
  * Gtk+-3.20 Sottomarini: impostato il colore per le etichette che dissolvono in elenca colonne
  * Temi tradizionali: impostati più colori per il bordo nelle schede notebook marcate
  * Gtk+-3.20 temi sottomarini: impostato un padding per la barra di stato
  * Gtk+-3.20: corretto un pulsante saltellante nella barra degli strumenti mate-font-viewer
  * Gtk+-3.20 temi Sottomarini: migliorate le barre di intestazione e i menù a comparsa 
  * Gtk+-3.20 temi sottomarini: impostato un padding per la barra di stato di gedit
  * Gtk+-3.20 temi Menta: aggiunto border-image mancante per button.fat:checked in filezilla e atril
  * Gtk+-3.20 temi Menta: alcuni miglioramenti al notebook 
  * Corretti oi colori degli URL per i suggerimenti di ricerca di firefox 
  * Gtk+-3.20 temi Menta: rilavorati i bordi per le cornici ed altre migliorie (mega commit)
  * temi Tradizionali: reso più piccolo il padding nelle schede del notebook
  * Gtk+-3.20 temi Sottomarini: diversi miglioramenti
  * Gtk+-3.22 temi Sottomarini: alcuni miglioramenti a notebook
  * Gtk+-3.22 temi Sottomarini: ri-lavorati i bordi delle cornici
  * Gtk+-3.20 temi Sottomarini: corretta la commessa precedente per rubberband
  * Gtk+-3.20 Temi Sottomarini: corretto rubberband per mate-screenshot
  * Gtk+-3.20 temi Sottomarini: corretto il colore dell'etichetta della barra degli strumenti
  * temi Tradizionali: utilizzato una sfumatura sulle schede attive
  * Gtk+-2.0 Greenlaguna: utilizzati i colori esadeciamali hardcoded in gtkrc
  * Gtk+-2.0 molti temi: tilizzato uno oneliner per le definizioni dei colori in gtkrc
  * temi Tradizionali: aggiunta una border-image per alcune applet
  * Gtk+-3.20 temi Tradizionali: utilizzato un bordo per l'intero GtkInfobar
  * Gtk+-3.20 temi Tradizionali: scappatoia, corretti alcuni bordi in firefox
  * Gtk+-3.20 temi tradizionali: corretta un pulsante di combobox saltellante
  * Gtk+-3.20 molti temi: corretta la barra laterale di GtkAssistant
  * Gtk+-3.20 temi Sottomarini: corretta la barra laterale di GtkAssistant
  * Gtk+-3 tutti i temi: non impostare più NaTrayApplet-icon-size

### mate-notification-daemon 1.20.0

  * implementazione di WidthOfScreen e HeightOfScreen
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_get_n_monitors`
  * Risolto l'elevato utilizzo del CPU con larghi timeout
  * unescape i percorsi con codifica-URI per i file delle icone
  * Aggiornate le traduzioni

### mate-control-center 1.20.0

  * Scalati i font DPI per i display HiDPI
  * Aggiunto il supporto per i display HiDPI
  * theme-installer.c: risolto il mancante `g_object_unref` in `mate_theme_install_real`
  * theme-util.c: risolto il problema della reinstallazione di un tema cancellato che provocava un malfunzionamento
  * Supportato il pacchetto per la compressione dei temi per installare i formati XZ
  * eliminate le variabili non utilizzate
  * eggcellrendererkeys.c: risolti dei warning di compilazione
  * rimossi alcuni rimasugli correlati al supporto MacOS
  * theme-thumbnail.c: Risolti warning di compilazione con `write` e `pipe`:
  * libslab: memorizzato il widget di ingresso di ricerca come `GtkEntry`
  * libslab: risolto il disallineamento dell'icona di ricerca
  * Aggiornate le traduzioni

### mate-screensaver 1.20.0

  * Aggiunto il supporto HiDPI per il blocco dello schermo
  * gs-lock-plug.c: Risolto un warning in compilazione
  * implementazione di WidthOfScreen e HeightOfScreen
  * ripristinata la pagina man di mate-screensaver-command corretta
  * corrette le dichiarazioni iniziale dei cicli
  * Correzione: mostrato lo slider inattivo in tutte le lingue
  * eliminata la richiesta di glib nella sua versione massima
  * evitata la deprecata `gdk_screen_get_width/height`
  * non utilizzare la deprecata `gtk_show_uri`
  * Implementata la autenticazione OpenBSD utilizzando  `bsd_auth(3)`.
  * Bug eliminato: `g_get_real_name` non ritornerà mai il puntatore NULL
  * lock-dialog UI: evitati i widget deprecati
  * Bug eliminato: lo screensaver e la finestra di blocco non venivano correttamente mostrati  nelle configurazioni con geometrie di monitor sovrapposte
  * [GTK+3.20] Passaggio a GdkSeat
  * Impostato lo scopo di input per il componente widget di inserimento della password
  * copy theme dialog: risolto un warning di compilazione sul tipo errato di una variabile
  * Aggiornate le traduzioni

### mate-media 1.20.0

  * gvc-applet: non incrementare refcount per un elemento NULL
  * gvc-combo-box: risolti gli argomenti dei segnali
  * applet: icona di ripristino per l'elemento del menù "Preferenze Audio"
  * evitata la deprecata `gdk_screen_get_height`
  * applet: utilizzato GdkSeat con GTK+ >= 3.20
  * applet: resa funzionante la tastiera nei popup
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`... :
  * aggiornata l'icona del vassoio al cambio del tema delle icone
  * mixer-dialog: rimossa la classe di stile .frame da un oggetto scrolledwindow
  * volume-control-dialog: evitata la deprecata GtkAlignment
  * applet: mostrato il volume nel popup anche quando è muto
  * applet: migliorati gli incrementi del volume
  * abilitati in modo predefinito i warning di deprecazione
  * Aggiornate le traduzioni

### mate-power-manager 1.20.0

  * evitata la deprecata GtkStock
  * inhibit: corretto l'errore che spammava i log dal commit precedente
  * inhibit applet: risolta la renderizzazione dell'icona
  * implementazione di WidthOfScreen e HeightOfScreen
  * corretto errori di battitura in alcuni commenti al codice
  * Corretto un errore di digitazione.
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * non uscire dall'applicazione in modo anomalo su un nome di segnale DBus sconosciuto
  * evitata la deprecata `gdk_screen_get_width/height`
  * Evitata la deprecata `gdk_display_get_screen`
  * non utilizzare la deprecata `gtk_show_uri`
  * aggiornata l'icona del vassoio al cambio del tema delle icone
  * controllato il valore della variabile `$XPROTO_REQUIRED`
  * statistics UI: aggiunta la classe di stile mpm-statistics
  * Aggiornate le traduzioni

### mate-system-monitor 1.20.0

  * procman.cpp: risolto un warning di compilazione: l'argomento 1 null era atteso non-null
  * sysinfo.cpp: risolto un warning di compilazione:questa clausola 'if'  non esegue il controllo...
  * proctable.cpp: risolto un warning di compilazione: questa clausola 'else' non esegue il controllo...
  * risolto l'allineamento del lofgo di sistema
  * implementazione di WidthOfScreen e HeightOfScreen
  * process table: resa la ricerca insensibile alle maiuscole
  * sysinfo: disabilitato il focus in tutte le etichette
  * evitata la deprecata `gdk_screen_width/height`
  * sysinfo: evitata la deprecata GtkAlignment
  * Aggiornate le traduzioni

### atril 1.20.0

  * compilazione: rimossa l'opzione pre-GTK+3
  * epub: minizip supporta più varianti BSD
  * previewer: aggiunta la classe di stile atril-previewer-window
  * implementazione di WidthOfScreen e HeightOfScreen
  * shell: mostrata il cursore nel menù di navigazione
  * ev-link-accessible: Migliorata l'efficienza dei metodi per ottenere gli indici di avvio e di fine
  * Esposti i campi dei form come AtkObject figli della pagina
  * Esposte le immagini come AtkObject figlie della pagina
  * Esposti i link come AtkObject figli della pagina
  * ev-view-accessible: aggiunto un metodo per determinare se un dato doc rect è in visualizzazione
  * ev-page-cache: Aggiunto un metodo per determinare se una data pagine è stata messa in cache
  * libview: Aggiornato il cursore quando si salta ad un risultato della ricerca
  * libview: Aggiornato `ATK_STATE_SHOWING` quando cambiano i limiti della pagina visibile
  * libview: Implementato AtkComponent per le pagine
  * libview: corretta la selezione del testo con shift + clic
  * a11y: assicurato che il testo sia in cache quando si richiede un EvPageAccessible
  * a11y: gestione degli stati atk su EvPageAccessible
  * a11y: aggiungere se si applica ATK_RELATION_FLOWS_TO/FROM a EvPageAccessible
  * a11y: spostata l'implementazione AtkHyperText da EvViewAccessible a EvPageAccessible
  * a11y: spostata l'implementazione AtkText da EvViewAccessible a EvPageAccessible
  * a11y: esposto EvPageAccessible come figlio di EvViewAccessible
  * a11y: nuova EvPageAccessible
  * libview: risolti alcuni aspetti non funzionanti del supporto del testo EvViewAccessible
  * libview: presa in considerazione la navigazione col cursore quando si ottengono gli indici AtkHyperlink
  * a11y: pulita l'implementazione di `atk_text_get_caret_offset`
  * a11y: corretta l'implementazione di `atk_text_get_caret_offset`
  * view: set_caret_cursor_position dovrebbe segnalare "cursor-moved" se richiesto
  * Rimosso il supporto per il deprecato `atk_text_get_text_{before,after}_offset()`
  * a11y: implementato AtkDocument su EvViewAccessible
  * a11y: con la navigazione col cursore attiva, l'accessibilità della pagina corrente è la pagina del cursore
  * ev-view-accessible: chiamata `document_changed_cb` quando si imposta il modello
  * Alcune correzioni al testo per l'area messaggi del cursore
  * ev-view-accessible: fissato un crash in `ev_view_accessible_get_link`
  * ev-view-accessible: cancellati i dati in cache quando la pagina corrente
  * shell: rimosso `view_actions_focus_out_cb`
  * shell: rimosso `ev_window_set_view_accels_sensitivity`
  * shell: accelerazione in avanti verso il widget che ha il focus
  * Utilizzo di un array globale per visualizzare l'azione di accelerazione
  * Risolto un crash quando si seleziona del testo nei documenti djvu
  * risolto l'elemento stock nell'area del messaggio
  * docs: libview: Riaggiunta la sezionei dei tipi integrati
  * Risolto un crash dei documenti epub quando si naviga con il cursore
  * Memorizzata la posizione del cursore nei metadata del documento
  * libview: aggiunto `ev_view_set_caret_cursor_position`
  * libview: aggiorna la pagina corrente anche quando lo scorrimento in sospeso deve trovare una posizione
  * libview: non programma più il ridisegno quando si abilita/disabilita la navigazione con il cursore 
  * libview: eliminato il lampeggiamento del cursore se si trova in una pagina non visualizzata
  * shell: abilitare/disabilitare la navigazione con il cursore con F7
  * libview: aggiunto `ev_view_supports_caret_navigation()`
  * ev-link-accesible: ritornato l'indice/offset dopo l'ultimo carattere nel collegamento
  * help: Rimuovere i riferimenti alla modalità di selezione rimossa
  * libview: risolta la selezione che inizia/finisce ai margini della pagina
  * libview: ridotte le pagine da analizzare per la selezione
  * libview: Rimossa la modalità di selezione rettangolare inutilizzata
  * libview: Rilavorato ev_view_accessible_get_selection
  * libview: non si ridisegna più l'intera vista quando viene spostato il cursore 
  * libview: Aggiornata l'area del cursore dopo il posizionamento del cursore quando ci si muove tra le righe
  * ev-view-accessible: Corretta `ev_view_accesssible_get_n_selections`
  * ev-view-accessible: Corretta get_caret_offset quando la navigazione col cursore è abilitata
  * libview: utilizzato il segnale acustico di errore e il ritorno anticipato quando il movimento tra le righe fallisce
  * libview: non programma più un ridimensionamento in `ensure_rectangle_is_visible`
  * libview: Interrotto il lampeggiamento del cursore quando ci sono selezioni attive
  * libview: Deprecare ev_view_scroll in favore di `g_signal_emit_by_name`
  * ev-window: Si utilizza il nome g_signal_emit_by al posto di `ev_view_scroll`
  * previewer: Rimossi gli acceleratori dello scorrimento
  * ev-window: Rimossi gli acceleratori dello scorrimento
  * libview: Aggiunti più tasti per lo scroll ad EvView
  * libview: Corretto il tipo del secondo parametro del segnale di scorrimento per i collegamenti h, j, k e l
  * libview: utilizzato merge_selection_region che passa il valore NULL per cancellare la selezione
  * ev-pixbuf-cache: Cancellare la regione della selezione anche quando si cancella la selezione del job
  * ev-pixbuf-cache: risolta la condizione per quando risulta necessaria una nuova selezione 
  * ev-view-accessible: Riscritto get_run_attributes per restituire gli attributi del testo dal documento
  * pdf: implmentata `ev_document_text_get_text_attrs()`
  * libview: presi gli attributi dal backend e salvati in una pagina della cache
  * libdocument: Aggiunto `ev_document_text_get_text_attrs()`
  * libview: emessi i segnali AtkText, text-caret-moved e text-selection-changed
  * libview: cancellata la selezione quando il cursore viene mosso
  * libview: Non viene più mostrato il cursore quando ci sono selezioni attive
  * libview: Restituisce NULL invece di regioni vuote dalla cache pixbuf
  * libview: Non viene più disegnato il cursore quando la vista non è in focus
  * libview: risolto il movimento del cursore tra le linee in documenti a più colonne
  * libview: precaricate in cache alcune pagine precedenti/successive all'intervallo di pagine corrente
  * ev-pixbuf-cache: effettuato lo scheduling dei lavori precedenti o successivi dipendenti dalla direzione di scorrimento
  * ev-pixbuf-cache: effettuato lo scheduling dei lavori per renderizzare le pagine precedenti in ordine inverso
  * libview: Aggiunto il segnale 'cursor-moved' per segnalare quando viene mosso il cursore
  * libview: Evitata la copia di regioni non necessarie quando si seleziona il testo
  * libview: Utilizzata una maggiore area di danno per ridisegnare le selezioni
  * libview: Non accoda più un ridisegnamento quando la regione danneggiata non è cambiata
  * libview: Invalidata l'unione della vecchia e della nuova selezione
  * libview: Spostare il cursore quando si fa clic fuori da una selezione
  * libview: Rimossa il membro inutilizzato in_selection dalla struct SelectionInfo
  * libview: Mantenuto l'offset dentro una riga quando si muove il cursore tra le righe
  * libview: Posizionato il cursore all'inizio/fine della riga
  * libview: non effettuare lo scheduling di un ridisegnamento quando si seleziona tutto il testo
  * Utilizzato preponi + inverti anziché aggiungi alla fine per creare elenchi di selezioni
  * libview: Utilizzato GSlice per allocare EvViewSelection
  * libview: Reso selezionabile il testo utilizzando il cursore.
  * libview: Aggiornato il cursore dopo aver selezionato del testo con il mouse
  * libview: presi in considerazione i bordi della pagina quando si elabora la selezione
  * libview: Risolto un crash quando si seleziona più di una pagina
  * libview: Fatto in modo che il cursore lampeggi dopo averlo spostato con un clic
  * libview: unire `get_caret_cursor_rect_from_offset` e `get_caret_cursor_area`
  * libview: Notificati gli errori di navigazione col cursore mediante l'avviso acustico di errore
  * libview: non ridisegnare se dopo un clic la posizione del cursore non è cambiata
  * libview: Utilizzato GtkBindings per la navigazione col cursore
  * libview: Rinominato il segnale EvView::binding-activated come EvView::scroll
  * libview: Posizionato il cursore con il clic del mouse
  * libview: Utilizzato `EvPixbufCache` per trovare la regione della selezione
  * libview: Suddivisa `ev_pixbuf_cache_get_selection_surface` in due funzioni
  * libview: Disegnata l'evidenziazione della selezione dalla regione
  * libview: Corretta l'area danneggiata utilizzata per ridisegnare il cursore.
  * libview: Aggiornata la pagina quando il cursore si muove da una pagina differente
  * libview: Evitato di aggiornare la pagina corrente e di scorrere la posizione del cursore, se il cursore non è stato aggiornato
  * libview: reso il cursore lampeggiante
  * libview: Utilizzati attributi logici invece del layout del testo per spostare il cursore
  * libview: Aggiunto un modo per ottenere gli attributi logici dalla pagina cache
  * libview: Implementazione iniziale della navigazione con il cursore
  * libview: Rifattorizzato il codice per disegnare la pagina e le superfici di selezione
  * shell: disabilitato `ViewDualOddLeft` nei menù per gli epub
  * libview: accede solo alla cache della pagina rilevante per la richiesta di altezza
  * Attivati tasti scorciatoia per la disposizione doppia e continua
  * ev-view: Inoltra gli eventi della tastiera al campo del modulo con focus
  * Aggiunti tasti scorciatoia per le opzioni fit-page e fit-width
  * shell: Non aprire i pdf di una singola pagina in modalità duale
  * libview: Non aggiornare la pagina_corrente ad un numero negativo
  * libview: Reso una modalità il layout di pagina
  * libview: Aggiunto un nuovo livello di zoom che ottimizza per la leggibilità
  * Rinominato Fit Page Width come Fit Width
  * Rinominato Best Fit come Fit Page
  * Spostata la visuale a pagina doppia con pagine dispari a sinistra nel menu di visualizzazione
  * libview: eliminato l'utilizzo deprecato di gtk_container_set_resize_mode
  * shell: Verificare se il documento implementa l'interfaccia Annotazioni prima del cast
  * Aggiornare la barra laterale delle annotazioni alla cancellazione
  * libdocument: Resa `ev_mapping_list_remove` void
  * page-cache: Aggiunti parametri flag a `ev_page_cache_mark_dirty()`
  * pdf: Resettata la mappatura delle annotazioni quando non ci sono più annotazioni
  * Aggiunta una opzione per rimuovere le annotazioni al menù a comparsa della visualizzazione
  * libview: aggiunta ev_view_remove_annotation
  * pdf: Implementata la funzione virtuale remove_annotation
  * libdocument: aggiunta ev_mapping_list_remove
  * libdocument: Aggiunta remove_annotation a DocumentAnnotations.
  * pdf: Resi i nomi delle annotazioni unici
  * pdf: Aggiunto il supporto per aggiungere altri tipi di annotazioni
  * libview: Rinominata ev_view_set_focused_element e resa pubblica internamente
  * Modificata l'opacità della finestra delle annotazioni
  * Modificato il colore della finestra delle annotazioni
  * libview: Ottenere il focus dai campi dei moduli e dai collegamenti alla pressione del tasto del mouse
  * libdocument: Aggiunta `ev_mapping_list_get`
  * pdf: Aggiunto il collegamento di attivazione per Campi che lo possiedono
  * libview: Gestito se presente il link di attivazione del Campo di un Modulo
  * libdocument: Aggiunto l'attivation_link alla struttura EvFormField
  * ev-properties-licence: non più utilizzata la deprecata GtkAlignment
  * libview: evitata la deprecata gtk_adjustment_changed
  * ev-job-find: segnati due metodi come skip
  * ev-jobs: `ev_job_failed_from_error` deve nascondere `ev_job_failed`
  * libview: aggiunti il trasferimento mancante e le annotazioni element-type
  * ev-mapping-list: reso un tipo con box
  * libdocument: aggiunti il trasferimento mancante e le annotazioni element-type
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`... :
  * evitata `gdk_screen_get_primary_monitor/gdk_screen_get_monitor_scale_factor`
  * ev-document-misc.c: evitata la deprecata `gdk_screen_get_width/height_mm`
  * dvi: Mitigati gli attacchi command injection mediante il nome del file
  * mdvi-lib: Risolto un warning di compilazione (const-correctness)
  * libmisc: impostata la largheza dei caratteri per l'etichetta della pagina
  * libview: fatte scorrere le pagine piccole in modo non-continuo
  * libview: Abilitati gli eventi `GDK_SMOOTH_SCROLL` per la visualizzazione
  * libview: Reso lo zoom Ctrl + rotellina del mouse centrato-attorno-al-puntatore e non centrato-alla-finestra
  * ev-view: Aggiunto il gesto pan per cambiare pagina
  * ev-view: richiedere esplicitamente `GtkScrolledWindow`  come widget genitore
  * ev-view: Aggiunti i gesti pizzico/zoom per gestire lo zoom del documento
  * sidebar-thumbnails: risolto lo spostamento non desiderato che si avviava dopo il fullscreen
  * sidebar-thumbnails: precaricato un intervallo visibile extra quando si esegue lo scroll
  * sidebar-thumbnails: mantenute le miniature già renderizzate
  * sidebar-thumbnails: risolto il problema sullo scorrimento
  * annotations-sidebar: Pulito lo stile
  * ev-annotation-window: Risolta l'impostazione del colore del bordo della finestra
  * libview: risolto il cambio di focus della finestra delle annotazioni dopo la creazione
  * libview: Risolto il focuso su ev_annotation_window
  * libview: Non modificato il colore del font della finestra delle annotazioni
  * shell: Utilizzato GdkRGBA  per le annotazioni
  * libdocument: Aggiunta l'API EvAnnotation che utilizza GdkRGBA 
  * libdocument: Utilizzate le nuove macro di deprecazione
  * Aggiunte le macro di deprecazione
  * risolti dei warning in esecuzione causati dal commit HDPI precedente
  * Preso in considerazione il fattore di scala del monitor quando si calcola lo zoom.
  * Aggiunto il supporto hi-dpi per la vista principale.
  * shell: abbandonato gimpcellrenderertoggle
  * sidebar-layers: Reso utilizzabile e fissato un warning in esecuzione
  * libview: impostate le dimensioni delle icone della finestra delle annotazioni
  * libview: salvati i cambiamenti in un dropdown nel modulo integrato
  * libdocument: aggiustato il rendering dell'ombra per le pagine attive ed inattive
  * evitata la deprecata `gdk_screen_make_display_name`
  * ev-window: rimossa la deprecata `GtkToolbar-shadow-type`
  * annotation-properties-dialog: non utilizza più una barra di intestazione
  * evitate le deprecate `gdk_display_get_screen` e `gdk_display_get_n_screens`
  * ev-window: non utilizzare la deprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * compilazione: ripulito correttamente il file generato.caja-extension
  * compilazione: richiesto cairo >= 1.10.0 ed eliminato del vecchio codice 
  * shell: rimosso il codice inutilizzato da utils
  * ev-view: evitata la deprecata `gtk_drag_begin`
  * egg-editable-toolbar: evitata la deprecata `gtk_drag_begin`
  * message-area: sostituite alcune deprecazioni di `GtkStock`
  * ev-sidebar: evitata l'icona deprecata `GTK_STOCK_CLOSE`
  * password-view: sostituite alcune deprecazioni di `GtkStock`
  * password-view: non più utilizzata la deprecata `GtkAlignment`
  * toolbar-editor: non più utilizzata la deprecata `GtkAlignment`
  * Aggiornate le traduzioni

### caja-extensions 1.20.0

  * xattr-tags: Utilizzato un inglese migliore nella descrizione delle estensioni
  * po: aggiunte le stringhe traducibili mancanti dall'estensione xattr
  * xattr-tags: migliorata la descrizione dell'estensione
  * open-terminal: non è stato utilizzato un alto numero di stringhe duplicate
  * evitata la deprecata `gdk_screen_make_display_name`
  * sendto burn: evitato il deprecato `gtk_show_uri`
  * xattr-tags: rimosso hack, adesso non ce n 'è bisogno
  * xattr-tags: risolto un errore di digitazione che causava un riferimento indefinito
  * Aggiustata la dichiarazione della variabile `libcaja_gksu_la_LDFLAGS`
  * xattr-tags: aggiunto il ritorno a capo mancante al messaggio di avvio
  * xattr-tags: unescaping degli attributi memorizzati.
  * Aggiornate le traduzioni

### engrampa 1.20.0

  * compilazione: utilizzato `PKG_CONFIG` per risolvere la cross-compilazione
  * Aggiunto il nostro copyright alla finestra di dialogo About e  a Caja extensions
  * 7z: risolto il rinominamento dei file senza che l'elenco sia cifrato
  * 7z: Risolta la cancellazione/rinominamento di file/cartelle con l'elenco cifrato
  * evitato il deprecato `gdk_screen_make_display_name`
  * non più utilizzato il deprecato `gtk_show_uri`
  * utilizzata una funzione gtk+ più comune
  * evitata la deprecata `gdk_screen_get_number`
  * Aggiunto il pulsante "Mostra i file ed esci" nella finestra di dialogo di avanzamento
  * Risolto: creare file zip con il livello di compressione "massimo"
  * Risolto: l'esplorazione della cronologia non era corretta
  * nascoste le cartelle in "Visualizza tutti i file"
  * Risolto: Cattivo comportamento del pulsante Salta nella finestra di dialogo Sostituisci
  * File UI: evitate le deprecazioni
  * gtk-utils: rimosse alcune deprecazioni di `GTK_STOCK`
  * gtk-utils: evitato il deprecato gtk_icon_size_lookup_for_settings
  * fr-window: rimosse alcune deprecazioni di `GTK_STOCK`
  * aggiunta la classe di stile cornice a scrolledwindows
  * fr-window: evitate le deprecate `GtkMisc` e `GtkAlignment`
  * dlg-add-folder: evitata la deprecata `gtk_alignment_new()`
  * Compilazione: utilizzo di variabili invece di nomi file hardcoded quando si esegue la pulizia
  * Aggiornate le traduzioni

### eom 1.20.0

  * eliminato il CSS per GTK+ 3.18
  * egg-editable-toolbar.c/egg-toolbars-model.c: eliminate le variabili inutilizzate
  * print-preview: sostituito il codice personalizzato con chiamate di funzione GDK
  * gtk 3.22: eliminate le funzioni deprecate `gdk_screen_get_monitor` functions:
  * non utilizzare la deprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * eliminato il warning nel chiudere una finestra vuota con più finestre di eom aperte
  * EomThumbView: Sostituita la funzione deprecata `gtk_menu_popup`
  * multiple-save-as-dialog.ui: evitati i widget deprecati
  * error-message: sostituito l'utilizzo di GtkStock
  * Un po' di correzioni ai warning di introspezione
  * EomScrollView: corretta la chiamata alla deprecata override_background
  * EomPropertiesDialog: Corretti i warning di deprecazione
  * EomThumbNav: risolti i warning delle funzioni deprecate
  * EomScrollView: Sostituita la funzione deprecata `gtk_menu_popup`
  * EomScrollView: Passaggio da GtkDeviceManager a GdkSeat
  * corretto un errore di battitura nell'annotazione di una funzione
  * utilizzati file css differenti per < gtk+=3.20
  * EomWindow: Impostata la finestra di dialogo apri file come transiente per la sua finestra genitrice
  * settings: utilizzata la definizione di colore rgb come predefinita
  * UI: evitato l'utilizzo di widget deprecati
  * EomCloseConfirmationDialog: impostata l'ampiezza massima dei caratteri nell'etichetta primaria
  * EomCloseConfirmationDialog:  Corretta la richiesta di grandezza per l'elenco delle immagini
  * L'orientamento della carta in stampa dovrebbe essere determinato dalle dimensioni dell'immagine
  * Evitato di ricomprimere le JPEG come PNG quando si stampa
  * EomFileChooser: Utilizzato MateThumbnailFactory per creare una anteprima dell'immagine
  * EomPropertiesDialog: Consentito RGBA per il colore dello sfondo trasparente
  * preferences-ui: eliminato l'uso di `MateColorButton`
  * EomScrollView: Passato a `GdkRGBA` per lo sfondo ed i colori trasparenti
  * EomPrintPreview: Evitato l'analisi del colore non necessaria
  * Risolte alcune deprecazioni di GtkStock
  * EomCloseConfirmationDialog: sostituita la deprecata `GTK_STOCK_DIALOG_WARNING`
  * toolbar-editor: evitata la deprecata GtkAlignment
  * Aggiornata la gestione SVG di eom-image.c, adesso riconosce in modo appropriato i tipi di file svgz
  * eom_uri_converter: corretto un memory leak di GList
  * Aggiornate le traduzioni

### mate-applets 1.20.0

  * multiload: Ridimensionato il grafico di rete utilizzando soglie definite dall'utente
  * multiload: Risolte miscele di tabulazioni/spazi in più posti
  * multiload: corretta la spaziatura in alcuni posti
  * multiload: rimossi alcuni spazi non necessari
  * weather: risolto un possibile crash aprendo la finestra delle preferenze
  * Eliminata invest-applet perché rotta e rimosse tutte le dipendenze Python
  * Corretto un warning di compilazione: ignorato il valore di ritorno di `fgets`,
  * command: aumentata l'ampiezza dell'intervallo
  * implementazione di WidthOfScreen e HeightOfScreen
  * compilazione: quando gtksourceview non viene trovato, mostrare questo nome di pacchetto
  * Cpufreq: Aggiornati i tooltip con gli ultimi valori
  * Cpufreq: corretto un warning di compilazione
  * Cpufreq: corretto il saltellamento dei numeri muovendo l'etichetta delle unità
  * Corretto un errore di arrotondamento nel disegno
  * cpufreq: corretto il calcolo dell'ampiezza massima delle etichette frequenza/unità/percentuale
  * stickynotes: corretta la selezione del testo
  * cpufreq: aggiornata la dimensione dell'applet al variare dello stile (es. dimensione del font)
  * Le variazioni GSettings sono riconosciute dinamicamente
  * Gsettings per il colore del segno di spunta mostrato per i volumi montati
  * cpufreq: corretta la scomparsa casuale dell'applet
  * I dispositivi montati mostrano un'icona leggermente diversa
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * Eliminati l'indentatione_fuorviante e i warning in compilazione maybe-uninitialized
  * evitata la deprecata `gdk_screen_width/height`
  * evitata la deprecata `gdk_screen_get_width/height`
  * all applets: non utilizzare la deprecata `gtk_show_uri`
  * aggiunto un nuovo tema digitale
  * drivemount: corretto un warning in compilazione
  * cpufreq-prefs: non utilizzare la deprecata `gtk_show_uri`
  * libmateweather portato alla versione 1.19.1
  * weather: se la località cambia, impedire ogni aggiornamento in sospeso
  * wearher: Aggiunta la logica per non inviare notifiche se l'aggiornamento è uguale (così come viene stabilito da `weather_info_equal()`) all'aggiornamento precedente
  * evitata la deprecata `gdk_screen_get_number`
  * drivemount: se l'elenco è vuoto mostrerà l'icona del floppy
  * stickynotes: riformulare un po' il compito precedente e non fare spreco di memoria con il nome della directory
  * stickynotes: creare una cartella genitrice per `stickynotes-applet.xml` se questa non esiste.
  * La scala del grafico di carico si ridimensiona automaticamente in base al carico medio
  * trashapplet: rimosso il codice inutilizzato
  * cpufreq: impostare la requenza su tutti i core
  * Corretto un memory leak di GError
  * Correzione di un crash nell'applet Command
  * Aggiornate le traduzioni

### mate-calc 1.20.0

  * Aggiunta una icona sul pulsante chiudi della finestra di dialogo preferenze
  * evitata la deprecata GtkStock
  * aggiunta l'icona mancante alla finestra di dialogo Informazioni
  * math-window: non utilizzare la deprecata `gtk_show_uri`
  * Aggiornate le traduzioni

### mate-icon-theme-faenza 1.20.0

  * Modificata la licenza a GPL3, come da progetto originale
  * Corretto l'utilizzo del logo MATE per i temi scuri

### mate-indicator-applet 1.20.0

  * Supportata la compilazione contro Ayatana Indicators e Ubuntu Indicators
  * Aggiornate le traduzioni

### mate-netbook 1.20.0

  * implementazione di WidthOfScreen e HeightOfScreen
  * window picker: disconnessi i gestori dei segnali nella funzione dispose
  * window picker: aggiunta l'icona alla finestra di dialogo preferenze
  * window picker: disabilitare l'espansione verticale dei pulsanti nel la finestra di dialogo preferenze
  * window picker: aggiunta l'icona per la taskbar nella finestra di dialogo Informazioni
  * maximus: non va più in crash su un ID di finestra non valido
  * Aggiornate le traduzioni

### mate-sensors-applet 1.20.0

  * compilazione: abilitato nuovamente il plugin udisk2
  * Rimosso il plugin deprecato udisks
  * udisks plugin: corretta la gestione della memoria per le variabili GValue
  * Rimosso il plugin deprecato eee
  * Corretta la cascata di popup alla rimozione di HDD
  * ibm-acpi.c: Risolto un warning in compilazione:
  * eee-plugin.c: Risolto un warning in compilazione:
  * active-sensor.c: Risolto un warning in compilazione:
  * sensors-applet.c: Risolto un warning in compilazione:
  * Corrette le indentazioni
  * Corretta la pulizia del progetto
  * Fermato il saltellamento dell'applet quando cambiano i numeri
  * corretto l'ordine di salvataggio dei sensori
  * aggiornato nascondi le unità di temperatura
  * rimosse porzioni di codice duplicate
  * sensor-applet.c: sostituita la deprecata GtkMisc
  * sensor-applet.c: evitata la deprecata `GTK_STOCK_MISSING_IMAGE`
  * sensor-config-dialog: evitata la deprecata GtkAlignment
  * sensor-config-dialog: non più utilizzata la deprecata GtkColorButton
  * prefs-dialog: aggiunta una classe di stile cornice a scrolledwindows
  * prefs-dialog: evitata la deprecata GtkAlignment
  * prefs-dialog: evitate le deprecate `GTK_VBUTTON_BOX`, `GTK_TYPE_{H,V}BOX`
  * utilizzato `GTK_ALIGN_CENTER` per la griglia di `sensor_applet`
  * Aggiornate le traduzioni

### mate-terminal 1.20.0

  * richiesto VTE 0.46
  * screen: cessato di impostare le variabili di ambiente `TERM` e `COLORTERM`
  * schema: corretti il sommario e la descrizione di qualche tasto
  * rimosso "..." dalla scorciatoia di tastiera Trova
  * profile-editor: inizializzato in modo corretto il primo colore della tavolozza
  * terminal-screen.c: eliminate le variabili non utilizzate
  * Risolto un warning in compilazione: ignorato il valore ritornato da `chdir`,
  * clic centrale su una scheda: aggiunta la chiave gsettings per abilitare questa caratteristica
  * resa l'indentazione più uniforme in alcuni file
  * risolto un possibile bug quando si gestisce la chiamata al metodo DBus
  * Ortografia: spazio bianco rimosso, nel temr minale, Ctrl
  * aggiunti i temi Solarizzati per gnome-terminal
  * implementazione di WidthOfScreen e HeightOfScreen
  * aggiunta la capacità di scorrere tra le schede utilizzando <kbd>ctrl</kbd> + <kbd>tab</kbd> e <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>tab</kbd>
  * permettere la rimappatura delle scorciatoie da tastiera "ricerca".
  * Supportate le immagini di sfondo con VTE3
  * find-dialog.ui: risolta la selezione con la tastiera
  * Evitata la deprecata `vte_terminal_search_get_gregex`
  * aggiunta la scorciatoia da tastiera "seleziona tutto": <kbd>control</kbd> + <kbd>shift</kbd> + <kbd>A<kbd>
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_make_display_name`
  * terminal-ui: evitata la deprecata  `gtk_show_uri`
  * Evitata la deprecata `gdk_display_get_screen`
  * evitata la deprecata `gdk_screen_get_number`
  * Risolto: doppio clic col pulsante destro manda Xorg in crash
  * Aggiornate le traduzioni

### mate-user-share 1.20.0

  * compilazione: utilizzate le macro corrette per la cross-compilazione
  * non utilizzare la deprecata `gtk_show_uri`
  * Aggiornate le traduzioni

### mate-utils 1.20.0

  * aggiunto il supporto per lo screenshot dei display HiDPI
  * mate-screenshot: aggiunto il pulsante Nuovo
  * screenshot-save.c: risolto un warning di compilazione con `pipe` `write` e `read`:
  * aggiunta una classe di stile logview-window
  * Aggiornate le traduzioni
  * Implementazione di WidthOfScreen e HeightOfScreen
  * baobab: reso possibile lo zoom con la rotella del mouse sul grafico
  * screenshot: rimosso del codice inutilizzato
  * screenshot: non memorizzare il nome della finestra perché dopo non è utilizzato
  * baobab/logview/dictionary: aggiunto il nostro copyright alla finestra di dialogo Informazioni
  * baobab: impostato il genitore transiente per la finestra di dialogo di connessione remota
  * baobab: resa la finestra di dialogo delle preferenze non visibile nel file .ui
  * baobab: impostata la finestra genitrice per il dialogo Informazioni
  * evitata la deprecata `gdk_screen_get_active_window`
  * gtk 3.22: evitate le funzioni deprecate `gdk_screen_get_monitor`
  * evitata la deprecata `gdk_screen_width/height`
  * evitata la deprecata `gdk_screen_get_width/height`
  * screenshot: evitati gli oggetti deprecati GdkDevice
  * dictionary: evitati gli oggetti deprecati GdkDevice
  * evitata la deprecata `gdk_screen_get_n_monitors`
  * evitata la deprecata `gdk_screen_make_display_name`
  * gdict-applet: non utilizzare la deprecata `gtk_show_uri`
  * non utilizzare la deprecata `gtk_show_uri`
  * evitata la deprecata `gdk_screen_get_number`
  * searchtool e logview: evitata la deprecata GtkAlignment
  * mate-screenshot: evitato di mostrare il cursore impegnato quando si salva lo screenshot dell'area
  * screenshot: non tradurre il timestamp nel nome del file
  * mate-dictionary: inclusi gli header corretti per risolvere gli occasionali FTBFS
  * Aggiornate le traduzioni

### mozo 1.20.0

  * Aggiornate le traduzioni

### pluma 1.20.0

  * posizionato `peas_engine_enable_loader` nel posto corretto
  * Risolto: fatto funzionare di nuovo l'elenco dei file utilizzati di recente
  * eliminate le variabili non utilizzate
  * pluma-spell-checker-language.c:risolto un warning in compilazione:
  * pluma.c: Risolto un warning in compilazione:
  * pluma-document.c: Risolto un warning in compilazione:
  * pluma-window: posizionato GtkRecentData sullo stack invece di allocarlo
  * Implementazione di WidthOfScreen e HeightOfScreen
  * Risolte le sostituzioni nelle espressioni regolari con backreferences (es. `"\0"`)
  * pluma-view.c: utilizzata una variabile statica invece di due per effettuare lo stesso lavoro
  * fatto in modo che pluma apra nella stessa finestra dello spazio di lavoro
  * Risolto: il problema di pluma che chiude inaspettatamente le schede con clic [destro + centrale] <kbd>ctrl</kbd> + <kbd>+</kbd> / <kbd>ctrl</kbd> + <kbd>-</kbd> utilizzando il tastierino numerico
  * aggiunta una chiave gsettings: Mostrare la conferma del salvataggio se il file è stato modificato
  * Risolto: errato comportamento tenendo premuto il tasto [centrale + destro] <kbd>ctrl</kbd> + <kbd>+</kbd> / <kbd>ctrl</kbd> + <kbd>-</kbd> per incrementare/diminuire la dimensione del font
  * non richiesto più il salvataggio di file senza modifiche
  * aggiunta una chiave gsettings per nascondere/mostrare(predefinito) le schede con il pannello laterale
  * Nascondere le schede se stiamo utilizzando la barra laterale
  * gtk 3.22: eliminate le funzioni deprecate `gdk_screen_get_monitor`:
  * evitata la deprecata `gdk_screen_get_width/height`
  * evitata la deprecata `gdk_screen_make_display_name`
  * pluma-help: non utilizzare la deprecata `gtk_show_uri`
  * filebrowser non utilizzare la deprecata `gtk_show_uri`
  * evitate le deprecate `gdk_display_get_screen` e `gdk_screen_get_number`
  * attivata la possibilità di salvare il documento se è stato modificato dall'esterno
  * disattivata la possibilità di salvare il documento se non ha modifiche
  * print-preferences UI: risolte alcune deprecazioni basilari
  * encoding-dialog UI: risolte alcune deprecazioni basilari
  * preferences-dialog UI: risolte alcune deprecazioni basilari
  * pluma-panel: rimossi i tipi deprecati GtkImage
  * plumal-panel: rimosse alcune deprecazioni GtkStock
  * search-dialogs: risolto un warning -Wpointer-compare
  * tag-list-plugin: evitata la deprecata GtkStock
  * file-browser-widget:risolta una deprecazione di stock
  * configure: eliminato `GLIB_VERSION_MAX_ALLOWED`
  * File browser: non utilizza più GIOScheduler (deprecato)
  * file-browser-view: silenziati alcuni warning di compilazione
  * pluma-view: evitate le deprecazioni di GtkStock
  * pluma-tab: sostituite alcune icone di GtkStock
  * pluma-notebook: non utilizzare la deprecata `gdk_cursor_new`
  * progress-message-area: risolta una deprecazione GtkStock
  * io-error-message-dialog: risolti alcuni warning di deprecazione di GtkStock
  * Risolto: pluma chiude le schede inaspettatamente con il clic del tasto centrale del mouse
  * pluma-notebook.c: risolto un warning in compilazione
  * doppio clic a destra dell'ultima scheda aperta per aprirne una nuova
  * Supporto per nuove posizioni per il file dei segnalibri di gtk
  * docs: abbiamo codifiche combobox, non menù opzioni
  * rimossi i riferimenti a PlumaStatus
  * docs: rimossi alcuni riferimenti a materiale inesistente
  * non analizzare manualmente i file .hidden - GIO lo fa sin dalla 2.36
  * chiudere la finestra di dialogo di conferma: abilitare la selezione + disabilitare il focus in tutte le etichette
  * chiudere la finestra di dialogo di conferma: impostata la dimensione massima per le etichette
  * corretto un errore di battitura nei commenti al codice
  * corretta l'esecuzione sotto wayland
  * modelines: risolto un crash casuale alla chiusura di una delle diverse finestre aperte di Pluma
  * Aggiornate le traduzioni

### python-caja 1.20.0

  * Aggiornate le traduzioni
