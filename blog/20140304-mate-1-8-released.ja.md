<!--
.. link:
.. description:
.. tags: Releases
.. date: 2014-03-04 21:39:36
.. title: MATE 1.8 リリース
.. slug: 2014-03-04-mate-1-8-released
.. author: Stefano Karapetsas
-->

私たちチームは、MATE デスクトップ 1.8 のリリースを公表できてうれしく思います。MATE の貢献者やユーザーのみなさんに感謝します。

![情報](/assets/img/blog/about-mate-1.8.png)

1.8 の主な変更点は次のとおりです。

**Caja (ファイルマネージャ)**

  * SI 単位の代わりに IEC 単位を使用するオプションを追加
  * 検索ビューのコンテキストメニューに “Open parent location” オプションを追加

**Marco (ウィンドウマネージャ)**

  * 並べて表示する機能を追加 (ウィンドウのスナップ)

**パネル**

  * 実行ダイアログおよびメインメニューでの Metacity キーバインディングのサポート追加
  * ログアウトダイアログに進捗バーを追加

**コントロールセンタ**

  * Metacity をウィンドウマネージャとして使用可能にするための対応

**MATE デスクトップライブラリ**

  * MATE ユーザーガイドを追加

**Eye Of MATE (画像ビューア)**

  * スライドショーにシャッフルモードを追加

**Engrampa (ファイルアーカイバ)**

  * 常に "展開先" のコンテキストメニューを Cajaに表示

**スクリーンセーバ**

  * ロックダイアログに日付と時刻を表示

**各種アプレット**

  * 付箋アプレットに元に戻す機能を追加
  * コマンドの出力を表示する、新しい "コマンド" アプレットを追加
  * C 言語で "timer" アプレットを書き換え
  * 音量アプレット上で中マウスボタンをクリックしてミュートに切り替え

**廃止したパッケージ**

  * `mate-doc-utils` を `yelp-tools` へと置き換え
  * `libmatekeyring` と `mate-keyring` を `libsecret` と `gnome-keyring` に置き換え
  * `libmatewnck` を `libwnck` へ置き換え
  * `mucharmap` を `gucharmap` へ置き換え
  * `mate-bluetooth` を [blueman](https://github.com/blueman-project/blueman) へ置き換え
  * すべての  Caja 拡張機能を 1 つのパッケージに統合
  * netspeed アプレットに同等の機能があるため、modem lights アプレットを削除。

**その他の改善**

  * 多くの非推奨コードを修正
  * 多数の不具合を修正
  * ビルドシステムの改良
  * 多くの翻訳の追加と改善

<br/><br/>

いつもの通り、MATEを配布しているディストリビューションの方々に、私たちのデスクトップ環境をどう思っているのか尋ねてみました。

**Mike Gabriel**, [Debian](https://www.debian.org/) 開発者兼 MATE メンテナ:

> 私は、MATE がDebian Jessie (およびそれ以降) で最も利用されるデスクトップ環境の 1 つになると予想しています。

**Tom Wijsman**, [Gentoo](https://www.gentoo.org) 開発者兼 MATE メンテナ:

> 私たちのユーザーの中には、GNOME 2 を使い続けたいと言っている人もいます。以前のようなものが好きなので、古いハードウェアを動かしたり、もっと軽量なデスクトップを欲しがっているのです。GNOME 2 がサポートされなくなり、さまざまな維持や後退、セキュリティ上の問題のために最終的に私たちのメタディストリビューションから削除されることを考えると、MATE は活発な開発チームに栄光を取り戻してくれます。彼らの GNOME 2 開発の継続は、未解決の問題を修正し、新しくて役に立つ機能をもたらし、古くても良いエクスペリエンス提供し続けます。

**Willy Sudiarto Raharjo**、[MATE SlackBuilds プロジェクト](https://mateslackbuilds.github.io/) の共同開発者:

> MATE は Slackware と同じ基本的な考え方を共有しており、シンプルさ、安定性、そして固定されたリリーススケジュールはありません。MATE は準備ができた時にリリースされ、正常に動作していることが証明されている同じメタファを保持しています。また、MATE は Slackware 上で容易にメンテナンスし、統合することができます。それは、Patrick Volkerding が2005年以来 Slackware に欠けていた GNOME ベースのデスクトップ環境の必要性を MATE がしっかり満たす基盤を提供しているからです。私は、MATE 開発者が MATE の次期メジャーリリースで統合する進化的な変更を楽しみにしています。

**Chess Griffin**、[MATE SlackBuilds プロジェクト](https://mateslackbuilds.github.io/) の共同開発者:

> MATEは、古い GNOME 2 のエクスペリエンスを気に入っている人々にとって、すばらしいデスクトップ環境です。MATE を安定させ、成熟させると同時に、必要に応じて新しい難問を組み込んでいくために、MATE に課せられたあらゆる努力に大変感謝しています。ユーザーのオペレーティング・システムやディストリビューションに関して MATE を懐疑的に捉える努力も賞賛されます。私は MATE SlackBuilds プロジェクトの一員であることを楽しんでいます。このプロジェクトは、MATE デスクトップを Slackware Linux コミュニティに持ち込むことを目的としています。MATE チームの皆さんに感謝します。

**Benjamin Denisart**、[openSUSE](https://www.opensuse.org/) MATE メンテナ:

> OpenSUSE チームは、この新バージョンを提供していただいた MATE 開発者に感謝の意を表するとともに、従来の使いやすいデスクトップに惹かれたユーザーを喜ばせる `gnome-main-menu` の提供を発表できたことを誇りに思います。MATE チームと共に働くことができて光栄です。彼らにお祝いの言葉を送りたいと思います。

**Clement Lefebvre**、[Linux Mint](https://www.linuxmint.com/) 創設者兼プロジェクトリーダー:

> MATE は GNOME 2 の特色を自信持って搭載しており、元のプロジェクトが中断したところから続いています。いろいろな意味で、多くの人にとって、MATE はわが家のように感じられます。シンプルで安定しすべての機能を備えています。最近のデスクトップは新しいコンセプトを実験していますが、MATE は期待どおりに動作する環境を提供しています。これは、ユーザーに人気があり、Linux Mint が 2006 年が年から技術と独自性を構築してきたデスクトップです。MATE をサポートできて私たちは非常に誇りに思っていますし、非常に嬉しく思います。新しいリリースがあるだびに喜んでいます。

**Wolfgang Ulbrich**, [Fedora](https://fedoraproject.org/) の MATE メンテナ: 

> Fedora 15/16 リリースの間、私は提供されているデスクトップ解決法に非常に不満がありました。10ヶ月間 XFCE を使用した後、私は MATE を発見し、2011 年 12月に Fedora 用に私自身用のデスクトップを作成することにしました。この作業の結果、Fedora 用に初めて MATE デスクトップの外部リポジトリが作成され、ロシア、ラトビア、インドネシアでの私がパッケージした Fedora スピンを含み、世界中の多くのユーザーによって使用されました。この作業の当然な結果は、公式なFedora 内に Dan Mashal for Fedora 18 と一緒に MATE デスクトップを導入することでした。2度のリリース後、Fedora 20 には安定して使用可能な MATE 1.6 のデスクトップソリューション生まれました。MATE 1.8 は現在 Fedora rawhide にあり、2014 年夏に Fedora 21 と合わせてリリースされる予定です。

**Martin Wimpress**、[Arch Linux](https://www.archlinux.org/) 用の MATE メンテナ:

> MATE は元々 Arch Linux ユーザーによって作成されましたが、MATE が正式なArch Linux および Arch Linux の ARM パッケージリポジトリで利用できるようになったことをうれしく思います。MATE は完全に統合された、応答性の高い従来のデスクトップ体験と一貫したワークフローを、私の [Raspberry Pi](www.raspberrypi.org)、[CuBox Pro](https://www.solid-run.com/cubox)、ノートパソコンおよびデスクトップで提供しています。すばらしい！

<br/><br/>

MATE 1.8 は、11 カ月間の精力的な開発の成果であり、57 人のメンバーによる 1845 件の貢献と 291 人以上の翻訳者による成果です。

  * [MATE 1.8 スクリーンショット](/gallery/1.8/)

<br/><br/>
