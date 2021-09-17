<!--
.. link:
.. description:
.. tags: Releases,Salix,Linux Mint,Sabayon,Fedora
.. date: 2013-04-02 19:23:50
.. title: Rilasciato MATE 1.6
.. slug: 2013-04-02-mate-1-6-released
.. author: Stefano Karapetsas
-->

Il team MATE è orgoglioso di annunciare il rilascio di MATE Desktop 1.6. Questa release è un enorme passo in avanti rispetto alla versione 1.4. In questo rilascio, abbiamo sostituito molti pacchetti e librerie deprecate con nuove tecnologie disponibili in
GLib. Abbiamo aggiunto anche un gran numero di nuove funzionalità a MATE. Vorremmo ringraziare
ciascun collaboratore e utente di MATE.

![about](/assets/img/blog/about-mate-1.6.png)

I principali cambiamenti nella versione 1.6 sono:

**il supporto a systemd e logind**

  * Aggiunto il supporto per `systemd-logind` in `mate-session-manager` e `mate-screensaver`
  e `mate-power-manager` (adesso si può riavviare/spegnere senza ConsoleKit)

**Caja (gestore dei file)**

  * Migliorata la barra laterale delle posizioni
  * Aggiunto il supporto per nuove specifiche di miniaturizzazione
  * Aggiunta una nuova cornice per le miniature
  * Gli sfondi adesso vengono caricati in cache per una migliore gestione della memoria
  * Un nuovo dialogo per il server di connessione da Nautilus 3
  * Aggiunto il supporto per freedesktop.org
  * Interfaccia DBus del File Manager
  * Risolto il problema con la selezione della cartella precedente vs genitrice
  * L'estensione open terminal adesso supporta l'apertura di un terminale remoto 

**Pannello**

  * Aggiunta l'opzione `--run-dialog` per aprire la finestra di dialogo per l'esecuzione dell'elenco delle Finestre: è possibile
  usare il pulsante centrale del mouse per chiudere una finestra selettore di Spazio di lavoro:
  * Aggiunta una opzione per scorrere tra gli spazi di lavoro con la rotellina del mouse
  * Aggiunto un modo semplice per le distribuzioni per sovrascrivere il layout del pannello predefinito
  Sfortunatamente, a seguito della migrazione a GSettings, perderete il vostro attuale layout del pannello .
  Tutte le altre impostazioni saranno portate se avete installato MateConf 1.4.

**Marco (gestore delle finestre)**

  * Aggiunta una opzione per aprire le finestre al centro dello schermo

**Centro di controllo**

  * Aggiunta l'opzione per abilitare il gestore di compositing Marco e spostarsi rapidamente con alt-tab tra le preferenze della finestra
  * Impostato il tema GSettings/GConf metacity se compiz o metacity sono in esecuzione
  * Utilizzate le stesse impostazioni proxy di GNOME del pacchetto `gsettings-desktop-schemas`
  * Applicazioni predefinite: consente di impostare il terminale predefinito

**Atril (visualizzatore di documenti)**

  * Aggiunto il backend XPS

**Calc**

  * Aggiornato il codice base
  * Aggiunti i pulsanti per per il supporto delle funzioni trigonometriche inverse

**Demone delle notifiche**

  * Aggiunta l'opzione per [specificare su quale schermo mostrare le notifiche](/blog/2013-01-20-changes-to-mate-notification-daemon/)
  * Mostrare sempre una notifica se lo schermo ha come timeout 'non spegnere mai' (anche se lo screensaver è attivo o o ci sono finestre a schermo pieno attive)

**Temi**

  * [Nuovi temi GTK2/3](/blog/2013-03-26-new-themes/) (Menta, BlackMATE, GreenLaguna, TraditionalGreen)
  * Aggiunto il supporto GTK3 per altri temi GTK2 (TraditionalOk, TraditionalOkTest, Contrasto elevato) 
  * Abilitata l'anteprima del testo dei file di testo
  * Aggiunte alcune nuove icone

**Demone per le impostazioni**

  * Aggiunto il supporto MPRIS2 per mandare il segnale dai tasti multimediali ai lettori multimediali
  * Aggiunta l'opzione per disegnare lo sfondo se Caja non è attivo
  * Il demone viene adesso fatto ripartire da `mate-session` se va in crash

**Applet Netbook**

  * Abilitato maximus solo se l'applet del window picker è aggiunta al pannello

**Pacchetti eliminati**

  * Sostituito MateConf con GSettings
  * Sostituito MateCorba/MateComponent con DBus
  * Sostituito MateVfs con GIO/GVFS
  * Sostituito `libmatenotify` con `libnotify`
  * Rimosso `libmate` (mate-open sostituito con gvfs-open, gli schemi GSettings spostati nel pacchetto mate-desktop)
  * Rimossi dei pacchetti deprecati
    * `libmateui`
    * `libmatecanvas`
    * `libmatecomponentui`
    * `mate-mime-data`

**Altri miglioramenti**

  * Corretto molto codice deprecato
  * Eliminati molti bug
  * Aggiunte e migliorate molte traduzioni

Abbiamo chiesto agli utenti delle distribuzioni che offrono MATE cosa pensano del
nostro Ambiente Desktop

**George Vlahavas**, fondatore e capo progetto di [Salix](https://www.salixos.org/):

> Crediamo che MATE sia un abbinamento perfetto per Salix. MATE ci fornisce un ambiente desktop familiare
che è potente, solido e veloce. Inoltre, il team di MATE è
molto amichevole ed è piacevole lavorarci assieme e questo significa molto per noi. Grazie ragazzi, per
averci dato la scelta di rimanere con il nostro desktop preferito

**Clement Lefebvre**, fondatore e capo progetto di [Linux Mint](https://www.linuxmint.com/):

> È estremamente importante per noi che le persone siano felici con il loro computer. Quando quell'ambiente
che tutti abbiamo amato e lavorato duramente per migliorare dal 2006 è stato
interrotto non eravamo felici di lasciarlo andare e di chiedere alle persone di migrare a
qualcosa di nuovo o di diverso. Abbiamo lavorato molto duramente per assicurarci che i nostri
utenti potessero continuare ad usare il loro computer come volevano e abbiamo incontrato un
team di persone che la pensavano come noi e che avevano preso l'iniziativa di supportare quell'ambiente
e  svilupparlo ulteriormente. Mint e MATE vanno di pari passo e
il rapporto tra i team è eccellente. Mint ha giocato un ruolo importante
nella promozione e nel sostegno di MATE e continuiamo ad aiutare il suo
sviluppo. Siamo molto soddisfatti di MATE, è esattamente quello che volevamo,
ha iniziato da dove GNOME aveva lasciato e con ogni nuovo ciclo continua a migliorare.

**Joos Ruis**, Consulente di strategia di  [Sabayon](https://www.sabayon.org/):

> Non ci piace come l'upstream abbia forzato i cambiamenti agli utenti e vogliamo che i nostri utenti abbiano
l'opzione di decidere cosa usare. Con MATE nei nostri repository siamo certi
che i nostri utenti possano sempre scegliere ciò che funziona meglio per loro.

**Dan Mashal**, Manutentore MATE in [Fedora](https://fedoraproject.org/): 

> Da quando è stata rilasciata Fedora 15 sono stato estremamente infelice e
frustrato con la mia esperienza desktop fino a quando ho scoperto MATE. Ora su Fedora
posso finalmente avere un desktop che è sano, stabile, veloce e soprattutto facile
da usare. Con il duro lavoro che il team ha fatto per patchare anche compiz per farlo lavorare sulle
nuove versioni di Fedora, ora posso avere la mia Fedora 14 (considerata da molti
essere la migliore release di Fedora) con finestre tremolanti, desktop
cubico, animazioni ed effetti 3d. Non posso sottolineare quanto questa sia stata una grande perdita per molti utenti, incluso
me stesso. Ora con MATE non devo preoccuparmi di cosa si romperà con
la prossima release di Gnome e quali folli idee di design avranno, costringendomi a reimparare un'interfaccia desktop ad ogni singolo rilascio di Fedora.
Con MATE 1.6 posso sentirmi a casa sulla mia distribuzione Linux preferita
e tornare a lavorare.

Abbiamo anche chiesto un commento dalla
[compagnia che ha donato il server dove ospitiamo i servizi MATE](/blog/2012-12-27-thank-you-first-colo/). **Martin Verges**, CEO di [FirstColo GmbH](https://www.first-colo.net/en/):

> Siamo davvero felici di usare l'ambiente desktop MATE. In questo modo possiamo mantenere un desktop pulito
e ben funzionante senza un sacco di roba inutile che distrae. Fino alla fine del
2012 tutta la nostra azienda stava lavorando con Ubuntu, ma con il desktop Unity
e molte altre "funzionalità per l'utente finale", stavamo cercando nuovi modi per ottenere un
desktop, libero da software che pretende di renderci la vita più facile. Con MATE
Desktop su Debian 7 Wheezy, abbiamo trovato un desktop ben funzionante e ad alte prestazioni
che funziona semplicemente come lo conosciamo da anni. Speriamo che il team MATE mantenga
il nostro classico desktop Linux e gli dia nuova vita con nuove caratteristiche, ma
con il buon flusso di lavoro in mano. Finora hanno fatto un ottimo lavoro, e noi
speriamo che presto i manutentori Debian aggiungano il desktop MATE ai loro
mirror (e, naturalmente, che anche molti altri usino MATE!).

MATE 1.6 è il risultato di 8 mesi di intenso sviluppo e contiene 1800
contribuzioni da 39 persone, e più di 150 traduttori. 

  * [MATE 1.6 Screenshots](/gallery/1.6/)
