<!-- 
.. link: 
.. description: MATE Desktop collaborates with Blueman project.
.. tags: Blueman,BlueZ,Bluetooth,News
.. date: 2014/03/11 07:45:00
.. title: MATE Desktop canta il BlueZ
.. slug: 2014-03-11-mate-desktop-singing-the-bluez
.. author: Martin Wimpress
-->

I team di MATE sono deliziati di annunciare che stiamo collaborando col [progetto Blueman](https://github.com/blueman-project/blueman) ed aiutandoli ad aggiornare Blueman a BlueZ 5.x.

## Perché abbandonare mate-bluetooth?

`mate-bluetooth` supporta BlueZ 4.x che è stato abbandonato e molte distribuzioni nei loro repository di pacchetti, hanno rimpiazzato BlueZ 4.x con BlueZ 5.x., , o sono sul punto di farlo. Portare `mate-bluetooth` a BlueZ 5.x si stava delineando un grandissimo lavoro e non avrebbe comunque offerto la ricchezza di caratteristiche disponibili in Blueman.

## Perché Blueman? Non è un progetto morto?

Sebbene il progetto originale Blueman fosse stagnante, [Christopher Schramm](https://github.com/cschramm)
ha riacceso lo sviluppo ed ha iniziato a migrare Blueman a BlueZ 5.x. Nonostante occorra del lavoro per aggiornare Blueman nel supportare BlueZ 5.x, ci sentiamo che esso potrà fornire una  migliore interfaccia Bluetooth per MATE.

## Quando sarà pronta la versione aggiornata di Blueman?

Qualcuno di voi potrebbe aver notato che l'[annuncio di rilascio di MATE 1.8](/blog/2014-03-04-mate-1-8-released/)
menzionava già il fatto che `mate-bluetooth` era stato sostituito con Blueman
e gli osservatori ancora più attenti avranno notato che una versione nuova di Blueman
non è ancora stata rilasciata. Si, abbiamo commesso un errore, scusateci.

Mentre riconosciamo di aver sbagliato, stiamo attivamente contribuendo nello sforzo di portare Blueman a BlueZ 5.x e all'introspezione di GObject. Speriamo di averlo pronto
per la versione 1.8.1 che è intesa principalmente come una versione di bug fix.

## Non potete fare prima, cavolo?!

Sì. Chiunque di voi che sia pratico di BlueZ 4.x/5.x, dbus, PyGObject e PyGTK è incoraggiato 
a contribuire attraverso il [repository Blueman GitHub](https://github.com/blueman-project/blueman).
