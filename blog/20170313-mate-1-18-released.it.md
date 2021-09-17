<!--
.. link:
.. description:
.. tags: Releases
.. date: 2017-03-13 23:30:00
.. title: Rilasciato MATE 1.18
.. slug: 2017-03-13-mate-1-18-released
.. author: Martin Wimpress
-->

Dopo 6 mesi di sviluppo il team di MATE Desktop è orgoglioso di annunciare
il rilascio di MATE Desktop 1.18. Vorremmo ringraziare ogni collaboratore MATE per il suo aiuto nel rendere possibile questo rilascio.

![about](/assets/img/blog/about-mate-1.18.png)

## Cosa c'è di nuovo in MATE 1.18

Questo rilascio è focalizzato a completare la migrazione a GTK3+ e
ad adottare nuove tecnologie per sostituire alcuni dei componenti deprecati
su cui MATE Desktop 1.16 era ancora basato.

I principali cambiamenti in MATE Desktop 1.18 sono:

  * **L'intera suite di applicazioni e componenti del Desktop MATE adesso è esclusivamente GTK3+!**
    * Richiesto GTK+ >= 3.14.
    * Tutto il codice GTK2+ è stato eliminato assieme all'opzione di compilazione `--with-gtk`.
  * Completata la migrazione a `GtkApplication` da `libunique`.
  * **Aggiunto il supporto `libinput` per mouse e touchpad.**
    * Separati i settaggi per la mano utilizzata sul mouse (sinistra/destra) e l'accelerazione/soglia del movimento.
  * **Migliorato di molto il supporto all'accessibilità (in modo particolare per gli utenti con difficoltà visive).**
     * Molte grazie ai nostri amici di [Hypra.fr](https://hypra.fr/-Home-17-.html?lang=en) per il loro contributo!
  * **Caja aggiunge numerose nuove funzionalità** includendo:
      * L'aggiunta di una coda di copia e la pausa di un processo di copia.
      * La richiesta di conferma prima di spostare i file nel Cestino.
      * Il supporto dei pulsanti del mouse indietro/avanti per la navigazione delle cartelle.
      * La notifica di quando è sicuro rimuovere i dispositivi espulsi. 
  * **Il blocco dello schermo carica lo sfondo scelto dall'utente** invece di quello predefinito di sistema.
  * Il Pannello di MATE riceve diversi miglioramenti, che includono:
    * **Aggiunto il supporto delle [azioni desktop](https://specifications.freedesktop.org/desktop-entry-spec/latest/) per avere opzioni di lancio aggiuntive**.
    * Aggiunto il supporto dello StatusNotifier.
    * **Aggiunto il supporto per l'editor di menù [Menulibre](https://smdavis.us/projects/menulibre/)**, se viene installato,  questo è preferito a Mozo.
  * Engrampa, il gestore degli archivi, include diversi miglioramenti:
    * Aggiunti `ear` e `war` all'elenco dei tipi supportati.
    * Ci si è assicurati della versione di rar/unrar se viene mostrata la data corretta.
    * Corretta la compressione di rar e 7z suddivisa in volumi.
  * **La notifica adesso implementa il supporto delle icone di azione**, ad esempio le icone di controllo della riproduzione utilizzate dai riproduttori multimediali.
  * Riscritto il visualizzatore dei font dei caratteri per aggiungere la modalità di esplorazione del font, supportare i font TTC ed esporli nei menù come comportamento predefinito.
  * **Sostituite le funzioni deprecate sospendi/iberna di `upower` con gli equivalenti di ConsoleKit2**
  * Il terminale di MATE aggiunge la funzionalità di chiudere le schede con il clic del tasto centrale del mouse.
  * **Atril, il visualizzatore di documenti, ha di molto migliorato il tempo di caricamento delle pagine** e aggiunge il supporto per `unarchiver` utilizzato da alcuni formati di fumetti.
  * Sono stati sostituiti molti dei metodi GTK+ deprecati e sono stati corretti diversi bug.
  * **Il sistema dei plugin, e tutti i plugin C e Python, in Eye of MATE e Pluma, sono stati portati a `libpeas`.**
  * Le traduzioni sono state aggiornate. *Grazie al nostro team di traduttori!*
  * **Sono stati eliminati un certo numero di memory leaks**.
  * *E cosa più eccitante di tutte...* **MATE Calculator è tornato ed è stato portato a GTK3+** `:-D`

I vari componenti di MATE 1.18 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.18/>

## Changelog

Segue una analisi più dettagliata di ciò che è cambiato.

### mate-common 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    Per rendere più semplice la creazione dei comunicati degli annunci di rilascio 

### mate-desktop 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    Per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    opzione di compilazione
  * Eliminato lo strumento mpaste (non funzionerà comunque senza il sito web)
  * Sfondo: Corretto il problema della dissolvenza incrociata con le versioni recenti di GTK+
  * Sfondo: Corretti alcuni altri problemi grafici per consentire a Caja di utilizzare lo sfondo
    per le finestre delle directory
  * Sfondo: eliminati i memory leaks e vari altri problemi 
  * Selezione del colore: Corrette alcune deprecazioni di GTK+
  * Schemi: alcuni aggiustamenti e pulizie varie
  * mate-about: aggiornato l'anno del copyright
  * mate-about: corretto il problema del centraggio dell'URL
  * Aggiornate le traduzioni

### mate-user-guide 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiornate le traduzioni

### libmatekbd 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    Per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Aggiornate le traduzioni

### libmatemixer 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiornate le traduzioni

### libmateweather 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Eliminati i binding Python e l'opzione --enable-python (non funzionerà
    con GTK+3)
  * Località: aggiunta Dunedin, Nuova Zelanda
  * Località: aggiunta Yogyakarta, Indonesia
  * Località: spostata l'Indonesia sotto la regione Asia
  * Località: corrette le coordinate di Pune, India
  * Aggiornate le traduzioni

### mate-icon-theme 1.18.0

  * Aggiornate le traduzioni

### caja 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazionde: richiede libmate-desktop >= 1.17.3
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    opzioni di compilazione
  * Port da libunique a GtkApplication
  * Implementata la coda di copia e la pausa
  * Aggiunta l'opzione di chiedere conferma prima di spostare i file nel Cestino.
  * Aggiunto il supporto dei pulsanti del mouse indietro/avanti per la navigazione delle cartelle.
  * Aggiunta la notifica di quando è sicuro rimuovere i dispositivi espulsi (e richiede
    libnotify al momento della compilazione)
  * Aggiunta l'opzione da riga di comando --force-desktop per forzare Caja a gestire sempre
    il desktop
  * Aggiunta la possibilità di ottenere feedback da Orca su quando le icone aggiuntive sono 
    selezionate/deselezionate
  * Eliminato lo strumento di conversione dei metadati
  * Corretto il problema della dissolvenza incrociata con le versioni recenti di GTK+
  * Corretti alcuni altri problemi grafici per consentire a Caja di utilizzare lo sfondo per
    le finestre delle cartelle cartelle
  * Rimosse ulteriori deprecazioni GTK+ e warning di runtime
  * Schema: alcuni aggiustamenti e pulizie varie
  * Aggiornate le traduzioni

### mate-polkit 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Risolte alcune deprecazioni di GTK+
  * Aggiornate le traduzioni

### marco 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * Visualizzatore dei temi: Corretto il problema di compilazione per GTK+3 e rimosse alcune deprecazioni GTK+
  * Aggiunta la possibilità di disabilitare la visualizzazione del bordo della finestra preselezionata con alt-tab
  * Aggiunta la possibilità di ignorare le applicazioni quando show-desktop è attivo
  * Schema: reso il compositing attivo per default
  * Workspaces: possibilità di commutare la modalità di comportamento tra 'classico' e 'toroidale'
    (in qualche modo era stata invertita)
  * Aggiornate le traduzioni

### mate-settings-daemon 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiest XInput senza condizioni
  * Compilazione: richiesti libmatemixer >= 1.10, libxklavier >= 5.2, dconf >= 0.13
  * Compilazione: richiesti libmatekbd e libmate-desktop >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * Aggiunto il supporto `libinput` per mouse e touchpad
  * Touchpad: aggiunte impostazioni separate per l'utilizzo della mano (sinistra/destra)
    e l'accelerazione/soglia del movimento
  * Sfondo: ripristinata l'opzione per permettere a Caja di disegnare lo sfondo con GTK+ 3.22
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-session-manager 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Sostituite le funzioni deprecate sospendi/iberna di `upower` con gli equivalenti di ConsoleKit2
    (ed eliminata l'opzione di compilazione  --enable-upower)
  * Aggiornate le traduzioni

### mate-desktop 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiornate le traduzioni

### mate-panel 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesti libmate-menu >= 1.10 e dconf >= 0.13.4
  * Compilazione: richiesti libmateweather e libmate-desktop >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Lanciatori: aggiunto il supporto delle azioni desktop per lanci aggiuntivi
    opzioni
  * Applet del menù: aggiunto il supporto per l'editor di menù Menulibre e preferirlo
    a Mozo se sono entrambi installati
  * Area di notifica: Aggiunto il supporto per StatusNotifier
  * Rimosse ulteriori deprecazioni GTK+ e warning di runtime
  * Non spamma le modifiche del nome accessibile quando viene tradotto 
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mate-backgrounds 1.18.0

   * Aggiornate le traduzioni

### mate-notification-daemon 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Implementato il supporto per le icone di azione (es. le icone di controllo della riproduzione
    utilizzati dai riproduttori multimediali)
  * Temi: corretti alcuni problemi con il conto alla rovescia a torta
  * Aggiornate le traduzioni

### mate-control-center 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesti libmatekbd, libmate-desktop, marco, m-s-d >= 1.17
  * Compilazione: richiesti XCursor e XInput senza condizioni
  * Mmigrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * Port da libunique a GtkApplication
  * Riscrittura di font-viewer: aggiunta la modalità di esplorazione dei font, supporto per i font TTC,
    E reso visibile nei menù
  * Aggiunto il supporto libinput per mouse e touchpad
  * Mouse: aggiunte le impostazioni di moto del touchpad separate nella scheda del touchpad
  * Mouse: cambiato il nome della scheda da Generale a Mouse
  * Mouse: modificato il mnemonico per lo scorrimento naturale da 'a' ad 'n'
  * Risolte molte deprecazioni di GTK+
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-screensaver 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesto libmate-menu >= 1.10
  * Compilazione: richiesti libmatekbd e libmate-desktop >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * Blocco dello schermo: carica lo sfondo dell'utente al posto di quello di sistema
  * Preferenze: risolte alcune deprecazioni di GTK+
  * Aggiornate le traduzioni

### mate-media 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesti libmatemixer >= 1.10 e libmate-desktop >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * Port da libunique a GApplication e GtkApplication
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mate-power-manager 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesto xproto >= 7.0.15
  * Compilazione: richiesto mate-panel >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Sostituite le funzioni deprecate sospendi/iberna di `upower` con
    gli equivalenti di ConsoleKit2
  * Utilizzo delle pagine man così come sono invece di generarle da sgml (e
    non richiedere più dockbook2man per generale)
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-system-monitor 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiunto il supporto a `pkexec` per utilizzare `kill` e `renice` sui processi degli altri
    utenti e tentare di usarlo prima di provare `gksu`
  * Risolte alcune deprecazioni di GTK+
  * Aggiornate le traduzioni

### atril 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesto caja >= 1.17.1
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione
  * [fumetti] aggiunto il supporto per unarchiver (unrar e Isar)
  * [libview] aumentata la dimensione della cache di pagina per ridurre il numero di caricamenti delle pagine
  * Rimosso il codice di migrazione dei metadati
  * Forzato il backend X11
  * Risolte molte deprecazioni di GTK+
  * Risolti alcuni problemi a11y
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### caja-dropbox 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesti libcaja-extension 1.17.1 e GLib 2.36

### caja-extensions 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesti caja >= 1.17.1 e libmate-desktop >= 1.17.0
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    opzione di compilazione
  * Aggiunta l'estensione xattr-tags per mostrare i tag xattr in una nuova colonna
  * Aggiornate le traduzioni

### engrampa 1.18.0

  * Verifica la versione rar/unrar per usare il nuovo stile di data con tutte le versioni
  * Correzione: l'elenco dei file rar, con il nuovo file binario, adesso mostra la data corretta
  * Correzione: apertura del primo split volume 7z dopo la compressione
  * Corretto un errore in NEWS: engrampa al posto di engramp
  * Correzione: compressione rar suddivisa in volumi
  * Correzione: compressione 7z suddivisa in volumi
  * Compilazione rimossa l'opzione che disabilita il materiale deprecato
  * zip: aggiunti ear e war all'elenco dei tipi supportati.
  * Aggiornato engrampa NEWS per un utilizzo consistente, esteso a tutto il progetto, della
    formattazione tipo-markdown.
  * Compilazione: richiesti Caja >= 1.17.1 per compilare la versione GTK+3
    di libcaja-extension
  * tar: aggiunto il supporto per pixz per i file tar.xz
  * tar: aggiunto il supporto per lbzip2 per i file tar.bz2
  * lha: aggiunto il supporto per i file Amiga
  * Alcune correzioni nello schema di GSettings
  * Aggiornate le traduzioni

### eom 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesto libmate-desktop >= 1.17
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Eliminati i binding Python e l'opzione --enable-python
  * Portati il sistema dei plugin e i plugin a libpeas
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mate-applets 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesti libmateweather e mate-panel >= 1.17
  * migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Meteo: risolto il posizionamento dell'etichetta della temperatura
  * Meteo: mostrato l'aiuto corretto per ciascuna sezione nella scheda della finestra di dialogo delle preferenze
  * Rimosse ulteriori deprecazioni GTK+ e warning di runtime
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mate-calc 1.18.0

  * Aggiunto Appdata.

### mate-icon-theme-faenza 1.18.0

  * Versione aggiornata

### mate-indicator-applet 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: mostra lo stato del supporto del nuovo indicatore di stile nel sommario
  * Compilazione: richiesto mate-panel >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Aggiornate le traduzioni

### mate-netbook 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesto mate-panel >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Aggiornate le traduzioni

### mate-sensors-applet 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesto mate-panel >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Risolte alcune deprecazioni di GTK+
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### mate-terminal 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiunta la funzionalità di chiudere le schede con il clic del tasto centrale del mouse.
  * Aggiornate le traduzioni

### mate-user-share 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio
  * Compilazione: richiesto caja >= 1.17.1
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e rimosso --with-gtk
    come opzione di compilazione

### mate-utils 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Compilazione: richiesto mate-panel >= 1.17
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Corretto la rottura occasionale del distcheck
  * Alcune rifiniture al codice
  * Aggiornate le traduzioni

### mozo 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Aggiornate le traduzioni

### pluma 1.18.0

  * NEWS: utilizzo consistente, esteso a tutto il progetto, della formattazione tipo-markdown
    Per rendere più semplice la creazione dei comunicati degli annunci di rilascio 
  * Migrazione a GTK+3 (richiesto GTK+ >= 3.14), rimosso il codice GTK+2 e
    l'opzione di compilazione --with-gtk
  * Compilazione: attualmente compilato con i dati di introspezione GObject
  * Compilazione: rimossa l'opzione --enable-deprecations che di fatto
    disabilita tutto il materiale deprecato
  * Aggiunta la possibilità di cercare/sostituire del testo utilizzando le espressioni regolari
  * Eliminati i binding a Python e l'opzione di compilazione  --enable-python
  * Portato il sistema plugin e i plugin C e Python a libpeas
  * Plugin Snippets: non si espongono più le funzioni sul bus di messaggi di Pluma
    (non funziona con l'introspezione di Gobject)
  * Plugin Snippets: risolta la permanenza di porzioni dello snippet dopo Ctrl-Z
  * Risolta la chiusura inaspettata della prima scheda se si fa clic col tasto centrale del mouse
    sotto la colonna dei numeri di linea
  * Risolti alcuni warning nei plugin
  * Correzioni varie e pulizia
  * Aggiornate le traduzioni

### python-caja 1.18.0

  * Aggiornate le traduzioni
  * supportato solo GTK+3: richiesti Caja 1.17.1 e pygobject-3.0
  * eliminato il vecchio controllo di Python 2.5, adesso non occorre più
