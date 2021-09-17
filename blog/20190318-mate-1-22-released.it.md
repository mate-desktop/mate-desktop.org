<!--
.. link:
.. description:
.. tags: Releases
.. date: 2019-03-18 09:00:00
.. title: Rilasciato MATE 1.22
.. slug: 2019-03-18-mate-1-22-released
.. author: Victor Kareh
-->

Dopo circa un anno di sviluppo il Team di MATE Desktop ha finalmente rilasciato MATE 1.22. Un grosso ringraziamento a tutti i collaboratori che hanno aiutato a renderlo possibile.

![about](/assets/img/blog/about-mate-1.22.png)

## Cosa c'è di nuovo in MATE 1.22

Questo rilascio contiene una gran quantità di correzioni critiche e migliorie nascoste. Alcuni dei più evidenti cambiamenti includono:

* IL **pannello MATE** ha ricevuto un lavoro pazzesco per farlo lavorare con il backend per display [Wayland](https://wayland.freedesktop.org/) 
    * L'**applet display** ha subito una completa revisione in modo da poter meglio controllare i monitor direttamente dal pannello. 
    * L'**applet timer** adesso ha una migliore interazione con il mouse
    * **Wanda the Fish** adesso funziona correttamente sui display HiDPI (l'immagine del pesce è ancora pixellata, mantenendo il suo aspetto originario)
* Il supporto per i [temi metacity] (https://wiki.gnome.org/Attic/GnomeArt/Tutorials/MetacityThemes) è finalmente stato aggiornato alla versione 3 nel gestore delle finestre **marco**
    * Abbiamo inoltre modernizzato la finestra e il selettore dello spazio di lavoro per renderli visivamente più accattivanti
* Il **gestore della sessione** adesso termina correttamente tutti i processi su [systemd](https://freedesktop.org/wiki/Software/systemd/). Inoltre tutte le applicazioni possono essere avviate automaticamente dopo un ritardo specificato dall'utente.
* Abbiamo completamente portato un certo numero di applicazioni a Python 3, inclusi **Eye of MATE** e le librerie plugin **python-caja**, così come la libreria **mate-menus**
* Il file manager **caja** può opzionalmente mostrare le notifiche desktop per operazioni su file che richiedono parecchio tempo
* **Eye of MATE** ha una sidebar che è stata riscritta e un miglior supporto dei metadati delle immagini
* Le schede in **pluma** adesso hanno la possibilità di poter essere alternate con delle scorciatoie da tastiera o con lo scroll del mouse
* La **Calcolatrice** adesso può supportare fino a 15 caratteri di accuratezza. Il supporto per la copia e l'incollaggio è stato anch'esso un po' migliorato
* **Engrampa** ha ricevuto il supporto per diversi nuovi formati di archiviazione, ed anche nuova funzionalità di pausa/ripresa
* Sono state aggiunte alcuni nuovi **tasti scorciatoia** inclusi il supporto per diversi tipi di dispositivi come Bluetooth, WiFi, touchpad, e interruttori di terminazione globali
* È stato intrapreso un lavoro di manutenzione interna per alcuni compiti:
    * Molti dei nostri progetti sono migrati da [dbus-glib](https://developer.gnome.org/dbus-glib/unstable/) a [GDBus](https://developer.gnome.org/gio/stable/gdbus-convenience.html)
    * Abbiamo migliorato la stabilità di molti nostri progetti chiudendo le falle di memoria e risolvendo i warning di compilazione
    * Abbiamo rimosso il vecchio codice deprecato per essere aggiornati con l'ultima versione di [GTK] (https://developer.gnome.org/gtk3/stable/)
    * Sono state aggiunte/corrette diverse guide di documentazione
    * Tutti i nostri progetti adesso utilizzano  [Travis CI](https://travis-ci.org/) per garantire compilazioni pulite su alcune delle nostre maggiori distribuzioni

I vari componenti di MATE 1.22 sono disponibili per il download a questo indirizzo:

  * <https://pub.mate-desktop.org/releases/1.22/>

## Changelog

Ecco tutti i dettagli truculenti.

### atril
* [9031100](https://github.com/mate-desktop/atril/commit/9031100) Aggiunto lo script update-authors.pl che aiuta ad aggiornare atril.about
* [a67e572](https://github.com/mate-desktop/atril/commit/a67e572) Leggere authors (aggiornato) da atril.about gresource
* [9a4748b](https://github.com/mate-desktop/atril/commit/9a4748b) Abilitato Travis Cl per tutti i rami
* [f68afd7](https://github.com/mate-desktop/atril/commit/f68afd7) Inizializzato il supporto a Travis Cl
* [96f9b79](https://github.com/mate-desktop/atril/commit/96f9b79) Aggiornato Documenters
* [d776f3f](https://github.com/mate-desktop/atril/commit/d776f3f) Rimossi i file generati
* [4a7e48f](https://github.com/mate-desktop/atril/commit/4a7e48f) Tx: sincronizzati con le traduzioni fisse da Transifex
* [9b87168](https://github.com/mate-desktop/atril/commit/9b87168) [ephy-zoom-control] Evitata la deprecata g_type_class_add_private
* [d9c803e](https://github.com/mate-desktop/atril/commit/d9c803e) [ephy-zoom-action] Evitata la deprecata g_type_class_add_private
* [ca538e8](https://github.com/mate-desktop/atril/commit/ca538e8)  Aggiunti i TypeDescription di pixbuf, tiff e xps a POTFILES.in
* [869cb47](https://github.com/mate-desktop/atril/commit/869cb47) eggsmclient: Evitata la deprecata 'g_type_class_add_private'
* [2a49c6c](https://github.com/mate-desktop/atril/commit/2a49c6c) spostato appdata nella cartella metainfo
* [fde24d0](https://github.com/mate-desktop/atril/commit/fde24d0) message-area: impostato il nome oggetto a11y dall'attuale nome dell'icona 
* [d43c675](https://github.com/mate-desktop/atril/commit/d43c675) shell: rimosso un controllo condizionale duplicato
* [19c3072](https://github.com/mate-desktop/atril/commit/19c3072) tiff: corretto un possibile dereferenziamento del puntatore NULL
* [6457c82](https://github.com/mate-desktop/atril/commit/6457c82) pdf: aggiunta una istruzione break mancante
* [70ba1fb](https://github.com/mate-desktop/atril/commit/70ba1fb) libdocument: eliminata l'inutile cancellazione del puntatore NULL
* [1b95162](https://github.com/mate-desktop/atril/commit/1b95162) comics: corretto il mimetype errato che indicava di aprire e fare le miniature di tutti i file RAR
* [3c75360](https://github.com/mate-desktop/atril/commit/3c75360) disabilitati i warning di deprecazione per distcheck
* [eaae975](https://github.com/mate-desktop/atril/commit/eaae975) utilizzate funzioni make per HELP_LINGUAS
* [7d9dab7](https://github.com/mate-desktop/atril/commit/7d9dab7) comics: supporto per il tipo MIME application/vnd.rar
* [699ce12](https://github.com/mate-desktop/atril/commit/699ce12) shell: salvare un documento nello stesso percorso da cui era stato aperto
* [a6fc396](https://github.com/mate-desktop/atril/commit/a6fc396) Ridotta la loquacità del demone di atril
* [c9ea2a3](https://github.com/mate-desktop/atril/commit/c9ea2a3) EvView: Corretto il movimento del cursore quando l'ordine delle righe logiche e visuali è diverso
* [bb47386](https://github.com/mate-desktop/atril/commit/bb47386) Aggiornato atril_start_window.png
* [c95b319](https://github.com/mate-desktop/atril/commit/c95b319) modificato moveable (vecchia grafia) -> movable
* [856bf94](https://github.com/mate-desktop/atril/commit/856bf94) Aggiornato lo screenshot in Catalano
* [6e19591](https://github.com/mate-desktop/atril/commit/6e19591) presentation: evitata la deprecata 'gtk_style_context_set_background'
* [29fc232](https://github.com/mate-desktop/atril/commit/29fc232) corretto Linguas
* [9a9999c](https://github.com/mate-desktop/atril/commit/9a9999c) sincronizzazione con transifex
* [6a9d8eb](https://github.com/mate-desktop/atril/commit/6a9d8eb) aggiornato atril.pot
* [03a697c](https://github.com/mate-desktop/atril/commit/03a697c) ev-sidebar-bookmarks: utilizzato NULL al posto di una variabile non inizializzata
* [05e6aa3](https://github.com/mate-desktop/atril/commit/05e6aa3) navigation-action-widget: sostituita la funzione deprecata gtk_menu_popup
* [510ea85](https://github.com/mate-desktop/atril/commit/510ea85) shell: sostituita la funzione deprecata gtk_menu_popup
* [0fd2124](https://github.com/mate-desktop/atril/commit/0fd2124) ev-sidebar-links: sostituita la funzione deprecata gtk_menu_popup
* [be5fadc](https://github.com/mate-desktop/atril/commit/be5fadc) ev-sidebar-bookmarks: sostituita la funzione deprecata gtk_menu_popup
* [eac71e1](https://github.com/mate-desktop/atril/commit/eac71e1) ev-sidebar: sostituita la funzione deprecata gtk_menu_popup
* [95d6f03](https://github.com/mate-desktop/atril/commit/95d6f03) editable-toolbar: sostituita la funzione deprecata gtk_menu_popup
* [3168191](https://github.com/mate-desktop/atril/commit/3168191) libview: sostituita la deprecata gtk_flush
* [135e208](https://github.com/mate-desktop/atril/commit/135e208) disabilitata l'azione StartPresentation a schermo pieno se il documento non contiene pagine
* [de8c0ae](https://github.com/mate-desktop/atril/commit/de8c0ae) disabilitata l'azione ViewPresentation se il documento non contiene pagine
* [28243c0](https://github.com/mate-desktop/atril/commit/28243c0) libdocument: utilizzata gdk_pixbuf_get_from_surface()
* [c1a56c9](https://github.com/mate-desktop/atril/commit/c1a56c9) thumbnailer: Rimosso il codice inutilizzato
* [e5c8ce7](https://github.com/mate-desktop/atril/commit/e5c8ce7) view: Corretto il rendering della pagina durante il caricamento
* [3349fb9](https://github.com/mate-desktop/atril/commit/3349fb9) libdocument: Deprecata misc_get_page_border_size()
* [dc1432d](https://github.com/mate-desktop/atril/commit/dc1432d) view: Utilizzata una cornice renderizzata invece di un bordo personalizzato
* [bc7af60](https://github.com/mate-desktop/atril/commit/bc7af60) a11y: Ritornati i corretti offset di inizio e di fine
* [7c7c7ef](https://github.com/mate-desktop/atril/commit/7c7c7ef) a11y: Corretto un crash con il lettore dello schermo Orca
* [f3e061c](https://github.com/mate-desktop/atril/commit/f3e061c) libview: eliminato il codice deprecato non necessario
* [d909dd4](https://github.com/mate-desktop/atril/commit/d909dd4) ev-loading-message: Rimosse le variabili inutilizzate
* [6816696](https://github.com/mate-desktop/atril/commit/6816696) libview: corretta la selezione del testo con il mouse nella finestra delle annotazioni
* [efe29e6](https://github.com/mate-desktop/atril/commit/efe29e6) libview: corretta la compilazione senza epub
* [d03d688](https://github.com/mate-desktop/atril/commit/d03d688) shell: Non fare il dist i file generati
* [9c08159](https://github.com/mate-desktop/atril/commit/9c08159) Disabilitata la visualizzazione della presentazione se non c'è alcun documento
* [dc77310](https://github.com/mate-desktop/atril/commit/dc77310) Consentita la modifica della pagina di una presentazione
* [b0ea2c7](https://github.com/mate-desktop/atril/commit/b0ea2c7) libview: Corretta la finestra di goto nella modalità di presentazione
* [0c160a1](https://github.com/mate-desktop/atril/commit/0c160a1) libview: evitata la deprecata gdk_screen_get_monitor
* [557d371](https://github.com/mate-desktop/atril/commit/557d371) La renderizzazione sui monitor HiDPI è stata corretta 
* [5345f83](https://github.com/mate-desktop/atril/commit/5345f83) libview: corretta la condizione g_return in set_device_scale_on_surface()
* [2cae078](https://github.com/mate-desktop/atril/commit/2cae078) EvView: La renderizzazione sui monitor HiDPI è stata corretta
* [1d90b70](https://github.com/mate-desktop/atril/commit/1d90b70) libview: utilizzati i css per disegnare lo sfondo delle presentazioni
* [1b1f2c5](https://github.com/mate-desktop/atril/commit/1b1f2c5) Spostare i css personalizzati in un file compilato come gresource
* [11fc5dc](https://github.com/mate-desktop/atril/commit/11fc5dc) shell: Utilizzata GResource per i file di dati
* [5d51dc6](https://github.com/mate-desktop/atril/commit/5d51dc6) toolbar-editor: Aggiunti i metodi per caricare da GResource
* [c3fe25e](https://github.com/mate-desktop/atril/commit/c3fe25e) previewer: Utilizzata GResource per i file di dati
* [9668d3f](https://github.com/mate-desktop/atril/commit/9668d3f) compilazione: Aggiunta una verifica di configure per glib-compile-resources
* [3cb3227](https://github.com/mate-desktop/atril/commit/3cb3227) aggiornato il materiale per le traduzioni
* [0f605a3](https://github.com/mate-desktop/atril/commit/0f605a3) corretto distcheck
* [f671e62](https://github.com/mate-desktop/atril/commit/f671e62) libview: Verificato il numero delle pagine quando si processano gli eventi dei pulsanti
* [8597c1d](https://github.com/mate-desktop/atril/commit/8597c1d) libview: Aggiunta una verifica per i documenti senza pagine a ev_view_accessible_focus_changed
* [9fc7889](https://github.com/mate-desktop/atril/commit/9fc7889) libview: Verifica del numero delle pagine su ev_view_document_changed_cb, corretto un crash sui PDF corrotti senza pagine
* [a04ab7f](https://github.com/mate-desktop/atril/commit/a04ab7f) Usato GtkOverlay per mostrare il messaggio di caricamento
* [9ac0d1a](https://github.com/mate-desktop/atril/commit/9ac0d1a) shell: Rimossi i marshaler inutilizzati
* [cfbab0a](https://github.com/mate-desktop/atril/commit/cfbab0a) thumbnailer: inviati i messaggi di errore sullo stderr
* [2f89fcc](https://github.com/mate-desktop/atril/commit/2f89fcc) shell: utilizzato GtkApplication per inibire lo screensaver
* [15073fb](https://github.com/mate-desktop/atril/commit/15073fb) shell: port a GtkApplication
* [715e15b](https://github.com/mate-desktop/atril/commit/715e15b) shell: utilizzata g_printerr al posto di g_warning
* [da9c89f](https://github.com/mate-desktop/atril/commit/da9c89f) daemon: port a GtkApplication
* [131b29e](https://github.com/mate-desktop/atril/commit/131b29e) daemon: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Daemon
* [f44500b](https://github.com/mate-desktop/atril/commit/f44500b) shell: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Window
* [3f48838](https://github.com/mate-desktop/atril/commit/3f48838) shell: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Application
* [e51014b](https://github.com/mate-desktop/atril/commit/e51014b) libview: salvare i colori invertiti in un documento
* [4bb14f5](https://github.com/mate-desktop/atril/commit/4bb14f5) Salvare/ripristinare il contesto quando si recuperano i colori per uno stato differente
* [1f6278d](https://github.com/mate-desktop/atril/commit/1f6278d) epub: consente di salvare i documenti epub
* [ea3dfb1](https://github.com/mate-desktop/atril/commit/ea3dfb1) epub: corretto il caricamento delle miniature dei file epub
* [e79d266](https://github.com/mate-desktop/atril/commit/e79d266) controllo dei confini validi delle pagine accessibili
* [291facd](https://github.com/mate-desktop/atril/commit/291facd) shell: corretto l'acceleratore del menù per i colori invertiti
* [185e7b9](https://github.com/mate-desktop/atril/commit/185e7b9) shell: aggiunti gli acceleratori da tastierino numerico per il reset_zoom
* [580e4fa](https://github.com/mate-desktop/atril/commit/580e4fa) Aggiunto il reset dello zoom
* [35e1622](https://github.com/mate-desktop/atril/commit/35e1622) aggiunto atril.pot per auto-aggiornare le traduzioni
* [615a1d0](https://github.com/mate-desktop/atril/commit/615a1d0) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione 
* [7a91219](https://github.com/mate-desktop/atril/commit/7a91219) evitata la deprecata GtkStock
* [bb0203b](https://github.com/mate-desktop/atril/commit/bb0203b) aggiunto il supporto a travis-Cl
* [f16828c](https://github.com/mate-desktop/atril/commit/f16828c) rimossi i file generati
* [31b0fe8](https://github.com/mate-desktop/atril/commit/31b0fe8) Aggiunti i TypeDescription di pixbuf, tiff e xps a POTFILES.in
* [966e36f](https://github.com/mate-desktop/atril/commit/966e36f) spostato appdata nella cartella metainfo
* [a440818](https://github.com/mate-desktop/atril/commit/a440818) disabilitati i warning di deprecazione per distcheck
* [8bf0fa7](https://github.com/mate-desktop/atril/commit/8bf0fa7) utilizzate funzioni make per HELP_LINGUAS
* [413f6cc](https://github.com/mate-desktop/atril/commit/413f6cc) comics: supporto per il tipo MIME application/vnd.rar
* [91d5b0f](https://github.com/mate-desktop/atril/commit/91d5b0f) shell: salvare un documento nello stesso percorso da cui era stato aperto
* [f4b9c80](https://github.com/mate-desktop/atril/commit/f4b9c80) Ridotta la loquacità del demone di atril
* [a7d0b8d](https://github.com/mate-desktop/atril/commit/a7d0b8d) EvView: Corretto il movimento del cursore quando l'ordine delle righe logiche e visuali è diverso
* [2f89c60](https://github.com/mate-desktop/atril/commit/2f89c60) Aggiornato atril_start_window.png
* [bf74341](https://github.com/mate-desktop/atril/commit/bf74341) modificato moveable (vecchia grafia) -> movable
* [81934df](https://github.com/mate-desktop/atril/commit/81934df) Aggiornato lo screenshot in Catalano
* [a6c6e13](https://github.com/mate-desktop/atril/commit/a6c6e13) sincronizzazione con transifex
* [d980c12](https://github.com/mate-desktop/atril/commit/d980c12) aggiornato atril.pot
* [b365c22](https://github.com/mate-desktop/atril/commit/b365c22) disabilitata l'azione StartPresentation a schermo pieno se il documento non contiene pagine
* [e710942](https://github.com/mate-desktop/atril/commit/e710942) disabilitata l'azione ViewPresentation se il documento non contiene pagine
* [73ca242](https://github.com/mate-desktop/atril/commit/73ca242) libdocument: utilizzata gdk_pixbuf_get_from_surface()
* [62ca1c0](https://github.com/mate-desktop/atril/commit/62ca1c0) thumbnailer: Rimosso il codice inutilizzato
* [027a658](https://github.com/mate-desktop/atril/commit/027a658) view: Corretto il rendering della pagina durante il caricamento
* [df069ae](https://github.com/mate-desktop/atril/commit/df069ae) libdocument: Deprecata misc_get_page_border_size()
* [c09efef](https://github.com/mate-desktop/atril/commit/c09efef) view: Utilizzata una cornice renderizzata invece di un bordo personalizzato
* [0d84113](https://github.com/mate-desktop/atril/commit/0d84113) a11y: Ritornati i corretti offset di inizio e di fine
* [e3ce0a4](https://github.com/mate-desktop/atril/commit/e3ce0a4) a11y: Corretto un crash con il lettore dello schermo Orca
* [4065873](https://github.com/mate-desktop/atril/commit/4065873) libview: eliminato il codice deprecato non necessario
* [bb4e4b7](https://github.com/mate-desktop/atril/commit/bb4e4b7) ev-loading-message: Rimosse le variabili inutilizzate
* [05b1f12](https://github.com/mate-desktop/atril/commit/05b1f12) libview: corretta la selezione del testo con il mouse nella finestra delle annotazioni
* [4ecb058](https://github.com/mate-desktop/atril/commit/4ecb058) libview: corretta la compilazione senza epub
* [6fe6574](https://github.com/mate-desktop/atril/commit/6fe6574) shell: Non fare il dist dei file generati
* [c238f51](https://github.com/mate-desktop/atril/commit/c238f51) Disabilitata la visualizzazione presentazione se non c'è alcun documento
* [50bdf3f](https://github.com/mate-desktop/atril/commit/50bdf3f) Consentita la modifica della pagina di una presentazione
* [454ca8b](https://github.com/mate-desktop/atril/commit/454ca8b) libview: Corretta la finestra goto nella modalità presentazione
* [b9dcc2a](https://github.com/mate-desktop/atril/commit/b9dcc2a) libview: evitata la deprecata gdk_screen_get_monitor
* [c0cf2c6](https://github.com/mate-desktop/atril/commit/c0cf2c6) EvPresentationView: La renderizzazione sui monitor HiDPI è stata corretta 
* [14c88f2](https://github.com/mate-desktop/atril/commit/14c88f2) libview: corretta la condizione g_return in set_device_scale_on_surface()
* [58486bb](https://github.com/mate-desktop/atril/commit/58486bb) EvView: La renderizzazione sui monitor HiDPI è stata corretta
* [02970c6](https://github.com/mate-desktop/atril/commit/02970c6) libview: utilizzati i css per disegnare lo sfondo delle presentazioni
* [1e531cb](https://github.com/mate-desktop/atril/commit/1e531cb) Spostare i css personalizzati in un file compilato come gresource
* [c7fcfa1](https://github.com/mate-desktop/atril/commit/c7fcfa1) shell: Utilizzata GResource per i file di dati
* [e0f26b9](https://github.com/mate-desktop/atril/commit/e0f26b9) toolbar-editor: Aggiunti i metodi per caricare da GResource
* [6b84d6f](https://github.com/mate-desktop/atril/commit/6b84d6f) previewer: Utilizzata GResource per i file di dati
* [95437d1](https://github.com/mate-desktop/atril/commit/95437d1) build: Aggiunta una verifica di configure per glib-compile-resources
* [eaee969](https://github.com/mate-desktop/atril/commit/eaee969) aggiornato il materiale per le traduzioni
* [c417e7c](https://github.com/mate-desktop/atril/commit/c417e7c) corretto distcheck
* [3fddbe7](https://github.com/mate-desktop/atril/commit/3fddbe7) libview: Verificato il numero delle pagine quando si processano gli eventi dei pulsanti
* [10d764d](https://github.com/mate-desktop/atril/commit/10d764d) libview: Aggiunta una verifica per i documenti senza pagine a ev_view_accessible_focus_changed
* [aa3bcfa](https://github.com/mate-desktop/atril/commit/aa3bcfa) libview: Verifica del numero delle pagine su ev_view_document_changed_cb, corretto un crash sui PDF corrotti senza pagine
* [6346384](https://github.com/mate-desktop/atril/commit/6346384) Usato GtkOverlay per mostrare il messaggio di caricamento
* [7d0ac84](https://github.com/mate-desktop/atril/commit/7d0ac84) shell: Rimossi i marshaler inutilizzati
* [c99d768](https://github.com/mate-desktop/atril/commit/c99d768) thumbnailer: inviati i messaggi di errore sullo stderr
* [21073d4](https://github.com/mate-desktop/atril/commit/21073d4) shell: utilizzato GtkApplication per inibire lo screensaver
* [674a6b3](https://github.com/mate-desktop/atril/commit/674a6b3) shell: port a GtkApplication
* [b0f83ee](https://github.com/mate-desktop/atril/commit/b0f83ee) shell: Utilizzata g_printerr al posto di g_warning
* [0884be6](https://github.com/mate-desktop/atril/commit/0884be6) daemon: port a GtkApplication
* [3728fb7](https://github.com/mate-desktop/atril/commit/3728fb7) daemon: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Daemon
* [e2420ea](https://github.com/mate-desktop/atril/commit/e2420ea) shell: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Window
* [18a20e8](https://github.com/mate-desktop/atril/commit/18a20e8) shell: Utilizzato gdbus-codegen per l'interfaccia org.mate.atril.Application
* [e4f8fce](https://github.com/mate-desktop/atril/commit/e4f8fce) libview: salvare i colori invertiti in un documento
* [6217a89](https://github.com/mate-desktop/atril/commit/6217a89) Salvare/ripristinare il contesto quando si recuperano i colori per uno stato differente
* [56e08ae](https://github.com/mate-desktop/atril/commit/56e08ae) aggiornato il file pot per le traduzioni
* [27f459a](https://github.com/mate-desktop/atril/commit/27f459a) epub: consente di salvare i documenti epub
* [bd799f4](https://github.com/mate-desktop/atril/commit/bd799f4) epub: corretto il caricamento delle miniature dei file epub
* [8770730](https://github.com/mate-desktop/atril/commit/8770730) shell: corretto l'acceleratore del menù per i colori invertiti
* [1c2e9ea](https://github.com/mate-desktop/atril/commit/1c2e9ea) shell: aggiunti gli acceleratori da tastierino numerico per il reset_zoom
* [7619dc6](https://github.com/mate-desktop/atril/commit/7619dc6) Aggiunto il reset dello zoom
* [58e7446](https://github.com/mate-desktop/atril/commit/58e7446) evitata la deprecata GtkStock
* [005d885](https://github.com/mate-desktop/atril/commit/005d885) controllo dei confini validi delle pagine accessibili
* [4f0467b](https://github.com/mate-desktop/atril/commit/4f0467b) aggiunto atril.pot per auto-aggiornare le traduzioni
* [42e6a5f](https://github.com/mate-desktop/atril/commit/42e6a5f) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione 

### caja
* [601c853](https://github.com/mate-desktop/caja/commit/601c853) eel-gdk-pixbuf-extensions: corretta una divisione per zero
* [6e6c9c6](https://github.com/mate-desktop/caja/commit/6e6c9c6) caja-file: Corretto l'utilizzo della memoria dopo che è stata liberata
* [0bd2d81](https://github.com/mate-desktop/caja/commit/0bd2d81) caja-icon-container: Corretto l'utilizzo della memoria dopo che è stata liberata
* [1848d37](https://github.com/mate-desktop/caja/commit/1848d37) fm-tree-model: Corretto l'utilizzo della memoria dopo che è stata liberata
* [7c9ae01](https://github.com/mate-desktop/caja/commit/7c9ae01) caja-information-panel: Corretto l'utilizzo della memoria dopo che è stata liberata
* [7b605dd](https://github.com/mate-desktop/caja/commit/7b605dd) fm-directory-view:  Corretto l'utilizzo della memoria dopo che è stata liberata
* [58312fd](https://github.com/mate-desktop/caja/commit/58312fd) caja-tree-view-drag-dest: corretto un memory leak
* [7a26045](https://github.com/mate-desktop/caja/commit/7a26045) [Security] eel-string: utilizzo di 'g_strlcat' al posto di 'strcat'
* [fede367](https://github.com/mate-desktop/caja/commit/fede367) [Security]  Utilizzo di 'g_strlcpy' al posto di 'strcpy'
* [da3b634](https://github.com/mate-desktop/caja/commit/da3b634) Aggiunto lo script update-authors.pl che aiuta ad aggiornare caja.about
* [5379181](https://github.com/mate-desktop/caja/commit/5379181) Leggere authors e documenters dal file caja.about
* [f5e08dd](https://github.com/mate-desktop/caja/commit/f5e08dd) Assicurata la corretta traduzione del titolo della finestra di dialogo informazioni
* [65aaac0](https://github.com/mate-desktop/caja/commit/65aaac0) Prepararsi per l'unione di docker-build 0.1.1 al master
* [222fcc0](https://github.com/mate-desktop/caja/commit/222fcc0) Aggiornato authors
* [ba01c8c](https://github.com/mate-desktop/caja/commit/ba01c8c) Aggiornato documenters
* [852f992](https://github.com/mate-desktop/caja/commit/852f992) utilizzate le immagini archlinux/base 
* [42082f6](https://github.com/mate-desktop/caja/commit/42082f6) Rimosso l'override del valore di ritorno di distcheck
* [86b93da](https://github.com/mate-desktop/caja/commit/86b93da) aggiornato caja.pot per transifex
* [9bec3b7](https://github.com/mate-desktop/caja/commit/9bec3b7) corretto il fallimento di distcheck su debian
* [2d59514](https://github.com/mate-desktop/caja/commit/2d59514) corretta la stringa di aiuto di --disable-self-check
* [5e5c47f](https://github.com/mate-desktop/caja/commit/5e5c47f) restituire sempre 0 per distcheck
* [78b7682](https://github.com/mate-desktop/caja/commit/78b7682) aggiornato travis per il supporto ad archlinux e abilitato distcheck
* [91f1dc6](https://github.com/mate-desktop/caja/commit/91f1dc6)  Aggiunto --disable-self-check a configure
* [3daa55c](https://github.com/mate-desktop/caja/commit/3daa55c) Evitata la deprecata g_type_class_add_private in src
* [4e42def](https://github.com/mate-desktop/caja/commit/4e42def) Corretta l'incompatibilità dei tipi dei puntatori
* [e99050a](https://github.com/mate-desktop/caja/commit/e99050a) Evitata la deprecata g_type_class_add_private in src
* [7920f97](https://github.com/mate-desktop/caja/commit/7920f97) Evitata la deprecata g_type_class_add_private in libcaja-private
* [0b07371](https://github.com/mate-desktop/caja/commit/0b07371) Evitata la deprecata g_type_class_add_private in libcaja-private
* [e5129f9](https://github.com/mate-desktop/caja/commit/e5129f9)  Evitata la deprecata g_type_class_add_private in libcaja-private
* [e226dda](https://github.com/mate-desktop/caja/commit/e226dda) Abilitato Travis Cl
* [9cd63d4](https://github.com/mate-desktop/caja/commit/9cd63d4) Evitata la deprecata g_type_class_add_private in libcaja-private
* [4196136](https://github.com/mate-desktop/caja/commit/4196136) Evitata la deprecata g_type_class_add_private in src
* [328d820](https://github.com/mate-desktop/caja/commit/328d820) corretti i warning di compilazione
* [dbfd51e](https://github.com/mate-desktop/caja/commit/dbfd51e) Consentire alle unità di misura dei file di seguire le preferenze dell'utente
* [0a37810](https://github.com/mate-desktop/caja/commit/0a37810) Fissati il valore 6 mesi ed 1 anno.
* [3a22d4c](https://github.com/mate-desktop/caja/commit/3a22d4c) Supportata l'interrogazione dei file per data di modifica e per dimensione
* [e8f124d](https://github.com/mate-desktop/caja/commit/e8f124d) Evitata la deprecata g_type_class_add_private
* [331a0e1](https://github.com/mate-desktop/caja/commit/331a0e1) Aggiornato il copyright al 2019
* [d373d6c](https://github.com/mate-desktop/caja/commit/d373d6c) CajaApplication: Evitata la deprecata 'g_type_class_add_private'
* [a9211bd](https://github.com/mate-desktop/caja/commit/a9211bd) caja-menu: Evitata la deprecata g_type_class_add_private
* [10efec8](https://github.com/mate-desktop/caja/commit/10efec8) [eel][libegg] Utilizzo della macro G_DEFINE_TYPE_WITH_PRIVATE
* [f0775c8](https://github.com/mate-desktop/caja/commit/f0775c8) configure.ac: Aggiunto un controllo perché sia impostato PKG_CONFIG.
* [7408146](https://github.com/mate-desktop/caja/commit/7408146) corretto distcheck
* [a35b46f](https://github.com/mate-desktop/caja/commit/a35b46f) caja-application: controllare smclient prima del tentativo di caricare la sessione
* [3eb0ff8](https://github.com/mate-desktop/caja/commit/3eb0ff8) [eel] Evitata la deprecata g_type_class_add_private
* [9fc6f1f](https://github.com/mate-desktop/caja/commit/9fc6f1f) [libegg] Evitata la deprecata g_type_class_add_private
* [9991fb1](https://github.com/mate-desktop/caja/commit/9991fb1) [libcaja-private] Ri-verificato il tipo MIME prima della selezione di una applicazione
* [e51b16d](https://github.com/mate-desktop/caja/commit/e51b16d) [file-manager] Corretto un bug apparente nel menù contestuale aggiornando il codice.
* [cf23b9a](https://github.com/mate-desktop/caja/commit/cf23b9a) Ritornati a "fm-directory-view.c: e Diminuito l'intervallo minimo di aggiornamento."
* [e7b68e0](https://github.com/mate-desktop/caja/commit/e7b68e0) Correzione: oggetto bizzarro nei segnalibri se veniva rimossa la cartella
* [1846d75](https://github.com/mate-desktop/caja/commit/1846d75) Lieve miglioramento della qualità del codice
* [89db50e](https://github.com/mate-desktop/caja/commit/89db50e) Dimenticato di inizializzare il campo is_backup
* [34d0676](https://github.com/mate-desktop/caja/commit/34d0676) Modificata la scorciatoia a mostra/nascondi i file di backup
* [2d66485](https://github.com/mate-desktop/caja/commit/2d66485) Rimossi inutili commenti, corretta la stringa descrittiva
* [06b4f4c](https://github.com/mate-desktop/caja/commit/06b4f4c) Saltare solo i file nascosti, non i backup
* [58e9876](https://github.com/mate-desktop/caja/commit/58e9876) Aggiunta un indipendente nascondi/mostra file di backup
* [040a897](https://github.com/mate-desktop/caja/commit/040a897) cancellata l'inutile icona di nautilus
* [75e89ca](https://github.com/mate-desktop/caja/commit/75e89ca) caja-progress-info: nuovo comportamento con notifiche:
* [08f479a](https://github.com/mate-desktop/caja/commit/08f479a) caja-progress-info: mostra le notifiche con la chiave gsettings:
* [d054f14](https://github.com/mate-desktop/caja/commit/d054f14) spostato appdata nella cartella metainfo
* [750c034](https://github.com/mate-desktop/caja/commit/750c034) disabilitati i warning di deprecazione per distcheck
* [116ba41](https://github.com/mate-desktop/caja/commit/116ba41) caja-places-sidebar: sostituire due altri usi di g_drive_poll_for_media_finish
* [884870c](https://github.com/mate-desktop/caja/commit/884870c) Corretto un segfault quando si fermano gli hard disk USB
* [c12b61b](https://github.com/mate-desktop/caja/commit/c12b61b) caja-bookmark: corretto il memory leak
* [a8de3bb](https://github.com/mate-desktop/caja/commit/a8de3bb) fm-properties-window: corretti i memory leak
* [09eda67](https://github.com/mate-desktop/caja/commit/09eda67) caja-desktop-link-monitor: corretto il memory leak
* [056832f](https://github.com/mate-desktop/caja/commit/056832f) eel-gtk-extensions: corretti i memory leak
* [6dbdc90](https://github.com/mate-desktop/caja/commit/6dbdc90) Gsettings dovrebbe inizializzarsi prima di utilizzarlo
* [74d2b19](https://github.com/mate-desktop/caja/commit/74d2b19) sincronizzazione con transifex
* [2676eaf](https://github.com/mate-desktop/caja/commit/2676eaf) Corretto un confronto che ignora le maiuscole in running_in_mate
* [0bffad7](https://github.com/mate-desktop/caja/commit/0bffad7) monitor: corretto il crash nello smontare i filesystem remoti
* [d8d375b](https://github.com/mate-desktop/caja/commit/d8d375b) CajaFile: corretto il crash in modify_link_hash_table
* [ae033ba](https://github.com/mate-desktop/caja/commit/ae033ba) connect-server-dialog: Rispettate le impostazioni del salvataggio delle password
* [bc0b2cb](https://github.com/mate-desktop/caja/commit/bc0b2cb) properties-window: corretto il controllo di uno stato incoerente
* [8fff655](https://github.com/mate-desktop/caja/commit/8fff655) monitor: controllati i montaggi non-nativi su GVolumeMonitor
* [09146ca](https://github.com/mate-desktop/caja/commit/09146ca) Aggiunta una interfaccia 'Configurable' e aggiunto il supporto a caja-file-management-properties
* [adeaed2](https://github.com/mate-desktop/caja/commit/adeaed2) caja-application.c: Rimosse le linee vuote ridondanti
* [dba8610](https://github.com/mate-desktop/caja/commit/dba8610) Aggiornata la pagina man di caja con le informazioni sull'opzione "--force-desktop"
* [6c423bc](https://github.com/mate-desktop/caja/commit/6c423bc) Caja-icon-info: Ottimizzato l'aspetto dell'icona da GIcon.
* [021ff2a](https://github.com/mate-desktop/caja/commit/021ff2a) fm-directory-view.c: Diminuito l'intervallo minimo di aggiornamento.
* [336f351](https://github.com/mate-desktop/caja/commit/336f351) Rimosso il codice morto e corretto un memory leak
* [6a31ce6](https://github.com/mate-desktop/caja/commit/6a31ce6) Aggiungere l'opzione per aprire più URI in schede all'avvio
* [fb9a3cf](https://github.com/mate-desktop/caja/commit/fb9a3cf) Annullare "aggiungere l'opzione per aprire più URI in schede all'avvio"
* [0d7a79d](https://github.com/mate-desktop/caja/commit/0d7a79d) Annullare "corretto un memory leak"
* [e362fef](https://github.com/mate-desktop/caja/commit/e362fef) Annullare "Correggere l'indentazione, aggiornare i documenti per riflettere la capacità di aprire più URI in schede"
* [424cf44](https://github.com/mate-desktop/caja/commit/424cf44) Correggere l'indentazione, aggiornare i documenti per riflettere la capacità di aprire più URI in schede
* [04f7e80](https://github.com/mate-desktop/caja/commit/04f7e80) corretto un memory leak
* [fd1f45f](https://github.com/mate-desktop/caja/commit/fd1f45f) Aggiungere l'opzione per aprire più URI in schede all'avvio
* [3619f72](https://github.com/mate-desktop/caja/commit/3619f72) pathbar: Attivato il pannello quando si cambia posizione
* [c455418](https://github.com/mate-desktop/caja/commit/c455418) aggiunta la possibilità di scorrere tra le schede con  [ctrl+tab] e [ctrl+shift+tab]
* [e740a98](https://github.com/mate-desktop/caja/commit/e740a98) caja-window: Corretto il non funzionamento del mouse con  [ctrl] + [.] o [ctrl] + [;]
* [5b20286](https://github.com/mate-desktop/caja/commit/5b20286) caja-desktop-directory: fermati i segfault in directory_ready_callback
* [a2fa06f](https://github.com/mate-desktop/caja/commit/a2fa06f) caja-directory.c: corretti i warning di compilazione
* [f9bae2f](https://github.com/mate-desktop/caja/commit/f9bae2f) pathbar: Aumentare il conteggio delle reference del percorso in update_button_types
* [acdb7e2](https://github.com/mate-desktop/caja/commit/acdb7e2) Corretti alcuni problemi trovati con l'analisi statica
* [191aa39](https://github.com/mate-desktop/caja/commit/191aa39) libcaja-private: Rimossa l'applicazione ridondante prefs dalla hash table
* [78d9182](https://github.com/mate-desktop/caja/commit/78d9182) [desktop-bg] Corretto il memory leak durante gli eventi della modifica dello sfondo
* [2d179e4](https://github.com/mate-desktop/caja/commit/2d179e4) caja-location-bar: Modificato il colore dello sfondo in base allo stato di attività
* [970cda6](https://github.com/mate-desktop/caja/commit/970cda6) sincronizzazione con transifex
* [76c2a2a](https://github.com/mate-desktop/caja/commit/76c2a2a) eel-gtk-extensions: mostrare le icone nel menù del tasto destro del mouse solo se è impostata "menus-have-icons"
* [eafef85](https://github.com/mate-desktop/caja/commit/eafef85) caja-sidebar-title: Correzione: immagini rotte nella barra laterale
* [a797afc](https://github.com/mate-desktop/caja/commit/a797afc) caja-progress-info.c: mostrare le notifiche con la chiave gsettings:
* [639c902](https://github.com/mate-desktop/caja/commit/639c902) caja-progress-info.c: Evitata la deprecata 'gtk_status_icon_get_visible'
* [e7942e9](https://github.com/mate-desktop/caja/commit/e7942e9) caja-sidebar-title: corretto il warning [-Wmaybe-uninitialized]
* [df6643a](https://github.com/mate-desktop/caja/commit/df6643a) desktop window: Aggiunto l'attributo is-desktop AtkObject
* [3720401](https://github.com/mate-desktop/caja/commit/3720401) caja-desktop-window.c: Corretto il crash inaspettato di caja
* [b0899ef](https://github.com/mate-desktop/caja/commit/b0899ef) evitata la deprecata 'gtk_widget_override_font'
* [347e1f1](https://github.com/mate-desktop/caja/commit/347e1f1) evitata la deprecata 'gtk_window_set_wmclass'
* [cfc9b47](https://github.com/mate-desktop/caja/commit/cfc9b47) caja-bookmark.c: eliminata una variabile inutilizzata
* [a3195d0](https://github.com/mate-desktop/caja/commit/a3195d0) caja-bookmark.c: Corrette le icone nei segnalibri
* [eb65d22](https://github.com/mate-desktop/caja/commit/eb65d22) icon-container: evitata la deprecata 'gtk_style_context_get_border_color'
* [6841bd7](https://github.com/mate-desktop/caja/commit/6841bd7) evitata la deprecata 'gtk_dialog_get_action_area'
* [c31de77](https://github.com/mate-desktop/caja/commit/c31de77) aggiornato il potfile
* [c0f159d](https://github.com/mate-desktop/caja/commit/c0f159d) Pathbar button: corretta la poca risposta al clic destro
* [9f08546](https://github.com/mate-desktop/caja/commit/9f08546) editable-label: evitata la deprecata 'gtk_im_multicontext_append_menuitems'
* [9bf65ee](https://github.com/mate-desktop/caja/commit/9bf65ee) zoom-control: utilizzato NULL al posto di una variabile non inizializzata
* [13fe58e](https://github.com/mate-desktop/caja/commit/13fe58e) rimossa una funzione inutilizzata
* [7cae49a](https://github.com/mate-desktop/caja/commit/7cae49a) utilizzato NULL al posto di una variabile non inizializzata
* [8a31b06](https://github.com/mate-desktop/caja/commit/8a31b06) eel-editable-label.c: evitata la deprecata 'gdk_keymap_get_default'
* [1aff6ea](https://github.com/mate-desktop/caja/commit/1aff6ea) eel-editable-label: evitata la deprecata gtk_style_context_set_background
* [c4777b0](https://github.com/mate-desktop/caja/commit/c4777b0) eel-gtk-extensions: sostituita la funzione deprecata gtk_menu_popup
* [42e5c91](https://github.com/mate-desktop/caja/commit/42e5c91) zoom-control: non più utilizzata la funzione eel_pop_up_context_menu
* [ddf6f38](https://github.com/mate-desktop/caja/commit/ddf6f38) sostituita la deprecata gtk_menu_popup
* [ded490e](https://github.com/mate-desktop/caja/commit/ded490e) libcaja-private: sostituite le funzioni deprecate gdk_error_trap
* [fc70465](https://github.com/mate-desktop/caja/commit/fc70465) fm-desktop-icon-view: sostituite le funzioni deprecate gdk_error_trap_push/pop
* [2392093](https://github.com/mate-desktop/caja/commit/2392093) sostituita la deprecata gdk_flush
* [5ed053f](https://github.com/mate-desktop/caja/commit/5ed053f) libcaja-private: corretto il warning di compilazione -Wlogical-not-parentheses
* [e88c26a](https://github.com/mate-desktop/caja/commit/e88c26a) evitata la deprecata 'gtk_style_context_get_background_color'
* [f250053](https://github.com/mate-desktop/caja/commit/f250053) sincronizzazione con transifex
* [c490029](https://github.com/mate-desktop/caja/commit/c490029) caja-spatial-window.c: evitata la deprecata 'gtk_vbox_new'
* [99cf0ca](https://github.com/mate-desktop/caja/commit/99cf0ca) Eliminata l'inondazione di eventi accessibili modificati-dai-figli sul ripopolamento del contenitore 
* [5e236e9](https://github.com/mate-desktop/caja/commit/5e236e9) Eliminata l'inondazione di eventi accessibili modificati-dai-figli durante aggiorna tutto
* [3c3f62d](https://github.com/mate-desktop/caja/commit/3c3f62d) Emesso il segnale  accessible-name-change per le icone solo quando le icone vengono rinominate
* [9f8d950](https://github.com/mate-desktop/caja/commit/9f8d950) libcaja-private/caja-recent.c: gvfs-open è uno strumento deprecato, passati a "gio open" da libglib2.0-bin.
* [4d4f750](https://github.com/mate-desktop/caja/commit/4d4f750) sidebar popup menu: mostrata l'icona "media-eject" tra gli elementi "unmount" 
* [f8e6051](https://github.com/mate-desktop/caja/commit/f8e6051) aggiornato il potfile
* [01a8519](https://github.com/mate-desktop/caja/commit/01a8519) pathbar: corretto un segfault casuale aprendo mounts dal Desktop
* [f6a4e9c](https://github.com/mate-desktop/caja/commit/f6a4e9c) fm-icon-view: Mostrata la dimensione del disco come criterio di ordinamento
* [7a76ce4](https://github.com/mate-desktop/caja/commit/7a76ce4) sidebar popup menu: mostrata l'icona "media-eject"
* [2786f3c](https://github.com/mate-desktop/caja/commit/2786f3c) aggiornato il potfile
* [0585258](https://github.com/mate-desktop/caja/commit/0585258) Aggiunto un criterio di ordinamento secondo i segmenti di estensione invertiti
* [68ace00](https://github.com/mate-desktop/caja/commit/68ace00) impostati i nomi delle icone invece degli identificativi stock in alcuni posti
* [b70d394](https://github.com/mate-desktop/caja/commit/b70d394) caja-spatial-window.c: evitata la deprecata GtkImageMenuItem
* [a00bad2](https://github.com/mate-desktop/caja/commit/a00bad2) Corretti i warning dai commit HiDPI
* [9ea3b71](https://github.com/mate-desktop/caja/commit/9ea3b71) sidebar: Rispettata la dimensione della barra laterale sugli HiDPI
* [554a036](https://github.com/mate-desktop/caja/commit/554a036) HiDPI: Convertiti i Pixbuf in Superfici Cairo
* [280ef82](https://github.com/mate-desktop/caja/commit/280ef82) general: utilizzata gdk_monitor_get_scale_factor
* [e28ff9c](https://github.com/mate-desktop/caja/commit/e28ff9c) list-view: utilizzata la superfice cairo come una icona trascinabile
* [ef78aa3](https://github.com/mate-desktop/caja/commit/ef78aa3) Scalare le dimensioni dello schermo
* [cfd5021](https://github.com/mate-desktop/caja/commit/cfd5021) icon-info: l'hash/store delle icone utilizza il fattore di scala così come la dimensione
* [47246e2](https://github.com/mate-desktop/caja/commit/47246e2) file: supportato HiDPI per le immagini delle miniature
* [c0d60fc](https://github.com/mate-desktop/caja/commit/c0d60fc) properties-window: supportato HiDpi per l'icona della finestra delle proprietà
* [bc1405c](https://github.com/mate-desktop/caja/commit/bc1405c) Supportate le icone HiDpi
* [779e0af](https://github.com/mate-desktop/caja/commit/779e0af) canvas-container: ascoltare il fattore di scala per invalidare le icone
* [a864855](https://github.com/mate-desktop/caja/commit/a864855) canvas-item: utilizzato gtk_render_icon_surface per la superficie Drag-n-Drop
* [35eb416](https://github.com/mate-desktop/caja/commit/35eb416) desktop-canvas-view: Scalata l'area di lavoro del desktop
* [37ebfa8](https://github.com/mate-desktop/caja/commit/37ebfa8) versione pre-aggiornamento
* [d20ceac](https://github.com/mate-desktop/caja/commit/d20ceac) caja-side-pane.c: evitata la deprecata GtkImageMenuItem
* [ffb953f](https://github.com/mate-desktop/caja/commit/ffb953f) caja-navigation-window-pane.c: evitata la deprecata GtkImageMenuItem
* [9b6b0dc](https://github.com/mate-desktop/caja/commit/9b6b0dc) caja-navigation-window-menus.c: eliminata una variabile inutilizzata
* [72968ab](https://github.com/mate-desktop/caja/commit/72968ab) caja-navigation-window-menus.c: evitata la deprecata GtkImageMenuItem
* [e9bd5cb](https://github.com/mate-desktop/caja/commit/e9bd5cb) caja-bookmark: evitata la deprecata GtkImageMenuItem
* [3403ff7](https://github.com/mate-desktop/caja/commit/3403ff7) caja-places-sidebar.c: evitata la deprecata GtkImageMenuItem
* [70ebaf4](https://github.com/mate-desktop/caja/commit/70ebaf4) caja-emblem-sidebar.c: evitata la deprecata GtkImageMenuItem
* [414fdf7](https://github.com/mate-desktop/caja/commit/414fdf7) fm-tree-view.c: eliminata una variabile inutilizzata
* [844df9d](https://github.com/mate-desktop/caja/commit/844df9d) modificato il codice di errore: fatto terminare lo statement con un punto e virgola
* [e031d4f](https://github.com/mate-desktop/caja/commit/e031d4f) fm-tree-view.c: evitata la deprecata GtkImageMenuItem
* [8bebf06](https://github.com/mate-desktop/caja/commit/8bebf06) renominata 'mate_image_menu_item...' in 'eel_image_menu_item_new_from_icon'
* [ffc9106](https://github.com/mate-desktop/caja/commit/ffc9106) eel-editable-label.c: evitata 'append_action_signal' con gli identificativi stock
* [7991810](https://github.com/mate-desktop/caja/commit/7991810) caja-query-editor.c: aggiunto #include &lt;eel/eel-stock-dialogs.h&gt;
* [7c9b80c](https://github.com/mate-desktop/caja/commit/7c9b80c) evitata 'gtk_file_chooser_dialog_new' con gli identificativi stock
* [4fb3590](https://github.com/mate-desktop/caja/commit/4fb3590) evitata gtk_dialog_new_with_buttons con gli identificativi stock
* [d4711ef](https://github.com/mate-desktop/caja/commit/d4711ef) aggiunto caja.pot per auto-aggiornare le traduzioni
* [68fb5e4](https://github.com/mate-desktop/caja/commit/68fb5e4) evitata gtk_dialog_add_buttons con gli identificativi stock
* [dfb6585](https://github.com/mate-desktop/caja/commit/dfb6585) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione 
* [683e944](https://github.com/mate-desktop/caja/commit/683e944) caja-file-management-properties.ui: evitate le deprecate GtkVBox e GtkHBox
* [d66b717](https://github.com/mate-desktop/caja/commit/d66b717) caja-bookmarks-window.ui: evitate le deprecate:
* [ed46e15](https://github.com/mate-desktop/caja/commit/ed46e15) renominato mate_dialog_add_button in eel_dialog_add_button
* [4901253](https://github.com/mate-desktop/caja/commit/4901253) utilizzata la versione di sviluppo
* [20fe122](https://github.com/mate-desktop/caja/commit/20fe122) versione pre-aggiornamento
* [7763ec9](https://github.com/mate-desktop/caja/commit/7763ec9) evitata eel_create_question_dialog con gli identificativi stock
* [f0ab0d4](https://github.com/mate-desktop/caja/commit/f0ab0d4) evitata eel_run_simple_dialog con gli identificativi stock
* [9778a3a](https://github.com/mate-desktop/caja/commit/9778a3a) eel-stock-dialogs: evitata gtk_dialog_add_button con gli identificativi stock
* [5f0ad00](https://github.com/mate-desktop/caja/commit/5f0ad00) caja-file-operations: evitata gtk_dialog_add_buttons con gli identificativi stock
* [01cec7e](https://github.com/mate-desktop/caja/commit/01cec7e) rimossi i warning in esecuzione nell'utilizzo di caja_clipboard_set_up_editable
* [ab30e57](https://github.com/mate-desktop/caja/commit/ab30e57) caja-file-conflict-dialog: evitata gtk_dialog_add_buttons con gli identificativi stock
* [e313685](https://github.com/mate-desktop/caja/commit/e313685) evitata la deprecata GtkButton:use-stock
* [012d9f8](https://github.com/mate-desktop/caja/commit/012d9f8) si possono selezionare tutte le parole chiave di ricerca con Ctrl+a. #918
* [54a9de1](https://github.com/mate-desktop/caja/commit/54a9de1) caja-autorun: evitata gtk_dialog_add_buttons con gli identificativi stock
* [ff1b432](https://github.com/mate-desktop/caja/commit/ff1b432) eel-editable-label.c: evitata gtk_image_menu_item_new_from_stock
* [cff14d0](https://github.com/mate-desktop/caja/commit/cff14d0) caja-file-management-properties.ui: evitate le proprietà stock:
* [f8a7e7a](https://github.com/mate-desktop/caja/commit/f8a7e7a) Toolbar: trova icona: utilizzato il nome invece dell'identificativo stock
* [7e8bb46](https://github.com/mate-desktop/caja/commit/7e8bb46) caja-bookmarks-window.ui: evitata la deprecata GtkButton:use-stock
* [dd4c0f7](https://github.com/mate-desktop/caja/commit/dd4c0f7) CAJA_TYPE_NAVIGATION_ACTION: evitata la proprietà deprecata "stock_id"
* [bbc0211](https://github.com/mate-desktop/caja/commit/bbc0211) corretto il rendering degli sfondi e del contenuto della finestra di dialogo dei simboli
* [bf3da8e](https://github.com/mate-desktop/caja/commit/bf3da8e) evitata la deprecata GtkStock
* [22aad8d](https://github.com/mate-desktop/caja/commit/22aad8d) utilizzate le immagini di archlinux/base
* [f2a22d2](https://github.com/mate-desktop/caja/commit/f2a22d2) Rimosso l'override del valore di ritorno di distcheck
* [7ae4cd8](https://github.com/mate-desktop/caja/commit/7ae4cd8) corretta la stringa di aiuto di --disable-self-check
* [89a3be2](https://github.com/mate-desktop/caja/commit/89a3be2) Aggiunto --disable-self-check per configure
* [e6bfa07](https://github.com/mate-desktop/caja/commit/e6bfa07) aggiunto config di travis-ci
* [22d0e28](https://github.com/mate-desktop/caja/commit/22d0e28) corretto il fallimento di distcheck su debian
* [017b058](https://github.com/mate-desktop/caja/commit/017b058) pathbar: corretto un segfault casuale aprendo mounts dal Desktop
* [94c2f1c](https://github.com/mate-desktop/caja/commit/94c2f1c) spostato appdata nella cartella metainfo
* [ed4730c](https://github.com/mate-desktop/caja/commit/ed4730c) disabilitati i warning di deprecazione per distcheck
* [311ab2b](https://github.com/mate-desktop/caja/commit/311ab2b) caja-places-sidebar: sostituire due altri usi di g_drive_poll_for_media_finish
* [df49a00](https://github.com/mate-desktop/caja/commit/df49a00) Corretto un segfault quando si fermano gli hard disk USB
* [157d047](https://github.com/mate-desktop/caja/commit/157d047) fm-properties-window: corretti i memory leak
* [bd0d998](https://github.com/mate-desktop/caja/commit/bd0d998) caja-desktop-link-monitor: corretto un memory leak
* [78607a5](https://github.com/mate-desktop/caja/commit/78607a5) Corretto un confronto che ignora le maiuscole in running_in_mate
* [5200838](https://github.com/mate-desktop/caja/commit/5200838) pathbar: Attivato il pannello quando si cambia posizione
* [f19255f](https://github.com/mate-desktop/caja/commit/f19255f) caja-window: corretto il non funzionamento del mouse con [ctrl] + [.] o [ctrl] + [;]
* [ba087de](https://github.com/mate-desktop/caja/commit/ba087de) desktop window: Aggiunto l'attributo AtkObject is-desktop 
* [a58d52a](https://github.com/mate-desktop/caja/commit/a58d52a) Corretti i warning dai commit HiDPI
* [ce14bef](https://github.com/mate-desktop/caja/commit/ce14bef) sidebar: Rispettata la dimensione della barra laterale sugli HiDPI
* [dade92d](https://github.com/mate-desktop/caja/commit/dade92d) HiDPI: Convertiti i Pixbuf in Superfici Cairo
* [556663a](https://github.com/mate-desktop/caja/commit/556663a) general: utilizzata gdk_monitor_get_scale_factor
* [0630180](https://github.com/mate-desktop/caja/commit/0630180) list-view: utilizzata la superfice cairo come una icona trascinabile
* [1a14801](https://github.com/mate-desktop/caja/commit/1a14801) Scalate le dimensioni dello schermo
* [4c377ba](https://github.com/mate-desktop/caja/commit/4c377ba) icon-info: l'hash/store delle icone utilizza il fattore di scala così come la dimensione
* [70534c0](https://github.com/mate-desktop/caja/commit/70534c0) file: supportato HiDpi per le immagini delle miniature
* [2e0c51f](https://github.com/mate-desktop/caja/commit/2e0c51f) properties-window: supportato HiDpi per l'icona della finestra delle proprietà
* [4bf67ac](https://github.com/mate-desktop/caja/commit/4bf67ac) Supportate le icone HiDpi
* [35c4dc6](https://github.com/mate-desktop/caja/commit/35c4dc6) canvas-container: ascoltato il fattore di scala per invalidare le icone
* [52d44de](https://github.com/mate-desktop/caja/commit/52d44de) canvas-item: utilizzato gtk_render_icon_surface per la superficie Drag-n-Drop
* [7f22b30](https://github.com/mate-desktop/caja/commit/7f22b30) modificato il codice di errore: fatto terminare lo statement con un punto e virgola
* [6082649](https://github.com/mate-desktop/caja/commit/6082649) rimossi i warning in esecuzione nell'utilizzo di caja_clipboard_set_up_editable
* [d885694](https://github.com/mate-desktop/caja/commit/d885694) si possono selezionare tutte le parole chiave di ricerca con Ctrl+a.
* [fcbee7f](https://github.com/mate-desktop/caja/commit/fcbee7f) aggiunto caja.pot per auto-aggiornare le traduzioni
* [33dc065](https://github.com/mate-desktop/caja/commit/33dc065) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [dabd62d](https://github.com/mate-desktop/caja/commit/dabd62d) corretto il rendering degli sfondi e del contenuto della finestra di dialogo dei simboli

### caja-dropbox
* [5fdcb17](https://github.com/mate-desktop/caja-dropbox/commit/5fdcb17) Utilizzato CAJA_EXTENSION_DIR_SYS per salvare e mostrare la directory di sistema di caja extensions
* [fdc25dc](https://github.com/mate-desktop/caja-dropbox/commit/fdc25dc) mostrato il percorso completo di caja-extension-dir
* [6d281bc](https://github.com/mate-desktop/caja-dropbox/commit/6d281bc) corretto distcheck su caja_extension_dir
* [dd70319](https://github.com/mate-desktop/caja-dropbox/commit/dd70319) Abilitato Travis Cl per tutti i rami
* [60bbb51](https://github.com/mate-desktop/caja-dropbox/commit/60bbb51) Inizializzato il supporto a Travis Cl
* [05e1e93](https://github.com/mate-desktop/caja-dropbox/commit/05e1e93) Corretto un fallimento di distcheck
* [285937d](https://github.com/mate-desktop/caja-dropbox/commit/285937d) utilizzato solo Python 3 durante la compilazione per completare la migrazione
* [3d48c5e](https://github.com/mate-desktop/caja-dropbox/commit/3d48c5e) migrazione da python2 a python3 di rst2man.py
* [4eab52b](https://github.com/mate-desktop/caja-dropbox/commit/4eab52b) rimossi più modificatori -u per dropbox-cli
* [cd91ced](https://github.com/mate-desktop/caja-dropbox/commit/cd91ced) Aggiornamento di Python 3 per dropbox-cli
* [f3fe4a4](https://github.com/mate-desktop/caja-dropbox/commit/f3fe4a4) Aggiunte la voce Keywords al file desktop
* [7ab9374](https://github.com/mate-desktop/caja-dropbox/commit/7ab9374) Utilizzata la macro cross-compilation-safe di pkg-config
* [c85aaec](https://github.com/mate-desktop/caja-dropbox/commit/c85aaec) Rimosse le chiamate deprecate all'API glib2.0
* [167bfab](https://github.com/mate-desktop/caja-dropbox/commit/167bfab) Utilizzati i binding GIR invece di pygtk
* [55e4f9b](https://github.com/mate-desktop/caja-dropbox/commit/55e4f9b) corretto UnicodeWarning quando il comando exclude è utilizzato con argomenti non-latin
* [343a3fb](https://github.com/mate-desktop/caja-dropbox/commit/343a3fb) Aggiornamento per le icone ridisegnate
* [1eb18c6](https://github.com/mate-desktop/caja-dropbox/commit/1eb18c6) piccole correzioni a caja-dropbox.in
* [527b9cc](https://github.com/mate-desktop/caja-dropbox/commit/527b9cc) Aggiunto un nuovo comando "dropbox update"
* [4cb4209](https://github.com/mate-desktop/caja-dropbox/commit/4cb4209) Scollegati i file che saranno sostituiti dallo spacchettamento
* [192451f](https://github.com/mate-desktop/caja-dropbox/commit/192451f) Verificato che dropbox viene eseguito dopo averlo scaricato
* [3d511a6](https://github.com/mate-desktop/caja-dropbox/commit/3d511a6) Utilizzato python-gpg invece di python-gpgme
* [68dd75a](https://github.com/mate-desktop/caja-dropbox/commit/68dd75a) Caricare esplicitamente utilizzando python2
* [a7da6a7](https://github.com/mate-desktop/caja-dropbox/commit/a7da6a7) Fare riferimento a .dropbox.dist in un solo posto
* [a939670](https://github.com/mate-desktop/caja-dropbox/commit/a939670) corretto 'exclude command raise UnicodeDecodeError'
* [5543711](https://github.com/mate-desktop/caja-dropbox/commit/5543711)  Evitato di leggere o scrivere indirizzi di memoria non validi
* [991a851](https://github.com/mate-desktop/caja-dropbox/commit/991a851) Mostrato l'url di collegamento sullo status
* [d3261c1](https://github.com/mate-desktop/caja-dropbox/commit/d3261c1) Aggiornato dropbox.py con le funzionalità shmodel, proxy e throttle.
* [a2ccaaf](https://github.com/mate-desktop/caja-dropbox/commit/a2ccaaf) aggiornato l'anno del Copyright
* [394578f](https://github.com/mate-desktop/caja-dropbox/commit/394578f) versione pre-aggiornamento

### caja-extensions
* [2e1a77b](https://github.com/mate-desktop/caja-extensions/commit/2e1a77b) Abilitato Travis Cl per tutti i rami
* [dde037d](https://github.com/mate-desktop/caja-extensions/commit/dde037d) Inizializzato il supporto a Travis Cl
* [512e1c8](https://github.com/mate-desktop/caja-extensions/commit/512e1c8) richiesto caja >= 1.21.3
* [22cb044](https://github.com/mate-desktop/caja-extensions/commit/22cb044) configure: corretti alcuni errori di battitura
* [e04adb3](https://github.com/mate-desktop/caja-extensions/commit/e04adb3) disabilitati i warning di deprecazione per distcheck
* [dd67d69](https://github.com/mate-desktop/caja-extensions/commit/dd67d69) Reso caja-open-terminal configurabile (Dipende da caja GitHub PR caja#1050)
* [3fecb36](https://github.com/mate-desktop/caja-extensions/commit/3fecb36) NEWS: utilizzata la versione di sviluppo
* [4b1141f](https://github.com/mate-desktop/caja-extensions/commit/4b1141f) versione pre-aggiornamento
* [27d49a6](https://github.com/mate-desktop/caja-extensions/commit/27d49a6) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [84e7fac](https://github.com/mate-desktop/caja-extensions/commit/84e7fac) aggiunto il supporto a travis-Cl
* [4f06445](https://github.com/mate-desktop/caja-extensions/commit/4f06445) disabilitati i warning di deprecazione per distcheck
* [d3b8be7](https://github.com/mate-desktop/caja-extensions/commit/d3b8be7) sincronizzazione con transifex
* [7db6ed1](https://github.com/mate-desktop/caja-extensions/commit/7db6ed1) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### engrampa
* [8e1c290](https://github.com/mate-desktop/engrampa/commit/8e1c290) fr-process: corretto un memory leak
* [84db3ea](https://github.com/mate-desktop/engrampa/commit/84db3ea) aggiunto il supporto a Travis-Cl
* [29b4e67](https://github.com/mate-desktop/engrampa/commit/29b4e67) Tx: sincronizzazione con le traduzioni fisse da transifex
* [e61212f](https://github.com/mate-desktop/engrampa/commit/e61212f) rar/unrar: Correzione: disabilitando "sovrascrivere i file esistenti" deve funzionare
* [b683362](https://github.com/mate-desktop/engrampa/commit/b683362) spostato appdata nella cartella metainfo
* [dc0f490](https://github.com/mate-desktop/engrampa/commit/dc0f490) disabilitati i warning di deprecazione per distcheck
* [95541ae](https://github.com/mate-desktop/engrampa/commit/95541ae) utilizzate funzioni make per HELP_LINGUAS
* [cd7f17a](https://github.com/mate-desktop/engrampa/commit/cd7f17a) Sostituito - Dokumentationteam
* [dd11160](https://github.com/mate-desktop/engrampa/commit/dd11160) Sostituito Dokumentationsprojekt con Documentation Project
* [9b4ba7a](https://github.com/mate-desktop/engrampa/commit/9b4ba7a) Manual: Aggiornate le descrizioni del formato dei file utilizzando shared-mime-info
* [2c9e615](https://github.com/mate-desktop/engrampa/commit/2c9e615) Corretto l'URL di ulinks per farlo puntare a mate-user-guide
* [2c60ca9](https://github.com/mate-desktop/engrampa/commit/2c60ca9) sistemi UNIX e Linux -> Linux e sistemi UNIX-like
* [2804b35](https://github.com/mate-desktop/engrampa/commit/2804b35) aggiornato engrampa.pot
* [fa7097c](https://github.com/mate-desktop/engrampa/commit/fa7097c) fr-window: corretto un errore di battitura
* [247093f](https://github.com/mate-desktop/engrampa/commit/247093f) sincronizzazione con transifex
* [1e1a94a](https://github.com/mate-desktop/engrampa/commit/1e1a94a) aggiornato engrampa.pot
* [6f824fe](https://github.com/mate-desktop/engrampa/commit/6f824fe) Aggiunto il supporto per .a (Ar)
* [3ee4f6c](https://github.com/mate-desktop/engrampa/commit/3ee4f6c) corretto il crash in uscita dopo aver utilizzato la finestra di dialogo Apri con
* [08a8eac](https://github.com/mate-desktop/engrampa/commit/08a8eac) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [c55754a](https://github.com/mate-desktop/engrampa/commit/c55754a) fr-process: corretto un memory leak
* [bbca40d](https://github.com/mate-desktop/engrampa/commit/bbca40d) Help: corretta la versione a 1.22 e aggiornato il file pot
* [d62cff0](https://github.com/mate-desktop/engrampa/commit/d62cff0) help: aggiornato il copyright
* [4e0a8da](https://github.com/mate-desktop/engrampa/commit/4e0a8da) Aggiornato il manuale a docbook 5.0
* [db21779](https://github.com/mate-desktop/engrampa/commit/db21779) Evitato l'array index out of bounds nell'analisi di dpkg-deb --info
* [333a9e9](https://github.com/mate-desktop/engrampa/commit/333a9e9) warning: Utilizzare la memoria dopo che è stata liberata
* [c9eb7cb](https://github.com/mate-desktop/engrampa/commit/c9eb7cb) Leggere authors (aggiornato) da engrampa.about gresource
* [5ceee4c](https://github.com/mate-desktop/engrampa/commit/5ceee4c) Abilitato Travis Cl
* [b0a7135](https://github.com/mate-desktop/engrampa/commit/b0a7135) eggsmclient: Evitata la deprecata 'g_type_class_add_private'
* [e929b84](https://github.com/mate-desktop/engrampa/commit/e929b84) aggiornato l'anno di copyright a 2019
* [647645d](https://github.com/mate-desktop/engrampa/commit/647645d) rar/unrar: Correzione: "sovrascrivere i file esistenti" disabilitato deve funzionare
* [9771782](https://github.com/mate-desktop/engrampa/commit/9771782) #225 corretto un errore di battitura
* [d5ef415](https://github.com/mate-desktop/engrampa/commit/d5ef415) corretto fr-command-cfile.c: fr_process_set_working_dir
* [0577456](https://github.com/mate-desktop/engrampa/commit/0577456) fr-command-cfile.c: corretta l'indentazione
* [afb8ebd](https://github.com/mate-desktop/engrampa/commit/afb8ebd) Aggiunto il test di integrità per brotli
* [ab9e18f](https://github.com/mate-desktop/engrampa/commit/ab9e18f) Aggiunto il test di integrità per i compressori cfile: gzip, bzip2, etc. Ma poiché molti di loro mostrano il messaggio con lo stato del file sullo STDERR anziché sullo STDOUT dovremmo mostrarli entrambi nella finestra .risultato del Test 
* [a699fa2](https://github.com/mate-desktop/engrampa/commit/a699fa2) spostato appdata nella cartella metainfo
* [3b4ae2f](https://github.com/mate-desktop/engrampa/commit/3b4ae2f) fr-window: mostrare il pulsante di pausa solo se la finestra di dialogo è in funzione
* [11bbca8](https://github.com/mate-desktop/engrampa/commit/11bbca8) disabilitati i warning di deprecazione per distcheck
* [3037620](https://github.com/mate-desktop/engrampa/commit/3037620) fr-window: evitata 'gtk_dialog_add_button' con gli identificativi stock
* [57b6906](https://github.com/mate-desktop/engrampa/commit/57b6906) fr-window: nascondere la barra di avanzamento quando il processo è in pausa
* [10fd1e2](https://github.com/mate-desktop/engrampa/commit/10fd1e2) fr-window: modificare l'etichetta informativa se il processo è messo in pausa o riattivato
* [d5560ec](https://github.com/mate-desktop/engrampa/commit/d5560ec) fr-window: piccoli miglioramenti nell'aspetto del pulsante pausa/riprendi
* [5eea3e1](https://github.com/mate-desktop/engrampa/commit/5eea3e1) Aggiunte le funzioni pausa e riprendi
* [b1d6ced](https://github.com/mate-desktop/engrampa/commit/b1d6ced) Corretta l'implementazione e l'utilizzo del nome di pacchetto alternativo  lookup
* [fa96f93](https://github.com/mate-desktop/engrampa/commit/fa96f93) Aggiunto il supporto per gli archivi tar compressi brotli (*.tar.br)
* [f06c216](https://github.com/mate-desktop/engrampa/commit/f06c216) Aggiunto il supporto per brotli
* [8ef808e](https://github.com/mate-desktop/engrampa/commit/8ef808e) utilizzate funzioni make per HELP_LINGUAS
* [ad74b5d](https://github.com/mate-desktop/engrampa/commit/ad74b5d) Sostituito -Dokumentationteam
* [d7d22b4](https://github.com/mate-desktop/engrampa/commit/d7d22b4) Sostituito Dokumentationsprojekt con Documentation Project
* [6c451b3](https://github.com/mate-desktop/engrampa/commit/6c451b3) Manual: Aggiornate le descrizioni del formato dei file utilizzando shared-mime-info
* [3b890f9](https://github.com/mate-desktop/engrampa/commit/3b890f9) sistemi UNIX e Linux -> Linux e sistemi UNIX-like
* [0c6a7a0](https://github.com/mate-desktop/engrampa/commit/0c6a7a0) aggiornato engrampa.pot
* [fc73b13](https://github.com/mate-desktop/engrampa/commit/fc73b13) fr-window: corretto un errore di battitura
* [c587ae1](https://github.com/mate-desktop/engrampa/commit/c587ae1) Aggiunta la capacità di supportare 'unar' sugli archivi .zip
* [10e665f](https://github.com/mate-desktop/engrampa/commit/10e665f) Aggiunto il supporto per i formati OpenDocument
* [7c0038a](https://github.com/mate-desktop/engrampa/commit/7c0038a) UI: sulla finestra di dialogo proprietà, dare il focus predefinito al pulsante Chiudi invece di quello Aiuto
* [7b1a66c](https://github.com/mate-desktop/engrampa/commit/7b1a66c) sincronizzazione con transifex
* [c96c85f](https://github.com/mate-desktop/engrampa/commit/c96c85f) versione pre-aggiornamento
* [499e600](https://github.com/mate-desktop/engrampa/commit/499e600) Aggiunto il supporto per .a (Ar)
* [ef714ac](https://github.com/mate-desktop/engrampa/commit/ef714ac) fr-window: Sostituite le funzioni deprecate gtk_menu_popup
* [a03aa8c](https://github.com/mate-desktop/engrampa/commit/a03aa8c) corretto il crash in uscita dopo aver utilizzato la finestra di dialogo Apri con
* [6d56e36](https://github.com/mate-desktop/engrampa/commit/6d56e36) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [2e9c1a1](https://github.com/mate-desktop/engrampa/commit/2e9c1a1) evitata la deprecata GtkStock

### eom
* [905f8b7](https://github.com/mate-desktop/eom/commit/905f8b7) Help: corretta la versione a 1.22 e aggiornato il file pot
* [bc141be](https://github.com/mate-desktop/eom/commit/bc141be) help: aggiornato il copyright
* [bbcca8d](https://github.com/mate-desktop/eom/commit/bbcca8d) Aggiornato il manuale a docbook 5.0
* [9f631a7](https://github.com/mate-desktop/eom/commit/9f631a7) Utilizzato un setup di pagina persistente
* [68ac123](https://github.com/mate-desktop/eom/commit/68ac123) Aggiunto lo script update-authors.pl che aiuta ad aggiornare eom.about
* [eed5511](https://github.com/mate-desktop/eom/commit/eed5511) Leggere authors (aggiornato) e documenters (aggiornato) da eom.about gresource
* [17ca341](https://github.com/mate-desktop/eom/commit/17ca341) Abilitato Travis Cl per tutti i rami
* [2c34542](https://github.com/mate-desktop/eom/commit/2c34542) Inizializzato il supporto a Travis Cl
* [119fd7e](https://github.com/mate-desktop/eom/commit/119fd7e) Assicurata la corretta traduzione del titolo della finestra di dialogo informazioni
* [941b0ec](https://github.com/mate-desktop/eom/commit/941b0ec) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [9cf9e2e](https://github.com/mate-desktop/eom/commit/9cf9e2e) Help - corrette le etichette gui
* [bd1f72d](https://github.com/mate-desktop/eom/commit/bd1f72d) disabilitati i warning di deprecazione per distcheck
* [e3a9345](https://github.com/mate-desktop/eom/commit/e3a9345) Aggiornato il file XML appdata
* [5e245f8](https://github.com/mate-desktop/eom/commit/5e245f8) utilizzate funzioni make per HELP_LINGUAS
* [0b573f4](https://github.com/mate-desktop/eom/commit/0b573f4) Corretto l'url di ulink per farlo puntare a mate-user-guide
* [8eca711](https://github.com/mate-desktop/eom/commit/8eca711) Aggiornato lo screenshot in Catalano
* [7af7c3b](https://github.com/mate-desktop/eom/commit/7af7c3b) corretti errori di ortografia e grammatica
* [1e17920](https://github.com/mate-desktop/eom/commit/1e17920) Aggiornato eom_start_window.png
* [e148897](https://github.com/mate-desktop/eom/commit/e148897) Ridotto il numero di chiamate a g_file_query_info durante l'apertura
* [e3cb374](https://github.com/mate-desktop/eom/commit/e3cb374) EomImage: Rimosso un costruttore inutilizzato
* [f4d798a](https://github.com/mate-desktop/eom/commit/f4d798a) corretto un memory leak
* [c98f5cc](https://github.com/mate-desktop/eom/commit/c98f5cc) docs: rimosso il riferimento a eom-dialog.xml per correggere distcheck
* [f4818d9](https://github.com/mate-desktop/eom/commit/f4818d9) sincronizzazione con transifex
* [18a612e](https://github.com/mate-desktop/eom/commit/18a612e) EomMetadataSidebar: Fatto in modo che la include guard dell'header file funzioni
* [b21b983](https://github.com/mate-desktop/eom/commit/b21b983) EomWindow: invertite le scorciatoie da tastiera per la barra laterale e la galleria
* [d066bae](https://github.com/mate-desktop/eom/commit/d066bae) ritoccata la ui della barra laterale
* [4185e8c](https://github.com/mate-desktop/eom/commit/4185e8c) EomPropertiesDialog: Utilizzato standard::display-name quando si mostra il genitore
* [0e708c5](https://github.com/mate-desktop/eom/commit/0e708c5) EomMetadataSidebar: Utilizzato standard::display-name quando si mostra il genitore
* [ab96aad](https://github.com/mate-desktop/eom/commit/ab96aad) Corretto il calcolo delle dipendenze di GResorce per le build fuori-albero
* [adfe0c7](https://github.com/mate-desktop/eom/commit/adfe0c7) Fatto in modo che la dipendenza libpeas-gtk non sia de-ottimizzata
* [c2fc002](https://github.com/mate-desktop/eom/commit/c2fc002) Rimossa l'helper class EomDialog
* [4b4a611](https://github.com/mate-desktop/eom/commit/4b4a611) EomPreferencesDialog: Convertito al template GtkBuilder
* [b18e263](https://github.com/mate-desktop/eom/commit/b18e263) EomThumbnail: Caricata la cornice delle miniature da un GResource
* [b1fb22d](https://github.com/mate-desktop/eom/commit/b1fb22d) Caricata EomMultipleSaveAsDialog da GResource
* [b5172a3](https://github.com/mate-desktop/eom/commit/b5172a3) eom-window: corretto l'utilizzo di GtkStock deprecato
* [22f5b20](https://github.com/mate-desktop/eom/commit/22f5b20) corretta la compilazione senza il supporto a XMP
* [70fd470](https://github.com/mate-desktop/eom/commit/70fd470) Caricata eom-image-properties-dialog.ui con una gresource
* [8734d0e](https://github.com/mate-desktop/eom/commit/8734d0e) properties-dialog: portato a gtk_show_uri_on_window
* [068315f](https://github.com/mate-desktop/eom/commit/068315f) EomPropertiesDialog: Convertito al template GtkBuilder
* [734ad19](https://github.com/mate-desktop/eom/commit/734ad19) EomPropertiesDialog: Rimossi i membri privati inutilizzati
* [e306d7a](https://github.com/mate-desktop/eom/commit/e306d7a) corretta la sidebar dei metadati con libexif disattivato
* [fd322e8](https://github.com/mate-desktop/eom/commit/fd322e8) Corretta la creazione dei docs dell'API senza libexif
* [c828347](https://github.com/mate-desktop/eom/commit/c828347) EomMetadataSidebar: Corretta la compilazione --without-libexif
* [f517d6d](https://github.com/mate-desktop/eom/commit/f517d6d) EomMetadataSidebar: Cancellata l'etichetta della cartella se non è impostata alcuna immagine
* [6aac9e3](https://github.com/mate-desktop/eom/commit/6aac9e3) EomSidebar: Incrementato il margine ai lati della barra laterale
* [6319bb3](https://github.com/mate-desktop/eom/commit/6319bb3) EomSidebar: Centrato e riformattato il selettore della pagina
* [ece3c97](https://github.com/mate-desktop/eom/commit/ece3c97) EomMetadataSidebar: corrette le stringhe che sprecavano memoria
* [a29a5d1](https://github.com/mate-desktop/eom/commit/a29a5d1) metadata-sidebar: aggiunto nuovamente il pulsante dettagli
* [6b0c2ae](https://github.com/mate-desktop/eom/commit/6b0c2ae) EomMetadataSidebar: Tentato di semplificare e migliorare l'aspetto della barra laterale
* [3d80a86](https://github.com/mate-desktop/eom/commit/3d80a86) GResource: liberare il css_file
* [6d164b4](https://github.com/mate-desktop/eom/commit/6d164b4) Migrazione di GResorce iniziale
* [e12f285](https://github.com/mate-desktop/eom/commit/e12f285) EomExifUtil: corretta la compilazione con il nuovo GCC
* [1e96c9d](https://github.com/mate-desktop/eom/commit/1e96c9d) EomExifUtil: Consentita la formattazione libera delle stringhe della data
* [9b4890e](https://github.com/mate-desktop/eom/commit/9b4890e) EomMetadataDetails: Migliorato il supporto alle coordinate GPS frazionarie
* [f965eb2](https://github.com/mate-desktop/eom/commit/f965eb2) EomPropertiesDialog: Separati i widget Exif/XMP-specifici da quelli generici
* [4e20a6d](https://github.com/mate-desktop/eom/commit/4e20a6d) EomMetadataDetails: non installare il file header
* [49c5c97](https://github.com/mate-desktop/eom/commit/49c5c97) EomExifDetails: Rinominato a EomMetadataDetails
* [9593351](https://github.com/mate-desktop/eom/commit/9593351) Eliminato eom_close_confirmation_dialog_set_sensitive
* [704107b](https://github.com/mate-desktop/eom/commit/704107b) scroll-view: Rimossa una chiamata a gdk_window_process_updates
* [416dc9b](https://github.com/mate-desktop/eom/commit/416dc9b) util: Portato a gtk_show_uri_on_window
* [4115f76](https://github.com/mate-desktop/eom/commit/4115f76) EomImage: Assicurare che sia emesso size-prepared dopo aver applicato l'orientamento
* [c3d8c61](https://github.com/mate-desktop/eom/commit/c3d8c61) EomImage: corretta la troppo anticipata emissione di size-prepared
* [5f6f184](https://github.com/mate-desktop/eom/commit/5f6f184) EomImage: Lieve ottimizzazione della struttura dati privata
* [a95925a](https://github.com/mate-desktop/eom/commit/a95925a) eliminato il file gtkrc dimenticato
* [1f2aba7](https://github.com/mate-desktop/eom/commit/1f2aba7) css: eliminato il linguaggio css vecchio ed obsoleto
* [447f5fe](https://github.com/mate-desktop/eom/commit/447f5fe) EomWindow: silenziato un warning introspettivo
* [94f7f44](https://github.com/mate-desktop/eom/commit/94f7f44) Convertito a G_DEFINE_TYPE_WITH_PRIVATE parte 3
* [fb7c539](https://github.com/mate-desktop/eom/commit/fb7c539)  Convertito a G_DEFINE_TYPE_WITH_PRIVATE parte 2
* [5a5612a](https://github.com/mate-desktop/eom/commit/5a5612a) Convertito a G_DEFINE_TYPE_WITH_PRIVATE parte 1
* [a3c97eb](https://github.com/mate-desktop/eom/commit/a3c97eb) EomApplication: Resi molti membri privati
* [bb3b0c0](https://github.com/mate-desktop/eom/commit/bb3b0c0) Aggiunto un nuovo plugin hook per i plugin specifici per l'applicazione
* [57506ff](https://github.com/mate-desktop/eom/commit/57506ff) Reso EomWindow un GtkApplicationWindow
* [5c58837](https://github.com/mate-desktop/eom/commit/5c58837) sidebar: Mostrata la directory completa sul tooltip del pulsante
* [b504d5a](https://github.com/mate-desktop/eom/commit/b504d5a) properties-dialog: Mostrata la directory completa sul tooltip del pulsante
* [a5ba9a2](https://github.com/mate-desktop/eom/commit/a5ba9a2) Creato un pulsante con l'etichetta-URI nella finestra di dialogo delle proprietà che mostri la cartella
* [14a755c](https://github.com/mate-desktop/eom/commit/14a755c) exif-details: resa selezionabile la colonna dei valori
* [b3f9b82](https://github.com/mate-desktop/eom/commit/b3f9b82) EomExifDetails: Presa in considerazione l'IFD di Exif nella creazione delle chiavi hash
* [a3a89e0](https://github.com/mate-desktop/eom/commit/a3a89e0) Spostati i tag Exif di GPS nella loro sottocategoria
* [fe21ccd](https://github.com/mate-desktop/eom/commit/fe21ccd) Riformattati i tag Exif per la posizione GPS per essere più comprensibili
* [32f2e6f](https://github.com/mate-desktop/eom/commit/32f2e6f) Fatto in modo che i tag Exif di GPS siano nominati e ordinati in modo corretto
* [017f7e5](https://github.com/mate-desktop/eom/commit/017f7e5) Uso della caratteristica "orientazione" di GdkPixbuf come fallback per l'auto-rotazione
* [7eec54c](https://github.com/mate-desktop/eom/commit/7eec54c) EomScrollView: Implementato un semplice filtraggio a due-passaggi
* [7f38bf6](https://github.com/mate-desktop/eom/commit/7f38bf6) EomScrollView: Utilizzato un migliore filtro downscaling
* [f607cda](https://github.com/mate-desktop/eom/commit/f607cda) Rimossa la non necessaria finalize() da EomListStore
* [9b79e09](https://github.com/mate-desktop/eom/commit/9b79e09) Aggiornati i plugin per utilizzare l'interfaccia EomWindowActivatable
* [026b114](https://github.com/mate-desktop/eom/commit/026b114) Aggiunta la nostra interfaccia attivabile ad EomWindow
* [17e6cdb](https://github.com/mate-desktop/eom/commit/17e6cdb) Sostituita gdk_spawn_command_line_on_screen()
* [7dbd1b8](https://github.com/mate-desktop/eom/commit/7dbd1b8) sidebar: sostituita la deprecata gtk_misc_set_alignment
* [15a0431](https://github.com/mate-desktop/eom/commit/15a0431) POTFILES.in: aggiunto  'src/eom-metadata-sidebar.c'
* [78f41c1](https://github.com/mate-desktop/eom/commit/78f41c1) EomWindow: Semplificato il titolo della barra laterale dei metadati
* [362b507](https://github.com/mate-desktop/eom/commit/362b507) EomSidebar: Impostata la proprietà dell'orientamento mediante g_object_new
* [32675ab](https://github.com/mate-desktop/eom/commit/32675ab) Sostituiti gli utilizzi rimanenti delle proprietà margin-left e margin-right
* [e6cda96](https://github.com/mate-desktop/eom/commit/e6cda96) EomMetadataSidebar: Consentito ai filename di essere racchiusi nei confini di un char
* [bcc8082](https://github.com/mate-desktop/eom/commit/bcc8082) sidebar: corretta una deprecazione
* [a46238b](https://github.com/mate-desktop/eom/commit/a46238b) EomMetadataSidebar: corretto un warning di deprecazione con le nuove GTK+
* [d7910a6](https://github.com/mate-desktop/eom/commit/d7910a6) MetadataSidebar: aggiunto un tooltip al pulsante della cartella
* [de32a70](https://github.com/mate-desktop/eom/commit/de32a70) MetadataSidebar: Cambiato il layout dei valori dei dati
* [ad13501](https://github.com/mate-desktop/eom/commit/ad13501) Resi selezionabili i valori in MetadataSidebar
* [d328203](https://github.com/mate-desktop/eom/commit/d328203) corretta la compilazione quando non si compila con libexif e/o exempi
* [09fea91](https://github.com/mate-desktop/eom/commit/09fea91) Non fare il force-enable della barra laterale all'apertura una volta che si è aggiunta una pagina
* [b1c0911](https://github.com/mate-desktop/eom/commit/b1c0911) Resi i riepiloghi Exif/XMP disponibili come barra laterale
* [28fbd14](https://github.com/mate-desktop/eom/commit/28fbd14) Eliminato il non più necessario TotemScreenSaver
* [4817ee9](https://github.com/mate-desktop/eom/commit/4817ee9) Utilizzato GtkApplication per inibire lo screensaver durante le presentazioni
* [9e687fa](https://github.com/mate-desktop/eom/commit/9e687fa) Ci si è assicurati che la sensibilità delle azioni UI sia impostata almeno una volta
* [bc859fd](https://github.com/mate-desktop/eom/commit/bc859fd) Rimosso il file di descrizione del servizio DBus avanzato
* [59ea038](https://github.com/mate-desktop/eom/commit/59ea038) Rimosso la spuria g_object_unref
* [0c78063](https://github.com/mate-desktop/eom/commit/0c78063) reload: ci siamo assicurati che gli aggiornamenti in sospeso ai componenti UI siano completi
* [20d704b](https://github.com/mate-desktop/eom/commit/20d704b) Portato EomApplication a GtkApplication
* [63a6313](https://github.com/mate-desktop/eom/commit/63a6313) Resa la visualizzata EomImage una proprietà di EomScrollView
* [cfc83b4](https://github.com/mate-desktop/eom/commit/cfc83b4) EomPropertiesDialog: Fatto in modo che la visualizzazione dei dettagli si espanda verticalmente
* [ed3ef44](https://github.com/mate-desktop/eom/commit/ed3ef44) Consentite più azioni Drag and Drop quando eom è l'origine del trascinamento
* [fb4446d](https://github.com/mate-desktop/eom/commit/fb4446d) Utilizzata la nuova API DBus per mostrare l'immagine corrente nel file browser
* [07de875](https://github.com/mate-desktop/eom/commit/07de875) Aggiunto un comando "Apri la cartella contenitore"
* [9815134](https://github.com/mate-desktop/eom/commit/9815134) sincronizzazione con transifex
* [e7df737](https://github.com/mate-desktop/eom/commit/e7df737) versione pre-aggiornamento
* [0e624a5](https://github.com/mate-desktop/eom/commit/0e624a5) toolbar: Aggiunto il menù popup mancante per lanciare l'editor della barra degli strumenti
* [f3bc78d](https://github.com/mate-desktop/eom/commit/f3bc78d) sidebar: sostituita la deprecata gtk_menu_popup
* [620071b](https://github.com/mate-desktop/eom/commit/620071b) editable-toolbar: sostituita la deprecata gtk_menu_popup
* [50d0a50](https://github.com/mate-desktop/eom/commit/50d0a50) editable-toolbar:  sostituita la deprecata gtk_drag_begin
* [530d7cb](https://github.com/mate-desktop/eom/commit/530d7cb) svg: Corrette le coordinate di offset quando si trasformano le immagini SVG sui display HiDPI
* [5da033e](https://github.com/mate-desktop/eom/commit/5da033e) richiesto libpeas 1.8.0
* [c94e091](https://github.com/mate-desktop/eom/commit/c94e091) plugins: Utilizzato Python 3.x per i plugin Python
* [a206e04](https://github.com/mate-desktop/eom/commit/a206e04) sostituita la deprecata gdk_flush
* [03783b9](https://github.com/mate-desktop/eom/commit/03783b9) corretti alcuni warning -Wincompatible-pointer-types
* [51fc70f](https://github.com/mate-desktop/eom/commit/51fc70f) Immagini HiDPI scalate correttamente
* [30940c7](https://github.com/mate-desktop/eom/commit/30940c7) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [29a62cd](https://github.com/mate-desktop/eom/commit/29a62cd) eom-window.c: evitata la deprecata GtkButton:use-stock
* [98d6a43](https://github.com/mate-desktop/eom/commit/98d6a43) evitata la deprecata GtkStock
* [96b1b4d](https://github.com/mate-desktop/eom/commit/96b1b4d) Utilizzato un setup di pagina persistente
* [db25ddd](https://github.com/mate-desktop/eom/commit/db25ddd) aggiunto il supporto a Travis-Cl
* [eba5461](https://github.com/mate-desktop/eom/commit/eba5461) Help - corrette le etichette gui
* [540e33f](https://github.com/mate-desktop/eom/commit/540e33f) Aggirnato il file XML appdata
* [cfdbd1f](https://github.com/mate-desktop/eom/commit/cfdbd1f) disabilitati i warning di deprecazione per distcheck
* [98a063e](https://github.com/mate-desktop/eom/commit/98a063e) Ridotto il numero di chiamate a g_file_query_info durante l'apertura
* [0d1a90a](https://github.com/mate-desktop/eom/commit/0d1a90a) EomImage: Rimosso un costruttore inutilizzato
* [49a85ee](https://github.com/mate-desktop/eom/commit/49a85ee) utilizzate funzioni make per HELP_LINGUAS
* [d434d35](https://github.com/mate-desktop/eom/commit/d434d35) Corretto l'url di ulink per farlo puntare a mate-user-guide
* [9b628a8](https://github.com/mate-desktop/eom/commit/9b628a8) corretti errori di ortografia e grammatica
* [9b033ce](https://github.com/mate-desktop/eom/commit/9b033ce) Aggiornato eom_start_window.png
* [5376650](https://github.com/mate-desktop/eom/commit/5376650) corretto un memory leak
* [dba717d](https://github.com/mate-desktop/eom/commit/dba717d) exif-details: resa selezionabile la colonna dei valori
* [667f5b2](https://github.com/mate-desktop/eom/commit/667f5b2) EomExifDetails: Presa in considerazione l'IFD di Exif nella creazione delle chiavi hash
* [0c6a01d](https://github.com/mate-desktop/eom/commit/0c6a01d) Spostati i tag Exif di GPS nella loro sottocategoria
* [87d59bd](https://github.com/mate-desktop/eom/commit/87d59bd) Riformattati i tag Exif per la posizione GPS per essere più comprensibili
* [af9cd83](https://github.com/mate-desktop/eom/commit/af9cd83) Fatto in modo che i tag Exif di GPS siano nominati e ordinati in modo corretto
* [7e9dc52](https://github.com/mate-desktop/eom/commit/7e9dc52) EomPropertiesDialog: Fatto in modo che la visualizzazione dei dettagli si espanda verticalmente
* [bbf490b](https://github.com/mate-desktop/eom/commit/bbf490b) EomScrollView: Utilizzato un migliore filtro downscaling
* [433c776](https://github.com/mate-desktop/eom/commit/433c776) reload: ci siamo assicurati che gli aggiornamenti in sospeso ai componenti UI siano completi
* [16f5b2c](https://github.com/mate-desktop/eom/commit/16f5b2c) corretti alcuni warning -Wincompatible-pointer-types
* [1523539](https://github.com/mate-desktop/eom/commit/1523539) sincronizzazione con transifex
* [2f04a37](https://github.com/mate-desktop/eom/commit/2f04a37) svg: Corrette le coordinate di offset quando si trasformano le immagini SVG sui display HiDPI
* [bca6a64](https://github.com/mate-desktop/eom/commit/bca6a64) Immagini HiDPI scalate correttamente
* [ae3e2a4](https://github.com/mate-desktop/eom/commit/ae3e2a4) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### libmatekbd
* [7e730f0](https://github.com/mate-desktop/libmatekbd/commit/7e730f0) Abilitato Travis Cl per tutti i rami
* [e6e0234](https://github.com/mate-desktop/libmatekbd/commit/e6e0234) Inizializzato il supporto a Travis Cl
* [dc04e96](https://github.com/mate-desktop/libmatekbd/commit/dc04e96) rinominata g_strv_equal in matekbd_strv_equal
* [c3a62d4](https://github.com/mate-desktop/libmatekbd/commit/c3a62d4) sincronizzazione con transifex
* [b11e6ca](https://github.com/mate-desktop/libmatekbd/commit/b11e6ca) versione pre-aggiornamento
* [a95a4f4](https://github.com/mate-desktop/libmatekbd/commit/a95a4f4) corretto lo scaling sui display HiDPI
* [81034cf](https://github.com/mate-desktop/libmatekbd/commit/81034cf) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [05c064e](https://github.com/mate-desktop/libmatekbd/commit/05c064e) utilizzata la risoluzione dello schermo di gdk per il font nell'icona del keyboard status notification, per essere scalata correttamente sui display HiDPI.
* [3fa26b6](https://github.com/mate-desktop/libmatekbd/commit/3fa26b6) aggiunto il supporto a Travis-Cl
* [c36d3ec](https://github.com/mate-desktop/libmatekbd/commit/c36d3ec) sincronizzazione con transifex
* [8740018](https://github.com/mate-desktop/libmatekbd/commit/8740018) corretti i file po
* [e6cd5be](https://github.com/mate-desktop/libmatekbd/commit/e6cd5be) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [90dba6e](https://github.com/mate-desktop/libmatekbd/commit/90dba6e) utilizzata la risoluzione dello schermo di gdk per il font nell'icona del keyboard status notification, per essere scalata correttamente sui display HiDPI.

### libmatemixer
* [4d4520c](https://github.com/mate-desktop/libmatemixer/commit/4d4520c) Abilitato Travis Cl per tutti i rami
* [8653076](https://github.com/mate-desktop/libmatemixer/commit/8653076) Inizializzato il supporto a Travis Cl
* [ae50369](https://github.com/mate-desktop/libmatemixer/commit/ae50369) aggiunto un file po mancante
* [af5d296](https://github.com/mate-desktop/libmatemixer/commit/af5d296) sincronizzazione con transifex
* [3c87f89](https://github.com/mate-desktop/libmatemixer/commit/3c87f89) versione pre-aggiornamento
* [d6a79fd](https://github.com/mate-desktop/libmatemixer/commit/d6a79fd) Richiede PulseAudio 5.0 ed è stato eliminato un po' di codice vecchio
* [e6a5518](https://github.com/mate-desktop/libmatemixer/commit/e6a5518) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [2fb29e6](https://github.com/mate-desktop/libmatemixer/commit/2fb29e6) aggiunto il supporto a Travis-Cl
* [f60062b](https://github.com/mate-desktop/libmatemixer/commit/f60062b) sincronizzazione con transifex
* [8afb1b3](https://github.com/mate-desktop/libmatemixer/commit/8afb1b3) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### libmateweather
* [33a4dd5](https://github.com/mate-desktop/libmateweather/commit/33a4dd5) Abilitato Travis Cl per tutti i rami
* [78e3339](https://github.com/mate-desktop/libmateweather/commit/78e3339) Inizializzato il supporto a Travis Cl
* [c0e6a9b](https://github.com/mate-desktop/libmateweather/commit/c0e6a9b) disabilitati i warning di deprecazione per distcheck
* [ada5129](https://github.com/mate-desktop/libmateweather/commit/ada5129) locations: Pulizia delle municipalità del Porto Rico
* [6a444b4](https://github.com/mate-desktop/libmateweather/commit/6a444b4) sincronizzazione con transifex
* [503f0b5](https://github.com/mate-desktop/libmateweather/commit/503f0b5) versione pre-aggiornamento
* [8d8508b](https://github.com/mate-desktop/libmateweather/commit/8d8508b) locations: Aggiunta Feira de Santana, Brasile
* [9c3dc44](https://github.com/mate-desktop/libmateweather/commit/9c3dc44) test_sun_moon.c: rimossa una variabile inutilizzata
* [113668f](https://github.com/mate-desktop/libmateweather/commit/113668f) weather-moon: corretta la bizzarria nei commenti
* [6197477](https://github.com/mate-desktop/libmateweather/commit/6197477) metar: corretta la ricerca della stringa da analizzare
* [2cb7572](https://github.com/mate-desktop/libmateweather/commit/2cb7572) metar: corretta in qualche modo l'indentazione
* [92346b7](https://github.com/mate-desktop/libmateweather/commit/92346b7) impostata la percentuale_minima ed il tipo nel file di configurazione
* [2054a03](https://github.com/mate-desktop/libmateweather/commit/2054a03) aggiunto il supporto a Travis-Cl
* [74edb1c](https://github.com/mate-desktop/libmateweather/commit/74edb1c) disabilitati i warning di deprecazione per distcheck
* [cecbcbb](https://github.com/mate-desktop/libmateweather/commit/cecbcbb) locations: Pulizia delle municipalità del Porto Rico
* [af00b18](https://github.com/mate-desktop/libmateweather/commit/af00b18) sincronizzazione con transifex
* [6ea8e08](https://github.com/mate-desktop/libmateweather/commit/6ea8e08) locations: Aggiunta Feira de Santana, Brasile
* [70e80da](https://github.com/mate-desktop/libmateweather/commit/70e80da) weather-moon: corretta la bizzarria nei commenti
* [4f556e0](https://github.com/mate-desktop/libmateweather/commit/4f556e0) metar: corretta la ricerca della stringa da analizzare
* [e059ca3](https://github.com/mate-desktop/libmateweather/commit/e059ca3) metar: corretta in qualche modo l'indentazione
* [11cd30b](https://github.com/mate-desktop/libmateweather/commit/11cd30b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### marco
* [369338f](https://github.com/mate-desktop/marco/commit/369338f) Non giudicare se una finestra è decorata o meno
* [230f96c](https://github.com/mate-desktop/marco/commit/230f96c) screen: Corretto l'utilizzo della memoria dopo che è stata liberata
* [76a5cff](https://github.com/mate-desktop/marco/commit/76a5cff) [Security] Utilizzo di 'g_strlcpy' al posto di 'strcpy'
* [fc162df](https://github.com/mate-desktop/marco/commit/fc162df) compositor-xrender: corretto un memory leak
* [7dd304a](https://github.com/mate-desktop/marco/commit/7dd304a) Prepararsi per l'unione di docker-build 0.1.1 al master
* [9523142](https://github.com/mate-desktop/marco/commit/9523142) Mostrata l'icona dello stato di build
* [7f48454](https://github.com/mate-desktop/marco/commit/7f48454) Adesso utilizzare docker-build sul ramo master
* [faed5d8](https://github.com/mate-desktop/marco/commit/faed5d8) modifica per utilizzare l'immagine archlinux/base
* [becec7e](https://github.com/mate-desktop/marco/commit/becec7e) Inizializzato il supporto a travis
* [fad23c9](https://github.com/mate-desktop/marco/commit/fad23c9) screen: Rimossa get_current_monitor in favore di get_current_xinerama
* [8abba9a](https://github.com/mate-desktop/marco/commit/8abba9a) Incrementata la dimensione dell'icona sui popup della scheda e dello spazio di lavoro
* [a931b08](https://github.com/mate-desktop/marco/commit/a931b08) screen: evitato 'NULL' nelle funzioni 'meta_error_trap...'
* [c0be5a7](https://github.com/mate-desktop/marco/commit/c0be5a7) prefs: evitata la deprecata 'g_settings_list_keys'
* [683d5cf](https://github.com/mate-desktop/marco/commit/683d5cf) aggiunto git.mk per l'auto-generazione dei file .gitignore
* [c3cad38](https://github.com/mate-desktop/marco/commit/c3cad38) abilitata la compilazione con l'output silenziato
* [4940310](https://github.com/mate-desktop/marco/commit/4940310) 'meta_error_trap_push' invece di 'meta_error_trap_push_with_return'
* [b4dcd38](https://github.com/mate-desktop/marco/commit/b4dcd38) errors.c: evitate le funzioni deprecate 'gdk_error_trap...':
* [898e941](https://github.com/mate-desktop/marco/commit/898e941) frames.c: eliminate le variabili inutilizzate
* [7a18fdd](https://github.com/mate-desktop/marco/commit/7a18fdd) compositor-xrender: evitata la deprecata 'gdk_error_trap_push/pop'
* [c5b4162](https://github.com/mate-desktop/marco/commit/c5b4162) corretta la compilazione con la traduzione della lingua 'as'
* [fff65b4](https://github.com/mate-desktop/marco/commit/fff65b4) sincronizzazione con transifex
* [a6f9462](https://github.com/mate-desktop/marco/commit/a6f9462) theme: riportato il formato del tema alla versione 3.6
* [fbae49d](https://github.com/mate-desktop/marco/commit/fbae49d) doc: aggiunte informazioni per le versioni del formato del tema 3.5 e 3.6
* [0b1c160](https://github.com/mate-desktop/marco/commit/0b1c160) ripristinata "libmarco-private: rimuovere la parte '-1' dal nome del percorso di include"
* [522ad73](https://github.com/mate-desktop/marco/commit/522ad73) Convertita la gestione delle regioni di cornice in regioni Cairo
* [93b5dd1](https://github.com/mate-desktop/marco/commit/93b5dd1) theme: aggiunto invisible_border al tema metacity
* [c49f361](https://github.com/mate-desktop/marco/commit/c49f361) aggiunto il supporto per il pulsante app-menu nel tema
* [cb9a1be](https://github.com/mate-desktop/marco/commit/cb9a1be) rimossa l'opzione per unire le finestre di dialogo modali
* [5418b40](https://github.com/mate-desktop/marco/commit/5418b40) theme: sostituito mutter/metacity con marco
* [9b6f737](https://github.com/mate-desktop/marco/commit/9b6f737) theme: Sostituiti i confronti con con gli elementi di un array di caratteri con strncmp
* [48b0b11](https://github.com/mate-desktop/marco/commit/48b0b11) tabpopup.c: mostare sempre 5px di bordo di outline
* [2ce772a](https://github.com/mate-desktop/marco/commit/2ce772a) tabpopup.c: Corretto * Correggere il bordo bianco mancante sulla outline window *. Non creare outline_window se non abbiamo intenzione di utilizzarla.
* [ffece2a](https://github.com/mate-desktop/marco/commit/ffece2a) Non mostrare ws switcher se si ha solo una Origine: Bug di Ubuntu: https://bugzilla.gnome.org/show_bug.cgi Bug-Ubuntu: https://bugs.launchpad.net/ubuntu/+source/metacity/+bug/506944 Author: Didier Roche <didrocks@ubuntu.com>
* [6203779](https://github.com/mate-desktop/marco/commit/6203779) theme: Consentire la disabilitazione dei colori di fallback in gtk:custom()
* [18bfff3](https://github.com/mate-desktop/marco/commit/18bfff3) theme: Consentito l'utilizzo di colori personalizzati dal tema GTK+
* [ed5eff6](https://github.com/mate-desktop/marco/commit/ed5eff6) theme: aggiunti gli stati della cornice tiled_left/tiled_right
* [997488f](https://github.com/mate-desktop/marco/commit/997488f) theme: Aggiunte le funzioni di sfondo ai singoli pulsanti
* [33c75c2](https://github.com/mate-desktop/marco/commit/33c75c2) theme-parser: Utilizzata peek_required_version() per la convalida
* [c9c3f85](https://github.com/mate-desktop/marco/commit/c9c3f85) Aggiunto il tipo cornice per unire le finestre modali
* [37fecf4](https://github.com/mate-desktop/marco/commit/37fecf4) Unire le finestre di dialogo modali in modo opzionale
* [4f47c5b](https://github.com/mate-desktop/marco/commit/4f47c5b) Aggiunto il metodo meta_window_get_transient_for()
* [a47f178](https://github.com/mate-desktop/marco/commit/a47f178) consentire ad un tema di specificare l'ampiezza ellittica di un titolo
* [728f002](https://github.com/mate-desktop/marco/commit/728f002) Aggiunte le variabili frame_x_center/frame_y_center ai temi
* [ed3004d](https://github.com/mate-desktop/marco/commit/ed3004d) metacity-theme-3.xml: Aggiunto un meccanismo di versione flessibile
* [2bea67f](https://github.com/mate-desktop/marco/commit/2bea67f) libmarco-private: rimuovere la parte '-1' dal nome del percorso di include
* [d06b592](https://github.com/mate-desktop/marco/commit/d06b592) theme-parser: rimosso un define inutilizzato
* [13e6a0d](https://github.com/mate-desktop/marco/commit/13e6a0d) sincronizzazione con transifex
* [4d70471](https://github.com/mate-desktop/marco/commit/4d70471) versione pre-aggiornamento
* [04e564c](https://github.com/mate-desktop/marco/commit/04e564c) corretta la posizione di ridimensionamento del popup sui display HiDPI
* [079c458](https://github.com/mate-desktop/marco/commit/079c458) Corretta la geometria della cornice per evitare il blocco del cursore di ridimensionamento
* [81fdb55](https://github.com/mate-desktop/marco/commit/81fdb55) Scalare la dimensione del cursore per HiDPI
* [4d8f163](https://github.com/mate-desktop/marco/commit/4d8f163) Utilizzata la finestra della cornice per determinare la scala
* [f6e3326](https://github.com/mate-desktop/marco/commit/f6e3326) Supportate le decorazioni delle finestre HiDPI
* [5989216](https://github.com/mate-desktop/marco/commit/5989216) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [03cffa3](https://github.com/mate-desktop/marco/commit/03cffa3) corretta la non corrispondenza delle enum nell'identificazione dell'associazione dei tasti per switch-panels e switch-panels-backward
* [42410fe](https://github.com/mate-desktop/marco/commit/42410fe) window: aggiungere _NET_WM_STATE_FOCUSED a _NET_WM_STATE
* [70d82d3](https://github.com/mate-desktop/marco/commit/70d82d3) evitata la deprecata GtkButton:use-stock
* [61c81eb](https://github.com/mate-desktop/marco/commit/61c81eb) evitata la deprecata GtkStock
* [6365649](https://github.com/mate-desktop/marco/commit/6365649) Correggere move_to_center che sposta la finestra tra i monitor
* [efac7b7](https://github.com/mate-desktop/marco/commit/efac7b7) Non giudicare se una finestra è decorata o meno
* [cd4c579](https://github.com/mate-desktop/marco/commit/cd4c579) Adesso utilizzare docker-build sul ramo master
* [10a4a9f](https://github.com/mate-desktop/marco/commit/10a4a9f) modifica per utilizzare l'immagine archlinux/base
* [c1f7c6c](https://github.com/mate-desktop/marco/commit/c1f7c6c) aggiunto config di travis-ci
* [8c11faa](https://github.com/mate-desktop/marco/commit/8c11faa) disabilitati i warning di deprecazione per distcheck
* [ae307ff](https://github.com/mate-desktop/marco/commit/ae307ff) sincronizzazione con transifex
* [8074c01](https://github.com/mate-desktop/marco/commit/8074c01) corretta la posizione di ridimensionamento del popup sui display HiDPI
* [45d8f75](https://github.com/mate-desktop/marco/commit/45d8f75) Corretta la geometria della cornice per evitare il blocco del cursore di ridimensionamento
* [df009f9](https://github.com/mate-desktop/marco/commit/df009f9) Aggiornato NEWS.
* [f45d299](https://github.com/mate-desktop/marco/commit/f45d299) Scalare la dimensione del cursore per HiDPI
* [95f4a7a](https://github.com/mate-desktop/marco/commit/95f4a7a) corretto as.po
* [bdc938b](https://github.com/mate-desktop/marco/commit/bdc938b) corretti i file po
* [44b60b0](https://github.com/mate-desktop/marco/commit/44b60b0) Utilizzata la finestra della cornice per determinare la scala
* [b9fd3c1](https://github.com/mate-desktop/marco/commit/b9fd3c1) Supportate le decorazioni delle finestre HiDPI
* [ff52d7b](https://github.com/mate-desktop/marco/commit/ff52d7b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [dc6ea05](https://github.com/mate-desktop/marco/commit/dc6ea05) corretta la non corrispondenza delle enum nell'identificazione dell'associazione dei tasti per switch-panels e switch-panels-backward
* [79f998c](https://github.com/mate-desktop/marco/commit/79f998c) Correggere move_to_center che sposta la finestra tra i monitor

### mate-applets
* [cb5ffc11](https://github.com/mate-desktop/mate-applets/commit/cb5ffc11) aggiunto il supporto a Travis-Cl
* [c6259e49](https://github.com/mate-desktop/mate-applets/commit/c6259e49) Problemi riportati dai traduttori
* [3b5b33a0](https://github.com/mate-desktop/mate-applets/commit/3b5b33a0) multiload: ignorati i mount point con privilegi
* [3e05a6ff](https://github.com/mate-desktop/mate-applets/commit/3e05a6ff) Compilazione con l'output silenziato
* [39d005b1](https://github.com/mate-desktop/mate-applets/commit/39d005b1) disabilitati i warning di deprecazione per distcheck
* [43a64acc](https://github.com/mate-desktop/mate-applets/commit/43a64acc) utilizzate funzioni make per HELP_LINGUAS
* [339fb827](https://github.com/mate-desktop/mate-applets/commit/339fb827) Netspeed Manual: ripulitura
* [eea28bc7](https://github.com/mate-desktop/mate-applets/commit/eea28bc7) Manual: Linux e sistemi UNIX -> Linux e altri sistemi UNIX-like
* [b233ee48](https://github.com/mate-desktop/mate-applets/commit/b233ee48) Utilizzate le liste ordinate per descrivere i passi per aggiungere l'applet al pannello
* [f211627e](https://github.com/mate-desktop/mate-applets/commit/f211627e) Manual: Corretto il titolo della finestra di dialogo Aggiungi al Pannello
* [41b743ee](https://github.com/mate-desktop/mate-applets/commit/41b743ee) Eyes Applet: corretto il titolo della finestra ed il factory name
* [e03b4852](https://github.com/mate-desktop/mate-applets/commit/e03b4852) Manual: OK -> Aggiungi (finestra di dialogo Aggiungi al Pannello)
* [48602d7f](https://github.com/mate-desktop/mate-applets/commit/48602d7f) trashapplet manual: guimenuitem Apri il Cestino
* [b452bf3b](https://github.com/mate-desktop/mate-applets/commit/b452bf3b) Aggiunti/Aggiornati gli screenshot in Catalano
* [eec0d1cd](https://github.com/mate-desktop/mate-applets/commit/eec0d1cd) Corretto il nome dell'applet Eyes
* [0600dbf6](https://github.com/mate-desktop/mate-applets/commit/0600dbf6) Fare riferimento alla pagina man fstab(5) per maggiori informazioni...
* [069a7a72](https://github.com/mate-desktop/mate-applets/commit/069a7a72) Rimossi i file png inutilizzati
* [565f521e](https://github.com/mate-desktop/mate-applets/commit/565f521e) Corretto l'url di ulink per farlo puntare a mate-user-guide
* [4dc452ba](https://github.com/mate-desktop/mate-applets/commit/4dc452ba) corretti errori di ortografia e grammatica
* [1f2d79bd](https://github.com/mate-desktop/mate-applets/commit/1f2d79bd) legal.xml
* [0a00b7cd](https://github.com/mate-desktop/mate-applets/commit/0a00b7cd) Cpufreq: costretta l'etichetta della frequenza alla renderizzazione se le frequenze non sono trovate istantaneamente
* [704fe986](https://github.com/mate-desktop/mate-applets/commit/704fe986) Cpufreq: Rilavorato per rimuovere ulteriori residui GTK2
* [0e139588](https://github.com/mate-desktop/mate-applets/commit/0e139588) Cpufreq: fatto in modo che l'etichetta della frequenza sia sempre mostrata se freq è selezionato
* [90633bf3](https://github.com/mate-desktop/mate-applets/commit/90633bf3) sincronizzazione con transifex
* [5ec87867](https://github.com/mate-desktop/mate-applets/commit/5ec87867) aggiornato mate-applets.pot
* [549542af](https://github.com/mate-desktop/mate-applets/commit/549542af) accessx: Convertite le icone da pixbuf a superfici Cairo
* [3aaeec39](https://github.com/mate-desktop/mate-applets/commit/3aaeec39) netspeed: Utilizzate le icone del tema invece di icone integrate
* [683946ed](https://github.com/mate-desktop/mate-applets/commit/683946ed) battstat: Caricate le icone del tema invece dei pixmaps
* [311ae4eb](https://github.com/mate-desktop/mate-applets/commit/311ae4eb) Convertite le icone da pixbuf a superfici
* [e83811d0](https://github.com/mate-desktop/mate-applets/commit/e83811d0) risolto il type mismatch in g_settings_set_value
* [e5ecb8b2](https://github.com/mate-desktop/mate-applets/commit/e5ecb8b2) solo la formattazione del testo per prepararsi al vero cambiamento
* [e35e9514](https://github.com/mate-desktop/mate-applets/commit/e35e9514) Corretta la spaziatura dell'applet cpufreq sui display HiDPI
* [4ece3d16](https://github.com/mate-desktop/mate-applets/commit/4ece3d16) multiload: aggiunta una classe di stile a multiload-applet
* [5426dfb4](https://github.com/mate-desktop/mate-applets/commit/5426dfb4) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [2b103078](https://github.com/mate-desktop/mate-applets/commit/2b103078) Abilitato Travis Cl per tutti i rami
* [a57ce1e1](https://github.com/mate-desktop/mate-applets/commit/a57ce1e1) Inizializzato il supporto a Travis Cl
* [ada156c7](https://github.com/mate-desktop/mate-applets/commit/ada156c7) Problemi riportati dai traduttori
* [7a8e4de6](https://github.com/mate-desktop/mate-applets/commit/7a8e4de6) disabilitati i warning di deprecazione per distcheck
* [cefd5e90](https://github.com/mate-desktop/mate-applets/commit/cefd5e90) Compilazione con l'output silenziato
* [dfad0318](https://github.com/mate-desktop/mate-applets/commit/dfad0318) Aggiunto il file git.mk
* [70085d23](https://github.com/mate-desktop/mate-applets/commit/70085d23) supporto per git.mk per generare .gitignore
* [e0793643](https://github.com/mate-desktop/mate-applets/commit/e0793643) sincronizzazione con transifex
* [3caf2ace](https://github.com/mate-desktop/mate-applets/commit/3caf2ace) utilizzate funzioni make per HELP_LINGUAS
* [867b495e](https://github.com/mate-desktop/mate-applets/commit/867b495e) Netspeed Manual: ripulitura
* [8d94f956](https://github.com/mate-desktop/mate-applets/commit/8d94f956) Manual: Linux e sistemi UNIX -> Linux e altri sistemi UNIX-like
* [0412e78e](https://github.com/mate-desktop/mate-applets/commit/0412e78e) Manual: Corretto il titolo della finestra di dialogo Aggiungi al Pannello
* [df8e737e](https://github.com/mate-desktop/mate-applets/commit/df8e737e) Eyes Applet: corretto il titolo della finestra ed il factory name
* [62c6b2bf](https://github.com/mate-desktop/mate-applets/commit/62c6b2bf) Manual: OK -> Aggiungi (finestra di dialogo Aggiungi al Pannello)
* [4802c6f0](https://github.com/mate-desktop/mate-applets/commit/4802c6f0) trashapplet manual: guimenuitem Apri il Cestino
* [030496ac](https://github.com/mate-desktop/mate-applets/commit/030496ac) Aggiunti/Aggiornati gli screenshot in Catalano
* [ca3008f4](https://github.com/mate-desktop/mate-applets/commit/ca3008f4) transifex: aggiornati i file pot:
* [365c147d](https://github.com/mate-desktop/mate-applets/commit/365c147d) Corretto il nome dell'applet Eyes
* [dacfd4dc](https://github.com/mate-desktop/mate-applets/commit/dacfd4dc) Fare riferimento alla pagina man fstab(5) per maggiori informazioni...
* [ec3d9f04](https://github.com/mate-desktop/mate-applets/commit/ec3d9f04) Rimossi i file png inutilizzati
* [5f1bb981](https://github.com/mate-desktop/mate-applets/commit/5f1bb981) Corretto l'url di ulink per farlo puntare a mate-user-guide
* [2783047f](https://github.com/mate-desktop/mate-applets/commit/2783047f) corretti errori di ortografia e grammatica
* [14a9913b](https://github.com/mate-desktop/mate-applets/commit/14a9913b) legal.xml
* [4e15c188](https://github.com/mate-desktop/mate-applets/commit/4e15c188) accessx-status: corretto un altro leak
* [6c34117f](https://github.com/mate-desktop/mate-applets/commit/6c34117f) Corretto un memory leak su  accessx-status.
* [246f078f](https://github.com/mate-desktop/mate-applets/commit/246f078f) sticky-notes: corretto un memory leak
* [ebabac90](https://github.com/mate-desktop/mate-applets/commit/ebabac90) timerapplet: Consentito il reset del timer quando inattivo
* [43b16f78](https://github.com/mate-desktop/mate-applets/commit/43b16f78) Weather: Applicato un nome widget al textview
* [1cd86c77](https://github.com/mate-desktop/mate-applets/commit/1cd86c77) weather: aggiunto un cssprovider per il widget non per lo schermo
* [a15746b9](https://github.com/mate-desktop/mate-applets/commit/a15746b9) mateweather-dialog.c: evitata la deprecata 'gtk_widget_override_font'
* [881233e8](https://github.com/mate-desktop/mate-applets/commit/881233e8) cpufreq: fermato il segfault con gtk3.23
* [6f4843f6](https://github.com/mate-desktop/mate-applets/commit/6f4843f6) trash applet: evitata la deprecata 'gtk_window_set_wmclass'
* [0746a55c](https://github.com/mate-desktop/mate-applets/commit/0746a55c) cpufreq: corretto un warning -Wimplicit-function-declaration
* [1a11a017](https://github.com/mate-desktop/mate-applets/commit/1a11a017) trash: corretto un warning -Wincompatible-pointer-types
* [2c31e385](https://github.com/mate-desktop/mate-applets/commit/2c31e385) weather-applet: sostituita la deprecata GtkAlignment
* [f4221bef](https://github.com/mate-desktop/mate-applets/commit/f4221bef) weather-dialog: sostituita la deprecata GtkAlignment
* [cf4ed850](https://github.com/mate-desktop/mate-applets/commit/cf4ed850) weather-prefs: sostituita la deprecata gtk_alignment_new
* [7551de5b](https://github.com/mate-desktop/mate-applets/commit/7551de5b) stickynotes: sostituite le funzioni deprecate gdk_error_trap_push/pop
* [3cd2d150](https://github.com/mate-desktop/mate-applets/commit/3cd2d150) cpu-freq: sostituita la deprecata gtk_menu_popup
* [d3bf8fd4](https://github.com/mate-desktop/mate-applets/commit/d3bf8fd4) sticknotes: sostituita la deprecata gtk_menu_popup
* [dc720b32](https://github.com/mate-desktop/mate-applets/commit/dc720b32) drivemount: sostituita la deprecata gtk_menu_popup
* [6270bb32](https://github.com/mate-desktop/mate-applets/commit/6270bb32) charpick: sostituita la deprecata gtk_menu_popup
* [0453aa6d](https://github.com/mate-desktop/mate-applets/commit/0453aa6d) sincronizzazione con transifex
* [f0b33d11](https://github.com/mate-desktop/mate-applets/commit/f0b33d11) Cpufreq: costretta l'etichetta della frequenza alla renderizzazione se le frequenze non sono trovate istantaneamente
* [618ab266](https://github.com/mate-desktop/mate-applets/commit/618ab266) Cpufreq: Rilavorata per rimuovere ulteriori residui GTK2
* [8bd11f81](https://github.com/mate-desktop/mate-applets/commit/8bd11f81) Cpufreq: fatto in modo che l'etichetta della frequenza sia sempre mostrata se freq è selezionato
* [a3c1c30f](https://github.com/mate-desktop/mate-applets/commit/a3c1c30f) aggiornato il file .pot
* [8a5af152](https://github.com/mate-desktop/mate-applets/commit/8a5af152) versione pre-aggiornamento
* [cbc200ff](https://github.com/mate-desktop/mate-applets/commit/cbc200ff) accessx: Convertite le icone da pixbuf a superfici Cairo
* [2b9d8bf7](https://github.com/mate-desktop/mate-applets/commit/2b9d8bf7) netspeed: Utilizzate le icone del tema invece di icone integrate
* [a03ead3c](https://github.com/mate-desktop/mate-applets/commit/a03ead3c) battstat: Caricate le icone del tema invece dei pixmaps
* [7185a704](https://github.com/mate-desktop/mate-applets/commit/7185a704) Convertite le icone da pixbuf a superfici
* [486f9e58](https://github.com/mate-desktop/mate-applets/commit/486f9e58) risolto il type mismatch in g_settings_set_value
* [23b0803d](https://github.com/mate-desktop/mate-applets/commit/23b0803d) solo la formattazione del testo per prepararsi al vero cambiamento
* [ea40c35e](https://github.com/mate-desktop/mate-applets/commit/ea40c35e) Corretta la spaziatura dell'applet cpufreq sui display HiDPI
* [ba596c20](https://github.com/mate-desktop/mate-applets/commit/ba596c20) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [147ca93e](https://github.com/mate-desktop/mate-applets/commit/147ca93e) multiload: aggiunta una classe di stile a multiload-applet
* [607d5228](https://github.com/mate-desktop/mate-applets/commit/607d5228) evitata la deprecata GtkStock

### mate-backgrounds
* [d741473](https://github.com/mate-desktop/mate-backgrounds/commit/d741473) Abilitato Travis Cl per tutti i rami
* [c3f5eb6](https://github.com/mate-desktop/mate-backgrounds/commit/c3f5eb6) Inizializzato il supporto a Travis Cl
* [556fd12](https://github.com/mate-desktop/mate-backgrounds/commit/556fd12) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [1e960de](https://github.com/mate-desktop/mate-backgrounds/commit/1e960de) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-calc
* [5600c81](https://github.com/mate-desktop/mate-calc/commit/5600c81) Inizializzato il supporto a Travis Cl
* [98f0b9b](https://github.com/mate-desktop/mate-calc/commit/98f0b9b) math-window: aggiornato l'anno di copyright a 2019
* [bfb8cd7](https://github.com/mate-desktop/mate-calc/commit/bfb8cd7) Tx: aggiornate le risorse per il server transifex
* [4637b01](https://github.com/mate-desktop/mate-calc/commit/4637b01) Incrementato l'intervallo di precisione a 15
* [187a975](https://github.com/mate-desktop/mate-calc/commit/187a975) math-display: evitata la deprecata 'gtk_widget_modify_bg'
* [bba427d](https://github.com/mate-desktop/mate-calc/commit/bba427d) currency-manager: evitata la deprecata 'g_type_class_add_private'
* [2c4aba1](https://github.com/mate-desktop/mate-calc/commit/2c4aba1) currency: evitata la deprecata 'g_type_class_add_private'
* [fc0720e](https://github.com/mate-desktop/mate-calc/commit/fc0720e) math-equation: evitata la deprecata 'g_type_class_add_private'
* [a61f07d](https://github.com/mate-desktop/mate-calc/commit/a61f07d) unit-manager: evitata la deprecata 'g_type_class_add_private'
* [25f0f0a](https://github.com/mate-desktop/mate-calc/commit/25f0f0a) unit-category: evitata la deprecata 'g_type_class_add_private'
* [e8ddb38](https://github.com/mate-desktop/mate-calc/commit/e8ddb38) unit: evitata la deprecata 'g_type_class_add_private'
* [5ffa9d9](https://github.com/mate-desktop/mate-calc/commit/5ffa9d9) mp-serializer: evitata la deprecata 'g_type_class_add_private'
* [e0e01b8](https://github.com/mate-desktop/mate-calc/commit/e0e01b8) math-variable-popup: evitata la deprecata 'g_type_class_add_private'
* [740f9a5](https://github.com/mate-desktop/mate-calc/commit/740f9a5) math-preferences: evitata la deprecata 'g_type_class_add_private'
* [0dd1f73](https://github.com/mate-desktop/mate-calc/commit/0dd1f73) math-variables: evitata la deprecata 'g_type_class_add_private'
* [b85ea87](https://github.com/mate-desktop/mate-calc/commit/b85ea87) math-converter: evitata la deprecata 'g_type_class_add_private'
* [f9e4e7e](https://github.com/mate-desktop/mate-calc/commit/f9e4e7e) math-buttons: evitata la deprecata 'g_type_class_add_private'
* [8c5611d](https://github.com/mate-desktop/mate-calc/commit/8c5611d) math-window: evitata la deprecata 'g_type_class_add_private'
* [9ac7540](https://github.com/mate-desktop/mate-calc/commit/9ac7540) Rimosso un assegnamento duplicato
* [49f81fb](https://github.com/mate-desktop/mate-calc/commit/49f81fb) corretto un errore di battitura
* [d0a089f](https://github.com/mate-desktop/mate-calc/commit/d0a089f) disabilitati i warning di deprecazione per distcheck
* [f13a023](https://github.com/mate-desktop/mate-calc/commit/f13a023) math-display: evitata la deprecata 'g_type_class_add_private'
* [ab8897e](https://github.com/mate-desktop/mate-calc/commit/ab8897e) math-window: corretto un memory leak
* [3693bc6](https://github.com/mate-desktop/mate-calc/commit/3693bc6) math-display.c: evitata la deprecata 'gtk_widget_ensure_style' (#66)
* [1546b67](https://github.com/mate-desktop/mate-calc/commit/1546b67) data: aggiornata la cartella appdata
* [be2b3b8](https://github.com/mate-desktop/mate-calc/commit/be2b3b8) ui files: aggiunte le icone mancanti nei titoli delle finestre di dialogo
* [a1cfbbd](https://github.com/mate-desktop/mate-calc/commit/a1cfbbd) buttons-programming.ui: Corretti i pulsasnti
* [6f31ccc](https://github.com/mate-desktop/mate-calc/commit/6f31ccc) utilizzate funzioni make per HELP_LINGUAS
* [5321fc4](https://github.com/mate-desktop/mate-calc/commit/5321fc4) Scritte le equazioni utilizzando MathML
* [d416464](https://github.com/mate-desktop/mate-calc/commit/d416464) corretto il nome dell'applicazione
* [0aee226](https://github.com/mate-desktop/mate-calc/commit/0aee226) corrette le parole ripetute
* [48a9bec](https://github.com/mate-desktop/mate-calc/commit/48a9bec) copiare le equazioni come testo ASCII
* [897ad51](https://github.com/mate-desktop/mate-calc/commit/897ad51) sincronizzazione con transifex
* [ea8f6ed](https://github.com/mate-desktop/mate-calc/commit/ea8f6ed) versione pre-aggiornamento
* [2ffd951](https://github.com/mate-desktop/mate-calc/commit/2ffd951) aggiornato il file .pot
* [58f106a](https://github.com/mate-desktop/mate-calc/commit/58f106a) UI: evitata la deprecata GtkButton:use-stock
* [074773b](https://github.com/mate-desktop/mate-calc/commit/074773b) UI: eliminati tutti gli elementi deprecati
* [fceb9a7](https://github.com/mate-desktop/mate-calc/commit/fceb9a7) math-preferences: aggiunta l'icona della finestra alla finestra di dialogo delle preferenze
* [e29978c](https://github.com/mate-desktop/mate-calc/commit/e29978c) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [6cd2c4d](https://github.com/mate-desktop/mate-calc/commit/6cd2c4d) Inizializzare gtk prima di math_equation_new; fix #44
* [f30835f](https://github.com/mate-desktop/mate-calc/commit/f30835f) evitata la deprecata gtk_image_menu_item_new_from_stock
* [eaa9ea6](https://github.com/mate-desktop/mate-calc/commit/eaa9ea6) aggiunto il supporto a Travis-Cl
* [0576c7c](https://github.com/mate-desktop/mate-calc/commit/0576c7c) disabilitati i warning di deprecazione per distcheck
* [38f08a4](https://github.com/mate-desktop/mate-calc/commit/38f08a4) data: aggiornata la cartella appdata
* [a279b86](https://github.com/mate-desktop/mate-calc/commit/a279b86) utilizzate funzioni make per HELP_LINGUAS
* [d7441b1](https://github.com/mate-desktop/mate-calc/commit/d7441b1) Scritte le equazioni utilizzando MathML
* [e486468](https://github.com/mate-desktop/mate-calc/commit/e486468) corretto il nome dell'applicazione
* [39590d8](https://github.com/mate-desktop/mate-calc/commit/39590d8) corrette le parole ripetute
* [de4b0c4](https://github.com/mate-desktop/mate-calc/commit/de4b0c4) copiare le equazioni come testo ASCII
* [b0890c3](https://github.com/mate-desktop/mate-calc/commit/b0890c3) sincronizzazione con transifex
* [a148e5b](https://github.com/mate-desktop/mate-calc/commit/a148e5b) math-preferences: aggiunta l'icona della finestra alla finestra di dialogo delle preferenze
* [10e6fdb](https://github.com/mate-desktop/mate-calc/commit/10e6fdb) Inizializzare gtk prima di math_equation_new
* [a64b304](https://github.com/mate-desktop/mate-calc/commit/a64b304) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-common
* [a89ecee](https://github.com/mate-desktop/mate-common/commit/a89ecee) travis ci iniziale

### mate-control-center
* [378becd](https://github.com/mate-desktop/mate-control-center/commit/378becd) yaml utilizza un numero inferiore di stringhe booleane 
* [ed6353d](https://github.com/mate-desktop/mate-control-center/commit/ed6353d) aggiunte le istruzioni di installazione
* [f0ec6cb](https://github.com/mate-desktop/mate-control-center/commit/f0ec6cb) Travis: utilizzato il link github per scaricare i tarball
* [21da1ad](https://github.com/mate-desktop/mate-control-center/commit/21da1ad) Prepararsi per l'unione di docker-build 0.1.1 al master
* [21d7f2c](https://github.com/mate-desktop/mate-control-center/commit/21d7f2c) corretti degli errori di battitura
* [b205683](https://github.com/mate-desktop/mate-control-center/commit/b205683) aggiunto archlinux build su travis-ci
* [81ae219](https://github.com/mate-desktop/mate-control-center/commit/81ae219) corretto il fallimento di distcheck su debian
* [8c0de1c](https://github.com/mate-desktop/mate-control-center/commit/8c0de1c) Abilitato travis per tutti i rami
* [43fd38d](https://github.com/mate-desktop/mate-control-center/commit/43fd38d) Aggiunto -Werror=format-security e mostrare che make distcheck ha fallito con il color
* [5dda92e](https://github.com/mate-desktop/mate-control-center/commit/5dda92e) script mantenuto silenzioso e distcheck restituisce sempre 0
* [da71960](https://github.com/mate-desktop/mate-control-center/commit/da71960) aggiunta la dipendenza mancante al pacchetto git code di mate-menus per debian/ubuntu
* [76ce83a](https://github.com/mate-desktop/mate-control-center/commit/76ce83a) utilizzato il codice git di mate-menus
* [7079813](https://github.com/mate-desktop/mate-control-center/commit/7079813) Inizializzato il supporto a travis
* [6d1a4aa](https://github.com/mate-desktop/mate-control-center/commit/6d1a4aa) eggcellrendererkeys: evitata la deprecata 'gtk_widget_modify_bg/fg'
* [bde8d11](https://github.com/mate-desktop/mate-control-center/commit/bde8d11) Aggiornato l'help di MCC
* [a62f043](https://github.com/mate-desktop/mate-control-center/commit/a62f043) default-applications: utilizzati più nomi di icone comuni per i documenti Office
* [3047735](https://github.com/mate-desktop/mate-control-center/commit/3047735) mate-display-properties: Migrazione da dbus-glib a GDBus
* [c5e048b](https://github.com/mate-desktop/mate-control-center/commit/c5e048b) corretto il warning in esecuzione su gtk_widget_destroy.
* [383d3da](https://github.com/mate-desktop/mate-control-center/commit/383d3da) Corretti un numero di errori cols dopo il reload dei menù.
* [512b446](https://github.com/mate-desktop/mate-control-center/commit/512b446) Corretto il crash quando si installa/rimuove una applicazione.
* [99b0d3e](https://github.com/mate-desktop/mate-control-center/commit/99b0d3e) capplets/mouse: file .svg invece che .png nell'artwork di doppio clic
* [7ebacdb](https://github.com/mate-desktop/mate-control-center/commit/7ebacdb) capplets/mouse: Nuove artwork di doppio clic con il logo mate
* [8f4dc20](https://github.com/mate-desktop/mate-control-center/commit/8f4dc20) disabilitati i warning di deprecazione per distcheck
* [9482529](https://github.com/mate-desktop/mate-control-center/commit/9482529) default-applications: corretto il fallimento di una assert su g_icon_to_string
* [08d1e4e](https://github.com/mate-desktop/mate-control-center/commit/08d1e4e) default-applications: aggiunto un widget per l'applicazione calcolatrice predefinita
* [a8d6bbb](https://github.com/mate-desktop/mate-control-center/commit/a8d6bbb) default-applications: utilizzato l'elaboratore di testi selezionato anche per RTF
* [3a3f389](https://github.com/mate-desktop/mate-control-center/commit/3a3f389) richiesto mate-settings-daemon-1.21.2
* [223c58a](https://github.com/mate-desktop/mate-control-center/commit/223c58a) keybindings: aggiunta una combinazione di tasti per commutare lo stato di muto del microfono
* [6a6da57](https://github.com/mate-desktop/mate-control-center/commit/6a6da57) keybindings: Aggiunte delle combinazioni di tasti per controllare agevolmente il volume
* [ee42ad7](https://github.com/mate-desktop/mate-control-center/commit/ee42ad7) richiesto m-s-d 1.21.1 a causa della nuova chiave control-center in schema
* [f8dc9a7](https://github.com/mate-desktop/mate-control-center/commit/f8dc9a7) Spiegato l'errore NULL quando si osserva G_IO_STATUS_EOF
* [c6c1db0](https://github.com/mate-desktop/mate-control-center/commit/c6c1db0) typing-break: sostituite le funzioni deprecate gdk_error_trap
* [73a72ba](https://github.com/mate-desktop/mate-control-center/commit/73a72ba) transifex: aggiornato mate-control-center.pot
* [2fcab0c](https://github.com/mate-desktop/mate-control-center/commit/2fcab0c) aggiornato l'hint per il doppio clic del mouse
* [8c44ea6](https://github.com/mate-desktop/mate-control-center/commit/8c44ea6) keybindings: doppio clic invece che clic singolo per modificare le scorciatoie da tastiera
* [ba5a88c](https://github.com/mate-desktop/mate-control-center/commit/ba5a88c) mate-keybinding-properties: evitata la deprecata 'gtk_widget_ensure_style'
* [b245b8d](https://github.com/mate-desktop/mate-control-center/commit/b245b8d) aggiunta l'opzione di ricerca per mate-font-viewer
* [dfa0fd1](https://github.com/mate-desktop/mate-control-center/commit/dfa0fd1) Caricata avatar-default come immagine predefinita
* [a6f0e57](https://github.com/mate-desktop/mate-control-center/commit/a6f0e57) per il supporto dei servizi di account
* [c5649ad](https://github.com/mate-desktop/mate-control-center/commit/c5649ad) keybindings: Aggiunta una combinazione di tasti alle impostazioni di lancio
* [03ef6ce](https://github.com/mate-desktop/mate-control-center/commit/03ef6ce) versione pre-aggiornamento
* [99f6f32](https://github.com/mate-desktop/mate-control-center/commit/99f6f32) Dipendenza da  mate-desktop 1.21.2 a causa di una nuova chiave gschema
* [291b050](https://github.com/mate-desktop/mate-control-center/commit/291b050) corretti errori di ortografia e grammatica
* [0a12038](https://github.com/mate-desktop/mate-control-center/commit/0a12038) legal.xml
* [1982f4f](https://github.com/mate-desktop/mate-control-center/commit/1982f4f) utilizzate funzioni make per HELP_LINGUAS
* [1034ff7](https://github.com/mate-desktop/mate-control-center/commit/1034ff7) Aggiunta una UI per controllare org.mate.accessibility-keyboard.stickykeys-latch-to-lock
* [be9b514](https://github.com/mate-desktop/mate-control-center/commit/be9b514) utilizzata la dimensione fissa per mostrare l'icona dell'utente
* [81d7a31](https://github.com/mate-desktop/mate-control-center/commit/81d7a31) Aggiunta una nuova api per EImageChooser
* [28c5512](https://github.com/mate-desktop/mate-control-center/commit/28c5512) Per ottenere/impostare l'icona del volto dell'utente utilizzare il servizio accounts
* [409e0a1](https://github.com/mate-desktop/mate-control-center/commit/409e0a1) sincronizzazione con transifex
* [397a588](https://github.com/mate-desktop/mate-control-center/commit/397a588) richiede mate-desktop-1.21.1
* [8c4ebef](https://github.com/mate-desktop/mate-control-center/commit/8c4ebef) typing-break: rendere le immagini più larghe e caricarle come superfice
* [19fdb3f](https://github.com/mate-desktop/mate-control-center/commit/19fdb3f) Mouse: Incluso un commutatore per abilitare o disabilitare l'incollaggio col il clic del tasto centrale del mouse che è predefinito su ON così da non modificare il comportamento atteso fin quando l'utente non lo modifica.
* [d5c8249](https://github.com/mate-desktop/mate-control-center/commit/d5c8249) capplets/keybindings: evitata la deprecata 'gdk_keymap_get_default'
* [657b706](https://github.com/mate-desktop/mate-control-center/commit/657b706) display-capplet.ui: sostituite le deprecazioni
* [d21cbad](https://github.com/mate-desktop/mate-control-center/commit/d21cbad) libslab: pulizia del codice
* [f6d429e](https://github.com/mate-desktop/mate-control-center/commit/f6d429e) wm-common: sostituite le funzioni deprecate gdk_error_trap
* [9edbc59](https://github.com/mate-desktop/mate-control-center/commit/9edbc59) libslab: sostituita la deprecata gtk_menu_popup
* [4facc83](https://github.com/mate-desktop/mate-control-center/commit/4facc83) msd-input-helper: sostituite le funzioni deprecate gdk_error_trap
* [e19868d](https://github.com/mate-desktop/mate-control-center/commit/e19868d) mouse: sostituite le funzioni deprecate gdk_error_trap
* [98b1b52](https://github.com/mate-desktop/mate-control-center/commit/98b1b52) sincronizzazione con transifex
* [ecb2d6a](https://github.com/mate-desktop/mate-control-center/commit/ecb2d6a) aggiornato mate-control-center.pot
* [110b5d8](https://github.com/mate-desktop/mate-control-center/commit/110b5d8) aggiornata la versione richiesta di mate-menus
* [7ba869d](https://github.com/mate-desktop/mate-control-center/commit/7ba869d) utilizzata la nuova api mate-menus
* [7137397](https://github.com/mate-desktop/mate-control-center/commit/7137397) utilizzata la nuova api
* [ede274e](https://github.com/mate-desktop/mate-control-center/commit/ede274e) utilizzata matemenu_tree_new
* [ea9ec0f](https://github.com/mate-desktop/mate-control-center/commit/ea9ec0f) appearance: corrette altre indentazioni
* [8a96f64](https://github.com/mate-desktop/mate-control-center/commit/8a96f64) appearance: corrette le indentazioni
* [31880fa](https://github.com/mate-desktop/mate-control-center/commit/31880fa) appearance: aggiunto lo switch buttons-have-icons
* [af21077](https://github.com/mate-desktop/mate-control-center/commit/af21077) aggiornato il potfile
* [acbde95](https://github.com/mate-desktop/mate-control-center/commit/acbde95) mouse: aggiunto lo switch di emulazione del pulsante centrale
* [3d3bb8b](https://github.com/mate-desktop/mate-control-center/commit/3d3bb8b) display-capplet: aggiunto un nome css per scrollarea
* [61e2e6e](https://github.com/mate-desktop/mate-control-center/commit/61e2e6e) Modificata la dimensione del cursore a 24px
* [1269bef](https://github.com/mate-desktop/mate-control-center/commit/1269bef) Scalare la dimensione del cursore per HiDPI quando si modifica il tema
* [b198f90](https://github.com/mate-desktop/mate-control-center/commit/b198f90) Corretta la geometria dello schermo per gestire la rotazione quando si esegue lo snapping.
* [48b4fc3](https://github.com/mate-desktop/mate-control-center/commit/48b4fc3) Aggiunto l'interruttore commutabile auto-detect
* [f083448](https://github.com/mate-desktop/mate-control-center/commit/f083448) transifex: impostata minimum_perc = 1
* [7eb6245](https://github.com/mate-desktop/mate-control-center/commit/7eb6245) transifex: aggiunto il tipo PO al file di configurazione del client
* [08252b1](https://github.com/mate-desktop/mate-control-center/commit/08252b1) po: aggiunto il file mancante a POTFILES.in
* [c7697c9](https://github.com/mate-desktop/mate-control-center/commit/c7697c9) theme-util.c: Corretto il segfalut sul tentativo di cancellare il tema personalizzato
* [257b236](https://github.com/mate-desktop/mate-control-center/commit/257b236) theme-thumbnail.c: evitata la deprecata GtkButton:use-stock
* [17b2017](https://github.com/mate-desktop/mate-control-center/commit/17b2017) evitata la deprecata GtkStock
* [9e312c4](https://github.com/mate-desktop/mate-control-center/commit/9e312c4) Rimosso il parametro inutilizzato in mate_theme_install_real
* [e76a646](https://github.com/mate-desktop/mate-control-center/commit/e76a646) theme-installer.c: aggiunti i suggerimenti quando si reinstalla un tema esistente
* [71e0779](https://github.com/mate-desktop/mate-control-center/commit/71e0779) aggiunto il supporto a Travis Cl
* [2ca7574](https://github.com/mate-desktop/mate-control-center/commit/2ca7574) corretto il fallimento di distcheck su debian
* [d93e910](https://github.com/mate-desktop/mate-control-center/commit/d93e910) Aggiornato l'help di MCC
* [22746a3](https://github.com/mate-desktop/mate-control-center/commit/22746a3) corretto il warning in esecuzione su gtk_widget_destroy.
* [56c1867](https://github.com/mate-desktop/mate-control-center/commit/56c1867) Corretti un numero di errori cols dopo il reload dei menù.
* [bc4e90b](https://github.com/mate-desktop/mate-control-center/commit/bc4e90b) disabilitati i warning di deprecazione per distcheck
* [a61bda0](https://github.com/mate-desktop/mate-control-center/commit/a61bda0) default-applications: utilizzato l'elaboratore di testi selezionato anche per RTF
* [9a36755](https://github.com/mate-desktop/mate-control-center/commit/9a36755) typing-break: rendere le immagini più larghe e caricarle come superfice
* [87d3627](https://github.com/mate-desktop/mate-control-center/commit/87d3627) aggiornato l'hint per il doppio clic del mouse
* [e5c3e4f](https://github.com/mate-desktop/mate-control-center/commit/e5c3e4f) keybindings: doppio clic invece che clic singolo per modificare le scorciatoie da tastiera
* [677966d](https://github.com/mate-desktop/mate-control-center/commit/677966d) corretti errori di ortografia e grammatica
* [439c26f](https://github.com/mate-desktop/mate-control-center/commit/439c26f) legal.xml
* [2d6e71b](https://github.com/mate-desktop/mate-control-center/commit/2d6e71b) utilizzate funzioni make per HELP_LINGUAS
* [7a3d258](https://github.com/mate-desktop/mate-control-center/commit/7a3d258) sincronizzazione con transifex
* [d06a1d3](https://github.com/mate-desktop/mate-control-center/commit/d06a1d3) display-capplet: aggiunto un nome css per scrollarea
* [954bf58](https://github.com/mate-desktop/mate-control-center/commit/954bf58) Modificata la dimensione del cursore a 24px
* [c026529](https://github.com/mate-desktop/mate-control-center/commit/c026529) Scalare la dimensione del cursore per HiDPI quando si modifica il tema
* [6d4493b](https://github.com/mate-desktop/mate-control-center/commit/6d4493b) Aggiunto l'interruttore commutabile auto-detect
* [4225308](https://github.com/mate-desktop/mate-control-center/commit/4225308) Rimosso il parametro inutilizzato in mate_theme_install_real
* [da86482](https://github.com/mate-desktop/mate-control-center/commit/da86482) Corretta la geometria dello schermo per gestire la rotazione quando si esegue lo snapping.
* [7165e06](https://github.com/mate-desktop/mate-control-center/commit/7165e06) theme-util.c: Corretto il segfalut sul tentativo di cancellare il tema personalizzato
* [8adccf3](https://github.com/mate-desktop/mate-control-center/commit/8adccf3) theme-installer.c: aggiunti i suggerimenti quando si reinstalla un tema esistente
* [598b187](https://github.com/mate-desktop/mate-control-center/commit/598b187) transifex: impostata minimum_perc = 1
* [61cde4b](https://github.com/mate-desktop/mate-control-center/commit/61cde4b) transifex: aggiunto il tipo PO al file di configurazione del client

### mate-desktop
* [137fd47](https://github.com/mate-desktop/mate-desktop/commit/137fd47) [Security] Utilizzo di 'g_strlcpy' al posto di 'strcpy'
* [3233410](https://github.com/mate-desktop/mate-desktop/commit/3233410) [Security] test-ditem: Utilizzo di 'g_strlcat' al posto di 'strcat'
* [b6bcccf](https://github.com/mate-desktop/mate-desktop/commit/b6bcccf) Prepararsi per l'unione di docker-build 0.1.1 al master
* [009ff2a](https://github.com/mate-desktop/mate-desktop/commit/009ff2a) utilizzata l'immagine archlinux/base 
* [89c003e](https://github.com/mate-desktop/mate-desktop/commit/89c003e) corretto il fallimento di make distcheck su debian.
* [87ff53b](https://github.com/mate-desktop/mate-desktop/commit/87ff53b) mate-colorsel: evitata la deprecata 'gtk_widget_modify_bg'
* [c15a018](https://github.com/mate-desktop/mate-desktop/commit/c15a018) Inizializzato il supporto a travis
* [b7dffb4](https://github.com/mate-desktop/mate-desktop/commit/b7dffb4) [mate-rr] Evitata la deprecata g_type_class_add_private
* [627a1d9](https://github.com/mate-desktop/mate-desktop/commit/627a1d9) migliorate le indentazioni
* [46950f4](https://github.com/mate-desktop/mate-desktop/commit/46950f4) Evitata la deprecata g_type_class_add_private
* [6d30b65](https://github.com/mate-desktop/mate-desktop/commit/6d30b65) [mate-colorsel] Evitata la deprecata g_type_class_add_private
* [e263ed7](https://github.com/mate-desktop/mate-desktop/commit/e263ed7) mate-bg: evitata la deprecata 'g_settings_list_keys'
* [0c8a787](https://github.com/mate-desktop/mate-desktop/commit/0c8a787) Aggiornato il copyright al 2019
* [470a488](https://github.com/mate-desktop/mate-desktop/commit/470a488) disabilitati i warning di deprecazione per distcheck
* [d98dcfc](https://github.com/mate-desktop/mate-desktop/commit/d98dcfc) mate-bg: Corretti alcuni commenti
* [6ca78f0](https://github.com/mate-desktop/mate-desktop/commit/6ca78f0) schemas: Definito schema per un calcolatore predefinito
* [f4ecfb3](https://github.com/mate-desktop/mate-desktop/commit/f4ecfb3) sincronizzazione con transifex
* [49dc665](https://github.com/mate-desktop/mate-desktop/commit/49dc665) versione pre-aggiornamento
* [98650b6](https://github.com/mate-desktop/mate-desktop/commit/98650b6) Aggiunta una nuova impostazione per controllare il latching del modificatore XKB
* [e9f904e](https://github.com/mate-desktop/mate-desktop/commit/e9f904e) sincronizzazione con transifex
* [f675d03](https://github.com/mate-desktop/mate-desktop/commit/f675d03) versione pre-aggiornamento
* [0b76914](https://github.com/mate-desktop/mate-desktop/commit/0b76914) interface: aggiunta una chiave per abilitare/disabilitare il copia/incolla con il pulsante centrale del mouse
* [f791ef8](https://github.com/mate-desktop/mate-desktop/commit/f791ef8) mate-desktop-item: sostituita la deprecata 'gdk_error_trap_push/pop'
* [6ef0247](https://github.com/mate-desktop/mate-desktop/commit/6ef0247) mate-rr-config: sostituita la deprecata gdk_flush
* [953da77](https://github.com/mate-desktop/mate-desktop/commit/953da77) mate-rr: sostituite le funzioni Gdk deprecate
* [c49a780](https://github.com/mate-desktop/mate-desktop/commit/c49a780) mate-bg-crossfade: sostituita la deprecata 'gdk_error_trap_push/pop'
* [5e16dc1](https://github.com/mate-desktop/mate-desktop/commit/5e16dc1) mate-bg: sostituita la deprecata 'gdk_error_trap_push/pop'
* [d21326d](https://github.com/mate-desktop/mate-desktop/commit/d21326d) corretto distcheck
* [ecf2fbd](https://github.com/mate-desktop/mate-desktop/commit/ecf2fbd) aggiunte le api di mate-language
* [f7cf0fd](https://github.com/mate-desktop/mate-desktop/commit/f7cf0fd) sincronizzazione con transifex 
* [58de8c0](https://github.com/mate-desktop/mate-desktop/commit/58de8c0) aggiornato mate-desktop.pot
* [ddc096e](https://github.com/mate-desktop/mate-desktop/commit/ddc096e) eliminato il vecchio ed inutilizzato acinclude.m4
* [fb4c986](https://github.com/mate-desktop/mate-desktop/commit/fb4c986) versione aggiornata
* [fa7491d](https://github.com/mate-desktop/mate-desktop/commit/fa7491d) Aggiunto un commutatore per sincronizzare QT_SCALE_FACTOR a GDK_SCALE_FACTOR
* [d28e063](https://github.com/mate-desktop/mate-desktop/commit/d28e063) Modificata la dimensione del cursore a 24px
* [6d06e18](https://github.com/mate-desktop/mate-desktop/commit/6d06e18) supportato il background fallback su HiDPI
* [1aa9a47](https://github.com/mate-desktop/mate-desktop/commit/1aa9a47) mate-rr-labeler: corretto il colore del font per i temi scuri
* [4ae8d1d](https://github.com/mate-desktop/mate-desktop/commit/4ae8d1d) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [41797c0](https://github.com/mate-desktop/mate-desktop/commit/41797c0) aggiunto il supporto a Travis-Cl
* [7304b6d](https://github.com/mate-desktop/mate-desktop/commit/7304b6d) corretto il fallimento di make distcheck su debian.
* [583659e](https://github.com/mate-desktop/mate-desktop/commit/583659e) disabilitati i warning di deprecazione per distcheck
* [19ded0f](https://github.com/mate-desktop/mate-desktop/commit/19ded0f) sincronizzazione con transifex 
* [51ce040](https://github.com/mate-desktop/mate-desktop/commit/51ce040) aggiornato mate-desktop.pot
* [6b137cb](https://github.com/mate-desktop/mate-desktop/commit/6b137cb) versione aggiornata
* [202d570](https://github.com/mate-desktop/mate-desktop/commit/202d570) Aggiunto un commutatore per sincronizzare QT_SCALE_FACTOR a GDK_SCALE_FACTOR
* [e71d548](https://github.com/mate-desktop/mate-desktop/commit/e71d548) Modificata la dimensione del cursore a 24px
* [b24f151](https://github.com/mate-desktop/mate-desktop/commit/b24f151) supportato il background fallback su HiDPI
* [abaa1e4](https://github.com/mate-desktop/mate-desktop/commit/abaa1e4) mate-rr-labeler: corretto il colore del font per i temi scuri
* [2059f58](https://github.com/mate-desktop/mate-desktop/commit/2059f58) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-icon-theme
* [eee2a8b](https://github.com/mate-desktop/mate-icon-theme/commit/eee2a8b) Abilitato Travis Cl per tutti i rami
* [3e72529](https://github.com/mate-desktop/mate-icon-theme/commit/3e72529) Inizializzato il supporto a Travis Cl
* [5823371](https://github.com/mate-desktop/mate-icon-theme/commit/5823371) versione pre-aggiornamento
* [2857b96](https://github.com/mate-desktop/mate-icon-theme/commit/2857b96) symlink all'icona input-touchpad.svg
* [0ba194a](https://github.com/mate-desktop/mate-icon-theme/commit/0ba194a) aggiunto un symlink per l'icona bluetooth
* [932961d](https://github.com/mate-desktop/mate-icon-theme/commit/932961d) aggiunte le icone per il touchpad
* [b4dd6b1](https://github.com/mate-desktop/mate-icon-theme/commit/b4dd6b1) sincronizzazione con transifex
* [9d16e11](https://github.com/mate-desktop/mate-icon-theme/commit/9d16e11) versione pre-aggiornamento
* [899a3e4](https://github.com/mate-desktop/mate-icon-theme/commit/899a3e4) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [8acc799](https://github.com/mate-desktop/mate-icon-theme/commit/8acc799) mate: aggiunto audio-volume-off
* [b9236af](https://github.com/mate-desktop/mate-icon-theme/commit/b9236af) Aggiunte le icone svg simboliche per i display video singolo e congiunto 
* [fbd4521](https://github.com/mate-desktop/mate-icon-theme/commit/fbd4521) symlink all'icona input-touchpad.svg
* [08cbd7e](https://github.com/mate-desktop/mate-icon-theme/commit/08cbd7e) sincronizzazione con transifex
* [d895041](https://github.com/mate-desktop/mate-icon-theme/commit/d895041) aggiunto un symlink per l'icona bluetooth
* [d1adafc](https://github.com/mate-desktop/mate-icon-theme/commit/d1adafc) aggiunte le icone per il touchpad
* [62293d7](https://github.com/mate-desktop/mate-icon-theme/commit/62293d7) mate: aggiunto audio-volume-off
* [98c5e84](https://github.com/mate-desktop/mate-icon-theme/commit/98c5e84) sincronizzazione con transifex
* [d454349](https://github.com/mate-desktop/mate-icon-theme/commit/d454349) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-indicator-applet
* [b8e45a5](https://github.com/mate-desktop/mate-indicator-applet/commit/b8e45a5) Abilitato Travis Cl per tutti i rami
* [e9b6aee](https://github.com/mate-desktop/mate-indicator-applet/commit/e9b6aee) Inizializzato il supporto a Travis Cl
* [eeed710](https://github.com/mate-desktop/mate-indicator-applet/commit/eeed710) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [24efcb7](https://github.com/mate-desktop/mate-indicator-applet/commit/24efcb7) tomboykeybinder: evitate 'gdk_error_trap_push/pop' e 'gdk_flush'
* [921f460](https://github.com/mate-desktop/mate-indicator-applet/commit/921f460) trasferire l'elenco delle lingue nel file po/LINGUAS
* [36a63e2](https://github.com/mate-desktop/mate-indicator-applet/commit/36a63e2) disabilitati i warning di deprecazione per distcheck
* [ee6ac63](https://github.com/mate-desktop/mate-indicator-applet/commit/ee6ac63) tomboykeybinder: evitata la deprecata 'gdk_keymap_get_default'
* [6a3c896](https://github.com/mate-desktop/mate-indicator-applet/commit/6a3c896) versione pre-aggiornamento
* [f918300](https://github.com/mate-desktop/mate-indicator-applet/commit/f918300) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [92472ab](https://github.com/mate-desktop/mate-indicator-applet/commit/92472ab) aggiunto il supporto a Travis-Cl
* [288c314](https://github.com/mate-desktop/mate-indicator-applet/commit/288c314) trasferire l'elenco delle lingue nel file po/LINGUAS
* [56f4d1b](https://github.com/mate-desktop/mate-indicator-applet/commit/56f4d1b) tomboykeybinder: evitata la deprecata 'gdk_keymap_get_default'
* [45d7501](https://github.com/mate-desktop/mate-indicator-applet/commit/45d7501) sincronizzazione con transifex
* [b51b549](https://github.com/mate-desktop/mate-indicator-applet/commit/b51b549) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-media
* [ad1f495](https://github.com/mate-desktop/mate-media/commit/ad1f495) Abilitato Travis Cl per tutti i rami
* [b7d4d16](https://github.com/mate-desktop/mate-media/commit/b7d4d16) Inizializzato il supporto a Travis Cl
* [f64fbb2](https://github.com/mate-desktop/mate-media/commit/f64fbb2) disabilitati i warning di deprecazione per distcheck
* [44967fe](https://github.com/mate-desktop/mate-media/commit/44967fe) sincronizzazione con transifex
* [be1dbeb](https://github.com/mate-desktop/mate-media/commit/be1dbeb) Ignorati gli ingressi "monitor" di PulseAudio quando viene mostrata l'icona del microfono
* [e06fd70](https://github.com/mate-desktop/mate-media/commit/e06fd70) gvc-mixer-dialog.c: evitata la deprecata 'gtk_widget_override_font'
* [a52e89c](https://github.com/mate-desktop/mate-media/commit/a52e89c) versione pre-aggiornamento
* [3588909](https://github.com/mate-desktop/mate-media/commit/3588909) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [778e116](https://github.com/mate-desktop/mate-media/commit/778e116) aggiunto il supporto a Travis-Cl
* [4fec5a8](https://github.com/mate-desktop/mate-media/commit/4fec5a8) disabilitati i warning di deprecazione per distcheck
* [78bac2f](https://github.com/mate-desktop/mate-media/commit/78bac2f) sincronizzazione con transifex
* [12539df](https://github.com/mate-desktop/mate-media/commit/12539df) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-menus
* [4bca866](https://github.com/mate-desktop/mate-menus/commit/4bca866) Corretta la posizione di installazione dei pacchetti
* [6226441](https://github.com/mate-desktop/mate-menus/commit/6226441) abilitato per tutti i rami
* [9d1f626](https://github.com/mate-desktop/mate-menus/commit/9d1f626) supporto a travis-ci iniziale
* [dcd67cc](https://github.com/mate-desktop/mate-menus/commit/dcd67cc) Aggiunto un include mancante
* [8210880](https://github.com/mate-desktop/mate-menus/commit/8210880) Passati al moderno realpath()
* [96505c4](https://github.com/mate-desktop/mate-menus/commit/96505c4) disabilitati i warning di deprecazione per distcheck
* [71e85c1](https://github.com/mate-desktop/mate-menus/commit/71e85c1) eliminati i residui del supporto di Python
* [1190fa5](https://github.com/mate-desktop/mate-menus/commit/1190fa5) Corretti problemi di transifex
* [15c1f94](https://github.com/mate-desktop/mate-menus/commit/15c1f94) sincronizzazione con transifex 
* [047e1d2](https://github.com/mate-desktop/mate-menus/commit/047e1d2) aggiornata la versione a 1.21.0
* [6399b84](https://github.com/mate-desktop/mate-menus/commit/6399b84) aggiornati gli esempi
* [524d3e4](https://github.com/mate-desktop/mate-menus/commit/524d3e4) backport per gnome-menus
* [b642c7c](https://github.com/mate-desktop/mate-menus/commit/b642c7c) utilizzato G_BEGIN/END_DECLS
* [9294083](https://github.com/mate-desktop/mate-menus/commit/9294083) richiesto gio-unix, eliminato l'esempio in python
* [edaad52](https://github.com/mate-desktop/mate-menus/commit/edaad52) richiesto gio-unix
* [2b06561](https://github.com/mate-desktop/mate-menus/commit/2b06561) eliminato il supporto a python2
* [d5896d5](https://github.com/mate-desktop/mate-menus/commit/d5896d5) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [4f2519d](https://github.com/mate-desktop/mate-menus/commit/4f2519d) aggiunto il supporto a Travis-Cl
* [1e2cc5d](https://github.com/mate-desktop/mate-menus/commit/1e2cc5d) disabilitati i warning di deprecazione per distcheck
* [d8ba530](https://github.com/mate-desktop/mate-menus/commit/d8ba530) sincronizzazione con transifex
* [df38513](https://github.com/mate-desktop/mate-menus/commit/df38513) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-netbook
* [288eaed](https://github.com/mate-desktop/mate-netbook/commit/288eaed) Abilitato Travis Cl per tutti i rami
* [7df6fe1](https://github.com/mate-desktop/mate-netbook/commit/7df6fe1) Inizializzato il supporto a Travis Cl
* [92910b6](https://github.com/mate-desktop/mate-netbook/commit/92910b6) evitate le deprecate 'gdk_error_trap_push/pop/pop_ignored' e 'gdk_flush'
* [5f26a3b](https://github.com/mate-desktop/mate-netbook/commit/5f26a3b) disabilitati i warning di deprecazione per distcheck
* [c488e7e](https://github.com/mate-desktop/mate-netbook/commit/c488e7e) tomboykeybinder: evitata la deprecata 'gdk_keymap_get_default'
* [4f78cde](https://github.com/mate-desktop/mate-netbook/commit/4f78cde) versione pre-aggiornamento
* [d3e0b44](https://github.com/mate-desktop/mate-netbook/commit/d3e0b44) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [37844ff](https://github.com/mate-desktop/mate-netbook/commit/37844ff) aggiunto il supporto a Travis-Cl
* [98c5585](https://github.com/mate-desktop/mate-netbook/commit/98c5585) disabilitati i warning di deprecazione per distcheck
* [1243c95](https://github.com/mate-desktop/mate-netbook/commit/1243c95) sincronizzazione con transifex
* [6c25a73](https://github.com/mate-desktop/mate-netbook/commit/6c25a73) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-notification-daemon
* [e143ad5](https://github.com/mate-desktop/mate-notification-daemon/commit/e143ad5) Prepararsi per l'unione di docker-build 0.1.1 al master
* [ae121af](https://github.com/mate-desktop/mate-notification-daemon/commit/ae121af) aggiornare per utilizzare l'immagine archlinux/base
* [fa47df1](https://github.com/mate-desktop/mate-notification-daemon/commit/fa47df1) Aggiornare per utilizzare l'ultimo script di docker-build
* [8e2df08](https://github.com/mate-desktop/mate-notification-daemon/commit/8e2df08) aggiunta debian sid al config di travis-CI
* [be2d132](https://github.com/mate-desktop/mate-notification-daemon/commit/be2d132) supporto a travis-CI iniziale
* [cf5a9a1](https://github.com/mate-desktop/mate-notification-daemon/commit/cf5a9a1) disabilitati i warning di deprecazione per distcheck
* [c586fe5](https://github.com/mate-desktop/mate-notification-daemon/commit/c586fe5) Evitato il warning in compilazione per g_type_class_add_private
* [3f3bc54](https://github.com/mate-desktop/mate-notification-daemon/commit/3f3bc54) sincronizzazione con transifex
* [73ad070](https://github.com/mate-desktop/mate-notification-daemon/commit/73ad070) aggiornato il file .pot
* [106ec3b](https://github.com/mate-desktop/mate-notification-daemon/commit/106ec3b) versione pre-aggiornamento
* [8217f2d](https://github.com/mate-desktop/mate-notification-daemon/commit/8217f2d) eliminata la dipendenza da dbus-glib
* [dccffbc](https://github.com/mate-desktop/mate-notification-daemon/commit/dccffbc) Utilizzato GVariant
* [960df18](https://github.com/mate-desktop/mate-notification-daemon/commit/960df18) Migrazione da dbus-glib a GDBus
* [f26d490](https://github.com/mate-desktop/mate-notification-daemon/commit/f26d490) aggiunti i segnali, rimosse le annotazioni dal file xml
* [4362bc3](https://github.com/mate-desktop/mate-notification-daemon/commit/4362bc3) utilizzati i file generati da gdbus
* [5e688bf](https://github.com/mate-desktop/mate-notification-daemon/commit/5e688bf) Aggiunto un nuovo file
* [6fd50ad](https://github.com/mate-desktop/mate-notification-daemon/commit/6fd50ad) Corrette alcune deprecazioni gdk
* [178eacc](https://github.com/mate-desktop/mate-notification-daemon/commit/178eacc) src/daemon/daemon.c: Sostituita la chiamata deprecata gvfs-open da "gio open" di libglib2.0-bin.
* [34baf35](https://github.com/mate-desktop/mate-notification-daemon/commit/34baf35) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [b164be0](https://github.com/mate-desktop/mate-notification-daemon/commit/b164be0) aggiunto il supporto a Travis-Cl
* [3af2c3d](https://github.com/mate-desktop/mate-notification-daemon/commit/3af2c3d) disabilitati i warning di deprecazione per distcheck
* [b899400](https://github.com/mate-desktop/mate-notification-daemon/commit/b899400) sincronizzazione con transifex
* [23fe34b](https://github.com/mate-desktop/mate-notification-daemon/commit/23fe34b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-panel
* [1db7d2a](https://github.com/mate-desktop/mate-panel/commit/1db7d2a) Assicurata la corretta traduzione del titolo della finestra di dialogo Informazioni
* [84c0435](https://github.com/mate-desktop/mate-panel/commit/84c0435) Prepararsi per l'unione di docker-build 0.1.1 al master
* [e0efbab](https://github.com/mate-desktop/mate-panel/commit/e0efbab) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [086ca8b](https://github.com/mate-desktop/mate-panel/commit/086ca8b) utilizzato docker-build sul ramo master
* [134d947](https://github.com/mate-desktop/mate-panel/commit/134d947) Corretto l'ultimo menù con gtk_menu_popup e il fallimento di seguire il tema del pannello
* [dacbd08](https://github.com/mate-desktop/mate-panel/commit/dacbd08) mate-panel-applet.c: sostituita la deprecata gtk_menu_popup
* [a577926](https://github.com/mate-desktop/mate-panel/commit/a577926) corretto il fallimento di make distcheck su debian.
* [5b873db](https://github.com/mate-desktop/mate-panel/commit/5b873db) utilizzata l'immagine archlinux/base
* [4a6c3df](https://github.com/mate-desktop/mate-panel/commit/4a6c3df) Allineate correttamente le posizioni dei menù dei pulsanti sui pannelli verticali
* [14fce6f](https://github.com/mate-desktop/mate-panel/commit/14fce6f) Testato il nuovo docker-build
* [15e3a68](https://github.com/mate-desktop/mate-panel/commit/15e3a68) supporto a travis-CI iniziale
* [371e3d7](https://github.com/mate-desktop/mate-panel/commit/371e3d7) corretto il crash quando si rimuove il vassoio
* [c733d20](https://github.com/mate-desktop/mate-panel/commit/c733d20) panel-action-protocol: Errore se viene utilizzato quando X11 è disabilitato
* [4fe2b74](https://github.com/mate-desktop/mate-panel/commit/4fe2b74) panel-force-quit: Errore se viene utilizzato quando X11 è disabilitato
* [db9a60c](https://github.com/mate-desktop/mate-panel/commit/db9a60c) panel-xutils: Errore se viene utilizzato quando X11 è disabilitato
* [00e26f7](https://github.com/mate-desktop/mate-panel/commit/00e26f7) xstuff: includere gli header GTK e GDK X11, così i file inclusi non devono
* [ab19ac4](https://github.com/mate-desktop/mate-panel/commit/ab19ac4) xstuff: aggiungere is_using_x11 ()
* [e3846eb](https://github.com/mate-desktop/mate-panel/commit/e3846eb) xstuff: Errore se X11 non è abilitato
* [62237a6](https://github.com/mate-desktop/mate-panel/commit/62237a6) Applets: compilare le applet X11 solo quando X11 è abilitato
* [d714792](https://github.com/mate-desktop/mate-panel/commit/d714792) Clock: supporto a Wayland
* [aa4754c](https://github.com/mate-desktop/mate-panel/commit/aa4754c) wncklet: Errore se si compila senza il supporto X11
* [d7edd93](https://github.com/mate-desktop/mate-panel/commit/d7edd93) Errore se si compila senza il supporto X11
* [3630b20](https://github.com/mate-desktop/mate-panel/commit/3630b20) applet.c: Rimossa l'inutilizzata mate_panel_applet_position_menu ()
* [b57daee](https://github.com/mate-desktop/mate-panel/commit/b57daee) libmate-panel-applet: Aggiunti i commenti negli header per spiegare il comportamento di Wayland
* [d30deb0](https://github.com/mate-desktop/mate-panel/commit/d30deb0) libmate-panel-applet: mate-panel-applet.c supporto a Wayland
* [8c9a517](https://github.com/mate-desktop/mate-panel/commit/8c9a517) libmate-panel-applet: Applet factory supporto a Wayland
* [3e4a50d](https://github.com/mate-desktop/mate-panel/commit/3e4a50d) libmate-panel-applet: Errore se panel-plug è compilato senza X11
* [23e1bda](https://github.com/mate-desktop/mate-panel/commit/23e1bda) libmate-panel-applet: Fermata la compilazione di file specifici di X11 su Wayland
* [793cc25](https://github.com/mate-desktop/mate-panel/commit/793cc25) eggsmclient: Evitata la deprecata 'g_type_class_add_private'
* [ab4812a](https://github.com/mate-desktop/mate-panel/commit/ab4812a) clock: impostato il padding orizzontale per clock-button
* [3d9cfcf](https://github.com/mate-desktop/mate-panel/commit/3d9cfcf) panel-config-global: evitata la deprecata 'g_settings_list_keys'
* [8d7aad1](https://github.com/mate-desktop/mate-panel/commit/8d7aad1) Memorizzata la dimensione della superficie del pesce per consentire il rendering senza codice specifico di backend
* [c4b2b33](https://github.com/mate-desktop/mate-panel/commit/c4b2b33) Rimossa la variabile screen inutilizzata dall'applet pesce
* [e7ed982](https://github.com/mate-desktop/mate-panel/commit/e7ed982) Rimosse le funzioni specifiche di X dall'applet pesce
* [c979fdf](https://github.com/mate-desktop/mate-panel/commit/c979fdf) README: non menzionare dbus-glib che non è più necessaria
* [9935eeb](https://github.com/mate-desktop/mate-panel/commit/9935eeb) Clock: Corretta la selezione della dimensione dell'icona meteo per l'altezza del pannello
* [8d0f753](https://github.com/mate-desktop/mate-panel/commit/8d0f753) Clock: Fatto in modo che l'icona del meteo si ridimensioni con il pannello
* [9484b05](https://github.com/mate-desktop/mate-panel/commit/9484b05) Tray: Corretta la spaziatura troppo ampia delle icone dopo che mate-polkit è stato utilizzato con sni
* [4c23197](https://github.com/mate-desktop/mate-panel/commit/4c23197) clock: forzata l'assenza di padding e margine verticale del pulsante
* [422f7e5](https://github.com/mate-desktop/mate-panel/commit/422f7e5) disabilitati i warning di deprecazione per distcheck
* [77d343b](https://github.com/mate-desktop/mate-panel/commit/77d343b) Non consentita la compilazione senza il supporto X11
* [0831806](https://github.com/mate-desktop/mate-panel/commit/0831806) Consentita l'abilitazione o la disabilitazione di un backend senza influenzare l'altro
* [c13a54c](https://github.com/mate-desktop/mate-panel/commit/c13a54c) Rimossi i file generati da Wayland con make clean
* [9b8511a](https://github.com/mate-desktop/mate-panel/commit/9b8511a) Sostituita l'opzione wayland-scanner private-code con del codice
* [3e73d66](https://github.com/mate-desktop/mate-panel/commit/3e73d66) clock.c: forzato il margine negativo, non passando su 'clockbutton'
* [a0d3068](https://github.com/mate-desktop/mate-panel/commit/a0d3068) Link con i protocolli e le librerie Wayland
* [b0fb7b5](https://github.com/mate-desktop/mate-panel/commit/b0fb7b5) Includere il makefile di generazione del protocollo Wayland nel sistema di compilazione
* [8dd32e8](https://github.com/mate-desktop/mate-panel/commit/8dd32e8) Incluso il makefile di generazione del protocollo Wayland
* [d7074e3](https://github.com/mate-desktop/mate-panel/commit/d7074e3) Aggiornato configure.ac per il supporto a Wayland
* [dc37f88](https://github.com/mate-desktop/mate-panel/commit/dc37f88) Aggiunto l'xml di protocollo XDG Shell
* [0ea564a](https://github.com/mate-desktop/mate-panel/commit/0ea564a) Aggiunto l'xml di protocollo Layer Shell
* [c50f7b3](https://github.com/mate-desktop/mate-panel/commit/c50f7b3) Rimosso il rilevamento dei pacchetti X11 legacy
* [9628efb](https://github.com/mate-desktop/mate-panel/commit/9628efb) panel-gtk: Corretti dei memory leak
* [76d6eff](https://github.com/mate-desktop/mate-panel/commit/76d6eff) versione pre-aggiornamento
* [22ab0e0](https://github.com/mate-desktop/mate-panel/commit/22ab0e0) sincronizzazione da transifex con le correzioni per il nuovo itstool
* [4302754](https://github.com/mate-desktop/mate-panel/commit/4302754) utilizzate funzioni make per HELP_LINGUAS
* [b9bd3f6](https://github.com/mate-desktop/mate-panel/commit/b9bd3f6) Controllato se manager->proxy è NULL
* [a34f531](https://github.com/mate-desktop/mate-panel/commit/a34f531) Migrato mate-panel da dbus-glib a gdbus
* [a73abb8](https://github.com/mate-desktop/mate-panel/commit/a73abb8) notification-area-preferences-dialog.ui: evitato GtkButton:use-stock
* [5764886](https://github.com/mate-desktop/mate-panel/commit/5764886) Corretto il warning di GdkSeat 
* [105f685](https://github.com/mate-desktop/mate-panel/commit/105f685) Ci siamo assicurati che alt-F1 possa mostrare il menù anche se non ci sono applet di menù sul pannello
* [d68268a](https://github.com/mate-desktop/mate-panel/commit/d68268a) na-tray: aggiunta una finestra di dialogo preferenze ed un ingresso al menù delle applet
* [10b9c30](https://github.com/mate-desktop/mate-panel/commit/10b9c30) na-tray: pannelli ampi, aggiunto GSettings all'applet
* [c7d431d](https://github.com/mate-desktop/mate-panel/commit/c7d431d) na-tray: pannelli ampi, convertito il display GtkBox principale in GtkGrid
* [9bdd469](https://github.com/mate-desktop/mate-panel/commit/9bdd469) na-tray: pannelli ampi, batch preliminare per rinominare da box a griglia
* [3f351d5](https://github.com/mate-desktop/mate-panel/commit/3f351d5) button-widget: pannelli ampi, limiti di ridimensionamento più adattabili su Widgets e frecce
* [e4fc17c](https://github.com/mate-desktop/mate-panel/commit/e4fc17c) README - Aggiunto un elenco delle dipendenze
* [423e74c](https://github.com/mate-desktop/mate-panel/commit/423e74c) legal.xml
* [0340a5e](https://github.com/mate-desktop/mate-panel/commit/0340a5e) Clock applet help: Per aggiustare la Data o l'Ora di Sistema
* [3fd6d38](https://github.com/mate-desktop/mate-panel/commit/3fd6d38) Clock applet help: Aggiunto Mostra i numeri della settimana nel calendario
* [b7a1ac5](https://github.com/mate-desktop/mate-panel/commit/b7a1ac5) Clock applet help: Corretta l'unità di velocità per i metri al secondo
* [16e6140](https://github.com/mate-desktop/mate-panel/commit/16e6140) sincronizzazione con transifex
* [f0f4c5e](https://github.com/mate-desktop/mate-panel/commit/f0f4c5e) menu-bar: trasferito correttamente il focus con alt-F1
* [4c30c52](https://github.com/mate-desktop/mate-panel/commit/4c30c52) panel: evitata una situazione critica
* [2e35407](https://github.com/mate-desktop/mate-panel/commit/2e35407) panel-toplevel: corretto un memory leak in calculate_minimum_height
* [31930d0](https://github.com/mate-desktop/mate-panel/commit/31930d0) applets: Guardarsi dalle correzioni di scale-factor di GTK su GtkSocket
* [139f183](https://github.com/mate-desktop/mate-panel/commit/139f183) window-list: Smesso di impostare i suggerimenti di dimensione fino a quando WnckTasklist non ha oggetti da mostrare.
* [f2f4d84](https://github.com/mate-desktop/mate-panel/commit/f2f4d84) applets: Corretti i messaggi di errore in runtime
* [b37f24e](https://github.com/mate-desktop/mate-panel/commit/b37f24e) mate-panel-applet: setup_x_error_handler anche per le applet in-process
* [a130fb0](https://github.com/mate-desktop/mate-panel/commit/a130fb0) GTK 3.23: corretta l'allocazione della dimensione delle applet
* [7369482](https://github.com/mate-desktop/mate-panel/commit/7369482) fish: evitata la deprecata 'gtk_window_set_wmclass'
* [9de3a86](https://github.com/mate-desktop/mate-panel/commit/9de3a86) Tray: semplificato force-redraw, utilizzato il codice che attualmente funziona
* [17ac8aa](https://github.com/mate-desktop/mate-panel/commit/17ac8aa) panel-actions: sostituita la deprecata gtk_menu_popup
* [8001d65](https://github.com/mate-desktop/mate-panel/commit/8001d65) applet-context-menu: sostituita la deprecata gtk_menu_popup
* [81896c0](https://github.com/mate-desktop/mate-panel/commit/81896c0) panel-context-menu: sostituita la deprecata gtk_menu_popup
* [3820f05](https://github.com/mate-desktop/mate-panel/commit/3820f05) GTK 3.23: non tagliare le icone troppo strette in modalità HiDPI
* [91f9afe](https://github.com/mate-desktop/mate-panel/commit/91f9afe) na-tray-child: rimossa na_tray_child_size_allocate
* [0022441](https://github.com/mate-desktop/mate-panel/commit/0022441) panel-menu-button: sostituita la deprecata gtk_menu_popup
* [6bad863](https://github.com/mate-desktop/mate-panel/commit/6bad863) na-tray-child: sostituite le funzioni deprecate gdk_error_trap_push/pop
* [7c63f61](https://github.com/mate-desktop/mate-panel/commit/7c63f61) libmate-panel-applet: sostituite le funzioni deprecate gdk_error_trap
* [20ea38d](https://github.com/mate-desktop/mate-panel/commit/20ea38d) panel-xutils: sostituite le funzioni deprecate gdk_error_trap
* [edb3e0d](https://github.com/mate-desktop/mate-panel/commit/edb3e0d) panel-util: sostituita la deprecata gdk_flush
* [36d1856](https://github.com/mate-desktop/mate-panel/commit/36d1856) main: sostituita la deprecata gdk_flush
* [5e296c1](https://github.com/mate-desktop/mate-panel/commit/5e296c1) panel-widget: sostituita la deprecata gdk_flush
* [c4aedbd](https://github.com/mate-desktop/mate-panel/commit/c4aedbd) panel-toplevel: aggiunta una classe css di posizionamento
* [9009c4e](https://github.com/mate-desktop/mate-panel/commit/9009c4e) panel-force-quit: sostituita la deprecata gtk_device_grab
* [cb34c54](https://github.com/mate-desktop/mate-panel/commit/cb34c54) panel-force-quit: sostituite le funzioni deprecate gdk_error_trap
* [08076de](https://github.com/mate-desktop/mate-panel/commit/08076de) panel-force-quit: sostituita la deprecata gdk_flush
* [b22dff4](https://github.com/mate-desktop/mate-panel/commit/b22dff4) menu.c: Correzione: mantenere gli spazi sulla sinistra se "menus-have-icons" è disattivato
* [5ca1fb1](https://github.com/mate-desktop/mate-panel/commit/5ca1fb1) Panel-gtk.c: Mostrare le icone del menù solo quando è impostato "menus-have-icons"
* [2d3406f](https://github.com/mate-desktop/mate-panel/commit/2d3406f) workspace-switcher: fornito un colore di fallback da tema
* [a5df21b](https://github.com/mate-desktop/mate-panel/commit/a5df21b) po: riportare pt_BR in LINGUAS
* [f8cbb7b](https://github.com/mate-desktop/mate-panel/commit/f8cbb7b) sincronizzazione con transifex
* [0c93617](https://github.com/mate-desktop/mate-panel/commit/0c93617) aggiornato mate-panel.pot
* [89e8e62](https://github.com/mate-desktop/mate-panel/commit/89e8e62) aggiornato il requisito di mate-menus
* [ac2778a](https://github.com/mate-desktop/mate-panel/commit/ac2778a) panel-menu-button.c: forzato l'utilizzo del basename per il confronto
* [2631577](https://github.com/mate-desktop/mate-panel/commit/2631577) Supportata la nuova api mate-menus
* [10b2021](https://github.com/mate-desktop/mate-panel/commit/10b2021) convertite le icone di lancio in superfici cairo
* [f775e89](https://github.com/mate-desktop/mate-panel/commit/f775e89) corretto il rendering e rimosse le applet in-process sul pannello non espanso
* [8e196da](https://github.com/mate-desktop/mate-panel/commit/8e196da) applet.c: evitata la deprecata GtkImageMenuItem
* [83be983](https://github.com/mate-desktop/mate-panel/commit/83be983) limitata la dimensione di panel-hide-button
* [9893c11](https://github.com/mate-desktop/mate-panel/commit/9893c11) clock: corretta la bizzarria nei commenti
* [3b9119b](https://github.com/mate-desktop/mate-panel/commit/3b9119b) clock: corretto l'errore di copia/incolla che causava use-after-free
* [7099408](https://github.com/mate-desktop/mate-panel/commit/7099408) clock: corretto use-after-free
* [74ec4df](https://github.com/mate-desktop/mate-panel/commit/74ec4df) fish: Installate le animazioni del pesce in una cartella fish-specifica 
* [f96c4ef](https://github.com/mate-desktop/mate-panel/commit/f96c4ef) fish: eliminata l'immagine wanda da gresource
* [8135c86](https://github.com/mate-desktop/mate-panel/commit/8135c86) sincronizzazione con transifex
* [38dbd34](https://github.com/mate-desktop/mate-panel/commit/38dbd34) css: utilizzato il segnale parsing-error per avvertire di immagini o file css errati
* [2170446](https://github.com/mate-desktop/mate-panel/commit/2170446) css: Conversione a GResource
* [fb3abe3](https://github.com/mate-desktop/mate-panel/commit/fb3abe3) na-tray: Conversione a GResource
* [e1db072](https://github.com/mate-desktop/mate-panel/commit/e1db072) wncklet: Conversione a GResource
* [1b7c43a](https://github.com/mate-desktop/mate-panel/commit/1b7c43a) panel: Conversione a GResource
* [ee07e90](https://github.com/mate-desktop/mate-panel/commit/ee07e90) clock: Utilizzata la nuova API GdkPixbuf per caricare le risorse
* [cfe0603](https://github.com/mate-desktop/mate-panel/commit/cfe0603) clock: Conversione a GResource
* [c61d371](https://github.com/mate-desktop/mate-panel/commit/c61d371) fish: Conversione a GResource
* [b6372ca](https://github.com/mate-desktop/mate-panel/commit/b6372ca) libpanel-applet: Aggiunta l'API panel_applet_setup_menu_from_resource()
* [45b2541](https://github.com/mate-desktop/mate-panel/commit/45b2541) Theme: consistente utilizzo del tema per le maniglie di trascinamento delle applet su tutti i temi
* [b060d2a](https://github.com/mate-desktop/mate-panel/commit/b060d2a) Ripristinato "panel-toplevel: Rimosso il controllo dei confini del puntatore in panel_toplevel_queue_auto_hide()"
* [8670151](https://github.com/mate-desktop/mate-panel/commit/8670151) panel-context-menu.c: evitata la deprecata GtkImageMenuItem
* [49a3b4a](https://github.com/mate-desktop/mate-panel/commit/49a3b4a) evitata 'gtk_file_chooser_dialog_new' con gli identificativi stock
* [8248680](https://github.com/mate-desktop/mate-panel/commit/8248680) aggiornato il potfile
* [15c910f](https://github.com/mate-desktop/mate-panel/commit/15c910f) Accessibility: maniglie delle applet in bianco e nero nei temi GNOME ad alto contrasto
* [50b0f8b](https://github.com/mate-desktop/mate-panel/commit/50b0f8b) panel-run-dialog.ui: evitate le deprecate:
* [7ebb494](https://github.com/mate-desktop/mate-panel/commit/7ebb494) fish.c: evitata 'gtk_dialog_new_with_buttons' con gli identificativi stock
* [33e4655](https://github.com/mate-desktop/mate-panel/commit/33e4655) Ripristinato "panel-run-dialog.ui: evitate le deprecate:"
* [67c1cd0](https://github.com/mate-desktop/mate-panel/commit/67c1cd0) Ripristinato "Ripristinare "panel-test-applets.ui: evitate le deprecate:""
* [f853512](https://github.com/mate-desktop/mate-panel/commit/f853512) ripristinato "panel-test-applets.ui: evitate le deprecate:"
* [d1aee5a](https://github.com/mate-desktop/mate-panel/commit/d1aee5a) panel-test-applets.ui: evitate le deprecate:
* [4d84a7e](https://github.com/mate-desktop/mate-panel/commit/4d84a7e) panel-run-dialog.ui: evitate le deprecate:
* [4d26d40](https://github.com/mate-desktop/mate-panel/commit/4d26d40) window-list.ui: evitate GtkVBox e GtkButton:use-stock
* [d3aacfe](https://github.com/mate-desktop/mate-panel/commit/d3aacfe) workspace-switcher.ui: evitata la deprecata GtkButton:use-stock
* [2e0a74d](https://github.com/mate-desktop/mate-panel/commit/2e0a74d) Theme: mostrare le maniglie delle applet nei temi non-MATE
* [d3d057d](https://github.com/mate-desktop/mate-panel/commit/d3d057d) panel-properties-dialog.ui: evitate GtkButton:use-stock e GtkImage:stock
* [d7ed6ff](https://github.com/mate-desktop/mate-panel/commit/d7ed6ff) fish.ui: evitate le deprecate:
* [55d46b4](https://github.com/mate-desktop/mate-panel/commit/55d46b4) clock.ui: evitate le deprecate:
* [a518a93](https://github.com/mate-desktop/mate-panel/commit/a518a93) evitata gtk_dialog_add_buttons con gli identificativi stock
* [3975311](https://github.com/mate-desktop/mate-panel/commit/3975311) corretto distcheck
* [fca5e6e](https://github.com/mate-desktop/mate-panel/commit/fca5e6e) workspace-switcher: supportato i3 window manager
* [6609af3](https://github.com/mate-desktop/mate-panel/commit/6609af3) workspace-switcher: supportato metacity window manager
* [bc66290](https://github.com/mate-desktop/mate-panel/commit/bc66290) Applicata la correzione per workspace-switcher di vkareh
* [fb2abbf](https://github.com/mate-desktop/mate-panel/commit/fb2abbf) Corretto il rendering dell'elenco delle finestre out-of-process con hidpi
* [0b15ea1](https://github.com/mate-desktop/mate-panel/commit/0b15ea1) hidpi: corretta lo spaziatura dell'icona del vassoio con window-scaling > 1
* [ff04f33](https://github.com/mate-desktop/mate-panel/commit/ff04f33) Corrette le dimensioni delle applet out-of-process per HiDPI
* [fa5cde3](https://github.com/mate-desktop/mate-panel/commit/fa5cde3) Corretto l'errore dei pulsanti che nascondono il pannello che lo rendevano più grande
* [6bbc333](https://github.com/mate-desktop/mate-panel/commit/6bbc333) run dialog: forzata la dimensione dell'icona quando si carica l'icona dell'applicazione
* [61ee811](https://github.com/mate-desktop/mate-panel/commit/61ee811) run dialog: corretta l'espansione del contenuto quando si ridimensiona la finestra
* [f6224f1](https://github.com/mate-desktop/mate-panel/commit/f6224f1) Corretto show-program-list della finestra di dialogo esegui
* [77be765](https://github.com/mate-desktop/mate-panel/commit/77be765) run-dialog: utilizzato F6 per alternare tra il campo di immissione e l'elenco dei programmi
* [27e2032](https://github.com/mate-desktop/mate-panel/commit/27e2032) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [73e025b](https://github.com/mate-desktop/mate-panel/commit/73e025b) Corrette le dimensioni dei montanti per HiDPI multi-monitors
* [a00f2c9](https://github.com/mate-desktop/mate-panel/commit/a00f2c9) Non scalare in basso le geometrie del monitor per i monitor GDK
* [87a3769](https://github.com/mate-desktop/mate-panel/commit/87a3769) Scalare in basso le geometrie del monitor ai pixel del dispositivo per supportare più monitor in HiDPI
* [b08bc13](https://github.com/mate-desktop/mate-panel/commit/b08bc13) Pulizia del codice del Cassetto e correzione del comportamento delle frecce
* [8d4877d](https://github.com/mate-desktop/mate-panel/commit/8d4877d) aggiunto il supporto a Travis-Cl
* [41e8a02](https://github.com/mate-desktop/mate-panel/commit/41e8a02) corretto il fallimento di make distcheck su debian.
* [cc33d66](https://github.com/mate-desktop/mate-panel/commit/cc33d66) Tray: Corretta la spaziatura troppo ampia delle icone dopo che mate-polkit è stato utilizzato con sni
* [bab2d5a](https://github.com/mate-desktop/mate-panel/commit/bab2d5a) na-tray: pannelli ampi, convertito il display GtkBox principale in GtkGrid
* [5027993](https://github.com/mate-desktop/mate-panel/commit/5027993) na-tray: pannelli ampi, batch preliminare per rinominare da box a griglia
* [d491abc](https://github.com/mate-desktop/mate-panel/commit/d491abc) button-widget: pannelli ampi, limiti di ridimensionamento più adattabili su Widgets e frecce
* [0a10e4b](https://github.com/mate-desktop/mate-panel/commit/0a10e4b) clock: impostato il padding orizzontale per clock-button
* [f701bec](https://github.com/mate-desktop/mate-panel/commit/f701bec) Clock: Corretta la selezione della dimensione dell'icona meteo per l'altezza del pannello
* [9803059](https://github.com/mate-desktop/mate-panel/commit/9803059) Clock: Fatto in modo che l'icona del meteo si ridimensioni con il pannello
* [b79d153](https://github.com/mate-desktop/mate-panel/commit/b79d153) clock: forzata l'assenza di padding e margine verticale del pulsante
* [1d99f02](https://github.com/mate-desktop/mate-panel/commit/1d99f02) disabilitati i warning di deprecazione per distcheck
* [2c548d1](https://github.com/mate-desktop/mate-panel/commit/2c548d1) Tray: semplificato force-redraw, utilizzato il codice che attualmente funziona
* [a014c7a](https://github.com/mate-desktop/mate-panel/commit/a014c7a) utilizzate funzioni make per HELP_LINGUAS
* [cdaf08f](https://github.com/mate-desktop/mate-panel/commit/cdaf08f) menu-bar: trasferito correttamente il focus con alt-F1
* [5b3cc79](https://github.com/mate-desktop/mate-panel/commit/5b3cc79) legal.xml
* [e6e3f39](https://github.com/mate-desktop/mate-panel/commit/e6e3f39) Clock applet help: Per aggiustare la Data o l'Ora di Sistema
* [01568a6](https://github.com/mate-desktop/mate-panel/commit/01568a6) Clock applet help: Aggiunto Mostra i numeri della settimana nel calendario
* [b1959f2](https://github.com/mate-desktop/mate-panel/commit/b1959f2) Clock applet help: Corretta l'unità di velocità per i metri al secondo
* [e7eda82](https://github.com/mate-desktop/mate-panel/commit/e7eda82) panel: evitata una situazione critica
* [de3e05b](https://github.com/mate-desktop/mate-panel/commit/de3e05b) panel-toplevel: corretto un memory leak in calculate_minimum_height
* [4c8fa18](https://github.com/mate-desktop/mate-panel/commit/4c8fa18) sincronizzazione con transifex
* [4bff213](https://github.com/mate-desktop/mate-panel/commit/4bff213) versione pre-aggiornamento
* [b179cad](https://github.com/mate-desktop/mate-panel/commit/b179cad) applets: Guardarsi dalle correzioni di scale-factor di GTK su GtkSocket
* [015cc74](https://github.com/mate-desktop/mate-panel/commit/015cc74) window-list: Smesso di impostare i suggerimenti di dimensione fino a quando WnckTasklist non ha oggetti da mostrare.
* [19bfc3d](https://github.com/mate-desktop/mate-panel/commit/19bfc3d) applets: Corretti i messaggi di errore in runtime
* [ae885fb](https://github.com/mate-desktop/mate-panel/commit/ae885fb) mate-panel-applet: setup_x_error_handler anche per le applet in-process
* [a673336](https://github.com/mate-desktop/mate-panel/commit/a673336) GTK 3.23: corretta l'allocazione della dimensione delle applet
* [b8c0dde](https://github.com/mate-desktop/mate-panel/commit/b8c0dde) GTK 3.23: non tagliare le icone troppo strette in modalità HiDPI
* [a5a079b](https://github.com/mate-desktop/mate-panel/commit/a5a079b) na-tray-child: rimossa na_tray_child_size_allocate
* [2c8de94](https://github.com/mate-desktop/mate-panel/commit/2c8de94) panel-toplevel: aggiunta una classe css di posizionamento
* [3e08875](https://github.com/mate-desktop/mate-panel/commit/3e08875) sincronizzazione con transifex
* [388ed1d](https://github.com/mate-desktop/mate-panel/commit/388ed1d) aggiornato mate-panel.pot
* [5c4eb86](https://github.com/mate-desktop/mate-panel/commit/5c4eb86) convertite le icone di lancio in superfici cairo
* [6e0188b](https://github.com/mate-desktop/mate-panel/commit/6e0188b) corretto il rendering e rimosse le applet in-process sul pannello non espanso
* [bc79584](https://github.com/mate-desktop/mate-panel/commit/bc79584) limitata la dimensione di panel-hide-button
* [8b287d0](https://github.com/mate-desktop/mate-panel/commit/8b287d0) clock: corretta la bizzarria nei commenti
* [9ff939b](https://github.com/mate-desktop/mate-panel/commit/9ff939b) clock: corretto l'errore di copia/incolla che causava use-after-free
* [a7dcec2](https://github.com/mate-desktop/mate-panel/commit/a7dcec2) fish: Installate le animazioni del pesce in una cartella fish-specifica 
* [cd623c5](https://github.com/mate-desktop/mate-panel/commit/cd623c5) fish: eliminata l'immagine wanda da gresource
* [f51051b](https://github.com/mate-desktop/mate-panel/commit/f51051b) utilizzato il segnale parsing-error per avvertire di immagini o file css errati
* [3db6772](https://github.com/mate-desktop/mate-panel/commit/3db6772) css: Conversione a GResource
* [9ee6deb](https://github.com/mate-desktop/mate-panel/commit/9ee6deb) na-tray: Conversione a GResource
* [ff613c4](https://github.com/mate-desktop/mate-panel/commit/ff613c4) wncklet: Conversione a GResource
* [6b461de](https://github.com/mate-desktop/mate-panel/commit/6b461de) panel: Conversione a GResource
* [72982f7](https://github.com/mate-desktop/mate-panel/commit/72982f7) clock: Utilizzata la nuova API GdkPixbuf per caricare le risorse
* [dcb6025](https://github.com/mate-desktop/mate-panel/commit/dcb6025) clock: Conversione a GResource
* [0e8b631](https://github.com/mate-desktop/mate-panel/commit/0e8b631) fish: Conversione a GResource
* [0b9863f](https://github.com/mate-desktop/mate-panel/commit/0b9863f) libpanel-applet: Aggiunta l'API panel_applet_setup_menu_from_resource()
* [cbdb7a5](https://github.com/mate-desktop/mate-panel/commit/cbdb7a5) Ripristinato "panel-toplevel: Rimosso il controllo dei confini del puntatore in panel_toplevel_queue_auto_hide()"
* [37ae832](https://github.com/mate-desktop/mate-panel/commit/37ae832) Accessibility: maniglie delle applet in bianco e nero nei temi GNOME ad alto contrasto
* [5f38df2](https://github.com/mate-desktop/mate-panel/commit/5f38df2) Theme: mostrare le maniglie delle applet nei temi non-MATE
* [db865a1](https://github.com/mate-desktop/mate-panel/commit/db865a1) corretto distcheck
* [dd6f3f7](https://github.com/mate-desktop/mate-panel/commit/dd6f3f7) workspace-switcher: supportato i3 window manager
* [496ac68](https://github.com/mate-desktop/mate-panel/commit/496ac68) Corretto il rendering dell'elenco delle finestre out-of-process con hidpi
* [72fb2fc](https://github.com/mate-desktop/mate-panel/commit/72fb2fc) workspace-switcher: supportato metacity window manager
* [88a2442](https://github.com/mate-desktop/mate-panel/commit/88a2442) Applicata la correzione per workspace-switcher di vkareh
* [d02fcc5](https://github.com/mate-desktop/mate-panel/commit/d02fcc5) hidpi: corretta lo spaziatura dell'icona del vassoio con window-scaling > 1
* [a32c8da](https://github.com/mate-desktop/mate-panel/commit/a32c8da) Corrette le dimensioni delle applet out-of-process per HiDPI
* [976ae5c](https://github.com/mate-desktop/mate-panel/commit/976ae5c) Corretto l'errore dei pulsanti che nascondono il pannello che lo rendevano più grande
* [3ce6c33](https://github.com/mate-desktop/mate-panel/commit/3ce6c33) run dialog: forzata la dimensione dell'icona quando si carica l'icona dell'applicazione
* [50aa81d](https://github.com/mate-desktop/mate-panel/commit/50aa81d) run dialog: corretta l'espansione del contenuto quando si ridimensiona la finestra
* [dce0491](https://github.com/mate-desktop/mate-panel/commit/dce0491) Corretto show-program-list della finestra di dialogo esegui
* [35205a5](https://github.com/mate-desktop/mate-panel/commit/35205a5) run-dialog: utilizzato F6 per alternare tra il campo di immissione e l'elenco dei programmi
* [77fdffd](https://github.com/mate-desktop/mate-panel/commit/77fdffd) Corrette le dimensioni dei montanti per HiDPI multi-monitors
* [06c84c7](https://github.com/mate-desktop/mate-panel/commit/06c84c7) Non scalare in basso le geometrie del monitor per i monitor GDK
* [3d15308](https://github.com/mate-desktop/mate-panel/commit/3d15308) Scalare in basso le geometrie del monitor ai pixel del dispositivo per supportare più monitor in HiDPI
* [13940c6](https://github.com/mate-desktop/mate-panel/commit/13940c6) Pulizia del codice del Cassetto e correzione del comportamento delle frecce
* [5ea3006](https://github.com/mate-desktop/mate-panel/commit/5ea3006) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-polkit
* [22de40a](https://github.com/mate-desktop/mate-polkit/commit/22de40a) Abilitato Travis Cl per tutti i rami
* [fbbd4e9](https://github.com/mate-desktop/mate-polkit/commit/fbbd4e9) Inizializzato il supporto a Travis Cl
* [5485eeb](https://github.com/mate-desktop/mate-polkit/commit/5485eeb) disabilitati i warning di deprecazione per distcheck
* [7469714](https://github.com/mate-desktop/mate-polkit/commit/7469714) versione pre-aggiornamento
* [1822c79](https://github.com/mate-desktop/mate-polkit/commit/1822c79) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [ee80536](https://github.com/mate-desktop/mate-polkit/commit/ee80536) aggiunto il supporto a Travis-Cl
* [e262a95](https://github.com/mate-desktop/mate-polkit/commit/e262a95) disabilitati i warning di deprecazione per distcheck
* [3ae929e](https://github.com/mate-desktop/mate-polkit/commit/3ae929e) sincronizzazione con transifex
* [264fefb](https://github.com/mate-desktop/mate-polkit/commit/264fefb) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-power-manager
* [fd27849](https://github.com/mate-desktop/mate-power-manager/commit/fd27849) aggiunti i pacchetti richiesti per archlinux
* [a763309](https://github.com/mate-desktop/mate-power-manager/commit/a763309) Inizializzato il supporto a Travis Cl
* [5dca0aa](https://github.com/mate-desktop/mate-power-manager/commit/5dca0aa) utilizzare libtool generato durante la compilazione rispetto a uno esterno
* [7badcbc](https://github.com/mate-desktop/mate-power-manager/commit/7badcbc) disabilitati i warning di deprecazione per distcheck
* [1514a0f](https://github.com/mate-desktop/mate-power-manager/commit/1514a0f) gpm-control: evitata la deprecata 'g_settings_list_schemas'
* [79fe889](https://github.com/mate-desktop/mate-power-manager/commit/79fe889) media-keys: arrotondare sempre le coordinate per il render delle icone dei servizi multimediali
* [ed4afca](https://github.com/mate-desktop/mate-power-manager/commit/ed4afca) media-keys: Modificata la posizione della barra della luminosità dell'OSD
* [2c2f966](https://github.com/mate-desktop/mate-power-manager/commit/2c2f966) osd-window: resa più piccola la finestra
* [a7b4e6c](https://github.com/mate-desktop/mate-power-manager/commit/a7b4e6c) media-keys: rese le icone più piccole sull'OSD
* [ff8f8d3](https://github.com/mate-desktop/mate-power-manager/commit/ff8f8d3) media-keys: Utilizzata una costante per la dimensione dell'icona sullo OSD
* [1a69d22](https://github.com/mate-desktop/mate-power-manager/commit/1a69d22) corretti errori di ortografia e grammatica
* [4dfae40](https://github.com/mate-desktop/mate-power-manager/commit/4dfae40) utilizzate funzioni make per HELP_LINGUAS
* [b3c86df](https://github.com/mate-desktop/mate-power-manager/commit/b3c86df) gpm-kbd-backlight: sostituita la deprecata GDK_DEVICE_MANAGER
* [71eb548](https://github.com/mate-desktop/mate-power-manager/commit/71eb548) gpm-backlight: sostituita la deprecata GDK_DEVICE_MANAGER
* [d5d6e8c](https://github.com/mate-desktop/mate-power-manager/commit/d5d6e8c) gpm-button: sostituite le funzioni Gdk deprecate
* [c569240](https://github.com/mate-desktop/mate-power-manager/commit/c569240) gpm-brightness: sostituite le funzioni Gdk deprecate
* [999651b](https://github.com/mate-desktop/mate-power-manager/commit/999651b) sincronizzazione con transifex
* [5f64b12](https://github.com/mate-desktop/mate-power-manager/commit/5f64b12) versione pre-aggiornamento
* [c4528fd](https://github.com/mate-desktop/mate-power-manager/commit/c4528fd) inhibit: scalare sempre l'icona per farla corrispondere alla dimensione del pannello
* [8e29023](https://github.com/mate-desktop/mate-power-manager/commit/8e29023) Inhibit Applet: Corretto l'eccessivo utilizzo della CPU
* [27482cc](https://github.com/mate-desktop/mate-power-manager/commit/27482cc) aggiunta l'icona della finestra mancante alla finestra di dialogo Informazioni
* [795df5f](https://github.com/mate-desktop/mate-power-manager/commit/795df5f) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [9929aea](https://github.com/mate-desktop/mate-power-manager/commit/9929aea) Scalare correttamente le dimensioni dell'OSD sui display HiDPI (#246)
* [8ea1469](https://github.com/mate-desktop/mate-power-manager/commit/8ea1469) corretta la grammatica
* [570a3be](https://github.com/mate-desktop/mate-power-manager/commit/570a3be) aggiunto il supporto a Travis-Cl
* [61f71d4](https://github.com/mate-desktop/mate-power-manager/commit/61f71d4) corretti errori di ortografia e grammatica
* [2dec591](https://github.com/mate-desktop/mate-power-manager/commit/2dec591) disabilitati i warning di deprecazione per distcheck
* [6ff9690](https://github.com/mate-desktop/mate-power-manager/commit/6ff9690) utilizzate funzioni make per HELP_LINGUAS
* [8a3e0c1](https://github.com/mate-desktop/mate-power-manager/commit/8a3e0c1) gpm-button: sostituite le funzioni Gdk deprecate
* [1ce6f4e](https://github.com/mate-desktop/mate-power-manager/commit/1ce6f4e) sincronizzazione con transifex
* [9530f79](https://github.com/mate-desktop/mate-power-manager/commit/9530f79) inhibit: scalare sempre l'icona per farla corrispondere alla dimensione del pannello
* [306b7e2](https://github.com/mate-desktop/mate-power-manager/commit/306b7e2) Inhibit Applet: Corretto l'eccessivo utilizzo della CPU
* [1e3fbac](https://github.com/mate-desktop/mate-power-manager/commit/1e3fbac) aggiunta l'icona della finestra mancante alla finestra di dialogo Informazioni
* [97163e8](https://github.com/mate-desktop/mate-power-manager/commit/97163e8) Scalare correttamente le dimensioni dell'OSD sui display HiDPI (#246)
* [ecc330b](https://github.com/mate-desktop/mate-power-manager/commit/ecc330b) corretta la grammatica
* [96eeaff](https://github.com/mate-desktop/mate-power-manager/commit/96eeaff) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-screensaver
* [f8bc365](https://github.com/mate-desktop/mate-screensaver/commit/f8bc365) Tx: sincronizzazione con transifex
* [cd70be5](https://github.com/mate-desktop/mate-screensaver/commit/cd70be5) effettuata la corretta esecuzione di distcheck su debian
* [feca97f](https://github.com/mate-desktop/mate-screensaver/commit/feca97f) Inizializzato il supporto a Travis Cl
* [ee41071](https://github.com/mate-desktop/mate-screensaver/commit/ee41071) Reso traducibile auth-username-label in lock-dialog-default.ui
* [11fedfe](https://github.com/mate-desktop/mate-screensaver/commit/11fedfe) mate-screensaver-command: supportato lo sblocco dello screensaver via CLI (--unlock)
* [84a14f0](https://github.com/mate-desktop/mate-screensaver/commit/84a14f0) disabilitati i warning di deprecazione per distcheck
* [43cfc3b](https://github.com/mate-desktop/mate-screensaver/commit/43cfc3b) sincronizzazione con transifex
* [dbd37df](https://github.com/mate-desktop/mate-screensaver/commit/dbd37df) corrette ulteriori deprecazioni correlate a GdkScreen
* [deb9266](https://github.com/mate-desktop/mate-screensaver/commit/deb9266) gs-grab-x11: sostituita la deprecata 'gdk_error_trap_push/pop'
* [ba96676](https://github.com/mate-desktop/mate-screensaver/commit/ba96676) gs-visual-gl: sostituita la deprecata 'gdk_error_trap_push/pop'
* [1bbadd3](https://github.com/mate-desktop/mate-screensaver/commit/1bbadd3) Rimosso il puntatore "monitor" dalle informazioni di debug
* [ef8f73d](https://github.com/mate-desktop/mate-screensaver/commit/ef8f73d) lock-plug: Scalare solo i widget lock-screen sulle versioni più vecchie di GTK
* [0d51a73](https://github.com/mate-desktop/mate-screensaver/commit/0d51a73) gs-lock-plug: evitata la deprecata 'gdk_keymap_get_default'
* [8d82e50](https://github.com/mate-desktop/mate-screensaver/commit/8d82e50) sincronizzazione con transifex
* [bba13cb](https://github.com/mate-desktop/mate-screensaver/commit/bba13cb) aggiornato mate-screensaver.pot
* [0ed125f](https://github.com/mate-desktop/mate-screensaver/commit/0ed125f) aggiornata la versione richiesta di mate-menus
* [c3807e7](https://github.com/mate-desktop/mate-screensaver/commit/c3807e7) Supportata la nuova api mate-menus
* [abaa88e](https://github.com/mate-desktop/mate-screensaver/commit/abaa88e) Corrette alcune deprecazioni gdk
* [ce87b58](https://github.com/mate-desktop/mate-screensaver/commit/ce87b58) corretto il warning gdk_flush  
* [675a41c](https://github.com/mate-desktop/mate-screensaver/commit/675a41c) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [145663b](https://github.com/mate-desktop/mate-screensaver/commit/145663b) evitata la deprecata GtkStock
* [2497b11](https://github.com/mate-desktop/mate-screensaver/commit/2497b11) aggiunto il supporto a Travis-Cl
* [faa8507](https://github.com/mate-desktop/mate-screensaver/commit/faa8507) disabilitati i warning di deprecazione per distcheck
* [e8d8b36](https://github.com/mate-desktop/mate-screensaver/commit/e8d8b36) Rimosso il puntatore "monitor" dalle informazioni di debug
* [1774853](https://github.com/mate-desktop/mate-screensaver/commit/1774853) sincronizzazione con transifex
* [465734b](https://github.com/mate-desktop/mate-screensaver/commit/465734b) corrette ulteriori deprecazioni correlate a GdkScreen
* [762ae73](https://github.com/mate-desktop/mate-screensaver/commit/762ae73) lock-plug: Scalare solo i widget lock-screen sulle versioni più vecchie di GTK
* [6498272](https://github.com/mate-desktop/mate-screensaver/commit/6498272) sincronizzazione con transifex
* [f94dbce](https://github.com/mate-desktop/mate-screensaver/commit/f94dbce) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-sensors-applet
* [707bf62](https://github.com/mate-desktop/mate-sensors-applet/commit/707bf62) Abilitato Travis Cl per tutti i rami
* [4ea376a](https://github.com/mate-desktop/mate-sensors-applet/commit/4ea376a) Inizializzato il supporto a Travis Cl
* [2628689](https://github.com/mate-desktop/mate-sensors-applet/commit/2628689) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [4cbcf29](https://github.com/mate-desktop/mate-sensors-applet/commit/4cbcf29) disabilitati i warning di deprecazione per distcheck
* [972866e](https://github.com/mate-desktop/mate-sensors-applet/commit/972866e) Aggiunto il supporto a NetBSD.
* [ff7769b](https://github.com/mate-desktop/mate-sensors-applet/commit/ff7769b) utilizzate funzioni make per HELP_LINGUAS
* [5bbef92](https://github.com/mate-desktop/mate-sensors-applet/commit/5bbef92) sincronizzazione con transifex
* [98da528](https://github.com/mate-desktop/mate-sensors-applet/commit/98da528) versione pre-aggiornamento
* [f8ca6f7](https://github.com/mate-desktop/mate-sensors-applet/commit/f8ca6f7) Corretto il copyright per i file dei plugin
* [915bd41](https://github.com/mate-desktop/mate-sensors-applet/commit/915bd41) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [34bc99e](https://github.com/mate-desktop/mate-sensors-applet/commit/34bc99e) Aggiunto un plugin dummy
* [78ab99a](https://github.com/mate-desktop/mate-sensors-applet/commit/78ab99a) pulizia del plugin UDisks2
* [64e3232](https://github.com/mate-desktop/mate-sensors-applet/commit/64e3232) sincronizzazione con transifex 
* [39a1a8c](https://github.com/mate-desktop/mate-sensors-applet/commit/39a1a8c) corretto l'ordine di salvataggio dei sensori v2
* [f876ed2](https://github.com/mate-desktop/mate-sensors-applet/commit/f876ed2) prefs-dialog: eliminato lo spazio non richiesto nella scheda generale
* [5359056](https://github.com/mate-desktop/mate-sensors-applet/commit/5359056) prefs-dialog: impostato min_width per enable_column
* [3f54c57](https://github.com/mate-desktop/mate-sensors-applet/commit/3f54c57) prefs-dialog: utilizzata la hscrollbar-policy GTK_POLICY_NEVER
* [7e48690](https://github.com/mate-desktop/mate-sensors-applet/commit/7e48690) corrette le deprecazioni di GtkStock
* [e06917d](https://github.com/mate-desktop/mate-sensors-applet/commit/e06917d) aggiunto il supporto a Travis-Cl
* [7063811](https://github.com/mate-desktop/mate-sensors-applet/commit/7063811) disabilitati i warning di deprecazione per distcheck
* [9af4264](https://github.com/mate-desktop/mate-sensors-applet/commit/9af4264) utilizzate funzioni make per HELP_LINGUAS 
* [8a41f1a](https://github.com/mate-desktop/mate-sensors-applet/commit/8a41f1a) sincronizzazione con transifex
* [5352e3b](https://github.com/mate-desktop/mate-sensors-applet/commit/5352e3b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [047590c](https://github.com/mate-desktop/mate-sensors-applet/commit/047590c) sincronizzazione con transifex
* [4ebb00d](https://github.com/mate-desktop/mate-sensors-applet/commit/4ebb00d) corretto l'ordine di salvataggio dei sensori v2
* [cba90be](https://github.com/mate-desktop/mate-sensors-applet/commit/cba90be) prefs-dialog: eliminato lo spazio non richiesto nella scheda generale
* [15b67d2](https://github.com/mate-desktop/mate-sensors-applet/commit/15b67d2) prefs-dialog: impostato min_width per enable_column
* [34edb53](https://github.com/mate-desktop/mate-sensors-applet/commit/34edb53) prefs-dialog: utilizzata la hscrollbar-policy GTK_POLICY_NEVER

### mate-session-manager
* [7f0a938](https://github.com/mate-desktop/mate-session-manager/commit/7f0a938) Prestare attenzione a systemd mancante
* [9e97673](https://github.com/mate-desktop/mate-session-manager/commit/9e97673) Prepararsi per l'unione di docker-build 0.1.1 al master
* [2dede6b](https://github.com/mate-desktop/mate-session-manager/commit/2dede6b) utilizzata l'immagine archlinux/base
* [9471682](https://github.com/mate-desktop/mate-session-manager/commit/9471682) aggiunto mate-wm.desktop.in nel tarball
* [db623bf](https://github.com/mate-desktop/mate-session-manager/commit/db623bf) corretto il fallimento di make distcheck su debian.
* [f3eb3e8](https://github.com/mate-desktop/mate-session-manager/commit/f3eb3e8) supporto a travis-CI iniziale
* [9c748b1](https://github.com/mate-desktop/mate-session-manager/commit/9c748b1) manager: riavviato il bus utente se ultima sessione grafica
* [37d538e](https://github.com/mate-desktop/mate-session-manager/commit/37d538e) systemd: aggiunge una api per verificare se questa sia l'ultima sessione grafica per un utente
* [409d9fc](https://github.com/mate-desktop/mate-session-manager/commit/409d9fc) gsm: Disconnettere tutti i dbus client quando dbus è disconnesso
* [0f4afbb](https://github.com/mate-desktop/mate-session-manager/commit/0f4afbb) manager: non attendere che tutti i client escano prima dell'uscita
* [2daa4af](https://github.com/mate-desktop/mate-session-manager/commit/2daa4af) [gsm-autostart-app] Migrazione da dbus-glib a gdbus
* [90346cd](https://github.com/mate-desktop/mate-session-manager/commit/90346cd) gsm-app-dialog: i secondi nello spinbutton sono stati resi traducibili
* [5c2ea73](https://github.com/mate-desktop/mate-session-manager/commit/5c2ea73) disabilitati i warning di deprecazione per distcheck
* [fbd7aa8](https://github.com/mate-desktop/mate-session-manager/commit/fbd7aa8) cambiare il ritardo di avvio di una app dove essa sia nel percorso di sistema
* [6f1578f](https://github.com/mate-desktop/mate-session-manager/commit/6f1578f) Rimosso il supporto a X-GNOME-Autostart-Delay
* [0e2eb8a](https://github.com/mate-desktop/mate-session-manager/commit/0e2eb8a) Aggiunta un'impostazione di ritardo a Startup Manager
* [34ef232](https://github.com/mate-desktop/mate-session-manager/commit/34ef232) gsm-properties-dialog: evitata 'gtk_dialog_add_button' con gli identificativi stock
* [7cd2ccc](https://github.com/mate-desktop/mate-session-manager/commit/7cd2ccc) evitata 'gtk_dialog_add_buttons' con gli identificativi stock
* [717a8f9](https://github.com/mate-desktop/mate-session-manager/commit/717a8f9) mate-session-save: mostrata l'icona nella finestra di dialogo di errore
* [f1427f0](https://github.com/mate-desktop/mate-session-manager/commit/f1427f0) Migrazione da dbus-glib a gdbus
* [413050e](https://github.com/mate-desktop/mate-session-manager/commit/413050e) Migrazione da dbus-glib a gdbus
* [f20dad8](https://github.com/mate-desktop/mate-session-manager/commit/f20dad8) session-properties.ui: evitata la deprecata GtkImage:stock
* [ef7100c](https://github.com/mate-desktop/mate-session-manager/commit/ef7100c) gsm-inhibit-dialog.ui: evitata la deprecata GtkVBox
* [c8cb269](https://github.com/mate-desktop/mate-session-manager/commit/c8cb269) session-properties.ui: evitate le deprecate:
* [7b99ea5](https://github.com/mate-desktop/mate-session-manager/commit/7b99ea5) gsm-manager: evitata la deprecata 'g_settings_list_schemas'
* [6b7875b](https://github.com/mate-desktop/mate-session-manager/commit/6b7875b) Evitato un warning in compilazione per g_type_class_add_private
* [bdec713](https://github.com/mate-desktop/mate-session-manager/commit/bdec713) Evitato un warning in compilazione per g_type_class_add_private
* [f3e8cce](https://github.com/mate-desktop/mate-session-manager/commit/f3e8cce) Evitato un warning in compilazione per g_type_class_add_private
* [6934f93](https://github.com/mate-desktop/mate-session-manager/commit/6934f93) Evitato un warning in compilazione per g_type_class_add_private
* [582bcba](https://github.com/mate-desktop/mate-session-manager/commit/582bcba) Evitato un warning in compilazione per g_type_class_add_private
* [851d9fe](https://github.com/mate-desktop/mate-session-manager/commit/851d9fe) Evitato un warning in compilazione per g_type_class_add_private
* [7df5759](https://github.com/mate-desktop/mate-session-manager/commit/7df5759) Mostrare il nome dell'applicazione solo quando viene eseguita con --version
* [f96eb6b](https://github.com/mate-desktop/mate-session-manager/commit/f96eb6b) Eliminate le virgolette semplici esterne dalla stringa restituita da gsettings nello script mate-wm.
* [8f35c04](https://github.com/mate-desktop/mate-session-manager/commit/8f35c04) sostituite le funzioni deprecate gdk_error_trap
* [a4540f2](https://github.com/mate-desktop/mate-session-manager/commit/a4540f2) Corretto un errore di battitura nell'opzione --logout-dialog
* [4dd5902](https://github.com/mate-desktop/mate-session-manager/commit/4dd5902) sincronizzazione con transifex
* [6883912](https://github.com/mate-desktop/mate-session-manager/commit/6883912) versione pre-aggiornamento
* [e10df32](https://github.com/mate-desktop/mate-session-manager/commit/e10df32) corretto un collegamento interrotto nelle pagine man
* [61b1c0b](https://github.com/mate-desktop/mate-session-manager/commit/61b1c0b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [91c840f](https://github.com/mate-desktop/mate-session-manager/commit/91c840f) evitata la deprecata GtkStock
* [9509073](https://github.com/mate-desktop/mate-session-manager/commit/9509073) aggiunto il supporto a Travis-Cl
* [8ceb3a0](https://github.com/mate-desktop/mate-session-manager/commit/8ceb3a0) aggiunto mate-wm.desktop.in nel tarball
* [5a20027](https://github.com/mate-desktop/mate-session-manager/commit/5a20027) corretto il fallimento di make distcheck su debian.
* [b5598ac](https://github.com/mate-desktop/mate-session-manager/commit/b5598ac) disabilitati i warning di deprecazione per distcheck
* [05bfead](https://github.com/mate-desktop/mate-session-manager/commit/05bfead) Corretto un errore di battitura nell'opzione --logout-dialog
* [65c9e10](https://github.com/mate-desktop/mate-session-manager/commit/65c9e10) sincronizzazione con transifex
* [2b6b543](https://github.com/mate-desktop/mate-session-manager/commit/2b6b543) corretto un collegamento interrotto nelle pagine man
* [9555a9c](https://github.com/mate-desktop/mate-session-manager/commit/9555a9c) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-settings-daemon
* [8c36ec4](https://github.com/mate-desktop/mate-settings-daemon/commit/8c36ec4) Prepararsi per l'unione di docker-build 0.1.1 al master
* [631481c](https://github.com/mate-desktop/mate-settings-daemon/commit/631481c) utilizzato debian.sh sul ramo master
* [5919cb0](https://github.com/mate-desktop/mate-settings-daemon/commit/5919cb0) corretto il fallimento di make distcheck su debian
* [5081e8f](https://github.com/mate-desktop/mate-settings-daemon/commit/5081e8f) corretta la compilazione di archlinux su travis
* [44844fc](https://github.com/mate-desktop/mate-settings-daemon/commit/44844fc) Inizializzato il supporto a travis
* [667c390](https://github.com/mate-desktop/mate-settings-daemon/commit/667c390) disabilitati i warning di deprecazione per distcheck
* [c19fce3](https://github.com/mate-desktop/mate-settings-daemon/commit/c19fce3) media-keys: Si esegue l'applicazione calcolatrice di default definita da schema
* [2830e71](https://github.com/mate-desktop/mate-settings-daemon/commit/2830e71) media-keys: Aggiunto il supporto per il tasto del silenziamento del microfono
* [3e77bd1](https://github.com/mate-desktop/mate-settings-daemon/commit/3e77bd1) msd-xrdb-manager: realizzato il widget
* [b2f3af2](https://github.com/mate-desktop/mate-settings-daemon/commit/b2f3af2) media-keys: Silenziati i cambiamenti del volume con Alt
* [0fdb1cd](https://github.com/mate-desktop/mate-settings-daemon/commit/0fdb1cd) msd-xrdb-manager.c: evitata la deprecata 'gtk_widget_ensure_style'
* [4434365](https://github.com/mate-desktop/mate-settings-daemon/commit/4434365) media-keys: arrotondare sempre le coordinate per il render delle icone dei servizi multimediali
* [e7222d9](https://github.com/mate-desktop/mate-settings-daemon/commit/e7222d9) media-keys: Modificata la posizione della barra del volume dell'OSD
* [f5ae497](https://github.com/mate-desktop/mate-settings-daemon/commit/f5ae497) osd-window: resa più piccola la finestra
* [8ec1bf0](https://github.com/mate-desktop/mate-settings-daemon/commit/8ec1bf0) media-keys: le icone sull'OSD sono state rese più piccole
* [bda6d7a](https://github.com/mate-desktop/mate-settings-daemon/commit/bda6d7a) media-keys: Utilizzata una costante per la dimensione dell'icona sull'OSD
* [4a54f68](https://github.com/mate-desktop/mate-settings-daemon/commit/4a54f68) media-keys: Aggiunto il test per le icone sull'OSD dello switch del display
* [d8eabb8](https://github.com/mate-desktop/mate-settings-daemon/commit/d8eabb8) media-keys: Aggiunto il supporto all'OSD per lo switch del display
* [62299ac](https://github.com/mate-desktop/mate-settings-daemon/commit/62299ac) media-keys: Non viene mostrato il livello quando è muto
* [5eb0645](https://github.com/mate-desktop/mate-settings-daemon/commit/5eb0645) corretta l'esecuzione di distcheck
* [2c5286d](https://github.com/mate-desktop/mate-settings-daemon/commit/2c5286d) sincronizzazione con transifex
* [6b00f4c](https://github.com/mate-desktop/mate-settings-daemon/commit/6b00f4c) media-keys: Aggiunto il test per le icone rfkill sull'OSD
* [3c54357](https://github.com/mate-desktop/mate-settings-daemon/commit/3c54357) media-keys: Aggiunta l'etichetta per l'OSD del touchpad
* [9e7a567](https://github.com/mate-desktop/mate-settings-daemon/commit/9e7a567) media-keys: Aggiunte le etichette per le icone rfkill dell'OSD
* [ea4ab83](https://github.com/mate-desktop/mate-settings-daemon/commit/ea4ab83) media-keys: Rimosso l'argomento inutile da show_level in msd_media_keys_window_set_action_custom
* [4971d19](https://github.com/mate-desktop/mate-settings-daemon/commit/4971d19) media-keys: Rimosso il test per le icone della luminosità dell' schermo dell'OSD
* [21469f2](https://github.com/mate-desktop/mate-settings-daemon/commit/21469f2) media-keys: Aggiunto il supporto per i tasti multimediali Killswitch
* [2b528ed](https://github.com/mate-desktop/mate-settings-daemon/commit/2b528ed) rfkill: Aggiunto il plugin di supporto RFKill sui sistemi Linux
* [765208e](https://github.com/mate-desktop/mate-settings-daemon/commit/765208e) Aggiunta una scorciatoia per avviare mate-control-center
* [11f25cd](https://github.com/mate-desktop/mate-settings-daemon/commit/11f25cd) versione pre-aggiornamento
* [c33458f](https://github.com/mate-desktop/mate-settings-daemon/commit/c33458f) media-keys: Aggiunto il testo per le icone sull'OSD del touchpad
* [7c5d340](https://github.com/mate-desktop/mate-settings-daemon/commit/7c5d340) media-keys: Rimosse le icone dell'OSD del touchpad ed utilizzate quelle del tema
* [45de88e](https://github.com/mate-desktop/mate-settings-daemon/commit/45de88e) media-keys: semplificato l'OSD del touchpad
* [193f3fb](https://github.com/mate-desktop/mate-settings-daemon/commit/193f3fb) media-keys: Aggiunto il supporto per XF86TouchpadOn/Off
* [b761b23](https://github.com/mate-desktop/mate-settings-daemon/commit/b761b23) Aggiunto il supporto per org.mate.accessibility-keyboard.stickykeys-latch-to-lock
* [3c9e5dd](https://github.com/mate-desktop/mate-settings-daemon/commit/3c9e5dd) Xrandr: rimossa una funzione inutilizzata
* [e0b7a6b](https://github.com/mate-desktop/mate-settings-daemon/commit/e0b7a6b) daemon: corretto un memory leak
* [763db9d](https://github.com/mate-desktop/mate-settings-daemon/commit/763db9d) daemon: Cessato l'utilizzo dell'API deprecata di GSettings
* [0d4ec03](https://github.com/mate-desktop/mate-settings-daemon/commit/0d4ec03) richiesto mate-desktop-1.21.1
* [654d96e](https://github.com/mate-desktop/mate-settings-daemon/commit/654d96e) xsettings: aggiunta l'impostazione per abilitare/disabilitare il copia/incolla con il pulsante centrale del mouse
* [66b5931](https://github.com/mate-desktop/mate-settings-daemon/commit/66b5931) xsettings: sostituita la deprecata gdk_error_trap_push/pop
* [03368ab](https://github.com/mate-desktop/mate-settings-daemon/commit/03368ab) xrandr-manager: sostituita la deprecata gdk_error_trap_push/pop
* [fb9e750](https://github.com/mate-desktop/mate-settings-daemon/commit/fb9e750) mouse-manager: sostituita la deprecata gdk_error_trap_push/pop
* [cfe1160](https://github.com/mate-desktop/mate-settings-daemon/commit/cfe1160) media-keys-manager: sostituita la deprecata GdkDeviceManager
* [d68a31d](https://github.com/mate-desktop/mate-settings-daemon/commit/d68a31d) keyboard-manager: sostituita la deprecata gdk_error_trap_push/pop
* [68df93b](https://github.com/mate-desktop/mate-settings-daemon/commit/68df93b) clipboard-manager: sostituita la deprecata gdk_error_trap_push/pop
* [3431355](https://github.com/mate-desktop/mate-settings-daemon/commit/3431355) background-manager: sostituite le funzioni GDK deprecate
* [7d65c47](https://github.com/mate-desktop/mate-settings-daemon/commit/7d65c47) a11y-keyboard-manager: sostituita la deprecata gdk_error_trap_push/pop
* [6ae456c](https://github.com/mate-desktop/mate-settings-daemon/commit/6ae456c) msd-input-helper: sostituita la deprecata gdk_error_trap_push/pop
* [3fe98d7](https://github.com/mate-desktop/mate-settings-daemon/commit/3fe98d7) plugins: evitata la deprecata 'gdk_keymap_get_default'
* [e60080f](https://github.com/mate-desktop/mate-settings-daemon/commit/e60080f) sincronizzazione con transifex
* [842ba62](https://github.com/mate-desktop/mate-settings-daemon/commit/842ba62) aggiornato m-s-d.pot
* [6d92e9c](https://github.com/mate-desktop/mate-settings-daemon/commit/6d92e9c) xrandr-applet-popup: aggiunta un'icona per l'elemento di configurazione
* [3cfc8b5](https://github.com/mate-desktop/mate-settings-daemon/commit/3cfc8b5) xrandr-applet-popup: aggiunto un elemento per duplicare lo schermo sui display
* [4e412a5](https://github.com/mate-desktop/mate-settings-daemon/commit/4e412a5) aggiornato il requisito per m-s-d
* [74f284c](https://github.com/mate-desktop/mate-settings-daemon/commit/74f284c) aggiornamento della versione 
* [0034a56](https://github.com/mate-desktop/mate-settings-daemon/commit/0034a56) Resa opzionale l'impostazione QT_SCALE_FACTOR.
* [01b8f12](https://github.com/mate-desktop/mate-settings-daemon/commit/01b8f12) xrandr-applet-popup: smorzare gli elementi del menu per il monitor disabilitato
* [409c8d8](https://github.com/mate-desktop/mate-settings-daemon/commit/409c8d8) xrandr-applet-popup: abilitata la possibilità di accendere/spegnere i monitor
* [05d1d3c](https://github.com/mate-desktop/mate-settings-daemon/commit/05d1d3c) xrandr-applet-popup: mostrare l'icona solo se "menus-have-icons" non è disattivata
* [0630644](https://github.com/mate-desktop/mate-settings-daemon/commit/0630644) xrandr-applet-popup: gestiti i temi Greybird (etc) di XFCE
* [2aa4cec](https://github.com/mate-desktop/mate-settings-daemon/commit/2aa4cec) Xrandr-applet-popup: caso speciale i temi GNOME per il testo nero sulle etichette dei monitor
* [7bc681f](https://github.com/mate-desktop/mate-settings-daemon/commit/7bc681f) xrandr-applet-popup: rimosso il callback di disegno
* [0ca8f6d](https://github.com/mate-desktop/mate-settings-daemon/commit/0ca8f6d) xrandr: corretta l'indentazione 
* [6bc54f1](https://github.com/mate-desktop/mate-settings-daemon/commit/6bc54f1) xrandr-applet-popup: concesso ai temi di sovrascrivere i colori delle etichette dei monitor
* [c6f5693](https://github.com/mate-desktop/mate-settings-daemon/commit/c6f5693) xrandr-applet-popup: aggiunto un bordo alle etichette colorate dei monitor
* [fff8a2f](https://github.com/mate-desktop/mate-settings-daemon/commit/fff8a2f) xrandr-applet-popup: riutilizzato lo sfondo colorato sulle etichette dei monitor
* [57b6fa4](https://github.com/mate-desktop/mate-settings-daemon/commit/57b6fa4) xrandr applet popup: aggiunte le icone del monitor agli elementi di menù dell'etichetta dei monitor
* [a386cd6](https://github.com/mate-desktop/mate-settings-daemon/commit/a386cd6) xrandr-applet: aggiunta una classe di stile per gli elementi di menù
* [0f32717](https://github.com/mate-desktop/mate-settings-daemon/commit/0f32717) xrandr-applet: eliminato lo sfondo non funzionante dal menù
* [2674157](https://github.com/mate-desktop/mate-settings-daemon/commit/2674157) xrandr-applet: non utilizzare colori harcoded per le etichette nel menù
* [2ae546b](https://github.com/mate-desktop/mate-settings-daemon/commit/2ae546b) supportato il background fallback su HiDPI
* [b60a6c8](https://github.com/mate-desktop/mate-settings-daemon/commit/b60a6c8) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [d036879](https://github.com/mate-desktop/mate-settings-daemon/commit/d036879) Evitato che i collegamenti ai tasti multimediali prevalgano sui tasti modificatori
* [705b5d1](https://github.com/mate-desktop/mate-settings-daemon/commit/705b5d1) Scalare correttamente le dimensioni dell'OSD sui display HiDPI (#212)
* [3e6987b](https://github.com/mate-desktop/mate-settings-daemon/commit/3e6987b) aggiunto il supporto a Travis-Cl
* [77eb37d](https://github.com/mate-desktop/mate-settings-daemon/commit/77eb37d) disabilitati i warning di deprecazione per distcheck
* [01c346f](https://github.com/mate-desktop/mate-settings-daemon/commit/01c346f) sincronizzazione con transifex
* [c54a0a2](https://github.com/mate-desktop/mate-settings-daemon/commit/c54a0a2) aggiornati i requisiti per mate-desktop
* [bbbc909](https://github.com/mate-desktop/mate-settings-daemon/commit/bbbc909) Resa opzionale l'impostazione QT_SCALE_FACTOR.
* [4efc6a4](https://github.com/mate-desktop/mate-settings-daemon/commit/4efc6a4) supportato il background fallback su HiDPI
* [a996cd9](https://github.com/mate-desktop/mate-settings-daemon/commit/a996cd9) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [b5cb3e0](https://github.com/mate-desktop/mate-settings-daemon/commit/b5cb3e0) Evitato che i collegamenti ai tasti multimediali prevalgano sui tasti modificatori
* [982a89b](https://github.com/mate-desktop/mate-settings-daemon/commit/982a89b) Scalare correttamente le dimensioni dell'OSD sui display HiDPI (#212)

### mate-system-monitor
* [ee025a6](https://github.com/mate-desktop/mate-system-monitor/commit/ee025a6) Abilitato Travis Cl per tutti i rami
* [0523541](https://github.com/mate-desktop/mate-system-monitor/commit/0523541) Inizializzato il supporto a Travis Cl
* [2eec5c4](https://github.com/mate-desktop/mate-system-monitor/commit/2eec5c4) Assicurata la corretta traduzione del titolo della finestra di dialogo informazioni
* [acd6123](https://github.com/mate-desktop/mate-system-monitor/commit/acd6123) Testo della Licenza nella finestra di dialogo informazioni
* [9fa6ae5](https://github.com/mate-desktop/mate-system-monitor/commit/9fa6ae5) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [0cd2493](https://github.com/mate-desktop/mate-system-monitor/commit/0cd2493) Aggiornato lo screenshot in Catalano
* [779f22e](https://github.com/mate-desktop/mate-system-monitor/commit/779f22e) Help - valori preimpostati prioritari, incluso il valore personalizzato
* [12959ae](https://github.com/mate-desktop/mate-system-monitor/commit/12959ae) procman: evitata la deprecata 'g_settings_list_keys'
* [b359baf](https://github.com/mate-desktop/mate-system-monitor/commit/b359baf) disabilitati i warning di deprecazione per distcheck
* [b991397](https://github.com/mate-desktop/mate-system-monitor/commit/b991397) spostato appdata nella cartella metainfo
* [8b1c92d](https://github.com/mate-desktop/mate-system-monitor/commit/8b1c92d) interface: evitata la deprecata gtk_menu_popup
* [7ecf16d](https://github.com/mate-desktop/mate-system-monitor/commit/7ecf16d) evitato il warning in compilazione per g_type_class_add_private
* [ad26a19](https://github.com/mate-desktop/mate-system-monitor/commit/ad26a19) Corretto un errore di grammatica e l'etichetta dell'interfaccia grafica
* [3575449](https://github.com/mate-desktop/mate-system-monitor/commit/3575449) utilizzate funzioni make per HELP_LINGUAS
* [515a338](https://github.com/mate-desktop/mate-system-monitor/commit/515a338) sincronizzazione con transifex
* [d182b1c](https://github.com/mate-desktop/mate-system-monitor/commit/d182b1c) versione pre-aggiornamento
* [5b1f551](https://github.com/mate-desktop/mate-system-monitor/commit/5b1f551) corretto il crash sui sistemi con pid 0
* [f411042](https://github.com/mate-desktop/mate-system-monitor/commit/f411042) aggiornato il materiale per le traduzioni
* [cd4f735](https://github.com/mate-desktop/mate-system-monitor/commit/cd4f735) Corretto il testo dell'intervallo di aggiornamento nella scheda risorse
* [7688aa2](https://github.com/mate-desktop/mate-system-monitor/commit/7688aa2) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [36bcd30](https://github.com/mate-desktop/mate-system-monitor/commit/36bcd30) evitata la deprecata GtkStock
* [386aac5](https://github.com/mate-desktop/mate-system-monitor/commit/386aac5) aggiunto il supporto a Travis-Cl
* [5a0ab35](https://github.com/mate-desktop/mate-system-monitor/commit/5a0ab35) Aggiornato lo screenshot in Catalano
* [b12ad42](https://github.com/mate-desktop/mate-system-monitor/commit/b12ad42)  Help - valori preimpostati prioritari, incluso il valore personalizzato
* [2bf87c9](https://github.com/mate-desktop/mate-system-monitor/commit/2bf87c9) disabilitati i warning di deprecazione per distcheck
* [b78db67](https://github.com/mate-desktop/mate-system-monitor/commit/b78db67) spostato appdata nella cartella metainfo
* [a0f01c5](https://github.com/mate-desktop/mate-system-monitor/commit/a0f01c5) Corretto un errore di grammatica e l'etichetta dell'interfaccia grafica
* [05fd8e6](https://github.com/mate-desktop/mate-system-monitor/commit/05fd8e6) utilizzate funzioni make per HELP_LINGUAS
* [533eeba](https://github.com/mate-desktop/mate-system-monitor/commit/533eeba) sincronizzazione con transifex
* [103d530](https://github.com/mate-desktop/mate-system-monitor/commit/103d530) corretto il crash sui sistemi con pid 0
* [d8673c6](https://github.com/mate-desktop/mate-system-monitor/commit/d8673c6) aggiornato il materiale per le traduzioni
* [9e4476e](https://github.com/mate-desktop/mate-system-monitor/commit/9e4476e) Corretto il testo dell'intervallo di aggiornamento nella scheda risorse
* [892030f](https://github.com/mate-desktop/mate-system-monitor/commit/892030f) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-terminal
* [4bd3e7c](https://github.com/mate-desktop/mate-terminal/commit/4bd3e7c) Abilitato Travis Cl per tutti i rami
* [b3ed723](https://github.com/mate-desktop/mate-terminal/commit/b3ed723) Inizializzato il supporto a Travis Cl
* [d30504d](https://github.com/mate-desktop/mate-terminal/commit/d30504d) Rimossi dei file inutilizzati nella directory dell'aiuto
* [a15f737](https://github.com/mate-desktop/mate-terminal/commit/a15f737) Rimossi i file generati
* [7fc129f](https://github.com/mate-desktop/mate-terminal/commit/7fc129f) Aggiunto update-authors.pl che aiuta ad aggiornare terminal.about
* [fb2f2e8](https://github.com/mate-desktop/mate-terminal/commit/fb2f2e8) Aggiornato authors
* [7ab20eb](https://github.com/mate-desktop/mate-terminal/commit/7ab20eb) Aggiornato Documenters
* [550b622](https://github.com/mate-desktop/mate-terminal/commit/550b622) eliminato il supporto umtp
* [69f4814](https://github.com/mate-desktop/mate-terminal/commit/69f4814) Help - Titolo della finestra quando MATE Terminal è avviato la prima volta
* [d07810d](https://github.com/mate-desktop/mate-terminal/commit/d07810d) Help - testo alternativo per l'immagine della finestra a schede
* [b0c0b20](https://github.com/mate-desktop/mate-terminal/commit/b0c0b20) Help - TERM=xterm-256color
* [f4bb742](https://github.com/mate-desktop/mate-terminal/commit/f4bb742) eggsmclient: evitata la deprecata 'g_type_class_add_private'
* [29536a9](https://github.com/mate-desktop/mate-terminal/commit/29536a9) src/terminal-screen.c: impostato  TERM a 'xterm-256color' (invece che semplicemente 'xterm'). Questo fornisce il supporto dell'applicazione di terminale con 256 colori.
* [000df06](https://github.com/mate-desktop/mate-terminal/commit/000df06) spostato appdata nella cartella metainfo
* [b226aa4](https://github.com/mate-desktop/mate-terminal/commit/b226aa4) disabilitati i warning di deprecazione per distcheck
* [3a145a7](https://github.com/mate-desktop/mate-terminal/commit/3a145a7) terminal-profile: Corretti dei memory leak
* [3ff3f27](https://github.com/mate-desktop/mate-terminal/commit/3ff3f27) terminal-screen: evitata la deprecata 'g_settings_list_schemas'
* [2260170](https://github.com/mate-desktop/mate-terminal/commit/2260170) utilizzate funzioni make per HELP_LINGUAS
* [d6efb07](https://github.com/mate-desktop/mate-terminal/commit/d6efb07) Sostituito Dokumentationsprojekt con Documentation Project
* [9081ba9](https://github.com/mate-desktop/mate-terminal/commit/9081ba9) terminal-window: corretti i warning con il menù a comparsa
* [7958d12](https://github.com/mate-desktop/mate-terminal/commit/7958d12) terminal-window: sostituita la deprecata gtk_menu_popup
* [7b6ba04](https://github.com/mate-desktop/mate-terminal/commit/7b6ba04) sincronizzazione con transifex
* [078d0b1](https://github.com/mate-desktop/mate-terminal/commit/078d0b1) term-screen: evitata la deprecata 'gtk_style_context_get_background_color'
* [7708278](https://github.com/mate-desktop/mate-terminal/commit/7708278) terminal-screen: evitata la deprecata 'vte_terminal_spawn_sync'
* [82e48ff](https://github.com/mate-desktop/mate-terminal/commit/82e48ff) terminal-window: evitata la deprecata 'vte_terminal_copy_clipboard'
* [a25437c](https://github.com/mate-desktop/mate-terminal/commit/a25437c) versione pre-aggiornamento
* [c4cedf7](https://github.com/mate-desktop/mate-terminal/commit/c4cedf7) Ripristinare "corretta l'impostazione della trasparenza quando viene utilizzato in GNOME3"
* [54558c5](https://github.com/mate-desktop/mate-terminal/commit/54558c5) terminal-window: Correzione: saturato il demone dbus della sessione
* [e1b834a](https://github.com/mate-desktop/mate-terminal/commit/e1b834a) corretta l'impostazione della trasparenza quando viene utilizzato in GNOME3
* [dbea928](https://github.com/mate-desktop/mate-terminal/commit/dbea928) impostata la percentuale_minima ed il tipo nel file di configurazione
* [43897cf](https://github.com/mate-desktop/mate-terminal/commit/43897cf) terminal-app: evitata gtk_dialog_add_buttons con gli identificativi stock
* [90f1e19](https://github.com/mate-desktop/mate-terminal/commit/90f1e19) evitata la deprecata GtkStock
* [2910ba6](https://github.com/mate-desktop/mate-terminal/commit/2910ba6) aggiunto il supporto a Travis-Cl
* [a1bab86](https://github.com/mate-desktop/mate-terminal/commit/a1bab86) Help - Titolo della finestra quando MATE Terminal è avviato la prima volta
* [4c24f9c](https://github.com/mate-desktop/mate-terminal/commit/4c24f9c) Help - testo alternativo per l'immagine della finestra a schede
* [8084ec4](https://github.com/mate-desktop/mate-terminal/commit/8084ec4) Help - TERM=xterm-256color
* [4f89d21](https://github.com/mate-desktop/mate-terminal/commit/4f89d21) src/terminal-screen.c: impostato TERM a 'xterm-256color' (invece che semplicemente 'xterm'). Questo fornisce il supporto dell'applicazione di terminale con 256 colori.
* [82c02f8](https://github.com/mate-desktop/mate-terminal/commit/82c02f8) spostato appdata nella cartella metainfo
* [acf0c5d](https://github.com/mate-desktop/mate-terminal/commit/acf0c5d) disabilitati i warning di deprecazione per distcheck
* [ac89c5a](https://github.com/mate-desktop/mate-terminal/commit/ac89c5a) utilizzate funzioni make per HELP_LINGUAS
* [ccb0007](https://github.com/mate-desktop/mate-terminal/commit/ccb0007) Sostituito Dokumentationsprojekt con Documentation Project
* [9edc6bc](https://github.com/mate-desktop/mate-terminal/commit/9edc6bc) sincronizzazione con transifex
* [02d300b](https://github.com/mate-desktop/mate-terminal/commit/02d300b) terminal-window: Correzione: saturato il demone dbus della sessione
* [b84724d](https://github.com/mate-desktop/mate-terminal/commit/b84724d) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-user-guide
* [a1f2703](https://github.com/mate-desktop/mate-user-guide/commit/a1f2703) Corretta la versione a 1.22
* [25ffe55](https://github.com/mate-desktop/mate-user-guide/commit/25ffe55) help: aggiornato il copyright
* [ee873c2](https://github.com/mate-desktop/mate-user-guide/commit/ee873c2) Aggiornato il manuale a docbook 5.0
* [5377ea8](https://github.com/mate-desktop/mate-user-guide/commit/5377ea8) Abilitato Travis Cl per tutti i rami
* [c5a6aa9](https://github.com/mate-desktop/mate-user-guide/commit/c5a6aa9) Inizializzato il supporto a Travis Cl
* [8d2d856](https://github.com/mate-desktop/mate-user-guide/commit/8d2d856) ritradotta la lingua Turca
* [a87c7ca](https://github.com/mate-desktop/mate-user-guide/commit/a87c7ca) sincronizzazione con transifex
* [4a8dbc8](https://github.com/mate-desktop/mate-user-guide/commit/4a8dbc8) aggiunto autogen.sh ad Extra_dist
* [5c87f57](https://github.com/mate-desktop/mate-user-guide/commit/5c87f57) sincronizzazione con transifex
* [de07670](https://github.com/mate-desktop/mate-user-guide/commit/de07670) utilizzate funzioni make per HELP_LINGUAS
* [408b7c8](https://github.com/mate-desktop/mate-user-guide/commit/408b7c8) aggiornate le istruzioni per modificare le scorciatoie da tastiera
* [5e2b4c3](https://github.com/mate-desktop/mate-user-guide/commit/5e2b4c3) aggiunta una scorciatoia da tastiera per mostrare i file nascosti
* [fed78ef](https://github.com/mate-desktop/mate-user-guide/commit/fed78ef) Sistemi senza profili dconf
* [3fcf0e2](https://github.com/mate-desktop/mate-user-guide/commit/3fcf0e2) sistema di archiviazione delle impostazioni dconf
* [f744124](https://github.com/mate-desktop/mate-user-guide/commit/f744124) transifex: aggiornato /mate-user-guide/mate-user-guide.pot
* [33fea23](https://github.com/mate-desktop/mate-user-guide/commit/33fea23) rimosso il carattere in più
* [acb4d76](https://github.com/mate-desktop/mate-user-guide/commit/acb4d76) GNOME Media è deprecato: rimuovere gstreamer-properties
* [1ab5f83](https://github.com/mate-desktop/mate-user-guide/commit/1ab5f83) Sostituito Dokumentationsprojekt con Documentation Project
* [ac6c437](https://github.com/mate-desktop/mate-user-guide/commit/ac6c437) Filesystem virtuale nei sistemi operativi Unix-like
* [4b9848a](https://github.com/mate-desktop/mate-user-guide/commit/4b9848a) Rimosso il punto (carattere) alla fine del titolo 
* [89f3ec6](https://github.com/mate-desktop/mate-user-guide/commit/89f3ec6) Rimossi gli screenshot non utilizzati
* [e4e988b](https://github.com/mate-desktop/mate-user-guide/commit/e4e988b) Aggiunto lo screenshot in Catalano - caja_restore_saved_search
* [265982e](https://github.com/mate-desktop/mate-user-guide/commit/265982e) Aggiunto lo screenshot in Catalano - caja_always_use_browser.png
* [4910cce](https://github.com/mate-desktop/mate-user-guide/commit/4910cce) corretti errori di ortografia e grammatica
* [c6b20b5](https://github.com/mate-desktop/mate-user-guide/commit/c6b20b5) Rimossa menu_panel.png
* [a5fa736](https://github.com/mate-desktop/mate-user-guide/commit/a5fa736) Mostrato il logo MATE nel pannello del menù
* [f7d047a](https://github.com/mate-desktop/mate-user-guide/commit/f7d047a) corretta l'installazione
* [95b316d](https://github.com/mate-desktop/mate-user-guide/commit/95b316d) versione pre-aggiornamento
* [e877fe8](https://github.com/mate-desktop/mate-user-guide/commit/e877fe8) Ridimensionato lo screenshot
* [ef40ed2](https://github.com/mate-desktop/mate-user-guide/commit/ef40ed2) La modalità browser è la predefinita in MATE
* [816f751](https://github.com/mate-desktop/mate-user-guide/commit/816f751) Aggiunti gli screenshot in Catalano
* [c2d1876](https://github.com/mate-desktop/mate-user-guide/commit/c2d1876) Corretto il titolo dell'illustrazione - barra di ricerca
* [af75d38](https://github.com/mate-desktop/mate-user-guide/commit/af75d38) sincronizzazione con transifex
* [f49bb03](https://github.com/mate-desktop/mate-user-guide/commit/f49bb03) versione pre-aggiornamento
* [2646a7c](https://github.com/mate-desktop/mate-user-guide/commit/2646a7c) transifex: aggiunto mate-user-guide-content
* [baf7c04](https://github.com/mate-desktop/mate-user-guide/commit/baf7c04) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [cdf9782](https://github.com/mate-desktop/mate-user-guide/commit/cdf9782) aggiunto il supporto a Travis-Cl
* [7cc5593](https://github.com/mate-desktop/mate-user-guide/commit/7cc5593) sincronizzazione con transifex
* [27854eb](https://github.com/mate-desktop/mate-user-guide/commit/27854eb) sincronizzazione con transifex
* [cc43baf](https://github.com/mate-desktop/mate-user-guide/commit/cc43baf) aggiunto autogen.sh ad Extra_dist
* [f90d157](https://github.com/mate-desktop/mate-user-guide/commit/f90d157) utilizzate funzioni make per HELP_LINGUAS
* [c2750bb](https://github.com/mate-desktop/mate-user-guide/commit/c2750bb) aggiornate le istruzioni per modificare le scorciatoie da tastiera
* [225e736](https://github.com/mate-desktop/mate-user-guide/commit/225e736) aggiunta una scorciatoia da tastiera per mostrare i file nascosti
* [cd1e5e1](https://github.com/mate-desktop/mate-user-guide/commit/cd1e5e1) Sistemi senza profili dconf
* [a7fc8df](https://github.com/mate-desktop/mate-user-guide/commit/a7fc8df) sistema di archiviazione delle impostazioni dconf
* [6a21e17](https://github.com/mate-desktop/mate-user-guide/commit/6a21e17) rimosso il carattere in più
* [4deb4a8](https://github.com/mate-desktop/mate-user-guide/commit/4deb4a8) GNOME Media è deprecato: rimuovere gstreamer-properties
* [1693760](https://github.com/mate-desktop/mate-user-guide/commit/1693760) Sostituito Dokumentationsprojekt con Documentation Project
* [67e0411](https://github.com/mate-desktop/mate-user-guide/commit/67e0411) Filesystem virtuale nei sistemi operativi Unix-like
* [ca99a5c](https://github.com/mate-desktop/mate-user-guide/commit/ca99a5c) Rimosso il punto (carattere) alla fine del titolo 
* [f1a6c23](https://github.com/mate-desktop/mate-user-guide/commit/f1a6c23) Rimossi gli screenshot non utilizzati
* [69f9195](https://github.com/mate-desktop/mate-user-guide/commit/69f9195) Aggiunto lo screenshot in Catalano - caja_restore_saved_search
* [44b7e77](https://github.com/mate-desktop/mate-user-guide/commit/44b7e77) Aggiunto lo screenshot in Catalano - caja_always_use_browser.png
* [98ade62](https://github.com/mate-desktop/mate-user-guide/commit/98ade62) corretti errori di ortografia e grammatica
* [d886cf5](https://github.com/mate-desktop/mate-user-guide/commit/d886cf5) Rimossa menu_panel.png
* [b8ddf92](https://github.com/mate-desktop/mate-user-guide/commit/b8ddf92) Mostrato il logo MATE nel pannello del menù
* [35012e9](https://github.com/mate-desktop/mate-user-guide/commit/35012e9) corretta l'installazione
* [8e749aa](https://github.com/mate-desktop/mate-user-guide/commit/8e749aa) Ridimensionato lo screenshot
* [e386194](https://github.com/mate-desktop/mate-user-guide/commit/e386194) La modalità browser è la predefinita in MATE
* [72b3f44](https://github.com/mate-desktop/mate-user-guide/commit/72b3f44) Aggiunti gli screenshot in Catalano
* [db82577](https://github.com/mate-desktop/mate-user-guide/commit/db82577) Corretto il titolo dell'illustrazione - barra di ricerca
* [f2ff3cc](https://github.com/mate-desktop/mate-user-guide/commit/f2ff3cc) corretto LINGUAS
* [787d11a](https://github.com/mate-desktop/mate-user-guide/commit/787d11a) user-guide-content: corretti alcuni di errori di sintassi xml
* [3b8dd88](https://github.com/mate-desktop/mate-user-guide/commit/3b8dd88) sincronizzazione con transifex
* [3a78834](https://github.com/mate-desktop/mate-user-guide/commit/3a78834) transifex: aggiunto mate-user-guide-content
* [446141e](https://github.com/mate-desktop/mate-user-guide/commit/446141e) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-user-share
* [626657a](https://github.com/mate-desktop/mate-user-share/commit/626657a) utilizzato lo stesso file legal.xml
* [b52e5e5](https://github.com/mate-desktop/mate-user-share/commit/b52e5e5) Inizializzato il supporto a Travis Cl
* [064c2ba](https://github.com/mate-desktop/mate-user-share/commit/064c2ba) caja-share-bar: evitata la deprecata 'g_type_class_add_private'
* [4602ece](https://github.com/mate-desktop/mate-user-share/commit/4602ece) eliminata in distcheck un'opzione di configure obsoleta
* [9ecc673](https://github.com/mate-desktop/mate-user-share/commit/9ecc673) utilizzate funzioni make per HELP_LINGUAS
* [5545476](https://github.com/mate-desktop/mate-user-share/commit/5545476) disabilitati i warning di deprecazione per distcheck
* [8fd39d4](https://github.com/mate-desktop/mate-user-share/commit/8fd39d4) file-share-properties.ui: evitate le deprecate:
* [4e4027f](https://github.com/mate-desktop/mate-user-share/commit/4e4027f) versione pre-aggiornamento
* [6506a3b](https://github.com/mate-desktop/mate-user-share/commit/6506a3b) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [1c7aea8](https://github.com/mate-desktop/mate-user-share/commit/1c7aea8) aggiunto il supporto a Travis-Cl
* [c1ec1ac](https://github.com/mate-desktop/mate-user-share/commit/c1ec1ac) eliminata in distcheck un'opzione di configure obsoleta
* [e48d551](https://github.com/mate-desktop/mate-user-share/commit/e48d551) utilizzate funzioni make per HELP_LINGUAS
* [0d75dab](https://github.com/mate-desktop/mate-user-share/commit/0d75dab) disabilitati i warning di deprecazione per distcheck
* [fc934b7](https://github.com/mate-desktop/mate-user-share/commit/fc934b7) sincronizzazione con transifex
* [6bfba36](https://github.com/mate-desktop/mate-user-share/commit/6bfba36) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mate-utils
* [0dd612b](https://github.com/mate-desktop/mate-utils/commit/0dd612b) Inizializzato il supporto a Travis Cl
* [f2c1234](https://github.com/mate-desktop/mate-utils/commit/f2c1234) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [879a0cf](https://github.com/mate-desktop/mate-utils/commit/879a0cf) ri-abilitate le traduzioni per ca@valencia
* [a6a07e7](https://github.com/mate-desktop/mate-utils/commit/a6a07e7) help - aggiornare dockbook 4.5
* [7f71199](https://github.com/mate-desktop/mate-utils/commit/7f71199) eggsmclient: evitata la deprecata 'g_type_class_add_private'
* [846b61f](https://github.com/mate-desktop/mate-utils/commit/846b61f) spostato appdata nella cartella metainfo
* [e57612b](https://github.com/mate-desktop/mate-utils/commit/e57612b) search-tool: disabilitate le traduzioni per ca@valencia
* [39a73e9](https://github.com/mate-desktop/mate-utils/commit/39a73e9) disabilitati i warning di deprecazione per distcheck
* [0c174e7](https://github.com/mate-desktop/mate-utils/commit/0c174e7) utilizzate funzioni make per HELP_LINGUAS
* [eeccbf6](https://github.com/mate-desktop/mate-utils/commit/eeccbf6) Tx: semplificare la generazione dei sorgenti e aggiornarli
* [6f9f947](https://github.com/mate-desktop/mate-utils/commit/6f9f947) Sostituito Dokumentationsprojekt con Documentation Project
* [2f8d89d](https://github.com/mate-desktop/mate-utils/commit/2f8d89d) mate-dictionary: Corretto un memory leak
* [6333405](https://github.com/mate-desktop/mate-utils/commit/6333405) corretti errori di ortografia e grammatica
* [d58400c](https://github.com/mate-desktop/mate-utils/commit/d58400c) search-tool: sostituita la deprecata gtk_menu_popup
* [fec8113](https://github.com/mate-desktop/mate-utils/commit/fec8113) screenshot: sostituita la deprecata gtk_flush
* [8f7ec5e](https://github.com/mate-desktop/mate-utils/commit/8f7ec5e) dictionary: sostituita la deprecata gtk_flush
* [3a9e118](https://github.com/mate-desktop/mate-utils/commit/3a9e118) dictionary: sostituita la deprecata gtk_menu_popup
* [c0800ef](https://github.com/mate-desktop/mate-utils/commit/c0800ef) dictionary: Sostituiti gli accessori deprecati di GtkFontButton
* [1a5e0dd](https://github.com/mate-desktop/mate-utils/commit/1a5e0dd) disk-usage-analyzer: sostituita la deprecata gtk_menu_popup
* [360512a](https://github.com/mate-desktop/mate-utils/commit/360512a) Aggiornati gli screenshot di mate-dictionary
* [ecb6203](https://github.com/mate-desktop/mate-utils/commit/ecb6203) Aggiunti gli screenshot in Catalano
* [9d98cf2](https://github.com/mate-desktop/mate-utils/commit/9d98cf2) Baobab help: Comando da terminale aggiornato a 'mate-disk-usage-analyzer'
* [8f04ddd](https://github.com/mate-desktop/mate-utils/commit/8f04ddd) baobab-chart: evitata la deprecata 'gtk_style_context_set_background'
* [5fbfca9](https://github.com/mate-desktop/mate-utils/commit/5fbfca9) gsearchtool: evitata la deprecata 'gtk_window_set_wmclass'
* [3c72131](https://github.com/mate-desktop/mate-utils/commit/3c72131) sincronizzazione con transifex
* [a613d00](https://github.com/mate-desktop/mate-utils/commit/a613d00) versione pre-aggiornamento
* [5cfaaf3](https://github.com/mate-desktop/mate-utils/commit/5cfaaf3) Aggiunto il supporto per gli screenshot non interattivi direttamente negli appunti
* [7f98287](https://github.com/mate-desktop/mate-utils/commit/7f98287) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [70a6011](https://github.com/mate-desktop/mate-utils/commit/70a6011) evitata la deprecata GtkStock
* [1e9dbc5](https://github.com/mate-desktop/mate-utils/commit/1e9dbc5) aggiunto il supporto a Travis-Cl
* [473550f](https://github.com/mate-desktop/mate-utils/commit/473550f) ri-abilitate le traduzioni per ca@valencia
* [4b6a269](https://github.com/mate-desktop/mate-utils/commit/4b6a269) help - aggiornare dockbook 4.5
* [a183245](https://github.com/mate-desktop/mate-utils/commit/a183245) spostato appdata nella cartella metainfo
* [98499a0](https://github.com/mate-desktop/mate-utils/commit/98499a0) search-tool: disabilitate le traduzioni per ca@valencia
* [106f3e7](https://github.com/mate-desktop/mate-utils/commit/106f3e7) disabilitati i warning di deprecazione per distcheck
* [8c38ae6](https://github.com/mate-desktop/mate-utils/commit/8c38ae6) utilizzate funzioni make per HELP_LINGUAS
* [c4dc6a6](https://github.com/mate-desktop/mate-utils/commit/c4dc6a6) Sostituito Dokumentationsprojekt con Documentation Project
* [443e6fa](https://github.com/mate-desktop/mate-utils/commit/443e6fa) corretti errori di ortografia e grammatica
* [78cd274](https://github.com/mate-desktop/mate-utils/commit/78cd274) Aggiunti gli screenshot in Catalano
* [c4875f6](https://github.com/mate-desktop/mate-utils/commit/c4875f6) sincronizzazione con transifex
* [9a7733d](https://github.com/mate-desktop/mate-utils/commit/9a7733d) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### mozo
* [ffe5e71](https://github.com/mate-desktop/mozo/commit/ffe5e71) Corretta la creazione di nuovi menù ed oggetti
* [30caedb](https://github.com/mate-desktop/mozo/commit/30caedb) Corretto il movimento di un menù che corrompe il menù
* [ae480e9](https://github.com/mate-desktop/mozo/commit/ae480e9) Corretta la voce di menù che non può essere spostata
* [ae538cd](https://github.com/mate-desktop/mozo/commit/ae538cd) Abilitato Travis Cl per tutti i rami
* [d8590dc](https://github.com/mate-desktop/mozo/commit/d8590dc) Inizializzato il supporto a Travis Cl
* [2bb36d0](https://github.com/mate-desktop/mozo/commit/2bb36d0) disabilitati i warning di deprecazione per distcheck
* [2512b76](https://github.com/mate-desktop/mozo/commit/2512b76) sincronizzazione con transifex
* [04cfe51](https://github.com/mate-desktop/mozo/commit/04cfe51) aggiornato mozo.pot
* [a9fb1f7](https://github.com/mate-desktop/mozo/commit/a9fb1f7) eliminato acinclude.m4 che non è più necessario
* [af19983](https://github.com/mate-desktop/mozo/commit/af19983) supportata la nuova api mate-menus
* [80873ff](https://github.com/mate-desktop/mozo/commit/80873ff) re-indentato il codice python
* [eb798b5](https://github.com/mate-desktop/mozo/commit/eb798b5) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione 
* [cc744aa](https://github.com/mate-desktop/mozo/commit/cc744aa) Corretto il trascinamento dei menù
* [7c03832](https://github.com/mate-desktop/mozo/commit/7c03832) aggiunto il supporto a travis-Cl
* [10f3924](https://github.com/mate-desktop/mozo/commit/10f3924) disabilitati i warning di deprecazione per distcheck
* [4737e00](https://github.com/mate-desktop/mozo/commit/4737e00) sincronizzazione con transifex
* [dbae4a6](https://github.com/mate-desktop/mozo/commit/dbae4a6) impostata la percentuale_minima ed il tipo nel file di configurazione

### pluma
* [cfe2c64](https://github.com/mate-desktop/pluma/commit/cfe2c64) help: aggiornato il copyright
* [396fe5a](https://github.com/mate-desktop/pluma/commit/396fe5a) Utilizzato ITS nell'info dell'articolo di docbook, convalidato con schemi dbits
* [82638e2](https://github.com/mate-desktop/pluma/commit/82638e2) Aggiornato il manuale a docbook 5.0
* [fddace2](https://github.com/mate-desktop/pluma/commit/fddace2) Aggiunto lo script update-authors.pl che aiuta ad aggiornare pluma.about
* [a56d506](https://github.com/mate-desktop/pluma/commit/a56d506) Leggere authors (aggiornato) dal file pluma.about
* [e27a451](https://github.com/mate-desktop/pluma/commit/e27a451) mostrare la versione enchant quando si esegue configure
* [73e0a82](https://github.com/mate-desktop/pluma/commit/73e0a82) sostituita la deprecata enchant_dict_add_to_pwl con enchant_dict_add.
* [87df43f](https://github.com/mate-desktop/pluma/commit/87df43f) corretto l'errore della mancata compilazione su Archlinux
* [1d86958](https://github.com/mate-desktop/pluma/commit/1d86958) Reso traducibile documenters nella finestra di dialogo Informazioni
* [861db5e](https://github.com/mate-desktop/pluma/commit/861db5e) Assicurata la corretta traduzione del titolo della finestra di dialogo informazioni
* [e4f88d7](https://github.com/mate-desktop/pluma/commit/e4f88d7) supporto a travis iniziale
* [068a1b7](https://github.com/mate-desktop/pluma/commit/068a1b7) Aggiunto il pulsante Licenza nella finestra di dialogo informazioni su Pluma 
* [6cdce0a](https://github.com/mate-desktop/pluma/commit/6cdce0a) Reso traducibile il copyright nella finestra di dialogo Informazioni
* [7c519e1](https://github.com/mate-desktop/pluma/commit/7c519e1) Aggiornato documenters
* [8e08ede](https://github.com/mate-desktop/pluma/commit/8e08ede) rimossi tipo e url attr di ulink nella traduzione
* [f64c037](https://github.com/mate-desktop/pluma/commit/f64c037) rimossa la sezione di aiuto deprecata: Aprire un file da un URI
* [68fc438](https://github.com/mate-desktop/pluma/commit/68fc438) eggsmclient: evitata la deprecata 'g_type_class_add_private'
* [2b00f65](https://github.com/mate-desktop/pluma/commit/2b00f65) indirizzi #391 - prendere la dimensione della finestra prima di distruggerla
* [71daf90](https://github.com/mate-desktop/pluma/commit/71daf90) semplice correzione di un bug dovuto a un underscore mal posizionato
* [94b3061](https://github.com/mate-desktop/pluma/commit/94b3061) disabilitati i warning di deprecazione per distcheck
* [eb0cc59](https://github.com/mate-desktop/pluma/commit/eb0cc59) spostato appdata nella cartella metainfo
* [f8a009b](https://github.com/mate-desktop/pluma/commit/f8a009b) pluma-utils:  Corretto un memory leak
* [e8cbd69](https://github.com/mate-desktop/pluma/commit/e8cbd69) pluma-window: corretti i memory leak
* [b29b045](https://github.com/mate-desktop/pluma/commit/b29b045) sincronizzazione con transifex
* [effba35](https://github.com/mate-desktop/pluma/commit/effba35) utilizzato lo stesso file legal.xml
* [81b480b](https://github.com/mate-desktop/pluma/commit/81b480b) utilizzate funzioni make per HELP_LINGUAS
* [4ba0265](https://github.com/mate-desktop/pluma/commit/4ba0265) Fare riferimento alla pagina man strftime(3) per maggiori informazioni...
* [c4cec0e](https://github.com/mate-desktop/pluma/commit/c4cec0e) Fare riferimento alla pagina man pluma(1) per maggiori informazioni...
* [2cd75f9](https://github.com/mate-desktop/pluma/commit/2cd75f9) rimossi gli screenshot inutilizzati
* [50c3b34](https://github.com/mate-desktop/pluma/commit/50c3b34) corretti errori di ortografia e grammatica
* [559328b](https://github.com/mate-desktop/pluma/commit/559328b) help: corretti i collegamenti di aiuto
* [763cc8c](https://github.com/mate-desktop/pluma/commit/763cc8c) Utilizzato lo screenshot attuale di pluma per la lingua Catalana
* [b6220de](https://github.com/mate-desktop/pluma/commit/b6220de) Utilizzato lo screenshot di pluma corrente 
* [ed8910b](https://github.com/mate-desktop/pluma/commit/ed8910b) corretti errori di ortografia e grammatica
* [7e110fa](https://github.com/mate-desktop/pluma/commit/7e110fa) prefs-manager: silenziati alcuni warning di compilazione
* [18eb46c](https://github.com/mate-desktop/pluma/commit/18eb46c) corretti alcuni warning di introspezione e di documentazione
* [239f0d3](https://github.com/mate-desktop/pluma/commit/239f0d3) corretta la ricerca all'indietro con regex
* [813e1ff](https://github.com/mate-desktop/pluma/commit/813e1ff) pluma-document: corretto un possibile memory leak
* [4d26225](https://github.com/mate-desktop/pluma/commit/4d26225) pluma-view: Correzione: non perdere il PRIMARY clipboard
* [4a74dc6](https://github.com/mate-desktop/pluma/commit/4a74dc6) pluma-document: Correzione: non andare in crash quando si utilizzano file con 'bom'
* [bc64980](https://github.com/mate-desktop/pluma/commit/bc64980) resa più grande la 'finestra di dialogo conferma di chiusura' con più file
* [b52da1a](https://github.com/mate-desktop/pluma/commit/b52da1a) pluma-view: Correzione: alternanza delle schede in modo inaspettato
* [320a44d](https://github.com/mate-desktop/pluma/commit/320a44d) close-confirmation-dialog: Correzione: non ridimensionare la finestra di dialogo in modo inaspettato
* [957fc58](https://github.com/mate-desktop/pluma/commit/957fc58) pluma-sort-plugin: evitata la riga vuota in più
* [ca00615](https://github.com/mate-desktop/pluma/commit/ca00615) pluma-view: corretti i font grassetto e corsivo nei menù
* [eb7a39b](https://github.com/mate-desktop/pluma/commit/eb7a39b) spell plugin: Controllo ortografico automatico con [control + F7]
* [03238f8](https://github.com/mate-desktop/pluma/commit/03238f8) aggiunta la possibilità di nascondere la prima scheda se c'è una sola scheda aperta
* [323d3a3](https://github.com/mate-desktop/pluma/commit/323d3a3) notebook: eliminata l'inutilizzata 'pluma_notebook_set_always_show_tabs'
* [06d6e5d](https://github.com/mate-desktop/pluma/commit/06d6e5d) pluma-view: corretto un possibile memory leak
* [d3757df](https://github.com/mate-desktop/pluma/commit/d3757df) pluma-view: utilizzate variabili statiche per cssprovider e per le impostazioni
* [b2ca8c4](https://github.com/mate-desktop/pluma/commit/b2ca8c4) pluma-view: sincronizzato il font nel menù contestuale con il valore nella chiave di gsettings
* [f952be3](https://github.com/mate-desktop/pluma/commit/f952be3) pluma-window: ci siamo assicurati che alcune risorse siano liberate
* [98edfd3](https://github.com/mate-desktop/pluma/commit/98edfd3) aggiunta la possibilità di alternare le schede utilizzando [ctrl+tab] e [ctrl+shift+tab]
* [9fa3649](https://github.com/mate-desktop/pluma/commit/9fa3649) pluma-view: corretto il font nel menù contestuale
* [e451bfe](https://github.com/mate-desktop/pluma/commit/e451bfe) pluma-view: pluma_override_font: aggiungere il provider soltanto una volta
* [8f3b1d6](https://github.com/mate-desktop/pluma/commit/8f3b1d6) pluma-view: Correzione: i font grassetto e corsivo non funzionano
* [c2dec6d](https://github.com/mate-desktop/pluma/commit/c2dec6d) sincronizzazione con transifex
* [be05278](https://github.com/mate-desktop/pluma/commit/be05278) pluma-utils.c: evitata la deprecata 'gdk_error_trap_push/pop'
* [924beb5](https://github.com/mate-desktop/pluma/commit/924beb5) pluma-notebook: evitato di aprire un nuovo file facendo doppio clic sulla barra di scorrimento verticale
* [3742ba4](https://github.com/mate-desktop/pluma/commit/3742ba4) pluma-notebook: evitato di aprire un nuovo file facendo doppio clic sul pulsante freccia avanti
* [f6f9fdc](https://github.com/mate-desktop/pluma/commit/f6f9fdc) pluma-notebook: Correzione: comportamento imprevisto con il drag and drop del testo selezionato
* [12e55b6](https://github.com/mate-desktop/pluma/commit/12e55b6) pluma-view: Correzione: comportamento imprevisto con il drag and drop sotto i numeri di linea
* [72edb5d](https://github.com/mate-desktop/pluma/commit/72edb5d) pluma-notebook: passare l'evento a gdk_seat_grab
* [28de7bc](https://github.com/mate-desktop/pluma/commit/28de7bc) pluma-window: utilizzato gtk_menu_popup_at_widget per GtkNotebook
* [8b793f4](https://github.com/mate-desktop/pluma/commit/8b793f4) pluma-utils: rimossa l'inutilizzata 'pluma_utils_menu_position_under_tree_view'
* [49f8520](https://github.com/mate-desktop/pluma/commit/49f8520) evitata la deprecata 'gtk_menu_popup'
* [4d80780](https://github.com/mate-desktop/pluma/commit/4d80780) pluma-print-preview: Correzione: comportamento bizzarro con i pulsanti del mouse
* [cced651](https://github.com/mate-desktop/pluma/commit/cced651) Correzione: Pluma va in crash se si utilizza la rotellina del mouse sopra una scheda
* [d6d1cdb](https://github.com/mate-desktop/pluma/commit/d6d1cdb) pluma-notebook.c: evitate le funzioni deprecate 'gdk_pointer_ ...'
* [7b7cd3f](https://github.com/mate-desktop/pluma/commit/7b7cd3f) pluma-notebook.c: evitata la deprecata 'gdk_window_at_pointer'
* [0bc141e](https://github.com/mate-desktop/pluma/commit/0bc141e) evitata la deprecata 'gtk_dialog_get_action_area'
* [310bfc2](https://github.com/mate-desktop/pluma/commit/310bfc2) pluma-view.c: evitata la deprecata 'gtk_widget_override_font'
* [a3dfb66](https://github.com/mate-desktop/pluma/commit/a3dfb66) evitata la deprecata 'gtk_font_button_set/get_font_name'
* [a28da51](https://github.com/mate-desktop/pluma/commit/a28da51) pluma-view.c: Correzione: migliorato "Mostra i numeri di riga" di GtkCheckMenuItem
* [7c692bd](https://github.com/mate-desktop/pluma/commit/7c692bd) pluma-file-browser-widget.c: evitata la deprecata GtkImageMenuItem
* [6ab8350](https://github.com/mate-desktop/pluma/commit/6ab8350) error-message-area: evitata 'gtk_info_bar_new_with_buttons' con gli identificativi stock
* [1eb3e78](https://github.com/mate-desktop/pluma/commit/1eb3e78) evitata 'gtk_info_bar_add_button' con gli identificativi stock
* [4c0af0c](https://github.com/mate-desktop/pluma/commit/4c0af0c) aggiornato potfile
* [4de5f87](https://github.com/mate-desktop/pluma/commit/4de5f87) evitata 'pluma_file_chooser_dialog_new' con gli identificativi stock
* [ac1a336](https://github.com/mate-desktop/pluma/commit/ac1a336) 'gtk_file_chooser_dialog_new' con gli identificativi stock
* [766c5b5](https://github.com/mate-desktop/pluma/commit/766c5b5) pluma-time-plugin.c: evitata 'gtk_dialog_new_with_buttons' con gli identificativi stock
* [15f06ce](https://github.com/mate-desktop/pluma/commit/15f06ce) evitata gtk_dialog_add_buttons con gli identificativi stock
* [3061bc9](https://github.com/mate-desktop/pluma/commit/3061bc9) spell-checker.ui plugin: evitate le deprecate:
* [ff705d7](https://github.com/mate-desktop/pluma/commit/ff705d7) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [92b4a13](https://github.com/mate-desktop/pluma/commit/92b4a13) sort.ui plugin: evitate le deprecate:
* [ea3be53](https://github.com/mate-desktop/pluma/commit/ea3be53) pluma-time-setup-dialog.ui plugin: evitate le deprecate:
* [6b9d287](https://github.com/mate-desktop/pluma/commit/6b9d287) pluma-time-dialog.ui plugin: evitate le deprecate:
* [d82591f](https://github.com/mate-desktop/pluma/commit/d82591f) corretto distcheck di make
* [3858a43](https://github.com/mate-desktop/pluma/commit/3858a43) alcune rifiniture per pluma-spell-setup-dialog.ui
* [f248f85](https://github.com/mate-desktop/pluma/commit/f248f85) pluma-spell-setup-dialog.ui plugin: evitata GtkRadioButton:xalign
* [e461fc8](https://github.com/mate-desktop/pluma/commit/e461fc8) pluma-search-dialog.ui: evitata la deprecata GtkButton:use-stock
* [904baaa](https://github.com/mate-desktop/pluma/commit/904baaa) pluma-preferences-dialog.ui: evitate GtkButton:use-stock e GtkImage:stock
* [a29f740](https://github.com/mate-desktop/pluma/commit/a29f740) pluma-encodings-dialog.ui: evitata la deprecata GtkButton:use-stock 
* [2b86db3](https://github.com/mate-desktop/pluma/commit/2b86db3) externaltools plugin: outputpanel.ui: evitate GtkHBox e GtkVButtonBox
* [028fb44](https://github.com/mate-desktop/pluma/commit/028fb44) spell plugin: languages-dialog.ui: evitate le deprecate:
* [b23add8](https://github.com/mate-desktop/pluma/commit/b23add8) docinfo.ui plugin: evitate GtkVBox, GtkHBox, GtkLabel:xpad/ypad e GtkTable
* [c43e5ef](https://github.com/mate-desktop/pluma/commit/c43e5ef) plugins: docinfo.ui: evitate GtkButton:use-stock e GtkImage:stock
* [6d7a076](https://github.com/mate-desktop/pluma/commit/6d7a076) spell plugin: pluma-spell-setup-dialog.ui: evitate le deprecate:
* [a674f90](https://github.com/mate-desktop/pluma/commit/a674f90) python console: config.ui: evitata la deprecata GtkButton:use-stock 
* [ed34d92](https://github.com/mate-desktop/pluma/commit/ed34d92) Le schede del notebook adesso sono scorrevoli
* [1d82cc7](https://github.com/mate-desktop/pluma/commit/1d82cc7) evitata la deprecata GtkButton:use-stock
* [12e54c4](https://github.com/mate-desktop/pluma/commit/12e54c4) Corretto un warning con il plugin di strumenti esterni
* [2217a02](https://github.com/mate-desktop/pluma/commit/2217a02) evitata la deprecata GtkStock
* [3309e0f](https://github.com/mate-desktop/pluma/commit/3309e0f) aggiunto il supporto a Travis-Cl
* [edae22f](https://github.com/mate-desktop/pluma/commit/edae22f) mostrare la versione enchant quando si esegue configure
* [433317a](https://github.com/mate-desktop/pluma/commit/433317a) sostituita la deprecata enchant_dict_add_to_pwl con enchant_dict_add.
* [50a3efc](https://github.com/mate-desktop/pluma/commit/50a3efc) corretto l'errore della mancata compilazione su Archlinux
* [e7c0390](https://github.com/mate-desktop/pluma/commit/e7c0390) rimossi tipo e url attr di ulink nella traduzione
* [1e66176](https://github.com/mate-desktop/pluma/commit/1e66176) rimossa la sezione di aiuto deprecata: Aprire un file da un URI
* [deda824](https://github.com/mate-desktop/pluma/commit/deda824) disabilitati i warning di deprecazione per distcheck
* [57d0d30](https://github.com/mate-desktop/pluma/commit/57d0d30) spostato appdata nella cartella metainfo
* [4b6ee7f](https://github.com/mate-desktop/pluma/commit/4b6ee7f) utilizzato lo stesso file legal.xml
* [ce2921c](https://github.com/mate-desktop/pluma/commit/ce2921c) utilizzate funzioni make per HELP_LINGUAS
* [9d4d394](https://github.com/mate-desktop/pluma/commit/9d4d394) Fare riferimento alla pagina man strftime(3) per maggiori informazioni...
* [c6c1cc5](https://github.com/mate-desktop/pluma/commit/c6c1cc5) Fare riferimento alla pagina man pluma(1) per maggiori informazioni...
* [fe12f7e](https://github.com/mate-desktop/pluma/commit/fe12f7e) rimossi gli screenshot inutilizzati
* [f974363](https://github.com/mate-desktop/pluma/commit/f974363) corretti errori di ortografia e grammatica
* [4bb323b](https://github.com/mate-desktop/pluma/commit/4bb323b) help: corretti i collegamenti di aiuto
* [7339842](https://github.com/mate-desktop/pluma/commit/7339842) Utilizzato lo screenshot di pluma corrente per la lingua Catalana
* [1823043](https://github.com/mate-desktop/pluma/commit/1823043) Utilizzato lo screenshot di pluma corrente 
* [a8ac68d](https://github.com/mate-desktop/pluma/commit/a8ac68d) corretti errori di ortografia e grammatica
* [efc1b02](https://github.com/mate-desktop/pluma/commit/efc1b02) pluma-view: alternanza delle schede in modo inaspettato
* [315ab11](https://github.com/mate-desktop/pluma/commit/315ab11) close-confirmation-dialog: Correzione: non ridimensionare la finestra di dialogo in modo inaspettato
* [9cb7cae](https://github.com/mate-desktop/pluma/commit/9cb7cae) pluma-sort-plugin: evitata la riga vuota in più
* [7a65b67](https://github.com/mate-desktop/pluma/commit/7a65b67) sincronizzazione con transifex
* [79f71d7](https://github.com/mate-desktop/pluma/commit/79f71d7) pluma-notebook: evitato di aprire un nuovo file facendo doppio clic sulla barra di scorrimento verticale
* [ea60fd3](https://github.com/mate-desktop/pluma/commit/ea60fd3) pluma-notebook: evitato di aprire un nuovo file facendo doppio clic sul pulsante freccia avanti
* [651a268](https://github.com/mate-desktop/pluma/commit/651a268) pluma-view: Correzione: comportamento imprevisto con il drag and drop sotto i numeri di linea
* [841ad2d](https://github.com/mate-desktop/pluma/commit/841ad2d) pluma-print-preview: Correzione: comportamento bizzarro con i pulsanti del mouse
* [ffd69ab](https://github.com/mate-desktop/pluma/commit/ffd69ab) Correzione: Pluma va in crash se si utilizza la rotellina del mouse sopra una scheda
* [d7a6b50](https://github.com/mate-desktop/pluma/commit/d7a6b50) pluma-view.c: Correzione: migliorato "Mostra i numeri di riga" di GtkCheckMenuItem
* [4212ffa](https://github.com/mate-desktop/pluma/commit/4212ffa) Le schede del notebook adesso sono scorrevoli
* [5b67394](https://github.com/mate-desktop/pluma/commit/5b67394) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione

### python-caja
* [00f7530](https://github.com/mate-desktop/python-caja/commit/00f7530) corretto distcheck quando utilizza python3
* [25a6c2a](https://github.com/mate-desktop/python-caja/commit/25a6c2a) utilizzo della variabile di compilazione PYTHON=python3
* [fd8e389](https://github.com/mate-desktop/python-caja/commit/fd8e389) Abilitato Travis Cl per tutti i rami
* [a5aeb40](https://github.com/mate-desktop/python-caja/commit/a5aeb40) Inizializzato il supporto a Travis Cl
* [7842b86](https://github.com/mate-desktop/python-caja/commit/7842b86) Examples: rimosso l'utilizzo di urllib/urlparse incompatibili con python 2/3.
* [05c5dd5](https://github.com/mate-desktop/python-caja/commit/05c5dd5) Riportata la versione effettiva di Python e la posizione della libreria alla fine di configure
* [98f55b6](https://github.com/mate-desktop/python-caja/commit/98f55b6) docs: Corrette le rimanenze incompatibili con Python 3
* [d349766](https://github.com/mate-desktop/python-caja/commit/d349766) Corretta la funzione Python 2 INT_ASLONG
* [7c4ff1a](https://github.com/mate-desktop/python-caja/commit/7c4ff1a) Inclusi i flag ABI di Python 3 nel nome della libreria condivisa
* [855e612](https://github.com/mate-desktop/python-caja/commit/855e612) Rese le istruzioni compatibili con la versione 2 e 3.
* [047c35b](https://github.com/mate-desktop/python-caja/commit/047c35b) Implementata la compatibilità dell'API C di Python 3 utilizzando condizionali e macro.
* [1eeb215](https://github.com/mate-desktop/python-caja/commit/1eeb215) consentito a "make dist" di compilare senza generare la documentazione.
* [ef861e9](https://github.com/mate-desktop/python-caja/commit/ef861e9) Impossibilità di compilazione se qualche simbolo referenziato non può essere risolto al momento del link. 
* [6447d7c](https://github.com/mate-desktop/python-caja/commit/6447d7c) Modernizzati gli esempi
* [fc99cc4](https://github.com/mate-desktop/python-caja/commit/fc99cc4) disabilitati i warning di deprecazione per distcheck
* [8b82241](https://github.com/mate-desktop/python-caja/commit/8b82241) versione pre-aggiornamento
* [ba72b87](https://github.com/mate-desktop/python-caja/commit/ba72b87) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
* [acb28d1](https://github.com/mate-desktop/python-caja/commit/acb28d1) aggiunto il supporto a Travis-Cl
* [deed071](https://github.com/mate-desktop/python-caja/commit/deed071) Eseguire fixxref.py con python2
* [a9c2545](https://github.com/mate-desktop/python-caja/commit/a9c2545) disabilitati i warning di deprecazione per distcheck
* [7ff7438](https://github.com/mate-desktop/python-caja/commit/7ff7438) sincronizzazione con transifex
* [27019fc](https://github.com/mate-desktop/python-caja/commit/27019fc) transifex: impostata la percentuale_minima ed il tipo nel file di configurazione
