<!--
.. link:
.. description:
.. tags: News
.. date: 2013-01-20 19:07:12
.. title: Modifiche a mate-notification-daemon
.. slug: 2013-01-20-changes-to-mate-notification-daemon
.. author: Steve Zesch
-->

`mate-notification-daemon` ha una nuova funzionalità in MATE 1.6 che consente
agli utenti di scegliere su quale monitor si vuole mostrare le notifiche. Il
comportamento attuale mostrale notifiche solo sul monitor correntemente attivo (cioè quello su cui si trova il puntatore del mouse). Il comportamento sarà per default quello che si è sempre avuto in precedenza, ma l'utente può cambiare le impostazioni modificando le chiavi "use-active-monitor"
e "monitor-number" mediante `dconf-editor` o eseguendo
`mate-notification-properties` e modificando le impostazioni da una Interfaccia Utente Grafica.

Qui sotto c'è uno screenshot di `mate-notification-properties` impostato per mostrare le notifiche su un monitor attivo. Si noti che "Use Active Monitor" è selezionato, il che disabilita la combobox per selezionare un monitor.

![active](/assets/img/blog/active-300x235.png)

Qui sotto c'è uno screenshot di `mate-notification-properties` impostato per mostrare le notifiche su uno specifico monitor. Si noti che "Use Active Monitor" **non** è
selezionato, il che abilita la combobox per selezionare un monitor da abilitare.
Il numero del monitor è impostato a 2. Questo mostrerà le notifiche sul mio terzo monitor, perché la numerazione inizia da 0 invece che da 1..

![monitor](/assets/img/blog/monitor-300x235.png)

