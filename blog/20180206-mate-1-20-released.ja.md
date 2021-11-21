<!--
.. link:
.. description:
.. tags: Releases
.. date: 2018-02-07 09:00:00
.. title: MATE 1.20 を公開しました
.. slug: 2018-02-07-mate-1-20-released
.. author: Martin Wimpress
-->

11 ヶ月の開発期間を経て、MATE デスクトップチームは MATE デスクトップ 1.20 のリリースを公表しました。このリリースを可能にしていただいた全ての MATE 貢献者の方々に感謝します。

![about](/assets/img/blog/about-mate-1.20.png)

## MATE 1.20 で新しくなったこと

このリリースの課題は、廃止されたコードを置き換え、コードベースの大部分を近代化することによって、MATE デスクトップを安定させることでした。また、ウィンドウマネージャ (Marco) を改善し、HiDPI のサポートを追加しました。その過程で、何百もの不具合を修正しました。

MATE デスクトップ 1.20 の主な変更点は次のとおりです。

  * **MATE デスクトップ 1.20 は、動的な検出とスケーリングによる HiDPI ディスプレイをサポートします。**
    * Qt アプリケーションのための HiDPI ヒントも、クロスツールキット統合を改善するために環境へプッシュされます。
    * HiDPI モードを切り替えると、動的なサイズ変更とスケールが生じるので、ログアウトやログインは必要ありません。
  * **Marco は現在、もし利用可能であれば [DRI3 と XPresent](https://lwn.net/Articles/569701/)** をサポートします。
     * Marco 使用中のゲームのフレームレートが大幅に向上しています。
  * Marcoは、**quadrant ドラッグウィンドウのタイリング**をサポートするようになりました。カーソルキーを使用して <kbd>Alt</kbd> + <kbd>Tab</kbd> スイッチャが操作可能になり、キーボードショートカットを使用してウィンドウを別のモニタへ移動できるようになりました。
  * **グローバルメニューのサポート** [vala-panel-appmenu](https://github.com/rilian-la-te/vala-panel-appmenu) などのプロバイダが追加されました。
  * MATE パネルは [Status Notifier Items (SNI)](https://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/) のサポートを大幅に改善しました。
  * **ブックマークが GTK3+ ロケーションをサポートするようになりました**。
  * MATE 端末は、背景画像をサポートし、Solarized テーマとキーバインディングを切り替えタブに追加しました。
  * **文書ビューアの Atril は、大規模なオーバーホールを受けた**ので、あらゆる点で改善されています。すべてが良くなりました。
    * 特に、視覚障害のあるユーザに対する操作支援サポートが大幅に改善されました。
    * キャレットナビゲーションを追加しました。
  * MATE アプレットから **Invest アプレットが削除されました** 。
    * Yahoo が提供するこの API は廃止されましたが、評判の良い代替品がありません。
  * パネルアプレットのサイズが、表示されている単位に基づいて正しく設定されるようになりました。また、多くのグラフが動的にスケールされます。
  * **MATE のテーマは大幅に改善された**ので、GTK 3.22 で公開されたすべてのスタイルクラスを完全に実装します。
  * Engrampa 書庫マネージャは、暗号化された 7z アーカイブのサポートを向上しました。
  * MATE センサーアプレットが (ようやく) udisks2 をサポートします。
  * OpenBSD 認証は MATE スクリーンセーバでサポートされていて、Atril の minizip はより多くの BSD バリアントをサポートしています。
  * 翻訳が更新されました。*翻訳者のチームに感謝します！*
  * また、ディストリビューションのメンテナーの方々にとっては、GTK3+ と GLib の最低要件に行き当たりました。
    * MATE デスクトップ 1.20 をビルドするためには、GTK3.22 と GLib2.50 またはそれ以降が必要です。
  * Wayland ログには Wayland への言及がいくつかあるかもしれませんが、あまり興奮しないでください。それはあなたが考えているようなことではありません `:-)`

MATE デスクトップ 1.20 の各種コンポーネントは、次の場所からダウンロードできます。

  * <https://pub.mate-desktop.org/releases/1.20/>

## Changelog 変更点

変更点の詳細は以下のとおりです。

### mate-desktop 1.20.0

  * ウィンドウのスケーリングファクターに gsettings を追加
  * 最小 GLib バージョンの追加チェックを削除
  * < gtk+-3.22 ビットを削除し、必要な gtk+ バージョンを引き上げ
  * schema: can-change-accels キーを削除。GTK+3 では動作しません。
  * WidthOfScreen と HeightOfScreen の実装
  * `MateAboutDialog` の削除
  * mate-about: libunique 参照の残りを削除
  * mate-about: `GtkAboutDialog` への切り替え
  * gtk3.22: 非推奨の `gdk_screen_get_monitor` 機能を回避:
  * 非推奨の `gdk_screen_get_width/height` を回避
  * mate-desktop-item: mate-about: 非推奨の `gtk_show_uri` を回避
  * mate-about: 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_screen_get_n_monitors` を回避
  * 非推奨の `gdk_screen_make_display_name` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * `man mate-about` のわずかな不正確さを修正
  * `mate-colorsel.c` 内の壊れたフォールバックカーソルを修正
  * mate-colorsel: 非推奨の `GTK_STOCK_COLOR_PICKER` を使用中止
  * グローバルメニューのサポートを追加
  * 翻訳の更新

### mate-user-guide 1.20.0

  * 翻訳の更新

### libmatekbd 1.20.0

  * < gtk+-3.22 ビットを削除し、必要な gtk+ を引き上げ
  * WidthOfScreen と HeightOfScreen の実装
  * matekbd-status: ステータスバーアイコン作成時の Gdk-CRITICAL 警告を修正
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * matekbd-indicator: 拡張しない
  * matekbd-indicator: 非推奨の`gdk_cairo_create`を使用しない
  * GtkIconInfo の奇妙な振る舞いを修正
  * matekbd-indicator: 非推奨の GtkAlignment を使用中止
  * keyboard-drawing: css の名前を matekbd-keyboard-drawing に設定
  * キーラベルのフォントサイズを少し拡大
  * matekbd-keyboard-drawing: ダブルバッファリングを設定を解除しない
  * matekbd-keyboard-drawing: `XkbGetKeyboard()` 失敗時に対処
  * matekbd-keyboard-drawing: gtk+keynav がフォーカスを奪うのを防止
  * イントロスペクションの警告を修正
  * show-layout.ui: 非推奨のウィジェットの使用中止
  * UI: kbdraw を垂直方向に拡張
  * 翻訳の更新

### libmateweather 1.20.0

  * 場所: ポーランド共和国ラドム市を追加
  * 場所: ジュコフスキー空港を追加 (ロシア共和国モスクワ市) を追加
  * 場所: シェレメチェボ空港の名前を修正 (ロシア共和国モスクワ市)
  * タイムアウトを追加し、weather_info_abort でセッションを無効化
  * `weather_info_equal()` 関数の最初の部分を作成することで、WeatherInfo スパムの削減を開始します。この関数は、アプリケーションが2つの天気予報インスタンスが通知を無視できるほど 「同じ」 かどうかを判断するのに役立ちます。
    &nbsp;
    &nbsp;
  * 実際に値をテストして、未使用 bsun の警告を削除します。
  * `soup_session_async_new()` の非推奨警告を修正
  * ポーランドで見落としがあった、空港のある都市を追加
  * Novosibirsk の時間帯を修正
  * プエルトリコに Ceiba を追加
  * doc : 古い MateConf の参考文献やその他の資料を削除
  * カザフスタンの都市を更新
  * 実際に `$GIO_REQUIRED` 変数の値をチェック
  * 翻訳の更新

### mate-icon-theme 1.20.0

  * 同じように壊れたフラグを置き換え
  * 翻訳の更新

### caja 1.20.0

  * GTK+ 3.14 用の CSS を廃止
  * 新しいタブを開いた時にタスクリストアイコンが変わるのを修正
  * <> の代わりに "" を使用してローカルファイルを含めます。
  * 検索の終了後に `search_dispose` および `search_finilize` を実行することはできません。
  * 拡張機能の About ダイアログに不足していたウィンドウアイコンを追加
  * libegg を一番上の srcdir へ移動し、残りの部分を削除
  * WidthOfScreen と HeightOfScreen の実装
  * caja-places-sidebar: サイドバーが広い場合のマウント解除拒否を修正
  * caja-places-sidebar: オーバーレイのスクロールバーを無効
  * 修正: リストビューでファイル名を変更する際の Enterキ ーの誤動作を修正
  * 新規ウィンドウでファイルを開く: <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>w</kbd>
  * zoom-control: マウスホイールのスクロールボタンでズームできるように変更
  * 表示 -> 表示列: ダイアログ内容の垂直方向の展開を修正
  * ディスクサイズの列の説明を少し書き換え
  * 修正: ファイル名の変更を行う際の誤った <kbd>Shift</kbd> + <kbd>Del</kbd> 動作
  * icon-dnd: ハードコードの強調されたを削除
  * 修正: 背景画像の読み込み中に CPU 使用率が高く不具合を修正
  * リストビュー: 拡大時に発生するアイコンの大きな余白を修正
  * デスクトップの壁紙の拡大/縮小がすべてのモニタで機能することを確認
  * ソースファイルから不正な +x 属性を削除
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 列のサイズを自動的に設定する機能を追加
  * 拡大率の変更時にすべての行を更新
  * ズーム時にウィジェットのを再描画を強制
  * pathbar: GTK+2 と同様にマウスホイールのスクロールを有効化
  * libcaja-private: 内部の README からの間違ったリンクを削除
  * private: 信頼できるシンボリックリンクから .desktop ファイルが起動可能なことを確認
  * 修正: デスクトップの壁紙が拡大/縮小できない問題
  * open-with-dialog: ラベルの max-char-width を設定
  * 「開く」ダイアログにおける「開く」ボタンのテキスト位置のずれを修正
  * 推奨されない `gdk_screen_width/height` を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_make_display_name` を回避
  * libegg: 廃止された `gtk_drag_begin` の入れ替え
  * eggsmclient:  -Wcomment によるビルド時の警告を修正
  * 非推奨の `gtk_show_uri` を使用しません
  * 非推奨の `gdk_screen_get_number` を回避
  * 挿入時におけるメディアの閲覧/自動実行を修正
  * `fm_icon_view_scroll_event()` での垂直方向にスクロールするコンパクト表示を修正
  * property-browser: scrolledwindows にスタイルクラスフレームを追加
  * `caja-pathbar.c` における off-by-one エラーを修正
  * 機能の追加: ファイルのサイズを表示する時、ディスク上のサイズを表示
  * DBus インターフェースの初期化を復元
  * CSS: GTK 3.14 で別の caja-desktop.css を読み込み
  * gtk+-3 のブックマークの場所を使用
  * ダイアログで開く: アイコンのサイズを強制
  * file: `caja_file_get_gicon` がカスタムアイコンも返すようにしました。
  * グリッド幅をキャンバスにまで拡張
  * `atk_component_get_extents` を `atk_component_get_position` の代わりに使用
  * 隠しファイルを手動で解析しないでください - 2.36 以降は GIO が実行します。
  * 存在しない `MATE22_USER_DIR` 環境変数をチェックしません。
  * 存在しない `~/.mate2` ディレクトリをチェックしません。
  * eel-accessibility: 使用されていないコードと古いコメントを削除
  * 選択後に正しい右クリックメニューを表示
  * eel: 要素の表示属性が変わると、キャンバス上でのキューサイズを変更
  * IconContainer に size_request を追加し、不要なリレーアウトを回避
  * IconCanvasItem: カーソルを合わせた時、ファイル名が重複するのを修正
  * eel: 不要な #include を条件付きで削除
  * eel: 未使用のコードを eel-gdk-pixbuf-extensions から削除
  * build 時の警告を修正 (そこでは const は必要ありません)
  * gcc 4.9.2 でのビルドを修正 (既定では c89 モードになっているようです)
  * 検索: タグサポート (xattr::xdg.tags) を追加
  * ファイル名のセル選択時に、リストビューの名前変更できない問題を修正
  * property-browser: scrolledwindows にスタイルクラスフレームを追加
  * caja-application.c: 初期化されない変数を修正
  * 翻訳の更新

### mate-polkit 1.20.0

  * polkitgtkmate ライブラリとその文書を削除
  * ステータス通知でのアイコンの再表示/非表示を修正
  * status-icon: ストックアイコンを使用しません。
  * polkitmateauthenticationdialog: 非推奨の GtkAlignment を回避
  * polkitmateauthenticationdialog: 非推奨の GTK_STOCK を置き換え
  * 翻訳の更新

### marco 1.20.0

  * build: 不要な pangoxft の要件を削除
  * move_to_X キーバインドの小さなバグを修正
  * サイズの異なるモニタでのバグを修正
  * モニタのキーバインド再構築と `save_rect` の調整
  * ウィンドウを別のモニタに移動するために簡単なショートカットを実装
  * schema: タイピングミスの修正
  * コンポジタ: 表示不能なウィンドウを描画しません。
  * フレームのないウィンドウでの `meta_window_titlebar_is_onscreen()` の誤った結果を修正
  * gtk3 の `_GTK_SHOW_WINDOW_MENU` イベントのサポートを追加
  * 新しいワークスペースへの移動キーバインドを処理するため、より洗練された方法を採用
  * トップのタイリングを無効にする設定を実装
  * ウィンドウを別のワークスペースに移動する際、タブのポップアップを実装
  * keybindings.c: ビルド時の警告を修正
  * 全画面表示のとき、tile_resized を false にリセット
  * ウィンドウを最大化しない時、`save_rect` にならない問題を修正
  * コーナーを並べて表示するとき、水平方向と垂直方向のサイズ変更を可能に
  * コーナーを並べないとき、ウィンドウが saved_rect にリセットされる問題を修正
  * コーナーに並べる場合のキーバインドを追加
  * マウスのドラッグによる簡単なコーナーへのタイリングを実装
  * WidthOfScreen と HeightOfScreen の実装
  * XFIXS 領域が paint_windows の実行中にリークします。
  * XPresent サポートなしで実行するために、より厳密なロジックを追加
  * XPresent のオプション化
  * xfwm4 からの一部変更を算入
  * エラー発生時に present_pending のフラグを解除
  * XPresent の拡張機能をサポート
  * ユーザーがタイル表示からサイズ変更した時、ウィンドウフラグを保存
  * 並べて表示したウィンドウが水平方向にサイズ変更可能に
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 推奨されていない `gdk_screen_width/height` を回避
  * 非推奨の `gdk_screen_get_width` を回避
  * display: 廃止された `GDK_DEVICE_MANAGER` を使用しません。
  * tools: marco-mag と marco-grayscaletools を削除
  * 合成 keybinding/button-grab ウィンドウを修正
  * 既定またはユーザ設定のスケールを使用する代わりに、ウィンドウマネージャのウィンドウスケールをを強制的に 1 に設定します。
  * 非推奨の `gdk_display_get_screen` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * Alt/tab - 矢印キーコード + テンキーの矢印を定義
  * <kbd>Alt</kbd> + <kbd>Tab</kbd> ポップアップ中に矢印の使用が可能になりました。
  * ui: フレーム内の無効なオブジェクト構築を修正
  * README: GSettings キーの名前を修正
  * キーバインド: 「現在のワークスペース」から大文字を削除
  * 現在のワークスペース名を変更するホットキーを追加
  * 非推奨のコードを修正
  * 翻訳の更新

### mate-settings-daemon 1.20.0

  * HiDPI: 初期化段階で xsettings を読み込みます。
  * XSettings に HiDPI の設定を追加
  * HiDPI ディスプレイへの対応を追加
  * プラグイン: `_GNUC_UNUSED` は未使用ですが必要な変数です。
  * xsettings: GTK+3 で動作しない CanChangeAccels を削除
  * msd-datetime-mechanism.c: ビルド時の警告を削除
  * msd-mpris-manager.c: ビルド時の警告を削除
  * configure.ac: `GLIB_VERSION_MAX_ALLOWED` を削除
  * 翻訳の更新

### mate-session-manager 1.20.0

  * gsm-manager.c: ビルド時の警告を削除
  * ログアウトまたはシャットダウン時のダイアログ表示で、フォーカスを失わないようにしました。
  * スタイルクラス `logout-dialog` を追加
  * 非推奨の `gdk_screen_make_display_name` を回避
  * 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * セッション開始時にすべてのユーザー定義環境を取得するには、systemd user-session を更新する必要があります。
  * セッション開始時にすべてのユーザー定義環境を取得するには、dbus を更新する必要があります。
  * 翻訳の更新

### mate-menus 1.20.0

  * gio のバージョンを 2.50.0 に上げました。
  * mate-applications-merged をシンボリックリンクに
  * 翻訳の更新

### mate-panel 1.20.0

  * HiDPI ディスプレイでのパネルの自動スケールに対応
  * 必要最低限の libwnck バージョンを 3.4.6 へ上げました。
  * status-notifier: ツールチップのタイプが違ってもクラッシュしないように
  * status-notifier: メニューレイアウトが正しくなくてもクラッシュしないように
  * ステータス通知のラジオボタンの描画を修正
  * panel-run-dialog: プログラムリストが有効な場合に不具合を修正
  * 「壊れたアプレット」ダイアログを表示する時はフォーカスを取得
  * ワークスペース切替プロパティのダイアログを更新
  * コードの一部を単純化
  * 背景の変更操作を取り消すプロセスを作り直し
  * status-notifier: アイテムの NULL ケースを適切に処理
  * status-notifier: パスによって呼び出された間違ったサイズのアイコンの処理
  * status-notifier: パスで指定されたアイコンを読み込む
  * アプリケーションがアイコン名ではなくパスを要求した場合、アイコンを読み込めない問題を修正
  * ビルド時の警告を修正: `toplevel_configure_event` defined but not used
  * ビルド時の警告を修正: `GLIB_VERSION_MIN_REQUIRED` redefined
  * status-notifier: アイコンが見つからない場合の表示を修正
  * WidthOfScreen と HeightOfScreen の実装
  * panel-toplevel: `panel_toplevel_queue_auto_hide()` でのポインタ境界チェックを削除
  * 以前から存在する gnome-panel の残りを削除
  * 解像度を大きく変更しても、右側のアイコン表示位置を維持
  * wncklet: 破壊時のデータによる信号の切断
  * clock: 破棄時にもう 1 つのシグナルハンドラを切断
  * panel-applet-frame-dbus-c: 新規未使用の変数をコメントアウト
  * Clock: <0 に対して <0 になり得ない変数はチェックしません。
  * panel-applet-frame-dbus.c: 使用されていないコードブロックをコメントアウト
  * panel-toplevel: 重複した break 文を削除
  * status-notifier: cppcheck によって検出された重複チェックを削除
  * status-notifier: パッシブな場合は mate-polkit アイコンを非表示
  * ポップアップの位置修正を GTK 3.20 以前に適用
  * GTK 3.22 ステータス通知: サイズ変更時にメニューを再配置
  * GTK 3.22/status-notifer: 前回の表示以降にサイズが変更された場合、メニューの位置を修正
  * 特定のプロセス外のアプレットを追加した時、パネルが壊れないようにしました。
  * ファイル/フォルダのランチャーが再び動作するようにしました。
  * panel-context-menu: パネルリセットオプションに確認ダイアログを追加
  * パネルのコンテキストメニューに「パネルのリセット」を追加
  * clock: 壊れた時にシグナルハンドラを切断
  * GLib 2.53.4 以降を使用してアプレットを移動/削除するとクラッシュする問題を修正
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * SNI サポートを有効/無効にするための gsettings キーを追加
  * wncklet: セグメンテーションの不具合、インプロセススイッチャとメニューリストの削除に関する警告を停止
  * fish: 削除後に元に戻る問題を修正
  * Fish: ビルドのプロセス中における削除に係るすべての警告を停止
  * Clock: 処理中のアプレットが削除された時の削除警告を修正
  * clock: ビルド実行中にアプレットを削除する時、セグメンテーション違反となるのを停止
  * libmate-panel-applet: タイプミスの修正 in id->factory_id
  * libmate-panel-applet: 必要な場合のみ、`_panel_applet_shlib_factory()` を宣言
  * libmate-panel-applet: dbus オブジェクトの登録解除中のエラーを修正
  * libmate-panel-applet: ビルド時の警告を修正
  * libmate-panel-applet: イントロスペクションの修正
  * libmate-panel-applet: 不明なバス名を修正し、dbus オブジェクトの登録解除
  * libmate-panel-applet GTK 3.14/3.16: custom bg w alpha の修正
  * libmate-panel-applet: 特定アプレットのファクトリにダミー変数を含めます。
  * libmate-panel-applet: プロセス中アプレットの背景描画を修正
  * libpanel-applet/panel-applet.h: ファクトリの ID を `factory_id` へ変更
  * libmate-panel-applet: panel-applet-private.h の追加
  * 実行中のアプレットに GtkPlug/GtkSocket を使用しません。
  * アプレットのウィジェットを取得できるようにしました。
  * libpanel-applet: `panel_applet_factory_get_applet_widget` の追加
  * libpanel-applet: プロセスの種類とアプレットの UID を返します。
  * libpanel-applet: ハッシュテーブルにファクトリを保存
  * libpanel-applet: GtkPlug の作成を遅延
  * libpanel-applet: プロセスの種類をプライベートデータへ追加
  * libpanel-applet: `panel_applet_factory_main()` から `out_process` を削除
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_get_n_monitors` を回避
  * fish: ビルド実行中にアプレットが細いラインで開くのを修正
  * 既定またはユーザ設定のスケールを使用する代わりに、パネルのウィンドウスケールをを強制的に 1 に設定します。
  * 非推奨の `gdk_screen_make_display_name` を回避
  * 非推奨の `gdk_display_get_screen` を回避
  * 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * 透過性の user-set パネル背景でアプレットがクラッシュする問題を修正
  * システムトレイ: 画像/透過色の背景上の非表示アイコンを修正
  * 垂直パネル上における、GTK テーマの画像背景サポートを修正
  * GTK テーマでのパネル画像の背景が再び機能します。
  * clock: 時間帯の文字上にカーソルを置くとパネルが画面の制限を超えて拡大する問題を修正
  * GTK 3.18+: 既定の透過性パネルの背景を修正
  * menu: メニュー項目を外にドラッグ&ドロップした後でフォーカスを回復
  * menu: メニュー項目のポップアップメニューを閉じた後にフォーカスを回復
  * 修正: メニューバー/メニューボタンで mozo が起動しない問題
  * menu: メニュー項目のポップアップメニューから誤ったコードを削除
  * ステータス通知: パネルの他の部分と同じメニューテーマに追従
  * パネル間でのアプレットの移動を修正
  * menu: 一部の .desktop ファイルに空のアイコンフィールドがある場合にクラッシュする問題を修正
  * clock: 編集ボタンの視認性を適正に処理
  * clock: 非推奨の `gtk_size_group_set_ignore_hidden` を削除
  * clock: GtkButton を別の水平な GtkBox の元へ移動
  * clock.c: 非推奨の `gtk_size_group_set_ignore_hidden` を削除
  * アプリケーションの名前と説明をローカライズ
  * menu-button: アプレットが削除された時は GSettings から切断
  * action-button: アプレットが削除された時は GSettings から切断
  * 不必要な glib のチェックを削除
  * ステータス通知: 不明なシグナル名でのクラッシュを修正
  * 場所メニューに GTK+3 のブックマークの位置を使用
  * doc: 存在しないものへの参照を一部削除
  * gcc 4.9.2 でのビルドを修正 (既定では c89 モードになっているようです)
  * 実行ダイアログ: 履歴表示を反転させるオプションを追加
  * 実行ダイアログ: 最大サイズ 1 の不正な履歴の長さを修正
  * 実行ダイアログ: 履歴サイズの変更を許可
  * doc: 古い MateConf の参考文献を削除
  * 実行ダイアログ: 誤った履歴順序の修正
  * ステータス通知: パッシブ項目を表示
  * パネルメニューバー: ビルド警告と一部のスペースを修正
  * 展開したパネルをより小さな画面サイズに適合
  * システムトレイ: 方向の変更を適切に伝達
  * 通知エリア: アイテムの向きを修正
  * ワークスペース切替: `GDK_SCROLL_SMOOTH` の処理とビルド警告の修正
  * ワークスペース切替のラッピングを再度有効化
  * プレバンプバージョン
  * スタイルの通知: icon-padding スタイルのプロパティを修正
  * WM でのパネル切り替え時に表示されるパネルの説明を簡略化
  * ステータス通知: メモリリークを防止
  * 使用されていない `sys/timeb.h` ヘッダを削除
  * status-notifier-watcher: 登録済みアイテムの再登録を許可
  * カスタムアイコンの設定
  * ステータス通知: メモリリークの防止
  * 通知エリア: メモリリークの分類項目を修正
  * 翻訳の更新

### mate-backgrounds 1.20.0

   * 以前から存在する gnome-panel の残りを削除
   * 翻訳の更新

### mate-themes 3.22.8 から 3.22.15 へ

  * サブマリンテーマ: engrampa のツールバーで box-shadow を削除
  * サブマリンテーマ: caja-sidebar ツリービューからパディングを削除
  * all themes caja: スクロールウィンドウの枠から右側の境界線を削除
  * Menta metacity テーマ: 最大化時にウィンドウの左/右境界線を削除
  * ブラック MATE: スクロールバーの谷に境界線を書き込みます。
  * すべてのテーマ: スクロールウィンドウの枠から右側の境界線を削除
  * サブマリンテーマ: ヘッダバーの button.suggested-action の前景色を修正
  * ブラック MATE: Yelp/Lireoffice/Firefox でのスクロールバーの問題を回避
  * 「Gtk+-3.20 all themes: Yelpでの再描画の問題修正」を元に戻しました。
  * TOK/TG: スライダ: 元のサイズを維持
  * Gtk+-3.20 サブマリン: サイドバーの treeview.selected/hover で境界の半径を小さくしました。
  * Gtk+-3.20 サブマリン: スピンボタンエントリのフォント色を設定
  * Gtk+-3.20 サブマリンテーマ: gitg のヘッダバーでのジャンプボタンを修正
  * Gtk+-3.20 サブマリンテーマ: caja-icon-view で dnd を設定
  * Gtk+-3.20 T. テーマ: mate-volume-control notebook における二重枠の修正
  * Gtk+-3.20 サブマリンテーマ: pluma-statusbar-button のフォーカス状態を修正
  * Gtk+-3.20 の多くのテーマ: メニュー項目のアクセラレータホバーをデザイン
  * すべてのテーマ: mate-1.20 用のパネルグリッドのイメージをロードするため、シンタックスを変更
  * Gtk+-3.20 サブマリンテーマ: トップの borderradius を .titlebar > headerbar へ設定
  * Gtk+-3.20 の多くのテーマ: GtkEntry のプライマリ/セカンダリイメージでのパディングを修正
  * Gtk+-3.20 TRAD テーマ: メニューの grey-out arrows の色を修正
  * TOK/TG: radio mixed というメニュー項目を追加
  * TOK/TG メニュー項目: checkboxes とラジオボタンを再度デザイン
  * Gtk+-3.20 の多くのテーマ: スライダが範囲外の場合に GtkScale スライダのマウス選択を修正
  * Gtk+-3.20 すべてのテーマ: yelp での再描画の問題を修正
  * Gtk+-3.20 グリーンラグナ: 一部のメニューを修正
  * Gtk+-3.20 Menta テーマ: メニューの矢印にトランジション効果を追加
  * Gtk+-3.20 Menta テーマ: Firefox メニューの設定を削除
  * Gtk+-3.20 サブマリンテーマ: ラベルからトランジション効果を削除
  * gtk+ ハイコントラストテーマ用の index.theme ファイルを追加
  * Gtk+-3.20 の多数のテーマ: 時計アプレットの clockmap 境界を設定
  * Gtk+-3.20 サブマリンテーマ: 時計アプレットの一部を修正
  * Gtk+-3.20 BlackMate: 一部のパネルクロック修正
  * TOK/TG: caja: ノートブックのヘッダーの境界を単色で表示
  * Gtk+-3.20 Menta テーマ: ツールヒントにハードコードされた背景色を使用
  * BlackMATE: CSD アプリケーションを合成されていないヘッダーバーを四角形のウィンドウ枠に一致
  * BlackMATE: 多数の CSD アプリケーション修正
  * BlackMATE: CSD アプリケーションの修正
  * Gtk+-3.20 Menta テーマ: パネルアプレットのボタン色を変更
  * Gtk+-3.20 Menta テーマ: メニューバーのメニュー項目の移行時間を変更
  * Gtk+-3.20 Menta テーマ: パネルに通常のメニューバーのメニュー項目スタイルを使用
  * Gtk+-3.20 Menta テーマ: メニュー項目からトランジション効果を削除
  * TOK/TG: mate-terminal:: ノートブックのヘッダーの境界を単色で表示
  * Gtk+-3.20 BlackMATE: Google Chrome における URL バーのフォント色を修正
  * Gtk+-3.20 BlackMATE: メニュー項目でのアクセラレータのフォント色を変更
  * TOK/TG: xfce4-terminal: ノートブックのヘッダー境界を単色に
  * TOK/TG: ノートブックのヘッダーからグラデーションを削除
  * カーソル: ファイル作成にカラーピッカーを追加
  * Gtk+-3.20 サブマリンテーマ: pluma のサイドバーを改善
  * Gtk+-3.20 サブマリンテーマ: pluma のエラーダイアログにおける前景色を修正
  * ブラックMATE: 完全なノンコンポジット m-s-d OSD をデザイン
  * ブラックMATE: 非コンポジット OSD ケースにて、新しい msd-osd-window-solid スタイルクラスをサポート
  * ブラックMATE: Caja のラベル名変更を読みやすくしました。
  * ハイコントラストの反転: テーマが実際に適用された時の Caja のリネームラベルを修正
  * カーソル: カラーピッカーのカーソル画像を追加
  * GTK+-3.20 サブマリンテーマ: mate- と mintmenu の改善
  * Gtk+-3.20 menta テーマ: mate- と mint-menu の改善
  * Gtk+-3.20 伝統的テーマ: 一部のダイアログウィンドウを改善
  * 伝統的テーマ: MATE インジケータアプレットの背景を描画しません。
  * Gtk+-3.20 の多数テーマ: caja の非表示ペインのリストビューで背景色を修正
  * Gtk+-3.20 すべてのテーマ: 新しい css 名 matekbd-keyboard-drawing を追加
  * metacity サブマリンテーマ: metacity または compiz WMが使用されている場合は、内枠を修正
  * TOK/TG: xfce4-terminal: ノートブックのヘッダー境界を階調色に
  * TOK/TG: ノートブックのタブの余白を 2 ピクセル大きくします
  * menta: "{{" typo で gtk-widgets.css ファイルが壊れる問題を修正
  * すべてのテーマ: 印刷ダイアログの用紙の描写が正しく表示されない問題を修正
  * Gtk+-3.20 Menta テーマ: バックドロップと通常の状態を区別しない
  * Gtk+-3.20 多数のテーマ: Mate-Panel の非表示ボタンを修正
  * TOK/TG: caja ではノートブックのヘッダー境界に階調色を設定
  * Gtk+-3.20 サブマリンテーマ: Mate-Panel の非表示ボタンを修正
  * TOK/TG: xfce4-terminal のタブと多分他のアプリケーションについても境界を修正
  * Gtk+-3.20 すべてのテーマ: mate-menu の改善
  * Gtk+-3.20 すべてのテーマ: キーボードレイアウトのデザインを改善
  * TOK/TG: mate-terminal: ノートブックのヘッダー境界を階調色に設定
  * Gtk+-3.20 トラディショナル: mate-terminal でノートブックのヘッダー境界に色を設定
  * Gtk+-3.20 Menta テーマ: mate-applications.css の分類
  * Menta テーマ: ノートブックのヘッダーの境界に色を設定
  * TOK/TG: パネルグリッドに新しい色を採用
  * Gtk+-3.20 すべてのテーマ: mate-keyboard-layout-viewer のデザイン
  * 伝統的テーマ - Menta のアプレットハンドルを使用
  * TOK/TG: mate-terminal: ノートブックの代わりにヘッダータブの枠線を使用
  * Gtk+-3.20 ハイコントラストの反転: 不足しているアセットを追加して実行時警告を回避
  * Menta テーマ: ロック画面における不適切な枠線の色を削除
  * Gtk+-3.20 サブマリン: ロック画面における不適切な枠線の色を削除
  * グリーンラグナ: MATE 端末のノートブックタブ境界を修正
  * サブマリンテーマ: MATE 端末のノートブックタブ境界を修正
  * Gtk+-3.20 Menta テーマ: MATE 端末のノートブックタブ境界を修正
  * 伝統的テーマ: MATE 端末の見かけ向上のために一部の行を削除
  * Gtk+-3.20 多数のテーマ: ノートブックの端末には境界線を使いません。
  * 伝統的テーマ: 印刷ダイアログの改善
  * 伝統的テーマ: pavu-control 用にノートブックの境界を設定 (適切に修正)
  * 伝統的テーマ: pavu-control 用にノートブックの境界を設定
  * Gtk+-3.20 グリーンラグナ: スクロールバーの接合部をデザイン
  * Gtk+-3.20: Firefox 用の煩わしいワイルドカードを追加
  * Gtk+-3.20 グリーンラグナ: caja サイドバーの一部の境界を修正
  * Gtk+-3.20 グリーンラグナ: GtkSwitch のボーダーの色を変更
  * Gtk+-3.20 グリーンラグナ: スクロールバーのボーダーの色を変更
  * GTK+-3.20 グリーンラグナ: insensitive_bg_color の変更
  * Gtk+-3.20 グリーンラグナ: ネットブックの改善
  * 伝統的テーマ: ノートブック内の不要な 2 行を削除
  * Gtk+-3.20 グリーンラグナ: フレームの境界部分の書き直しとその他の改善
  * グリーンラグナ metacity: ボーダーサイズの拡大
  * サブマリン metacity: ボーダーサイズの拡大
  * Gtk+-3.20 Submarine: リストの行の dim-labels に色を設定
  * 伝統的なテーマ: チェックマークが付いたノートブックのタブで、より多くの境界線の色を設定
  * Gtk+-3.20 サブマリンテーマ: ステータスバーにパディングを設定
  * Gtk+-3.20: mate-font-viewer ツールバーのジャンプボタンを修正
  * GTK+-3.20 サブマリンテーマ: ヘッダーバーとポップオーバーメニューの改善
  * Gtk+-3.20 サブマリンテーマ: gedit ステータスバーのパディングを設定
  * Gtk+-3.20 Menta テーマ: button.fat に不足していた border-image を追加。filezilla と atril で確認済み
  * Gtk+-3.20 Menta テーマ: ノートブックの一部改善
  * Firefox の検索候補に表示される URL の色を修正
  * Gtk+-3.20 Menta テーマ: フレームの境界部分の書き直しとその他の改善 (mega commit)
  * 伝統的なテーマ: ノートブックのタブのパディングを小さく
  * Gtk+-3.20 サブマリンテーマ: 複数の改善
  * Gtk+-3.22 サブマリンテーマ: ノートブックの一部改善
  * Gtk+-3.22 サブマリンテーマ: フレームのボーダーを再作成
  * Gtk+-3.20 サブマリンテーマ: rubberband の前回のコミットを修正
  * Gtk+-3.20 サブマリンテーマ: mate-screenshot の rubberband を修正
  * Gtk+-3.20 サブマリンテーマ: ツールバーのラベルカラーを修正
  * 伝統的なテーマ: アクティブなタブで階調色を使用
  * Gtk+-2.0 グリーンラグナ: gtkrc でハードコードされた 16 進数の色を使用
  * Gtk+-2.0 の多くのテーマ: gtkrc で色定義に oneliner を使用
  * 伝統的なテーマ: 一部のアプレットに border-image を追加
  * Gtk+-3.20 伝統的なテーマ: GtkInfobar 全体に境界を使用
  * Gtk+-3.20 伝統的なテーマ: Firefox で一部の境界を修正する回避策
  * Gtk+-3.20 伝統的なテーマ: コンボボックスボタンのジャンプを修正
  * Gtk+-3.20 多くのテーマ: GtkAssistant のサイドバーを修正
  * Gtk+-3.20 サブマリンテーマ: GtkAssistant のサイドバーを修正
  * Gtk+-3 すべてのテーマ: NaTrayApplet-icon-size を設定しません

### mate-notification-daemon 1.20.0

  * WidthOfScreen と HeightOfScreen の実装
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_get_n_monitors` を回避
  * タイムアウトが大きい場合に CPU 使用率が高くなるのを修正
  * アイコンファイルの URI-encode パスをアンエスケープ
  * 翻訳の更新

### mate-control-center 1.20.0

  * HiDPI ディスプレイ用にフォントの DPI を拡大
  * HiDPI ディスプレイへの対応を追加
  * theme-installer.c: `mate_theme_install_real` に `g_object_unref` がありません
  * theme-util.c: 削除したテーマの再インストールで失敗する問題を修正
  * XZ 形式をインストールするためのテーマ圧縮パッケージをサポート
  * 使用しない変数を削除
  * eggcellrendererkeys.c: ビルド時の警告を削除
  * MacOS のサポートに関連した一部の残骸を削除
  * theme-thumbnail.c: `write` と `pipe` でのビルド時の警告を修正
  * libslab: 検索エントリウィジェットを `GtkEntry` として格納
  * libslab: 検索アイコンの位置ずれを修正
  * 翻訳の更新

### mate-screensaver 1.20.0

  * ロック画面の HiDPI サポートを追加
  * gs-lock-plug.c: ビルド時の警告を修正
  * WidthOfScreen と HeightOfScreen の実装
  * mate-screensaver-command の正しい manpage を復元
  * 初期設定のループを修正
  * 修正: すべての言語でアイドルスライダを表示
  * glib が最大バージョンを要求するのを削除
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gtk_show_uri` を回避
  * `bsd_auth(3)` を使って OpenBSD 認証を実装しました。
  * バグ修正: `g_get_real_name` は決して NULL ポインタを返しません
  * lock-dialog UI: 非推奨のウィジェットを回避
  * バグ修正: モニタジオメトリがオーバーラップした構成で、スクリーンセーバとロック画面が正しく表示されない問題
  * [GTK+3.20] GdkSeat へ切り替え
  * パスワード入力ウィジェットに入力目的を設定
  * コピーテーマダイアログ: 変数タイプの誤りに関するビルド警告を修正
  * 翻訳の更新

### mate-media 1.20.0

  * gvc-applet: NULLオブジェクトの refcount を増やしません
  * gvc-combo-box: シグナルの引数を修正
  * アプレット: 「サウンド設定」メニューのアイコンを復元
  * 非推奨の `gdk_screen_get_height` を回避
  * アプレット: GTK+ >= 3.20 で GdkSeat を使用
  * アプレット: ポップアップでキーボードが機能します
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * アイコンテーマの変更時にトレイアイコンを更新
  * ミキサダイアログ: scrolledwindow よりスタイルクラスフレームを削除
  * 音量調節ダイアログ: 非推奨の GtkAlignment を回避
  * アプレット: 音量をミュートしてもポップアップで表示
  * アプレット: 音量の増加量を改善
  * 非推奨警告を既定で有効化
  * 翻訳の更新

### mate-power-manager 1.20.0

  * 非推奨の GtkStock を回避
  * inhibit: 先のコミットにおけるスパムログのエラーを修正
  * inhibit applet: アイコンの描画を修正
  * WidthOfScreen と HeightOfScreen の実装
  * さらに指摘のあったタイプミスを修正
  * 綴りの間違いを訂正しました。
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 不明な DBus シグナル名では中断しません
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_display_get_screen` を回避
  * 非推奨の `gtk_show_uri` を回避
  * アイコンテーマの変更時にトレイアイコンを更新
  * 実際に `$XPROTO_REQUIRED` 変数の値をチェック
  * statistics UI: スタイルクラス mpm-statistics の追加
  * 翻訳の更新

### mate-system-monitor 1.20.0

  * procman.cpp: ビルド警告の引数 1 が null で、non-null が期待される部分を修正
  * sysinfo.cpp: 次のビルド時警告を修正: this ‘if’ clause does not guard...
  * proctable.cpp: 次のビルド時警告を修正: this ‘else’ clause does not guard...
  * システムロゴの位置を修正
  * WidthOfScreen と HeightOfScreen の実装
  * プロセステーブル: 大文字と小文字を区別をしないで検索
  * sysinfo: すべてのラベルでフォーカスを無効化
  * 非推奨の `gdk_screen_width/height` を回避
  * sysinfo: 非推奨の GtkAlignment を回避
  * 翻訳の更新

### atril 1.20.0

  * build: GTK+3 以前のオプションを削除
  * epub: minizip がより多くの BSD バージョンに対応
  * previewer: スタイルクラス atril-previewer-window を追加
  * WidthOfScreen と HeightOfScreen の実装
  * シェル: メニューにキャレットナビゲーションを表示
  * ev-link-accessible: 開始と終了のインデックスを取得する方法の効率を改善
  * フォームフィールドをそのページの AtkObject の子として表示
  * 画像をページの AtkObject の子として公開
  * リンクをページの AtkObject の子として公開
  * ev-view-accessible: 特定の文書の矩形が表示されているかどうかの判別方法を追加
  * ev-page-cache: 指定したページがキャッシュされているかチェックする方法を追加
  * libview: 検索結果にジャンプする時、キャレットカーソルを更新
  * libview: 表示されるページ範囲が変更されたとき、`ATK_STATE_SHOWING` を更新
  * libview: ページに AtkComponent を実装
  * libview: Shift+クリックによるテキスト選択を修正
  * a11y: EvPageAccessible を要求したときはテキストがキャッシュされます
  * a11y: EvPageAccessible で atk の状態を管理
  * a11y: EvPageAccessible に ATK_RELATION_FLOWS_TO/FROM を適用する場合は追加
  * a11y: AtkHyperText の実装を EvViewAccessible から EvPageAccessible へ移動
  * a11y: AtkText の実装を EvViewAccessible から EvPageAccessible へ移動
  * a11y: EvPageAccessible を EvViewAccessible の子として公開
  * a11y: 新しい EvPageAccessible
  * libview: EvViewAccessible テキストサポートの一部の壊れた部分を修正
  * libview: AtkHyperlink インデックスを取得する際、キャレットナビゲーションを考慮
  * a11y: `atk_text_get_caret_offset` の実装を整理
  * a11y: `atk_text_get_caret_offset` の実装を修正
  * view: set_caret_cursor_position が適用された場合に "cursor-moved" と表示
  * 非推奨の `atk_text_get_text_{before,after}_offset()` への対応を削除
  * a11y: EvViewAccessible に AtkDocument を実装
  * a11y: キャレットナビゲーションが有効な場合、操作支援の現在のページはカーソルページになります。
  * ev-view-accessible: モデル設定時に `document_changed_cb` を呼び出します。
  * キャレットメッセージ領域の一部のテキストを修正
  * ev-view-accessible: `ev_view_accessible_get_link` でのクラッシュを修正
  * ev-view-accessible: 現在のページでキャッシュされたデータをクリア
  * shell: `view_actions_focus_out_cb` を削除
  * shell: `ev_window_set_view_accels_sensitivity` を削除
  * shell: フォーカスのあるウィジェットに順方向に加速
  * view accel アクションにグローバル配列を使用
  * djvu 文書内のテキストを選択した時クラッシュする問題を修正
  * shell: メッセージ領域のストックアイテムを修正
  * docs: libview: type builtins セクションの再追加
  * キャレットナビゲーション付きの epub 文書でのクラッシュを修正
  * キャレットカーソルの位置を文書のメタデータに保存
  * libview: `ev_view_set_caret_cursor_position` の追加
  * libview: スクロールで場所を検索しているあいだでも、現在のページを更新
  * libview: キャレットナビゲーションを有効/無効にした時、再描画のスケジュールを設定しません
  * libview: カーソルが表示されているページにない時にはキャレットカーソルの点滅を停止
  * shell: F7 キーを押すとキャレットナビゲーションが有効/無効化
  * libview: `ev_view_supports_caret_navigation()` の追加
  * ev-link-accesible: リンク内の最後の文字の後のインデックス/オフセットを返します
  * help: 除去された選択モードへの参照を削除
  * libview: ページ余白での開始/終了を修正
  * libview: 選択の際にスキャンするページを減らしました
  * libview: 使用しない矩形選択モードを削除
  * libview: ev_view_accessible_get_selection の作り直し
  * libview: キャレットカーソルが移動する時はビュー全体を再描画しません
  * libview: 行間移動時には、カーソルを配置した後でカーソル領域を更新
  * ev-view-accessible: `ev_view_accesssible_get_n_selections` の修正
  * ev-view-accessibl: キャレットナビゲーションが有効な時の get_caret_offset を修正
  * libview: 行間の移動が失敗した時は、エラーベルを使用してすぐ戻ります
  * libview: `ensure_rectangle_is_visible` でサイズ変更を予定しません
  * libview: 選択肢がある時はカーソルの点滅を停止
  * libview: ev_view_scroll を廃止して `g_signal_emit_by_name` を採用
  * ev-window: `ev_view_scroll` の代わりに g_signal_emit_by という名前を使用
  * previewer: スクロールアクセラレータを削除
  * ev-window: スクロールアクセラレータを削除
  * libview: スクロールキーのバインドを EvView へ追加
  * libview: h、j、k、l バインディングに対して、スクロールシグナルの第2パラメータのタイプを修正
  * libview: NULL を渡す merge_selection_region を使って選択を消去
  * ev-pixbuf-cache: ジョブ選択をクリアするときにも選択領域をクリア
  * ev-pixbuf-cache: 新しい選択が必要なときの条件を修正
  * ev-view-accessible: get_run_attributes を書き直して、文書のテキスト属性を返すようにしました
  * pdf: `ev_document_text_get_text_attrs()` の実装
  * libview: バックエンドからテキスト属性を取得し、ページキャッシュへ保存
  * libdocument: `ev_document_text_get_text_attrs()` の追加
  * libview: AtkText text-caret-moved および text-selection-changed シグナルを出力
  * libview: カーソルを移動したときは選択を解除
  * libview: アクティブな選択がある場合、キャレットカーソルを非表示
  * libview: pixbuf キャッシュから空の領域の代わりに NULL を返します
  * libview: ビューがフォーカスされていない時はキャレットカーソルを描画しない
  * libview: 列が複数ある文書内におけるキャレットカーソルの行間移動を修正
  * libview: 現在のページ範囲に複数の前後ページをプレキャッシュします。
  * ev-pixbuf-cache: スクロール方向に応じて、前または次のジョブを最初にスケジュールします
  * ev-pixbuf-cache: 前のページを逆の順序で描画するようにジョブをスケジュール
  * libview: キャレットカーソルが移動したことを通知する `cursor-moved` シグナルを追加しました。
  * libview: テキストを選択する時、不要な領域のコピーを回避
  * libview: より大きなダメージ領域を使用して選択を再描画
  * libview: 破損領域が変更されていない場合は再描画をキューに入れません
  * libview: 新旧選択の統合を無効化
  * libview: 選択範囲の外側をクリックした時はキャレットカーソルを移動
  * libview: 未使用の in_selection メンバを SelectionInfo 構造から削除
  * libview: 行間でキャレットを移動する場合は、オフセットを行の内側に保持
  * libview: 行の冒頭/末尾にキャレットカーソルを配置
  * libview: すべてのテキスト選択時は再描画のスケジュールを非設定
  * libview: 選択リストの作成には、append の代わりに prepend + reverse を使用
  * libview: GSslice を使用して EvViewSelection を割当て
  * libview: キャレットカーソルを使用してテキストを選択します。
  * libview: マウスでテキストを選択した後はキャレットカーソルを更新
  * libview: 選択を計算するとき、ページ境界線を考慮
  * libview: 複数のページを選択した時クラッシュする問題を修正
  * libview: カーソルをクリックして移動後、カーソルが点滅するようにしました
  * libview: `get_caret_cursor_rect_from_offset` と `get_caret_cursor_area` を統合
  * libview: エラーのベル音にて、キャレットナビゲーションのエラーを通知
  * libview: カーソル位置が変更されていない場合は、クリック後に再描画しません
  * libview: カレットナビゲーションに GtkBindings を使用
  * libview: EvView::binding-activated シグナルを EvView::scroll へ名前変更
  * libview: クリックすることでキャレットカーソルを配置
  * libview: `EvPixbufCache` を使用して選択領域を検索
  * libview: `ev_pixbuf_cache_get_selection_surface` を 2 つの関数に分割
  * libview: 領域から選択したハイライトを描画
  * libview: キャレットカーソルの再描画に使用される損傷領域を修正
  * libview: 別のページから対象を移動した時、実際にページを更新
  * libview: キャレットカーソルが更新されていない場合、現在のページを更新せず、カーソル位置までスクロール
  * libview: キャレットカーソルを点滅させます
  * libview: テキストレイアウトのかわりに論理属性を使用して、キャレットカーソルを移動
  * libview: ページキャッシュからテキスト論理属性を取得する方法を追加
  * libview: キャレットナビゲーションを初めて実装
  * libview: 描画ページと選択面のコードをリファクタリング
  * shell: epub のメニューで `ViewDualOddLeft` を無効化
  * libview: 高さ要求に関連するページキャッシュにのみアクセス
  * デュアルレイアウトと連続レイアウトのショートカットキーを有効化
  * ev-view: キーイベントをフォーカスされたフォームフィールドに転送
  * ページに合わせる、幅に合わせる、というオプションのショートカットキーを追加
  * shell: 既定では 1 ページだけの PDF をデュアルモードで開きません
  * libview: current_page を負の数値に更新しません
  * libview: ページレイアウトのモード化
  * libview: 可読性を最適化するために新しいズームモードを追加
  * Fit Page Width を Fit Width へ名前変更
  * Best Fit mode を Fit Page へ名前変更
  * 表示メニューに奇数ページを残してデュアルページを移動
  * libview: 非推奨となった gtk_container_set_resize_mode の使用を削除
  * shell: キャストする前に文書が注釈のインタフェースを実装しているかチェック
  * 削除時には注釈のサイドバーを更新
  * libdocument: `ev_mapping_list_remove` の無効化
  * page-cache: `ev_page_cache_mark_dirty()` へ flags パラメータを追加
  * pdf: 注釈がなくなった時は、注釈マッピングをリセット
  * ビューポップアップメニューに注釈を削除するオプションを追加
  * libview: ev_view_remove_annotation の追加
  * pdf: remove_annotation 仮想機能を実装
  * libdocument: ev_mapping_list_remove の追加
  * libdocument: remove_annotation を DocumentAnnotations へ追加
  * pdf: 注釈の名前を一意に
  * pdf: 他のタイプの注釈を追加するためのサポートを追加
  * libview: ev_view_set_focused_element と make it public internally の名前変更
  * 注釈ウィンドウの透過度を変更
  * 注釈ウィンドウの色を変更
  * libview: マウスボタンを押した時、フォームフィールドとリンクのフォーカスを取得
  * libdocument: `ev_mapping_list_get` の追加
  * pdf: アクティベーションリンクを持っているフィールドには、アクティベーションリンクを追加
  * libview: フォームフィールドのアクティブ化リンクが存在する場合には処理
  * libdocument: activation_link を EvFormField 構造に追加
  * ev-properties-licence: 非推奨となった GtkAlignment の使用回避
  * libview: : 非推奨の gtk_adjustment_changed を回避
  * ev-job-find: 2 つのメソッドをスキップとしてマーク
  * ev-jobs: `ev_job_failed_from_error` のシャドウを `ev_job_failed` に
  * libview: 不足している転送注釈と要素タイプ注釈を追加
  * ev-mapping-list: ボックス型にしました
  * libdocument: 不足している転送注釈と要素タイプ注釈を追加
  * gtk 3.22: 非推奨の gdk_screen_get_monitor... 関数を回避
  * `gdk_screen_get_primary_monitor/gdk_screen_get_monitor_scale_factor` を回避
  * ev-document-misc.c: 非推奨の `gdk_screen_get_width/height_mm` を回避
  * dvi: ファイル名を引用することで、コマンド・インジェクション攻撃を軽減
  * mdvi-lib: コンパイル時の警告 (const-correctness) を修正
  * libmisc: ページラベルの文字幅を設定
  * libview: 非連続モードで小さなページをスクロール
  * libview: ビューで `GDK_SMOOTH_SCROLL` イベントを有効化
  * libview: Ctrl+マウスホイールズームは、ウィンドウ中心ではなくポインタ中心に
  * ev-view: ページ切り替えにパンジェスチャを追加
  * ev-view: `GtkScrolledWindow` を親ウィジェットとして明示的に要求
  * ev-view: ピンチ/ズームジェスチャを追加して文書の拡大縮小を処理
  * sidebar-thumbnails: 全画面表示後に起きる不要な移動の開始を修正
  * sidebar-thumbnails: スクロール時に表示範囲を1つ余分にプリロード
  * sidebar-thumbnails: 描画済みのサムネイルを保持
  * sidebar-thumbnails: スクロールの不自然さを修正
  * annotations-sidebar: デザインの見直し
  * ev-annotation-window: ウィンドウ枠の色の設定を修正
  * libview: 作成後に注釈ウィンドウのフォーカスが変わるのを修正
  * libview: ev_annotation_window のフォーカスを修正
  * libview: 注釈ウィンドウのフォント色を変更しない
  * shell: 注釈に GdkRGBA を使用
  * libdocument: GdkRGBA を使用して EvAnnotation API を追加
  * libdocument: 新しい非推奨マクロの使用
  * 非推奨のマクロを追加
  * 以前の HDPI コミットによって発生するランタイム警告を修正
  * モニターの拡大率を考慮してズームを計算する。
  * メインビューに hi-dpi サポートを追加
  * shell: gimpcellrenderertoggle を廃止
  * sidebar-layers: 実際に使用可能にし、実行時の警告を修正
  * libview: 注釈ウィンドウのアイコンサイズを設定
  * libview: 変更をドロップダウンに埋め込み形式で保存
  * libdocument: アクティブページと非アクティブページのシャドウの描画を調整
  * 非推奨の `gdk_screen_make_display_name` を回避
  * ev-window: 非推奨の `GtkToolbar-shadow-type` を削除
  * annotation-properties-dialog: ヘッダバーを使用しない
  * 非推奨の `gdk_display_get_screen` と `gdk_display_get_n_screens` を回避
  * ev-window: 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * build: 生成された .caja-extension ファイルを適切に消去
  * build: cairo >=1.10.0 が必要で、古いコードをいくつかを削除
  * shell: utils から使用されていないコードを削除
  * ev-view: 非推奨の `gtk_drag_begin` を回避
  * egg-editable-toolbar: 非推奨の `gtk_drag_begin` を回避
  * message-area: 一部の `GtkStock` の非推奨を置き換え
  * ev-sidebar: 非推奨の `GTK_STOCK_CLOSE` アイコンを回避
  * password-view: 一部の非推奨 `GtkStock` を置き換え
  * password-view: 非推奨の `GtkAlignment` を使用中止
  * toolbar-editor: 非推奨の `GtkAlignment` を使用中止
  * 翻訳の更新

### caja-extensions 1.20.0

  * xattr-tags: 拡張機能の説明で適切な英語を使用
  * po: xattrs 拡張からの翻訳可能な文字列を追加
  * xattr-tags: 拡張機能の説明を修正
  * open-terminal: 文字列の重複を過度に使用しない
  * 非推奨の `gdk_screen_make_display_name` を回避
  * sendto burn: 非推奨の `gtk_show_uri` を回避
  * xattr-tags: 今では不要となったため、hack を削除。
  * xattr-tags: 未定義の参照を引き起こすタイプミスを修正
  * `libcaja_gksu_la_LDFLAGS` 変数の宣言を修正
  * xattr-tags: 起動メッセージに不足していた新しい行を追加
  * xattr-tags: 保存された属性をエスケープしない。
  * 翻訳の更新

### engrampa 1.20.0

  * build: `PKG_CONFIG` を使用してクロスビルドを修正
  * About ダイアログと Caja 拡張機能に著作権表示を追加
  * 7z: Fix: リストが暗号化されていないパスワードでファイル名変更
  * 7z: Fix: 暗号化されたリストを使用したファイル/フォルダの削除/名前変更
  * 非推奨の `gdk_screen_make_display_name` を回避
  * 非推奨の `gtk_show_uri` を回避
  * もっと一般的な gtk+ 関数を使用
  * 非推奨の `gdk_screen_get_number` を回避
  * 進捗ダイアログに「Show the Files and Quit」ボタンを追加
  * Fix: 「最大」圧縮レベルで zip ファイルを作成
  * 履歴を正しくブラウズしない問題を修正
  * 「すべてのファイルを表示」でフォルダを非表示
  * ファイルの置換ダイアログボックスにおける、スキップボタンの不正な動作を修正
  * UI files: 非推奨の回避
  * gtk-utils: `GTK_STOCK` の非推奨事項を削除
  * gtk-utils: 非推奨の gtk_icon_size_lookup_for_settings を回避
  * fr-window: `GTK_STOCK` の一部の非推奨事項を削除
  * スタイルクラスフレームを scrolledwindows へ追加
  * fr-window: 非推奨の `GtkMisc` と `GtkAlignment` を回避
  * dlg-add-folder: 非推奨の `gtk_alignment_new()` を回避
  * build: クリーニング時に、ハードコードされたファイル名の代わりに変数を使用
  * 翻訳の更新

### eom 1.20.0

  * GTK+ 3.18 用の CSS を廃止
  * egg-editable-toolbar.c/egg-toolbars-model.c: 未使用の変数を削除
  * print-preview: カスタムコードを GDK 関数の呼び出しと置き換え
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * 複数の eom ウィンドウがある空ウィンドウを閉じる時、その警告を修正
  * EomThumbView: 廃止された `gtk_menu_popup` 関数を置き換え
  * multiple-save-as-dialog.ui: 廃止されたウィジェットを回避
  * error-message: GtkStock を置き換え
  * 多数の instrospection 警告を修正
  * EomScrollView: 廃止された override_background の呼び出しを修正
  * EomPropertiesDialog: 非推奨の警告を修正
  * EomThumbNav: 廃止された関数という警告の修正
  * EomScrollView: 廃止された `gtk_menu_popup` 関数を置き換え
  * EomScrollView: GtkDeviceManager から GdkSeat へ切り替え
  * 関数の注釈でのタイプミスを修正
  * < gtk+=3.20 には異なる css ファイルを使用
  * EomWindow: 親ウィンドウのファイルを開くダイアログを一時的に設定
  * settings: RGB カラー定義をデフォルトとして使用
  * UI: 廃止されたウィジェットの使用を回避
  * EomCloseConfirmationDialog: プライマリラベルの最大幅文字を設定
  * EomCloseConfirmationDialog: 画像一覧のサイズを修正
  * 印刷用紙の向きは、既定でイメージ寸法に基づき設定
  * 印刷時に JPEG ファイルを PNG として再圧縮しない
  * EomFileChooser: 画像プレビューの生成に MateThumbnailFactory を使用
  * EomPropertiesDialog: 透過の背景色に RGBA を許可
  * preferences-ui: `MateColorButton` の使用を廃止
  * EomScrollView: 背景色と透過色を `GdkRGBA` へと切り替え
  * EomPrintPreview: 不要な色解析を回避
  * GtkStock の一部の非推奨事項を修正
  * EomCloseConfirmationDialog: 廃止された `GTK_STOCK_DIALOG_WARNING` の置き換え
  * toolbar-editor: 廃止された GtkAlignment を回避
  * eom-image.c の SVG 処理を最新にして、svgz ファイルタイプを正しく認識
  * eom_uri_converter: GList のリークを修正
  * 翻訳の更新

### mate-applets 1.20.0

  * multiload: ユーザ定義のしきい値を使用してネットワークグラフをスケーリング
  * multiload: タブとスペースが多くの場所で混在するのを修正
  * multiload: 一部の場所での空白を修正
  * multiload: 不要な空白の一部を削除
  * weather: 設定ダイアログを開いたといき発生する可能性のあるクラッシュを修正
  * 壊れた invest-applet とすべての Python 依存関係を削除
  * `fgets` の戻り値を無視するようにビルド警告を修正
  * command: 間隔の範囲を解除
  * WidthOfScreen と HeightOfScreen の実装
  * build: gtksourceview が見つからない時は、このパッケージ名を表示
  * Cpufreq: ツールチップを最新の値で更新
  * Cpufreq: ビルド時の警告を修正
  * Cpufreq: 数字がユニットラベルで移動するのを中止
  * 描画の丸め方でのエラーを修正
  * cpufreq: 周波数/単位/パーセントのラベル最大幅の計算を修正
  * stickynotes: テキストの選択を修正
  * cpufreq: スタイル変更時にアプレットサイズ（フォントサイズなど）を更新
  * GSettings の変更を動的に認識
  * GSettings: マウントされたボリュームに表示されるチェックマークの色
  * cpufreq: アプレットがランダムで見えなくなる問題を修正
  * マウントされたドライブは、少し異なるアイコンで表示
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * ビルド時の misleading_indentation and maybe-uninitialized という警告を修正
  * 非推奨の `gdk_screen_width/height` を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * すべてのアプレットは、非推奨の `gtk_show_uri` を使用しない
  * 新しいデジタルテーマを追加
  * drivemount: ビルド時の警告を修正
  * cpufreq-prefs: 非推奨の `gtk_show_uri` を使用しない
  * bump libmateweather は 1.19.1 が必要
  * weather: 場所が変更された場合、気象情報の更新を中止
  * weather: (`weather_info_equal()` によって決定されたように)、weather 更新が以前の更新と同じ場合に、通知を送信しないロジックを追加
  * 非推奨の `gdk_screen_get_number` を回避
  * drivemount: リストが空の場合、media-floppy アイコンを表示
  * stickynotes: 以前のコミットを少々書き直し、dir name をリークしない。
  * stickynotes: `stickynotes-applet.xml` の親ディレクトリが無い場合はそれを作成
  * 荷重グラフは平均荷重に従って自動的にスケール
  * trashapplet: 未使用のコードを削除
  * cpufreq: すべてのコアで周波数を設定
  * GError のメモリリークを修正
  * コマンドアプレットで crasher を修正
  * 翻訳の更新

### mate-calc 1.20.0

  * 設定ダイアログの閉じるボタンに、アイコン画像を追加
  * 非推奨の GtkStock を回避
  * About ダイアログに不足していたウィンドウアイコンを追加
  * math-window: 非推奨の `gtk_show_uri` を回避
  * 翻訳の更新

### mate-icon-theme-faenza 1.20.0

  * 元のプロジェクトに従い、ライセンスを GPL3 へ変更
  * ダークテーマに MATE ロゴを使用するよう修正

### mate-indicator-applet 1.20.0

  * Ayatana Indicators とUbuntu Indicators のどちらに対しても、ビルドをサポート
  * 翻訳の更新

### mate-netbook 1.20.0

  * WidthOfScreen と HeightOfScreen の実装
  * window picker: disconnect シグナルハンドラは、dispose 関数を指定
  * window picker: 設定ダイアログにアイコンを追加
  * window picker: 設定ダイアログボタンの垂直方向の拡張を無効に
  * window picker: タスクバーのアイコンを About ダイアログへ追加
  * maximus: 無効なウィンドウ ID でクラッシュしない
  * 翻訳の更新

### mate-sensors-applet 1.20.0

  * build: udisk2 プラグインを再び有効化
  * 廃止された udisks プラグインを削除
  * udisks plugin: GValue 変数のメモリ管理を修正
  * 非推奨の eee プラグインを削除
  * 取り外した HDD のポップアップシャワーを修正
  * ibm-acpi.c: ビルド時の警告を修正
  * eee-plugin.c: ビルド時の警告を修正
  * active-sensor.c: ビルド時の警告を修正
  * sensors-applet.c: ビルド時の警告を修正
  * インデントを修正
  * project クリーンアップの修正
  * 数字の変化に対応してアプレットの移動をを停止
  * センサーの保存順序を修正
  * 温度単位の非表示を更新
  * コードの重複を削除
  * sensor-applet.c: 廃止された GtkMisc を置き換え
  * sensor-applet.c: 非推奨の `GTK_STOCK_MISSING_IMAGE` を回避
  * sensor-config-dialog: 非推奨の GtkAlignment を回避
  * sensor-config-dialog: 非推奨の GtkColorButton を使用しない
  * prefs-dialog: スタイルクラスフレームを scrolledwindow へ追加
  * prefs-dialog: 非推奨の GtkAlignment を回避
  * prefs-dialog: 非推奨の `GTK_VBUTTON_BOX`, `GTK_TYPE_{H,V}BOX` を回避
  * `sensor_applet` グリッドに `GTK_ALIGN_CENTER` を使用
  * 翻訳の更新

### mate-terminal 1.20.0

  * VTE 0.46 が必要
  * screen: `TERM` および `COLORTERM` 環境変数の設定を無くす
  * schema: 一部のキーの要約と説明を修正
  * キーボードのショートカットより "..." を削除
  * profile-editor: 最初のパレットカラーを適切に初期化
  * terminal-screen.c: 未使用の変数を削除
  * `chdir` の戻り値を無視するようにビルド警告を修正
  * タブの中クリックで、gsettings キーが追加されて機能が有効化
  * インデントをいくつかのファイルでより統一
  * DBus メソッドの呼び出し処理時のクラッシュを修正
  * Spelling: 空白の削除, in the terminal, Ctrl
  * gnome-terminal より solarized テーマを追加
  * WidthOfScreen と HeightOfScreen の実装
  * <kbd>ctrl</kbd> + <kbd>tab</kbd> と <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>tab</kbd> を使用して、タブの切り替えを実現
  * 「検索」キーボードショートカットの再マッピングを許可
  * VTE3 で背景の画像ををサポート
  * find-dialog.ui: キーボードの選択を修正
  * 非推奨の `vte_terminal_search_get_gregex` を回避
  * 「すべて選択」キーボードショートカットを追加: <kbd>control</kbd> + <kbd>shift</kbd> + <kbd>A<kbd>
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_make_display_name` を回避
  * terminal-util: 非推奨の `gtk_show_uri` を回避
  * 非推奨の `gdk_display_get_screen` を回避
  * 非推奨の `gdk_screen_get_number` を回避
  * 右ボタンのダブルクリックで Xorg がクラッシュする問題を修正
  * 翻訳の更新

### mate-user-share 1.20.0

  * build: 正しいマクロを使用してクロスビルドを修正
  * 非推奨の `gtk_show_uri` を使用しない
  * 翻訳の更新

### mate-utils 1.20.0

  * HiDPI ディスプレイのスクリーンショットのサポート追加
  * mate-screenshot: 新しいボタンを追加
  * screenshot-save.c: `pipe` `write` および `read` でのビルド警告を修正
  * スタイルクラス logview-window を追加
  * 翻訳の更新
  * WidthOfScreen と HeightOfScreen の実装
  * baobab: グラフ上でマウスホイールを使用してズーム
  * screenshot: 未使用のコードを削除
  * screenshot: ウィンドウタイトルは、後で使用されないので取得しない
  * baobab/logview/dictionary: 著作権表示を About ダイアログへ追加
  * baobab: リモート接続ダイアログに一時的な親を設定
  * baobab:  ui ファイルで設定ダイアログを非表示
  * baobab: About ダイアログの親ウィンドウを設定
  * 非推奨の `gdk_screen_get_active_window` を回避
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gdk_screen_width/height` を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * screenshot: 非推奨の GdkDevice オブジェクトを回避
  * dictionary: 非推奨の GdkDevice オブジェクトを回避
  * 非推奨の `gdk_screen_get_n_monitors` を回避
  * 非推奨の `gdk_screen_make_display_name` を回避
  * gdict-applet: 非推奨の `gtk_show_uri` を使用しない
  * 非推奨の `gtk_show_uri` を使用しない
  * 非推奨の `gdk_screen_get_number` を回避
  * searchtool & logview: 廃止された GtkAlignment を回避
  * mate-screenshot: スクリーンショットの領域保存時における、ビジーカーソルの表示を修正
  * screenshot: ファイル名のタイムスタンプを変換しない
  * mate-dictionary: FTBFS を時々修正するために、正しいヘッダを含める
  * 翻訳の更新

### mozo 1.20.0

  * 翻訳の更新

### pluma 1.20.0

  * `peas_engine_enable_loader` を正しい場所に配置
  * 最近使用したファイル一覧が再び有効になるように修正
  * 使用しない変数を削除
  * pluma-spell-checker-language.c: ビルド時の警告を修正
  * pluma.c: ビルド時の警告を削除
  * pluma-document.c: ビルド時の警告を修正
  * pluma-window: GtkRecentData を割り当てる代わりにスタックさせる
  * WidthOfScreen と HeightOfScreen の実装
  * バックリファレンスによる正規表現置換を修正 ( 例: `"\0"` )
  * pluma-view.c: 同じジョブを実行するために、2つのの静的変数の代わりに1つの静的変数を使用
  * 同じワークスペースのウィンドウで Pluma が開いていることを確認する
  * Pluma が、[右 + 中クリック] <kbd>ctrl</kbd> + <kbd>+</kbd> / <kbd>ctrl</kbd> + テンキーの <kbd>-</kbd> を押すと、予期せずにタブが閉じる問題を修正
  * gsettings キーの追加: ファイルが変更された場合には保存の確認を表示
  * [中 + 右] ボタンを押しながら <kbd>ctrl</kbd> + <kbd>+</kbd> / <kbd>ctrl</kbd> + <kbd>-</kbd> をクリックしてフォントサイズを増減した際の不正な動作を修正
  * 変更が無い場合には文書の保存を要求しない
  * gsettings キーを追加して、サイドペインでタブを表示/非表示 (デフォルト) に
  * サイドバー使用時にはタブを表示しない
  * gtk 3.22: 非推奨の `gdk_screen_get_monitor` 関数を回避
  * 非推奨の `gdk_screen_get_width/height` を回避
  * 非推奨の `gdk_screen_make_display_name` を回避
  * pluma-help:  `deprecated gtk_show_uri` を使用しない
  * filebrowser: `deprecated gtk_show_uri` を使用しない
  * 非推奨の `gdk_display_get_screen` と `gdk_screen_get_number` を回避
  * もし外部で文書が変更された場合には、それを保存可能にする
  * もし文書に変更がない場合には、それを保存可能とはしない
  * print-preferences UI: 一部の基本的な非推奨事項を修正
  * encoding-dialog UI: 一部の基本的な非推奨事項を修正
  * preferences-dialog UI: 一部の基本的な非推奨事項を修正
  * pluma-panel: 廃止された GtkImage タイプを削除
  * plumal-panel: 一部の非推奨 GtkStock を削除
  * search-dialogs: -Wpointer-compare 警告を削除
  * tag-list-plugin: 非推奨の GtkStock を回避
  * file-browser-widget: 一個の非推奨ストックを修正
  * configure: `GLIB_VERSION_MAX_ALLOWED` を廃止
  * File browser: GIOScheduler を使用しない（廃止のため）
  * file-browser-view: 一部のビルド警告を非表示
  * pluma-view: 非推奨の GtkStock を回避
  * pluma-tab: 一部の GtkStock アイコンを置き換え
  * pluma-notebook: 非推奨の `gdk_cursor_new` を使用しない
  * progress-message-area: GtkStock の１個の非推奨を修正
  * io-error-message-dialog: 一部の GtkStock 非推奨警告を修正
  * Pluma の中ボタンをクリックすると、突然タブが終了する問題を修正
  * pluma-notebook.c: ビルド時の警告を削除
  * 直前に開いたタブの右側をダブルクリックして、新しいタブを開く
  * gtk ブックマークファイルの新しい場所をサポート
  * docs: オプションメニューではなく、エンコード・コンボボックスを用意
  * PlumaStatus への参照を削除
  * docs: 存在しないアイテムへの参照を削除
  * filebrowser: 隠しファイルを解析しない - 2.36 以降は GIO が実行します。
  * close confirm dialog: すべてのラベルで選択を有効にし、フォーカスを無効に
  * close confirm dialog: ラベルの最大幅を設定
  * コードコメントのタイプミスを修正
  * Wayland 上での起動を修正
  * modelines: 複数の Pluma ウィンドウのうちの1つを閉じた時、ランダムクラッシュする問題を修正
  * 翻訳の更新

### python-caja 1.20.0

  * 翻訳の更新
