<!--
.. link:
.. description:
.. tags: News
.. date: 2013-01-20 19:07:12
.. title: mate-notification-daemon への変更
.. slug: 2013-01-20-changes-to-mate-notification-daemon
.. author: Steve Zesch
-->

`mate-notification-daemon` は MATE 1.6 の新機能で、ユーザーはどのモニターに通知を表示するか選択可能になりました。現在の動作では、現在アクティブな(ポインタがある)モニターにのみ通知が表示されます。動作のデフォルトは以前と同じですが、ユーザーは `dconf-editor` で "use-active-monitor" キーと "monitor-number" キーを変更して設定を変更したり、`mate-notification-properties` を実行して GUI で設定を編集することができます。

以下は、`mate-notification-properties` のスクリーンショットで、アクティブモニタに通知を表示する設定です。「アクティブモニターを使う」が選択されていることに注意してください。これによって、モニタを選択するためのコンボボックスが無効になります。

![active](/assets/img/blog/active-300x235.png)

次のスクリーンショットは、特定のモニターに表示される通知に対して設定された `mate-notification-properties` です。「アクティブモニターを使う」が**選択されていない**ことに注意してください。これによって、有効にしたいモニターの選択用のコンボボックスが使用可能となります。図のモニター番号は 2 に設定されています。カウントは 1 からでなくて 0 から開始されるので、これで 3 番目のモニターに表示されます。

![monitor](/assets/img/blog/monitor-300x235.png)

