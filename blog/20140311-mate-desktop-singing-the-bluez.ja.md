<!-- 
.. link: 
.. description: MATE Desktop collaborates with Blueman project.
.. tags: Blueman,BlueZ,Bluetooth,News
.. date: 2014/03/11 07:45:00
.. title: MATE デスクトップは BlueZ を歌っています
.. slug: 2014-03-11-mate-desktop-singing-the-bluez
.. author: Martin Wimpress
-->

MATE チームは、[Blueman プロジェクト](https://github.com/blueman-project/blueman)と協力し、Blueman を BlueZ 5.x へとアップデートする支援が出来ることを公表できてうれしく思います。

## なぜ mate-bluetooth を捨てたのですか？

`mate-bluetooth` は BlueZ 4.x をサポートしていますが、BlueZ 4.x は開発終了であって、多くのディストリビューションがそれぞれのパッケージリポジトリでBlueZ 4.x を BlueZ 5.x に置き換えたか、置き換えようとしています。`mate-bluetooth` をBlueZ 5.x に移行するのは大変な作業であり、また、Blueman で利用可能な範囲の諸機能を提供しません。

## なぜブルーマンなのですか？開発中止なのでは？

当初の Bluemanプ ロジェクトは停滞しましたが、[Christopher Schramm](https://github.com/cschramm) が開発を再開し、Blueman の BlueZ 5.x への移植を開始しました。その一方で、BlueZ 5.x をサポートするために Blueman をアップデートする取り組みもあり、私たちはその方が MATE にずっと優れた Bluetooth インターフェースを提供すると思っています。

## Blueman のアップデートはいつ完了しますか？

[MATE1.8 リリースのお知らせ](/blog/2014-03-04-mate-1-8-released/)ではすでに `mate-bluetooth` が Blueman に置き換えられたとしていましたが、さらに詳しい人は、Blueman の新しいバージョンがまだリリースされていないことも気付いたでしょう。大変申し訳ありません。

間違っていたのは確かですが、私たちは Blueman を BlueZ5.x と GObject introspection へ移植するため積極的に貢献しています。私たちは主にバグ修正リリースとして意図されている MATE 1.8.1 のリリースに間に合うように準備したいと思っています。

## もっと早く出来ないのですか？

はい。BlueZ 4.x/5.x、dbus、PyGObject、PyGTK に詳しい方は、[Blueman GitHub repository](https://github.com/blueman-project/blueman) を利用して貢献していただくようお願いします。
