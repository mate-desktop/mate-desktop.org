<!--
.. link:
.. description:
.. tags: Releases
.. date: 2015-06-11 22:40:40
.. title: MATE 1.10 リリース
.. slug: 2015-06-11-mate-1-10-released
.. author: Martin Wimpress
-->

15ヶか月の開発期間を経て、MATE デスクトップチームは MATE デスクトップ 1.10 のリリースを公表できたことをうれしく思います。すべての MATE 貢献者とユーザーに感謝します。

![about](/assets/img/blog/about-mate-1.10.png)

## MATE 1.10 で新しくなったこと

MATE デスクトップ 1.10 の主な変更点は次のとおりです。

  * MATE のすべてのコンポーネントは、GTK2 と GTK3 でビルドできます。
    * GTK3 のサポートは依然として *試験的* とされています。
    * Arch Linux と Fedora は現在、代替で GTK3 ビルドを提供しています。
  * [GSoC 2014] Cajaには拡張マネージャがあるので、実行時にプラグインを有効/無効にできます。
  * [GSoC 2014] Atril は現在、[ePub](https://en.wikipedia.org/wiki/EPUB) をサポートしています。
  * [GSoC 2014] MATE デスクトップ用オーディオミキサー・ライブラリ `libmatemixer` が導入されました。
    * ミキサー機能へのアクセスを可能にする抽象的 API を提供
    PulseAudio では ALSA と OSS サウンドシステムを使用します。
  * 静的コード解析の結果、多くのメモリリークが塞がれました。
  * テーマサポートは、CSD および pop-over のサポートを含めて、GTK 3.8 から 3.16 まで拡張されました。

MATE 1.10 の各種コンポーネントは、次の場所からダウンロードできます。

  * <https://pub.mate-desktop.org/releases/1.10/>

## スクリーンショット

  * [MATE 1.10 スクリーンショット](/gallery/1.10/)

## 変更点

変更点の詳細を以下に示します。

### mate-common

  * `automake` 1.15 のサポートを追加
  * `lcov` 1.11 のサポートを追加
  * GLib`gettext` 使用時には `GLib-gettexize` へ移行
  * `APPDATA_XML` で `appdata-xml.m4` をチェック

### mate-desktop

  * `MateRRScreen`、`GnomeRRConfig`、`GnomeOutputInfo` を GObject へ移行
  * GObject Introspection の追加
  * GTK `xsetting` 用の automatic-mnemonics キーを追加
  * GTK3 で従来の about ダイアログを備えるように `MateAboutDialog` クラスを追加
  * GTK3 で従来の色選択ダイアログを使用するために `MateColorButton` クラスを追加
  * `org.mate.debug` GSettings のスキーマを追加
  * GTK 間の互換性のために `GDK_WINDOW_XID` を使用
  * ウェブサイト変更のために  `mpaste` を更新
  * 各翻訳の更新
  * desktop-docs の削除
  * ユーザーガイドの削除
  * `libunique` オプションの依存関係を削除
  * さまざまな RANDR 修正

### libmatekbd

  * 翻訳の更新
  * さまざまなバグ修正。

### libmatemixer

`libmatemixer` は MATE デスクトップ用の新しいミキサーライブラリで、PulseAudio、ALSA、OSS サウンドシステムで利用可能なミキサー機能へアクセスできる抽象的な API を提供します。

  * 最初のリリース

### お天気 MATE

  * 翻訳の更新
  * さまざまなバグ修正。

### mate-icon-theme

  * アイコンの追加
  * 新しいシンボリックアイコンの追加

### Caja

  * プラグイン管理を追加して、実行時に拡張機能を有効/無効を可能に
  * 翻訳の更新
  * さまざまなバグ修正。

### mate-polkit

  * 翻訳の更新

### Marco

  * `mate-dialogs` の代わりに `zenity` を使用
  * 翻訳の更新
  * さまざまなバグ修正。

### mate-settings-daemon 

  * API の変更に伴い、`MateRR*` へ移行しました。
  * media-keys プラグインを `libmatemixer` へ移行
  * 翻訳の更新
  * GStreamer を削除して、`libmatemixer`、`libcanberra`、PulseAudio をオプションの依存関係にしました

### MATE セッションマネージャ

  * `upower` サポートは標準で無効になったので、必要に応じて `--enable-upower` を使用してください
  * 翻訳の更新

### MATE メニュー

  * 翻訳の更新
  * さまざまなバグ修正。

### MATE パネル

  * `showdesktop` アイコンのサイズを修正しました。
  * 非推奨の GDK ポインタ API (GTK3) の使用を修正
  * すべての `GtkStyle` を `GtkStyleContext` (GTK3) へ移行
  * `gtk_rc_parse_string` を `GtkCssProvider` (GTK3) へ移行
  * `GDK_KEY_*` は Gtk+2.24.x でも使われています。
  * `panel-addto` から vbox が削除されたのは廃止予定のためです。
  * 翻訳の更新
  * さまざまなバグ修正。
    * クロックにシャドウ pixbuf を作成する前に、割り当てサイズをチェックしてください。
    * アプレットメニューを破棄する前に、メニュー信号の表示と非表示を解除します。
    * `SYSTEM_TRAY_CANCEL_MESSAGE` の処理
    * `gdk_x11_set_sm_client_id` 関数の暗黙の宣言を修正
    * 現在の pixbuf の gtkimage を button-widget へ追加
    * カスタムキャッシュの代わりに gtk アイコンキャッシュを使用

### mate-backgrounds 背景

  * Ubuntu のブランドは入っていない MATE 壁紙を追加
  * 新しい MATE-Stripes-Dark.png、MATE-Stripes-Light.png 壁紙を追加

### mate-themes テーマ

  * GTK 3.16、3.14、3.12、3.10、3.8 のサポートを追加
  * MATE GTK3 アプリケーションに関する多数の改善点を追加
  * GTK3 使用時に、ボタンとメニュー項目にトランジション効果を追加
  * CSD アプリケーションのサポートを追加
  * ポップオーバのサポートを追加
  * CSD アプリケーションのウィンドウシャドウを有効に
  * ウィンドウコントロールで通常のアイコンを有効に
  * シンボリックアイコンの使用禁止
  * スピナーアニメーションにメイトロゴを使用
  * GreenLaguna のリファクタリング
  * ContrastHigh テーマのリファクタリング
  * TraditionalOKTest は通常の構成フラグを使用してインストール可能
  * その他、多くの修正と改良

### mate-notification-daemon

  * さまざまなバグ修正。
  * 翻訳の更新

### mate-control-center コントロールセンタ

  * タイトルバーボタンのレイアウトを設定するオプションを追加
  * `metacity-theme-2.xml` のサポート追加
  * お気に入りのアプリケーションにオフィスアプリケーションのサポートを追加
  * API の変更に伴い、`MateRR*` へ移行
  * 翻訳の更新

### mate-screensaver スクリーンセーバ

  * API の変更に伴い、`MateRR*` へ移行
  * 翻訳の更新

### mate-media

  * PulseAudio の依存関係を削除
  * `gst-mixer` と `gst-mixer-applet` を削除
  * mate-volume-control を更新
    * PulseAudio から `libmatemixer` へ移行
    * 入出力コネクタの選択を可能に
    * スピーカーテストのアイコンに「閉じる」ボタンを追加
    * デバイスリストとストリームリストが並び替え可能に
    * 垂直パネル上にアイコンを非表示
    * ポップアップウィンドウ内でのクリックを許可
  * 翻訳の更新

### mate-power-manager MATE 電源管理

  * `upower` 0.99+ への対応を追加
  * 翻訳の更新
  * `udisks` の依存関係を削除

### mate-system-monitor MATE システムモニタ

  * GNOME システムモニタからバックポートして改善
  * 翻訳の更新
  * さまざまなバグ修正。

### Atril 文書ビューア

  * epub のサポートを追加
  * xz 圧縮のサポートを追加
  * プレゼンテーションモードで、CTRL+left と CTRL+right で回転可能に
  * コミックのバックエンドに `bsdtar` のサポートを追加
  * PDF のバックエンドに `pdf.xz` ファイルのサポートを追加
  * EvViewPresentation に外部リンクのサポートを追加
  * EvBookmarks に内部文書のブックマークを扱える機能を追加
  * PDF バックエンドに OCG State アクションのサポートを追加
  * サイズ変更モードがフリーの場合、既定で拡大率の設定を保存する機能を追加
  * ドラッグ＆ドロップを使って画像を保存するときに、`png` 拡張子を追加
  * SyncViewに timestamp パラメータを追加
  * Caja 拡張機能に ini ファイルを追加
  * appdata ファイルを追加
  * PDF バックエンドに `document_links_find_link_page()` を実装
  * djvu バックエンドに document_links_find_link_page()` を実装
  * `get_dest_page()` の `find_link_dest()` ではなく `find_link_page()` へ移行
  * プレゼンテーションモードで文書を再読み込みする時、現在のページを記憶する不具合を修正
  * PDF バックエンド内の名前付き宛先解決の問題を修正
  * サイドバーのサムネイルを修正して、ジョブをスケジュールする前に、ジョブ終了信号に接続するようにしました。
  * DVI バックエンドで、透過性のあるグリフを描画するように修正
  * DVI バックエンドでセキュリティ関連の複数の問題を修正
  * 複数の操作支援上の問題を修正
  * セグメンテーションの不具合と多くのメモリリークを修正
  * `poppler` 0.16.0 API へ変更したので更新
  * `libmate-desktop` から `MateAboutDialog` へ移行
  * 翻訳の更新
  * さまざまなバグ修正

### caja-extensions Caja 拡張機能

  * 「Set as wallpaper」という新しい拡張機能を追加
  * ビルドするのに `send-to` プラグインを選択するオプションを再導入
  * 翻訳の更新

### Engrampa 書庫マネージャ

  * Caja メニューからの iso イメージと tar アーカイブの圧縮ができる機能を追加
  * ドラッグ&ドロップでファイルを展開した時、上書き確認ダイアログを追加
  * keywords key を `.desktop` ファイルに追加
  * Caja 拡張機能に ini ファイルを追加
  * `engrampa.appdata.xml` を追加
  * RAR ファイル内にある RAR ファイルの開き方を修正
  * パスワード保護されたファイルで発生するエラーを修正
  * 7zip で複数のボリュームの RAR 書庫読み込み時の不具合を修正
  * ファイルの追加でキャンセルをクリックした時に発生するクラッシュを修正
  * `engrampa.1` の man ページにおいて、ハイフンをマイナス記号として扱う問題を修正
  * メモリリークの修正
  * Gtk+ <2.24 のサポートを削除
  * Glib < 2.32 のサポートを削除
  * Caja GSettings スキーマをオプションで使用
  * ハードコードされた `~/.config/mate` の代わりに `g_get_user_config_dir` を使用
  * `GtkRecentAction objects` を使用して最近のファイルチューザーを作成
  * 選択したアプリケーションをシステムの既定に設定しません。
  * ユーザーがサイズ変更可能なように、「直近の出力」ダイアログをモーダルダイアログとしては設定しません。
  * 翻訳の更新
  * さまざまなバグ修正

### Eye of MATE 画像ビューア

  * Eye of GNOME からバックポートして改善
  * 翻訳の更新
  * さまざまなバグ修正

### mate-applets MATE アプレット

  * `libmate-desktop` から `MateAboutDialog` へ移行
  * 翻訳の更新
  * さまざまなバグ修正

### mate-netbook MATE ネットブック

  * Windows Picker アプレットが Maximus の設定を強制的に変更する問題を修正
  * `libmate-desktop` から `MateAboutDialog` へ移行
  * 翻訳の更新
  * さまざまなバグ修正

### mate-netspeed MATE ネットスピード

  * MATE システムモニタのグラフと同様のネットワーク負荷グラフを追加
  * 翻訳の更新
  * さまざまなバグ修正

### mate-sensors-applet センサーアプレット

  * 翻訳の更新
  * さまざまなバグ修正

### mate-terminal 端末

  * `libmate-desktop` の共通機能へ移行
  * 翻訳の更新

### MATE ユーザー共有

  * 翻訳の更新
  * さまざまなバグ修正

### mate-utils

  * 翻訳の更新
  * さまざまなバグ修正

### Mozo メニューエディタ

  * 翻訳の更新

### Pluma テキストエディタ

  * `libmate-desktop` から `MateAboutDialog` へ移行
  * 翻訳の更新
  * さまざまなバグ修正

### python-caja

  * Caja の拡張タブに「拡張について」というボタンを追加
  * さまざまなバグ修正


<br/><br/>

