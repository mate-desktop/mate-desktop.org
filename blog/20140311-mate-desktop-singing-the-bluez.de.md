<!-- 
.. link: 
.. description: MATE-Desktop arbeitet mit dem Blueman-Projekt zusammen.
.. tags: Blueman,BlueZ,Bluetooth,News
.. date: 2014/03/11 07:45:00
.. title: MATE-Desktop singt den BlueZ
.. slug: 2014-03-11-mate-desktop-singing-the-bluez
.. author: Martin Wimpress
-->

Das MATE-Team freut sich bekanntzugeben, dass wir mit dem
[Blueman-Projekt](https://github.com/blueman-project/blueman) zusammenarbeiten 
und dabei helfen, Blueman auf BlueZ 5.x zu aktualisieren.

## Warum wird mate-bluetooth fallengelassen?

`mate-bluetooth` unterstützt BlueZ 4.x, das nicht weiter entwickelt wird. 
Außerdem haben viele Distributionen in ihren Repositorien BlueZ 4.x mit BlueZ 5.x ersetzt, oder sie sind im Begriff, es zu tun. 
`mate-bluetooth`  nach BlueZ 5.x zu migrieren stellte sich als sehr mühselig heraus, und das Programm bietet nicht den Funktionsumfang, der in Blueman zu finden ist.

## Warum Blueman? Ist es nicht tot?

Obwohl das originale Blueman-Projekt stagnierte, hat [Christopher Schramm](https://github.com/cschramm)
die Entwicklung wieder angetrieben und damit begonnen, Blueman auf BlueZ 5.x zu portieren.
Während es durchaus auch einige Mühen kosten wird, Blueman für eine Unterstützung von BlueZ 5.x weiterzuentwickeln,
haben wir das Gefühl, es wird ein deutlich besseres Bluetooth-Interface für MATE bieten.

## Wann wird der aktualisierte Blueman verfügbar sein?

Die Aufmerksamen unter Ihnen werden bemerkt haben, wie schon in der [MATE1.8 Release-Ankündigung ](/blog/2014-03-04-mate-1-8-released/) erwähnt, `mate-bluetooth` durch Blueman ersetzt wurde.
Und die besonders Aufmerksamen werden ferner bemerkt haben, dass eine neue Version von Blueman bis jetzt nicht veröffentlicht wurde.
Ja -- das war ein Fehler. Es tut uns leid.

Auch wenn wir diesen Fehler zugeben, tragen wir aktiv zu den Anstrengungen bei Blueman für BlueZ 5.x und GObject-Introspektion anzupassen.
Wir hoffen, es rechtzeitig fertig zu haben für MATE 1.8.1, das primär als Bugfix-Release gedacht ist.

## Könnt ihr nicht schneller arbeiten, verdammt?!

Klar. Jeder mit Kentnis über BlueZ 4.x/5.x, dbus, PyGObject and PyGTK ist dazu aufgefordert
eine Verbesserung [Blueman GitHub repository](https://github.com/blueman-project/blueman) beizutragen.
