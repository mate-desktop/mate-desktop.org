<!-- 
.. link: 
.. description: 
.. tags: LiveCD,Arch Linux,News
.. date: 2014/01/30 00:17:32
.. title: MATE デスクトップ Live CD
.. slug: 2014-01-30-mate-desktop-live-cd
.. author: Martin Wimpress
-->

MATE チームは、完全な MATE デスクトップが起動可能な Live CD を作成しました。

<div class="alert alert-info"><strong>更新</strong> LiveCD は2014年3月10日、MATE 1.8 へアップデートされました。</div>

この Live CD は、将来的な新規ユーザーが MATE デスクトップをシステムに影響しない方法で評価するために作成されました。イメージは DVD に書き込んだり、ISO ファイルとしてマウントしたり、`dd` のようなユーティリティを使って直接 USB メモリに書き込んだりすることができます。[Linux Luddites](https://luddites.latenightlinux.com/) では `unetbootin` はサポートされていません。以下からダウンロードできます。

### BitTorrent よりダウンロード (推奨)

バイト数に余裕がある場合は、ダウンロードが完了した後でクライアントを開いたままにしておいてください。そうすれば、他のユーザーにシードすることができます。*最も速いダウンロード速度を得るためには、ウェブシード対応のクライアントをお推めします。*

  * [matelivecd-14.069.1449.iso.torrent]

### HTTP で直接ダウンロード

上記の BitTorrent リンクに加えて、Live CD.iso は HTTP 経由でもダウンロード可能です。ダウンロードしたファイルが SHA1 チェックサムと一致することを確認してください。

  * [matelivecd-14.069.1449.iso] [ ~964MB ]
    * SHA1: `12b529d17d1ecef39d9b0e1122fb5271e0534c0a`

## 互換性

Live CD は、[Arch Linux](https://www.archlinux.org) と MATE 1.8 を使用して作成されています。Live CD は 32 ビットであるため、512MB 以上の RAM 搭載の i686 または x86_64 コンピュータで動作します。Intel (`i915`)、AMD/ATI (`radeon`)、nvidia (`nouveau`) 用の Xorg ドライバが含まれており、VESA にフォールバックします。Virtual Box および VMware 用のドライバも含まれているので、これらの仮想化ソリューションを使用した評価は簡単です。

[ZFS](http://open-zfs.org) を含むすべての一般的なファイルシステムがサポートされており、いくつかのデータリカバリおよびバックアップツールが含まれています。モバイルデバイスに接続すれば認識される可能性が高く、データにアクセスできるようになります。NetworkManager が、それに対応可能な VPN クライアントと共に含まれています。

## ユーザ名とパスワード

MATE デスクトップ Live CD には、次のアカウントが設定されています。

  * `root` - パスワードは `livecd` です。
  * `mate` - パスワードは `livecd` です。

`root` アカウントは当然 `root` です。`mate` アカウントは、完全なパスワードなしの `sudo` 権限を持つ通常のユーザーです。Live CD は `mate` アカウントを使って自動ログインします。

## アプリケーション

LiveCD はおもに MATE デスクトップを紹介する目的で作成されましたが、LiveCD が少しでも役立ち、楽しめるものにしたかったので、MATE デスクトップに含まれないアプリケーションも追加しました。

  * [Firefox](https://www.mozilla.org/firefox/)   - mozilla.org が開発したスタンドアロンのウェブブラウザ
  * [GParted](https://gparted.sourceforge.io/)   - Partition Magic のクローンで GNU Parted のフロントエンド
  * [HardInfo](https://www.berlios.de/software/hardinfo/)  - システム情報およびベンチマークツール
  * [HexChat](https://hexchat.github.io/)   - [#mate@libera](https://web.libera.chat/?#mate) に自動接続するように設定された IRC クライアント
  * [Onboard](https://www.gnome.org/projects/orca)      - 視覚障害者向けのスクリーンリーダー
  * [Orca](https://www.gnome.org/projects/orca)      - 操作障害者に有用な画面上のキーボード
  * [Pidgin](https://pidgin.im/)    - マルチプロトコルなインスタントメッセージクライアント
  * [Xnoise](http://www.xnoise-media-player.com/)    - 洗練された GUI を持ち、高速で豊富な機能を備えたメディアプレーヤー

## クリエイティブ・コモンズのコンテンツ

次のとおり、クリエイティブコモン・ライセンスのコンテンツを含んでいます。

  * [Think Python](https://www.greenteapress.com/thinkpython/)                        - Atrilと一緒に読む込まれます

## 言語の変更

既定では、Live CD は `en_US` ロケールを使用するように設定されていますが、ここで別の言語を有効にしたい場合には方法があります。次の例では、イタリア語が有効になります。

`/etc/locale.gen` を編集してロケールのコメントを外します。この場合、`it_IT.UTF-8UTF-8` を編集してロケールを再設定してください。

    sudo locale-gen

`/etc/locale.conf` を編集し、`LANG=` を変更してロケールを反映させます。この場合は `LANG=it_IT.UTF-8` です。最後にディスプレイマネージャを再起動すると、希望の言語を使って MATE セッションにログインできます。

    sudo systemctl restart lightdm

## Linux アクション表示機能

MATE デスクトップ LiveCD と MATE レビューを [CuBox 
Linux Review](https://www.jupiterbroadcasting.com/show/linuxactionshow/) の [Linux Action Show](https://www.jupiterbroadcasting.com/50842/cubox-linux-review-las-s30e08/) で紹介しました。下記に2つのクリップが埋め込まれています。最初はMATE デスクトップ LiveCD の概要であり、2番目は MATE が動作している CuBox i4 のレビューです。

### MATE デスクトップ LiveCD

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=608" frameborder="0" allowfullscreen></iframe>

### CuBox i4 Pro レビュー

<iframe width="640" height="360" src="//www.youtube.com/embed/y4OpjoJiAGE?start=1925" frameborder="0" allowfullscreen></iframe>

## フィードバック

Live CD を試用していただいて、MATE デスクトップの速さとシンプルさを実感してください。MATE デスクトップ Live CD を試されたら、感想をお聞かせいただくか、あるいは Live CD を使って [#mate IRC channel](https://webchat.freenode.net/?channels=#mate) に参加してみてください。

