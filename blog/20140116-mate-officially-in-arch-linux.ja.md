<!-- 
.. link: 
.. description: 
.. tags: Arch Linux,Raspberry Pi,News
.. date: 2014/01/16 22:22:22
.. title: MATE は Arch Linux で公式に入手できます
.. slug: 2014-01-16-mate-officially-in-arch-linux
.. author: Martin Wimpress
-->

MATE はようやく我が家に落ち着きました。

皆さんの中には、MATEが [Arch Linux](https://www.archlinux.org) のユーザー、Perberos さんによって作成されたことをご存知の方がいるかもしれません。MATE がこれまで正式な Arch Linux のパッケージリポジトリに収録されていなかったというのは、皮肉なことです。この通り、MATE はついに Arch Linux の `[community]` パッケージリポジトリで利用可能になりました！

Arch Linux に MATE をインストールするのに必要な情報は、次の Wiki ページですべて知ることができます。

  * <https://wiki.archlinux.org/index.php/MATE>

すべての Arch Linux ミラーが同期されると、現在は廃止となった非公式な MATE パッケージリポジトリが削除されることに注意してください。そのため、`/etc/pacman.conf` を更新し、`[mate]` パッケージリポジトリを削除してください。

MATE を正式な Arch Linux パッケージリポジトリに入れるもう 1 つの利点は、MATE が [Arch Linux ARM](https://archlinuxarm.org/) パッケージリポジトリでも機能するようになることです。私はついに Raspberry Pi (armv6h) と Cubox Pro (armv7h) のビルド*"サーバ"*を引退させることができます。すべての MATE パッケージが Arch Linux ARM パッケージリポジトリに現れるまでにどの位の時間がかかるのかは分かりませんが、すでにいくつかのパッケージがビルドされているのを確認しています。

MATE は 512MB の RAM を搭載した Raspberry Pi Model B で非常にうまく動作するので、もし Pi と予備の SDCARD があれば試してみてください。Arch Linux とMATE を Raspberry Pi にインストールする方法について、私はブログ記事を書くつもりです。近いうちに、パフォーマンス改善に役立つことも書きます。
