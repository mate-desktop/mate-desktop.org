<!--
.. link:
.. description:
.. tags: Releases,Fedora
.. date: 2015-06-11 22:30:30
.. title: Мејт 1.10 са Гтк3 за Федору 21 и 22
.. slug: 2015-06-11-mate-1-10-with-gtk3-for-fedora-21-22
.. author: Wolfgang Ulbrich
-->

Одржаваоци Мејтове радне површи за Федору са поносом објављују да је пробна Гтк3 
изградња доступна за тестирање на Федири 21 и 22. Ова Гтк3 изградња ради посао 
али има неке мање проблеме исцртавања, ваше повртане информације су нам потребне.

## Инсталација

Инсталирајте датотеку ризнице и извршите `yum update`.

### Федора 22

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-22/raveit65-Mate-GTK3-fedora-22.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-22.repo /etc/yum.repos.d/
    $ sudo yum update

### Федора 21

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-21/raveit65-Mate-GTK3-fedora-21.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-21.repo /etc/yum.repos.d/
    $ sudo yum update

Или користите наредбу `dnf`:

    $ sudo dnf copr enable raveit65/Mate-GTK3
    $ sudo dnf update

## Пријављивање проблема

Користите пратиоца грешака Мејтове радне површи на ГитХаб-у и укључите „Гтк3 и Федора“
у теми.

  * https://github.com/mate-desktop

Неке напомене:

  * Компиз ће радити само са `emerald`-ом као украшивачем прозора.
  * Немојте мешати Гтк2 пакете из стабилне Федоре и Гтк3 пакете из горње
  ризнице.
  * Немојте користити следеће Мејтове програме са Гтк3 изградњом Мејта; нису прилагођени за Гтк3:
    * „mintMenu“ и „MATE Menu“
    * mate-applet-streamer
    * mate-applet-lockkeys
    * mate-applet-softupd
    * caja-terminal
