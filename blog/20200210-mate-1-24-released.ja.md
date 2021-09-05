<!--
.. link:
.. description:
.. tags: Releases
.. date: 2020-02-10 09:00:00
.. title: MATE 1.24 を公開しました
.. slug: 2020-02-10-mate-1-24-released
.. author: Wolfgang Ulbrich
-->

約 1 年の開発期間を経て、MATE デスクトップチームはついに MATE 1.24 をリリースしました。このリリース実現のために協力していただいたすべての貢献者に感謝します。

![MATE ダイアログ情報](/assets/img/blog/about-mate-1.24.png){ width=50% }

## MATE 1.24 で新しくなったこと

このリリースには、多くの新機能、バグ修正、一般的な改善が含まれています。最も重要なハイライトは次のとおりです。

* ユーザーがセッションを開始すると、MATE デスクトップ環境は以前よりも使いやすくなりました。アプリケーションの起動を非表示にしたいですか？ 今では、起動時に表示するアプリケーションが設定できるようになりました。
* **Engrampa**は現在、複数の形式を追加でサポートするほか、一部の形式ではパスワードとユニコード文字のサポートが改善されています。
* **Eye of MATE** は現在、[Wayland](https://wayland.freedesktop.org/) をサポートしていて、埋め込みカラープロファイルもサポートしています。
    * サムネイルの生成は、いくつかの箇所で修正されています。
    * Webp ファイルのサポートが追加されました。
* 標準のウィンドウマネージャ **marco** には、次のように多くの変更があります。
    * 私たちはユーザーのノスタルジーを誘うために、以前のウィンドウ装飾をたくさん持ち込みました。
    * 最後に、非表示のサイズ変更境界を追加しました。マウスでキャプチャする際、境界を見つけるのに苦労する必要がなくなります！
    * すべてのウィンドウコントロール (最小、最大、閉じるボタンなどのこと) が HiDPI でレンダリングされるようになりました。
    * Alt+Tab およびワークスペース切替のポップアップは、_完全_に作り直されました。現在では、美しい OSD スタイルでレンダリングされ、設定が一層容易になって、キーボードの矢印キーに応答することができます。
    * キーボードを使用してウィンドウを並べて表示すると、ウィンドウのサイズを切り替えることができるようになりました。画面の半分に制約されていると感じる必要がなくなりました。
* **System Monitor** パネルアプレットは、NVMe ドライブをサポートするようになりました。
* **電卓**は、「pi」または「π」の使用をサポートするようになりました。
    * 科学的表記（指数表記）が改良されました。
    * 事前に定義された物理定数をサポートするためのいくつかの修正。
* **コントロールセンタ**のアイコンが HiDPI ディスプレイで正しく表示されるようになりました。
* 全く新しい**時刻と日付の設定**アプリが追加されました。
* **Mouse** アプリは、加速度プロファイルをサポートするようになりました。
* **お気に入りのアプリケーション**というアプリの支援技術が向上し、IM クライアントとの統合サポートも向上しました。
* **インジケーターアプレット**は、異なるサイズのアイコンとの対話性が若干向上しています。
* アイコンについて言えば、私たち自身のテーマ上でのネットワークマネージャアプレットアイコンは完全に再設計され、HiDPI ディスプレイで利用可能となりました。
* 忙しい時やプレゼンテーションをしている時、映画を見ている時に邪魔をされたくないタイプの人は、**通知デーモン**が Do-Not-Disturb モードをサポートするようになったことを知って喜ぶでしょう。
* **MATE パネル**にはいくつかのバグがあって、以前はレイアウトを変更するとクラッシュしていましたが、今では修正されました！
    * [Wayland](https://wayland.freedesktop.org/) との互換性が大幅に向上しました。
    * ステータスアイコン (**通知領域**または**システムトレイ**とも呼びます) は、HiDPI 表示をサポートします。
    * **おさかな君ワンダ**が変身したので、今あなたはおさかな君を HiDPI の壮観さの中で楽しむことができます。
    * **ウィンドウリスト**アプレットは、カーソルを上に置いた時、ウィンドウのサムネイルを表示するようになりました。
    * パネルと主要なアプレット全体で、さまざまな支援技術の改善が行われました。
* ご使用のシステムが [systemd](https://freedesktop.org/wiki/Software/systemd/) をサポートしていない場合、[elogind](https://github.com/elogind/elogind) のサポートが **MATEスクリーンセーバー**と **MATEセッション**の両方に追加されたことに関心があると思います。
* さらに、全く新しい **MATE ディスクイメージ・マウンタ**というユーティリティも追加されました。
* メニューエディタの **Mozo** は、「元に戻す」と「やり直し」操作をサポートするようになりました。
* **Pluma** プラグインは完全に Python 3 へ移行しました。
* **Pluma** はフォーマットマークを表示できるようになったので、他の複雑なエディタをうらやましく思う必要がなくなりました。
* i18n 関係: すべてのアプリケーションが intltools から gettext へ移行しました。



MATE デスクトップ 1.24 の各種コンポーネントは、次の場所からダウンロードできます。

  * <https://pub.mate-desktop.org/releases/1.24/>

## 詳細情報

詳細は以下のとおりです。

### Atril 文書ビューア
* ズーム時の大量のメモリ消費を修正
* サムネイルを作成してテキストに注釈を付ける際のメモリリーク修正
* ドラッグ＆ドロップ: ドラッグ＆ドロップ操作を開始するとき、 `pressed_button` アクションをリセット
* メニュー項目にアクセラレータを追加
* 'synctex' ライブラリの内部ビルドを削除し、ソフトウェアベンダーが提供する外部バージョンのみを使用
* ビルドターゲットを完了できないようになるギリシャ語ユーザガイドを修正
* Tiff バックエンド: TIFFReadRGBAImageOriented からの障害に対応
* Tiff バックエンド: tiff-document.c のバッファオーバーフローを修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告を修正
* テスト用に Python 3 へ移行
* GLib 2.54.0 以降が必要
* WebKitGTK-4.0 2.6.0 以降が必要
* Cairo 1.14.0 以降が必要
* WebKitGTK-3.0 のサポートを廃止
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な変更点はこちら: <https://github.com/mate-desktop/atril/commits/master/>

### Caja ファイルマネージャ
* gcc10 が使用可能に
* fm-properties: mate-desktop-thumbnail ヘルパーの使用を削除
* ファイル名をハイフネーションしません
* 新しい拡張インタフェースの追加: CajaWidgetViewProvider API
* 新しいオブジェクトの追加: FmWidgetView
* 翻訳者から報告された文法上の誤りを修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告を修正
* 韓国語ロケールでファイルを移動すると Caja がクラッシュする問題を修復
* ビュータブでアイコン表示のオプションを使用
* リストビュー内のアイコンを非表示にする設定オプションを追加
* いくつかのメニュー項目に無かったアイコンを追加
* サムネイルをリストビューで表示
* より多くのアイコンを cairo_surfaces としてレンダリングして、HIDPI のサポートを向上
* カスタム CSS の読み込みを別の関数にリファクタリング
* gla11y を使用して UI files のアクセシビリティをチェックするためのサポートを追加
* アイコンビューラベルの透過な背景を復元
* ファイルのプロパティと Caja の設定ウィンドウに、マウスホイールでのスクロールタブを追加
* desktop: 既定でデスクトップ項目に境界を設定しない
* URL プレフィックスを http から https へ変更
* caja-progress-info: ファイル転送ダイアログに tooltips を追加
* ファイル転送操作ダイアログボックスのボタンにアクセス可能な名前を追加
* eel: 日付と時刻の機能を削除
* caja-file: 不完全なファイル置換ダイアログを修正
* caja-file-operations: 誤検出警告のコメント追加
* あちこちで発生するメモリリークを修正
* i18n: グラフィックインタフェースのより多くの要素の翻訳を許可
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は次の changelog にあります: <https://github.com/mate-desktop/caja/commits/master/>

### Caja-dropbox
* CAJA_EXTENSION_DIR_SYS を使用して、Caja 拡張ディレクトリを保存および表示
* caja-extension-dir の絶対パスを表示

完全な変更点は次の changelog にあります: <https://github.com/mate-desktop/caja-dropbox/commits/master/>

### Caja 拡張機能
* caja-wallpaper-extension: メモリリークの修正
* image-converter: caja-image-resize.ui の非推奨事項を修正して最初から書き直し
* Clang Static Analyzer、Cppcheck、および GCC で報告されたコード解析、非推奨警告を修正
* gupnp のバージョン 1.0 または 1.2 を使用してビルド
* image-converter: コンテキストメニューに存在しないアイコンの使用中止
* i18n image-converter: 角度を選択するドロップダウンリストの翻訳を許可する
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は次の changelog にあります: <https://github.com/mate-desktop/caja-extensions/commits/master/>

### Engrampa 書庫マネージャ
* gcc 10 の使用が可能に
* fr-command-rpm: rpm パッケージ同梱の rpm2cpio バイナリを使用
* サポートされている mime-type に source rpm を追加
* 7z: 作業ディレクトリを設定しない、つまり、一時ディレクトリを使用
* ローカライズされた一時停止 UI ロジックを修正
* Zstandard: MIME type の更新
* Ar: MIME type の更新とマジックナンバーの追加
* LHA: インターネットメディアの種類を修正
* dlg-package-installer: エラーダイアログのボタンにアイコンを表示
* unace 2.5: アーカイブの概要をファイル一覧に表示しません
* java-utils: パッケージ名を読み取る前に空白スペースを削除
* zcompress サポートの追加
* fr-command-unarchiver: 必要に応じてパスワードを要求します
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告を修正
* 複数のメモリリークを修正
* マニュアルを docbook 5.0 にアップグレード
* udeb パッケージ形式のサポート
* コマンドラインにアプリケーションのバージョンを表示
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は次にあります：<https://github.com/mate-desktop/engrampa/commits/master/>

### eom
* webp ファイル用の eom-thumbnailer を追加
* thumbnail: mate-desktop-thumbnailヘルパーの使用を削除
* Wayland のサポートを有効化
* EomPrintPreview: HiDPI 表示のプレビューサムネイルを修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告を修正
* アルファチャンネルを使用したカラー補正イメージを許可
* GLib 2.52 以降が必要
* store: 現在のディレクトリ内のイメージファイルを store へ追加
* マニュアルを docbook 5.0 へアップグレード
* パーシステンス・ページ設定を使用
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は、<https://github.com/mate-desktop/eom/commits/master/> に掲載しています。

### libmatekbd
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* UIファイルに gresources を使用
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです <https://github.com/mate-desktop/libmatekbd/commits/master/>

### libmatemixer
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです <https://github.com/mate-desktop/libmatemixer/commits/master/>

### お天気 MATE
* 場所: Lleida–Alguaire Airport weather station を追加
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* 場所: ロシアの Rostov-on-Don 気象台の変更
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです <https://github.com/mate-desktop/libmateweather/commits/master/>

### marco
* テーマ: 全テーマのウィンドウ制御の非表示レンダリングを修正
* tabpopup: 完全な作り直し
* window: オプションのタイルサイズサイクルを追加
* ウィンドウの装飾テーマの追加: Atlanta、Esco、Gorilla、Motif、Raleigh を追加
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* コンポジットが使用されていない場合、frame.c で RBGA ビジュアルの使用を修正
* CSD クライアントと連携するために、ウィンドウのエッジへの移動を修正
* meson ビルドシステムのサポートを追加
* alt+tab を使用して最大列数の設定可能にし、ウィンドウラベル幅を考慮
* 非表示の枠線を追加
* テーマ: 最大化された状態で並べて表示する時のウィンドウ状態を修正
* constraints: meta_window_constrain() でのメモリリークを修正
* alt+tab ポップアップ: 作り直し
* Alt + Tab ポップアップで上下矢印キーを使用可能に
* 複数のメモリリークを修正
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです <https://github.com/mate-desktop/marco/commits/master/>

### mate-applets
* gcc10 を使用する準備が整っています
* デフォルトの D-Bus 設定ディレクトリとして ${datadir}/dbus-1/system.d を使用
* dbus ディレクトリを設定可能に
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* cpufreq ビルドをカーネルヘッダのバージョンから独立
* geyes: メモリリークの回避
* multiload: NVMe ドライブのサポート
* コマンドアプレットがコマンドを同期実行させる
* 「情報」ダイアログで翻訳可能な文書作成を可能に
* 「情報」ダイアログで著作権情報の翻訳を作成可能に
* 「情報」ダイアログのタイトルが正確に翻訳されていることを確認
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります： <https://github.com/mate-desktop/mate-applets/commits/master/>

### mate-backgrounds
* meson ビルドシステムのサポートを有効化
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-backgrounds/commits/master/>

### mate-calc

* 複素数の科学的表記を修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* mp-equation: 物理定数の値を更新して、数値ボタンのツールチップの値と一致
* 単位ツールチップを物理定数へ追加
* クリックにフォーカスしない
* mp-equation: 事前定義された物理定数を追加
* UI ファイルに gresources を使用
* mp: 計算結果 ln(e^(i*π)) を修正
* 科学的表記で小数を表示
* mate-calc: メモリリークを修正
* 「π」に加えて「pi」のサポートを追加
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-calc/commits/master/>

### mate-common
* MATE_CXX_WARNINGS マクロの更新
* コンパイラデバッグフラグを MATE_DEBUG_CHECK に設定
* AX_APPEND_FLAG および AX_CHECK_COMPILE_FLAG が使用可能かをチェック
* mate-compiler-flags マクロの更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-common/commits/master/>

### mate-control-center
* システムデータディレクトリ内でシステムのテーマを検索
* display: ヘルプボタンを有効に
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* HIDPI 表示用のいくつかのアイコン修正
* font-viewer: サポートされる MIME タイプに font/collection を追加
* font-viewer: font/ttf と font/otf の MIME タイプを追加
* 複数のアプリケーションでのメモリリークを修正
* mouse: 加速度プロファイルのサポートを追加
* at-properties: dbus-glib から gdbus へ移行
* ログイン設定のプログラムとして、lightdm-gtk-greeter-settings をサポート
* libXxf86 の依存関係を削除
* gla11y には python3 を使用
* 複数の Capplet にマウスホイール付きのスクロールタブを追加
* gla11y を使用して UI ファイルのアクセシビリティをチェックするサポートを追加
* 新しい time-admin アプリケーションを追加
* インスタントメッセンジャーのキーバインドを mate-keybinding-properties に追加
* default-applications: 既定のメッセンジャーアプリケーション用のウィジェット追加
* capplets: UIファイルに gresources を使用
* dbus-glib から GDBus へ移行
* システムデータ・ディレクトリを使用してキーバインディングを確定
* default-applications: UI のアクセシビリティ向上
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-control-center/commits/master/>

### mate-desktop
* mate_desktop_thumbnail_scale_down_pixbuf() の削除
* サムネイルのサイズを 256 へと増加
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析、非推奨警告の修正
* 残りの周辺機器スキーマを mate-settings-daemon へ移動
* schema: マウススキーマを mate-settings-daemon へ移動
* schemas: 既定メッセンジャのスキーマを定義
* mate-languages のテストコードを追加
* meson ビルドシステムのサポートを追加
* 複数のメモリリークを修正
* MateHSV の実装 (GtkHSV のフォーク)
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-desktop/commits/master/>

### mate-icon-theme
* モバイルネットワーク接続のステータスアイコンを追加
* volume-status アイコンの作り直し
* VPN ネットワークステータスアイコンを追加
* ネットワークステータスアイコンを追加
* dropbox-status アイコンを追加
* mate/256x256/actions/mail-send.png を追加
* mate/22x22/devices/printer.png の修正
* 22x22px のアイコンを 24x24px に拡大し、エッジに 1px を追加
* MATE ロゴのシャドウに放射状グラデーション (ぼかし 13.9%、不透明度 73.4%) を使用
* 欠落している preferences-system-time アイコンを追加
* パネル内のボリュームステータスのコントラスト向上
* paper-sheets.svg からpng MIME タイプアイコンを生成 - Mate theme
* ソースから preferences-system-time.png を生成
* ソースから png アイコンを生成 - Mate theme, apps, categories & devices
* mate theme の端末アイコンを更新
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-icon-theme/commits/master/>

### mate-indicator-applet
* インジケータアイコンのサイズをパネルに合わせて変更
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-indicator-applet/commits/master/>

### mate-media
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* gvc applet: 欠落している翻訳の追加 (i18n)
* media-key と同様に、ボリュームを設定可能な手順でスクロール
* マウスホイールを使用するスクロールインタフェースを追加
* ステータスアイコンまたはパネルアプレットのいずれかを無効可能に
* 出力のミュートメニュー項目を有効化
* 新しいリアルな panel-applet を追加
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-media/commits/master/>

### mate-menus
* gir ファイルのインストール時に datadir 変数と libdir 変数を使用
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-menus/commits/master/>

### mate-netbook
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* アプレットのウィンドウタイトルの太字を無効にするオプションを追加
* 'show-home-title' 機能を復活
* ウィンドウの picker アプレットの設定ラベルを変更し、ツールチップを追加
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-netbook/commits/master/>

### mate-notification-daemon
* mate-notification-properties.ui に gresource を使用
* mate-notification-properties: do-not-disturb 機能を追加
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: at <https://github.com/mate-desktop/mate-notification-daemon/commits/master/>

### mate-panel
* パネルのトップレベルでの a11y の重複説明を回避
* clock applet: ATK にコールを追加し、現在表示時刻を提供
* status-notifier: HIDPI サポートの改善
* fish: おさかな君ワンダに高解像度のイメージを使用
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* panel-toplevel: 拡張時の垂直パネル上のアプレット配置を修正
* [clock-applet] マウスホイールを使用したスクロールインタフェースタブを追加
* Wayland サポートをさらに改善
* システムトレイを X11 専用に
* panel-struts を X11 専用に
* panel-multimonitor を Wayland で利用可能に
* panel-background を Wayland で利用可能に
* panel-background-monitor を X11 専用に
* アプレットがサポートするプラットフォームのロードと保存
* panel-addto がアプレットの無効化をサポート
* Panel addto の Wayland 対応
* パネルのリセット後に既定のレイアウトを再ロードする問題を修正
* パネルリセット時のランダムクラッシュを修正
* window-list: カーソルを置いたときにウィンドウのプレビューを表示
* パネルアプレットのキーボードフォーカストラップを修正
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-panel/commits/master/>

### mate-polkit
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* GSimpleAsyncResult から GTask への移行
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-polkit/commits/master/>

### mate-power-manager
* icons: 高解像度のアイコンを追加
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* upower-0.99.8 以降が必要
* up_client_get_devices2() を使用
* UI ファイルに gresources を使用
* マウスホイールを使用するスクロールインタフェースタブを追加
* マウスのパワー低下時の警告を無効にする設定オプションを追加
* i18n: intltools から gettext への移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-power-manager/commits/master/>

### mate-screensaver
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* サスペンド時のロックとリジューム時のロック解除を確実に
* UI ファイルに gresources を使用
* libXxf86 の依存関係を削除
* ELOGIND サポートの追加
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-screensaver/commits/master/>

### mate-sensors-applet
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-sensors-applet/commits/master/>

### mate-session-manager
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* gnome-keyring 3.34 でタイムアウトする問題を修正
* GNOME_KEYRING_LIFETIME_FD を削除
* mate-session-properties の垂直方向のスケーリングを修正
* test-inhibit: gdbus へ移行
* hidden checkbox と gsettings flag の表示を追加.
* 起動時のアプリケーションで NoDisplay Apps を非表示に
* 複数のメモリリークを修正
* hardware-compatibility ファイルの追加
* org.gnome.SessionManager.Renderer プロパティが取得できない問題を修正
* mate_session_check_accelerated ヘルパーの追加
* ELOGIND サポートの追加
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-session-manager/commits/master/>

### mate-settings-daemon
* DBUS 1.10.0 以降が必要
* 既定の DBUS_SYS_DIR を ${datadir}/dbus-1/system.d へ変更
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* xrandr: トレイアプレットのアイコンサイズを大きく
* 起動時のアプリケーション capplet から MATE 設定デーモンを非表示に
* 残りの周辺機器スキーマを mate-desktop から追加
* マウス: 加速度プロファイルを追加
* gschema で media-keys の音量ステップのデフォルトを 6 から 5 に変更
* plugins: libXxf86 の依存関係を削除
* plugins housekeeping: コードの最適化
* media-keys: スキーマによって定義された既定のインスタントメッセージ・アプリケーションの実行
* locate-pointer: 位置を確認する時ポインタボタンを使用しない
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-settings-daemon/commits/master/>

### mate-system-monitor

* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* GLib 2.56.0 以降が必要
* HiDPI サポートの改善
* usage セクションと prefs セクションにディスクの I/O 情報を追加
* 複数のメモリリークを修正
* プロセス情報にディスク IO を追加
* システムタブに GPU 情報を表示
* 最大 32 個の CPU をサポート
* ZFS で使用可能なディスク容量を表示
* システムタブに OpenIndiana のリリースとカーネル情報を表示
* システムタブに FreeBSD の sysname、release、version を表示
* openSUSE Tumbleweed ローリングリリースの情報を修正
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-system-monitor/commits/master/>

### mate-terminal
* gcc 10 の使用が可能に
* 複数のメモリリークを修正
* terminal-screen: ウィンドウを閉じる時の警告を修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* 「マウスポインタ上にあるものを強調表示」を設定可能に
* タブを閉じる際、開いているタブが複数ある場合に確認ダイアログを表示
* マニュアルを docbook 5.0 へアップグレード
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-terminal/commits/master/>

### mate-user-guide
* reporting-bugs セクションの更新
* custom-command-options セクションを削除し、構文のアドレスを指定
* お気に入りのアプリケーションの項目を更新
* docbook リンクを xref に置き換え、linkend 属性 (#30) を修正
* マニュアルを docbook 5.0 へアップグレード
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-user-guide/commits/master/>

### mate-user-share
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* HTTPD の設定通知を修正
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-user-share/commits/master/>

### mate-utils
* gcc 10 の使用が可能に
* UI ファイルに gresources を使用
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* MATE ディスクイメージ・マウンタユーティリティを追加
* logview: 現在のロケールに任意の日付と時刻形式を使用
* マウスホイールを使用するスクロールタブを追加
* inkscape と rsvg-convert をオプションに
* 複数のメモリリークを修正
* svg ファイルから png アイコンを再生成
* about ダイアログの文書を更新
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/mate-utils/commits/master/>

### mozo
* 元に戻す ボタンと やり直し ボタンを追加
* アイテムのドラッグ＆ドロップによるコピー作成の修正および、元に戻す、やり直し、リフレッシュ時のクラッシュを修正
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* meson ビルドシステムのサポートを追加
* 新しいメニューと項目の作成を修正
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです: <https://github.com/mate-desktop/mozo/commits/master/>

### pluma
* 印刷できない文字 (スペース/タブ/改行) を表示する機能を追加
* Clang Static Analyzer、Cppcheck、および GCC によって報告されたコード解析や非推奨警告を修正
* window: GdkWindowState を上書きしない
* 複数のメモリリークを修正
* GtkSourceView 3.22 でビルドを修正
* スペルチェッカー・プラグイン: 欠落している翻訳(i18n)を追加
* gla11y を使用して UI files のアクセシビリティをチェックするためのサポートを追加
* コメント/コメント解除を切り替えるスニペットの追加
* pluma-print-preview: 警告の修正: identical expressions
* Python3 へ移行
* マニュアル: メニューから Pluma を開く方法を更新
* マニュアルを docbook 5.0 へアップグレード
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な変更点は次のとおりです: <https://github.com/mate-desktop/pluma/commits/master/>

### python-caja
* gcc 10 の使用が可能に
* Python 2 のサポートを廃止
* Python 3.9 を使用したビルドのサポートを追加
* i18n: intltools から gettext へ移行
* g10n: 翻訳の更新

完全な changelog は次にあります: <https://github.com/mate-desktop/python-caja/commits/master/>
