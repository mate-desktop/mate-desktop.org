<!--
.. link:
.. description:
.. tags: Releases
.. date: 2021-08-10 09:00:00
.. title: Rilasciato MATE 1.26
.. slug: 2021-08-08-mate-1-26-released
.. author: Johannes Unruh
-->

Questo rilascio potrebbe aver impiegato un po' più tempo del solito ma adesso, dopo 18 mesi di sviluppo, siamo veramente lieti di rilasciare MATE 1.26. Un grosso grazie a tutti i collaboratori che hanno aiutato a renderlo possibile.

![MATE About dialog](/assets/img/blog/about-mate-1.26.png)

## Cosa c'è di nuovo in MATE 1.26

La chiave di questo rilascio è stata quella di aggiungere nuove funzionalità al Desktop MATE e nel contempo mantenere l'aspetto che noi tutti conosciamo ed amiamo. Nonostante tutte le funzionalità aggiunte siano certamente eccitanti, non abbiamo dimenticato di correggere tonnellate di bug, modernizzando il codice base ed ottimizzando le prestazioni.

I principali cambiamenti in MATE Desktop 1.26 sono:

* Abbiamo aggiunto il supporto a [Wayland](https://wayland.freedesktop.org/) per Atril, Monitor di Sistema, Pluma, Terminal ed altri componenti del Desktop. In aggiunta a ciò, Calculator e Terminal possono essere compilati con [Meson](https://mesonbuild.com/).
* **Pluma** ha subito massicci miglioramenti.
    * C'è una nuova **mini mappa** che fornisce una panoramica istantanea del contenuto.
    * Il **nuovo sfondo con motivo quadrettato** converte Pluma in un blocchetto per scrivere.
    * Il plugin di ordinamento adesso supporta la funzionalità di annullare le operazioni effettuate.
    * Abbiamo aggiunto una scorciatoia per mostrare/nascondere il numeri di linea, <kbd>Ctrl</kbd> + <kbd>Y</kbd>.
    * La finestra di dialogo preferenze ha avuto bisogno di un completo ridisegno per poter ospitare tutte le nuove funzionalità.
* Assieme ai nuovi **Plugin di Pluma** il nostro editor di testi **può essere trasformato in una IDE ricca di funzionalità** con il supporto per l'*auto completamento delle parentesi*, il *Commento/Decommento del codice*, un *Terminale integrato* e l'*autocompletamento di una parola*.
* Il **Centro di Controllo** implementa una migliore finestra di dialogo per le preferenze delle Finestre offrendo più opzioni. Nella finestra di dialogo Display abbiamo aggiunto una opzione per mostrare lo scaling.
* Le notifiche sono diventate ancora più utili in quanto hanno ricevuto il supporto per i collegamenti ipertestuali. E abbiamo in fine **aggiunto una applet Non Disturbare**.
* In tema di applet, l'applet Window List ha una opzione per disabilitare lo scorrimento con il mouse. Le miniature opzionali della finestra adesso risultano **dettagliate e chiare perché sono renderizzate come superfici cairo**.
* L'applet Netspeed mostra per default più informazioni ed ha aggiunto il supporto per [netlink](https://www.man7.org/linux/man-pages/man7/netlink.7.html).
* **Calculator** è stato portato alla libreria [GNU MPFR](https://www.mpfr.org/)/[MPC](http://www.multiprecision.org/mpc) che significa maggiore precisione, calcolo più veloce e funzionalità aggiuntive (es. la funzione Zeta di Riemann, la funzione di errore di Gauss).
    * Abbiamo finalmente **aggiunto una cronologia per mostrare i calcoli effettuati di recente**.
    * Quando la cronologia è attivata, Calculator può essere ridimensionato.
    * È stata ampiamente migliorata la velocità della fattorizzazione di numeri interi.
    * Valutazione dell'aritmetica modulare più veloce (possibilità dell'esponenziamento modulare).
* Nel file manager **Caja** è possibile selezionare **una nuova barra laterale per i segnalibri**. Caja ha ottenuto il **supporto per formattare i dispositivi** dal menù contestuale. L'estensione **Caja Actions** che consente di eseguire programmi arbitrari via menù contestuale, adesso fa parte del Desktop.
* Scorrere all'interno di grossi documenti in **Atril** adesso è molto più veloce dopo aver sostituito una lenta ricerca lineare con una ricerca ad albero binario. L'**impronta di memoria del visualizzatore di documenti è stata ulteriormente ridotta** poiché un EvWebView adesso viene creato solo quando serve.
* Il gestore delle finestre **Marco** adesso ripristina le finestre minimizzate alla loro posizione originale in modo più affidabile
* **Engrampa** ha ricevuto il supporto per gli archivi Pubblicazioni Elettroniche (EPUB) e ARC. Inoltre è in grado di aprire archivi RAR cifrati.
* Il **Power Manager** ha una nuova opzione per abilitare lo smorzamento dell'illuminazione della tastiera ed è stato portato a [libsecret](https://wiki.gnome.org/Projects/Libsecret).
* Gran parte delle finestre di dialogo Informazioni sono state aggiornate con descrizioni più simpatiche. Perché le piccole cose contano `:-)`.
* Abbiamo corretto un gran numero di bug, alcuni memory leak e reso più moderno il codice base di quasi tutti i componenti del Desktop.
* C'è un nuovo [Wiki](https://wiki.mate-desktop.org/) che rende più agevole per i nuovi collaboratori unirsi al nostro progetto. Abbiamo bisogno urgente di gente motivata, quindi non esitate a [contattarci](https://wiki.mate-desktop.org/introduction/contributing/) o ad [iniziare a contribuire](https://wiki.mate-desktop.org/introduction/contributing/).
* Le traduzioni sono state aggiornate. Grazie al nostro team di traduttori!

I vari componenti di MATE 1.26 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.26/>


## Maggiori dettagli

Ecco i dettagli truculenti.

### atril
* Completamene riscritto l'Help (assicuratevi di leggere la nuova sezione synctex se scrivete parecchi file TeX)
* ev-window.c: Si crea un EvWebView solo se necessario
* ev-sidebar-links: Ottimizzata la ricerca all'indietro dei collegamenti di una pagina (la lenta ricerca lineare dei collegamenti nella barra laterale è stata sostituita con una ricerca in un albero binario specializzato)
* Aggiunto il supporto a Wayland
* Ci siamo assicurati che la finestra degli allegati riempia tutta la barra laterale
* Reso synctex opzionale
* Corretto un segfault se navMap è vuoto
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/atril/commits/master/>

### caja
* Ora è possibile aggiungere le informazioni dell'orario di creazione nelle colonne dell'elenco
* Aggiunta una opzione per bloccare la posizione delle icone fisse sul desktop
* Migliorato il controllo del filesystem sul Drag and Drop
* Adesso è finalmente possibile formattare i dispositivi direttamente in caja
* fm-properties-window: resa movibile la posizione delle cartelle di sistema
* Facendo clic con il tasto centrale del mouse sul pulsante ricarica duplica la scheda
* Creati per default i collegamenti sul trascinamento dai Browser Web
* Aggiunta la barra laterale "Segnalibri" a Caja
* Supportata una esplicita opzione `--select` per la riga di comando
* Chiesta la conferma prima dell'eliminazione durante una operazione di annullamento
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja/commits/master/>

### caja-actions
* Fa la sua prima comparsa in questo rilascio
* i18n: Migrazione da intltools a gettext
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

### caja-dropbox
* Aggiunto il supporto i18n
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja-dropbox/commits/master/>

### caja-extensions
* gksu: non eseguire il comando su un nuovo thread
* Richiede gtk+ 3.22 nei file glade
* sendto: Corretto il comando evolution per l'invio di una email
* image-converter: Completa riscrittura di caja-image-rotate.ui
* Corretti diversi memory leak
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/caja-extensions/commits/master/>

### engrampa
* rar 6.00: Corretta l'elencazione del contenuto di un archivio con l'elenco dei file cifrato
* Aggiunto il supporto per Electronic Publication (EPUB)
* Aggiunto il supporto per il formato di archiviazione ARC
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/engrampa/commits/master/>

### eom
* Aggiornati i file ui
* Ci siamo assicurati che la barra di scorrimento si muova quando viene trascinata per spostarsi nell'immagine
* Aggiunto il supporto per lo scorrimento delle schede nelle finestre di dialogo
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/eom/commits/master/>

### libmatekbd
* Ridotta la dimensione del font dei nomi dei tasti nella visualizzazione del layout della tastiera
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmatekbd/commits/master/>

### libmatemixer
* alsa: aggiunto il supporto per udev
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmatemixer/commits/master/>

### libmateweather
* Eliminato Berlin Tegel
* Aggiunte 2 città del Brasile
* Aggiornate le città della Thailandia
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/libmateweather/commits/master/>

### marco
* window: Aggiunto il supporto per _GNOME_WM_STRUT_AREA
* screen: Aggiunto il supporto per _GTK_WORKAREAS_Dn
* window: non renderizzare le ombre a destra/sinistra delle finestre affiancate
* iconcache: Utilizzato GDesktopAppInfo per trovare le icone delle applicazioni corrette
* window: traccia il rettangolo della finestra prima di affiancare agli angoli
* window: Traccia il rettangolo della finestra prima di affiancarla
* Aggiunti i tast VI (hjkl) per muovere e ridimensionare le finestre
* window: Espanso il supporto per alternare la dimensione di affiancamento
* Nel pop-up del selettore dello spazio di lavoro, viene mostrato lo spazio di lavoro selezionato
* Migliorato lo script di compilazione di meson
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/marco/commits/master/>

### mate-applets
* netspeed: consentito il selezionamento di una interfaccia che è 'down'
* netspeed: Mostrati tutti gli indirizzi ipv6 nella finestra di dialogo dei dettagli del dispositivo
* netspeed: Se attivato, vengono mostrati tutti gli indirizzi IP sui tooltip
* multiload: Utilizzo del bit rate nel grafico di netload
* multiload: Incrementata l'impostazione dell'ampiezza della velocità di aggiornamento
* battstat: Completa riscrittura della finestra di dialogo preferenze
* multiload: Mostrata sul tooltip l'accurata percentuale di utilizzo 
* netspeed: Utilizzate le unita IEC per le velocità di trasferimento
* netspeed: Aggiunto il supporto a netlink
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-applets/commits/master/>

### mate-backgrounds
* Nuovo sfondo con elefanti 'Qualcosa lentamente diviene chiara'
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-backgrounds/commits/master/>

### mate-calc
* Portato alla libreria GNU MPFR/MPC
* Aggiunta una cronologia opzionale per mostrare i calcoli recenti
* È possibile navigare nella cronologia con le scorciatoie da tastiera (Alt + Freccia Su)/(Alt + Freccia Giù)
* reso possibile il ridimensionamento della calcolatrice quando è attiva la cronologia
* Mostrati gli esponenti nella scomposizione in fattori primi
* Aumentata in modo considerevole la velocità di scomposizione nei fattori primi
* Nella scomposizione in fattori primi dei numeri maggiori di 2^64 vengono impiegati il test di primalità di Miller-Rabin e l'algoritmo rho di Pollard
* Valutazione dell'aritmetica modulare molto più veloce (capacità di esponenziamento modulare)
* Aggiunte la funzione zeta di riemann, la funzione di errore di gauss, la funzione di fattorizzazione dei numeri reali
* Aggiunto il supporto di meson alla compilazione 
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-calc/commits/master/>

### mate-common
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-common/commits/master/>

### mate-control-center
* windows-applet: Nuova opzione Mostra il bordo della finestra con Alt+Tab e Consenti l'opzione affiancamento dall'alto (Window-Snapping)
* windows-applet: Nuova scheda per il compositing manager
* windows-applet: Nuova opzione per il layout della barra del titolo "sinistra" (con menù) e "destra" (senza menù)
* Le finestre con decorazioni lato client adesso rispettano il layout della barra del titolo
* Corretta la preview nella finestra di dialogo aggiungi sfondo
* Aggiunte le opzioni per la selezione dei file nella sezione interfaccia delle finestre di dialogo dell'aspetto (il selettore  dei file è la finestra che viene mostrata quando si apre o si salva un file)
* Migrazione di alcuni componenti da dbus-glib a GDBus
* Supportato lo scorrimento col tasto tab delle finestre di dialogo della finestra e dell'aspetto
* L'applet Display adesso ha l'opzione di mostrare lo scaling
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-control-center/commits/master/>

### mate-desktop
* a11y-keyboard: Aggiunta l'opzione gsetting capslock-beep-enable
* Impostato l'intervallo per maximum-age della cache delle miniature
* Rimosso il warning di deprecazione GTimeVal per GLib 2.61.2+
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-desktop/commits/master/>

### mate-icon-theme
* Rimosso il bit di esecuzione da alcuni file png
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-icon-theme/commits/master/>

### mate-indicator-applet
* applet-main: Sostituita l'icona GtkStock
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-indicator-applet/commits/master/>

### mate-media
* Sostituito il checkmenuitem mute/unmute con imagemenuitem
* panel-applet: Fatto in modo che lo speaker possa essere mostrato affianco o sopra il microfono
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-media/commits/master/>

### mate-menus
* Aggiunto l'elemento di menù collezione
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-menus/commits/master/>

### mate-netbook
* mate-window: Sostituite le icone GtkStock
* mate-maximus-autostart.desktop: Rimossa la chiave deprecata Codifica
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-netbook/commits/master/>

### mate-notification-daemon
* Aggiunta l'applet Non Disturbare
* Aggiunto il backend iniziale di Wayland
* Aggiunto il supporto ai collegamenti ipertestuali nel corpo di una notifica
* Completa riscrittura di mate-notification-properties.ui
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-notification-daemon/commits/master/>

### mate-panel
* workspace-switcher: Supportato il window manager xmonad
* Reso di lunghezza variabile l'elenco dei Documenti recenti nel menù Risorse
* Aggiunta l'opzione di disabilitazione dello scorrimento con il mouse per l'elenco delle finestre
* Aggiunto il supporto alla visualizzazione delle etichette di testo per l'area di notifica
* window-list: Renderizzate le miniature come superfici cairo
* Eliminato il compositing dello sfondo
* Supporto Wayland per l'elenco delle finestre
* Ridisegnata la finestra di dialogo preferenze dell'applet window-list
* Corretta l'aggiunta dei lanciatori delle applicazioni al pannello quando si utilizza la finestra di dialogo Aggiungi al pannello
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-panel/commits/master/>

### mate-polkit
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-polkit/commits/master/>

### mate-power-manager
* mate-power-preferences: Aggiunta l'opzione per consentire l'attenuazione della luminosità della tastiera
* Reso predefinito libsecret rispetto a libgnome-keyring
* brightness applet: Impedito lo scorrimento per non intasare l'Interfaccia Utente
* Port da EggDebug al framework di logging integrato in GLib
* Completa riscrittura di gpm-prefs.ui
* Rimossa la funzionalità CPU wakeup
* Aggiunti alcuni file SVG mancanti
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-power-manager/commits/master/>

### mate-screensaver
* Consentita la modifica del formato di data e ora nella finestra di blocco
* Aggiunto il simbolo Mostra/Nascondi password nel campo di inserimento delle password
* mate-screensaver-preferences: Mostrata l'anteprima dell'immagine di blocco nel file chooser
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti diversi memory leak
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-screensaver/commits/master/>

### mate-sensors-applet
* Eliminato il plugin aticonfig
* sonypi-plugin.c: Abbiamo reso il plugin sonypi portabile su GNU/Hurd
* libsensors-plugin: Port a GRegex
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-sensors-applet/commits/master/>

### mate-session-manager
* Seguite le direttive freedesktop per disabilitare l'autorun utilizzando la chiave Hidden
* Supporto per xscreensaver quando mate-screensaver non è disponibile
* Aggiunto il supporto allo scorrimento delle schede per GTK3
* Accolta la Desktop Entry Specification v1.1
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretto un memory leak
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-session-manager/commits/master/>

### mate-settings-daemon
* xsettings: Migliorate le impostazioni dell'ambiente HiDPI di Qt
* a11y-keyboard: aggiunto il supporto per l'impostazione togglekeys-backend
* Aggiunta l'opzione --without-libatspi e la linea di stato assortita
* a11y-keyboard: Aggiunta l'opzione per far risuonare l'avviso acustico quando il tasto Blocca Maiuscole è attivo
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* Corretti due memory leak
* g10n: Aggiornate le traduzioni

Complete changelog at <https://github.com/mate-desktop/mate-settings-daemon/commits/master/>

### mate-system-monitor
* Aggiunto il supporto a Wayland
* Port a GTKApplication
* pretty-table: Preferito GIO per ottenere le icone delle applicazioni
* Aggiunto il supporto per le azioni sui processi multipli
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-system-monitor/commits/master/>

### mate-terminal
* Corretto il warning di convalida del file desktop
* Aggiunto il supporto di meson alla compilazione 
* Aggiunto il supporto per lo scorrimento delle schede per GTK3
* Aggiunto il supporto a Wayland
* Corretta la ricerca nella finestra del terminale
* Aggiunte le icone per "apri scheda" e "chiudi finestra/scheda"
* Prevenuto il crash per bad term spawn a causa delle chiamate a free ridondanti
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-terminal/commits/master/>

### mate-user-guide
* Rimosso il bit di esecuzione da alcune immagini in Italiano
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-user-guide/commits/master/>

### mate-user-share
* Utilizzato MATE_COMPILE_WARNINGS da mate-common
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-user-share/commits/master/>

### mate-utils
* mate-screenshot: Corretto l'ordine dei pulsanti sul fondo
* mate-screenshot: non utilizzare icone stock in mate-screenshot.ui
* logview: Completa riscrittura di logview-filter.ui
* gsearchtool: Aggiunta la voce di menu copia percorso al popup menù
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* compilazione: Aggiunta una opzione per disabilitare il Native Language Support (NLS) (`--disable-nls`)
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mate-utils/commits/master/>

### mozo
* Completa riscrittura di mozo.ui
* Corretto uno strano comportamento quando si modifica la directory della collezione
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/mozo/commits/master/>

### pluma
* Port del plugin di ordinamento alla nuova API GtkSourceView.
* Port dei plugin all'utilizzo della proprietà window-construct
* compilazione: port a gtksourceview-4
* Introdotti PlumaWindowActivatable, PlumaAppActivatable, PlumaViewActivatable
* Aggiunta la scorciatoia per mostrare/nascondere i numeri di riga (Ctrl+Y)
* Ridisegnata la finestra di dialogo Preferenze di Pluma
* Rimosso pluma-marshal.
* Aggiunto un motivo a quadretti opzionale
* Rimosso il plugin changecase. Questa funzionalità è fornita da GtkSourceView.
* Aggiunta una mappa d'insieme
* Port ad una nuova classe pluma-settings
* Aggiunto il supporto per Wayland
* Aggiunto il supporto per lo scorrimento delle schede per GTK3
* pluma.c: Impostato PlumaWindow size-request (min-size) a 250x250
* Corrette diverse analisi del codice, i warning di deprecazione sono stati riportati da Clang Static Analyzer, Cppcheck e GCC
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/pluma/commits/master/>

### pluma-plugins
* Fa la sua prima comparsa in questo rilascio
* Il pacchetto contiene i seguenti plugin aggiuntivi
    * bookmarks - *Navigazione facilitata tra i documenti con i segnalibri.*
    * bracketcompletion - *Aggiunta l'automatica chiusura delle parentesi.*
    * codecomment - *Commenta e decommenta blocchi di codice.*
    * smartspaces - *Scordatevi del fatto che non state utilizzando le tabulazioni*
    * synctex - *Sincronizzazione SyncTeX dei file Tex e la loro corrispondente rappresentazione PDF.*
    * terminal - *Terminale integrato nel pannello inferiore.*
    * wordcompletion - *Completamento della parola utilizzando il framework di completamento.*
    * sourcecodebrowser - *Visualizzazione ed esplorazione di funzioni, variabili e namespaces.*

### python-caja
* Corretto un memory leak riportato da scan-build
* g10n: Aggiornate le traduzioni

Il changelog completo è disponibile su <https://github.com/mate-desktop/python-caja/commits/master/>
