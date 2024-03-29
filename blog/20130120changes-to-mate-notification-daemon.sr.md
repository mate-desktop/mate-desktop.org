<!--
.. link:
.. description:
.. tags: News
.. date: 2013-01-20 19:07:12
.. title: Измене у мејтовом позадинцу обавештења
.. slug: 2013-01-20-changes-to-mate-notification-daemon
.. author: Steve Zesch
-->

`mate-notification-daemon` има нову функцију у Мејту 1.6 која омогућава
корисницима да изаберу на којем монитору желе да приказују обавештења.
Тренутно понашање приказује обавештења само на монитору који је тренутно
активан (где је показивач). Понашање ће се подразумевати као да је увек и
било, али корисник може да измени поставке тако што ће изменити кључеве
„користи-радни-монитор“ и „број-монитора“ путем `dconf-editor` или могу покренути
`mate-notification-properties` и уредити своје поставке путем ГКС-а.

Испод је снимак екрана `mate-notification-properties` постављеног за приказивање
обавештења на радном монитору. Приметите да је изабрано „Користи радни монитор“,
што искључује падајући списак за бирање монитора.

![active](/assets/img/blog/active-300x235.png)

Испод је снимак екрана `mate-notification-properties` постављеног за приказивање
обавештења на одређеном монитору. Приметите да „Користи радни монитор“ **није**
изабрано, што омогућава да се са падајућег списка изабере монитор који ће бити омогућен.
Број монитора је постављен на 2. Тимео ће се приказивати на трећем монитору, јер
бројање почиње од 0 уместо од 1.

![monitor](/assets/img/blog/monitor-300x235.png)

