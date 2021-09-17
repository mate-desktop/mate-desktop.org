<!--
.. link:
.. description:
.. tags: Releases,Fedora
.. date: 2015-06-11 22:30:30
.. title: MATE 1.10 con GTK3 per Fedora 21 e 22
.. slug: 2015-06-11-mate-1-10-with-gtk3-for-fedora-21-22
.. author: Wolfgang Ulbrich
-->

I manutentori del desktop MATE per Fedora sono lieti di annunciare che le build GTK3 sono disponibili per il test in Fedora 21 e 22. Queste build GTK3
funzionano ma soffrono di qualche difetto di rendering di lieve entità, apprezzeremmo il vostro feedback.

## Installazione

Installate il file repo ed eseguire uno `yum update`.

### Fedora 22

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-22/raveit65-Mate-GTK3-fedora-22.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-22.repo /etc/yum.repos.d/
    $ sudo yum update

### Fedora 21

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-21/raveit65-Mate-GTK3-fedora-21.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-21.repo /etc/yum.repos.d/
    $ sudo yum update

O utilizzate il comando `dnf`: 

    $ sudo dnf copr enable raveit65/Mate-GTK3
    $ sudo dnf update

## Riportare problemi

Per favore utilizzate l'issue tracker di MATE Desktop su GitHub ed includete 'GTK3 and Fedora' nell'oggetto.

  * https://github.com/mate-desktop

Alcune note:

  * Compiz funzionerà solo con `emerald` come window-decorator.
  * Non utilizzate pacchetti GTK2 da Fedora stable e pacchetti GTK3 dalla
  repo riportata più in alto.
  * Non utilizzate le seguenti applicazioni MATE con una build GTK3; poiché non sono ancora portate a GTK3:
    * mintMenu e MATE Menu
    * mate-applet-streamer
    * mate-applet-lockkeys
    * mate-applet-softupd
    * caja-terminal
