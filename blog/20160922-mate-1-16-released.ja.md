<!--
.. link:
.. description:
.. tags: Releases
.. date: 2016-09-21 21:00:00
.. title: MATE 1.16 リリース
.. slug: 2016-09-21-mate-1-16-released
.. author: Martin Wimpress
-->

6 ヶ月の開発期間を経て、MATE デスクトップチームは MATE デスクトップ 1.16 のリリースを公表できたことをうれしく思います。このリリースを可能にしていただいた全ての MATE 貢献者の方々に感謝します。

![about](/assets/img/blog/about-mate-1.16.png)

## MATE 1.16 での主な変更点:

今回のリリースでは、GTK3+ の互換性の向上、新しいライブラリへのコンポーネントの移行、バグの修正、コードのクリーン化に重点が置かれています。MATE デスクトップ 1.16 の主要項目の変更点は次の通りです。

  * MATE デスクトップ全体で GTK+3 のサポートが向上。
  * アプリケーションとテーマの GTK+ 3.22 サポート。
  * 多くのアプリケーションが GTK+3 のみのビルドに対応
    * Engrampa 書庫マネージャ
    * MATE 通知デーモン
    * MATE PolKit
    * MATE セッションマネージャ
    * MATE 端末
  * 一部のアプリケーションは `libmate-desktop` から切り離されました。
    * Engrampa 書庫マネージャ
    * MATE アプレット
    * MATE ネットブック
    * MATE 電源管理
    * MATE 端末
    * Pluma テキストエディタ
  * アプリケーションを GApplication または GtkApplication に移植する作業を開始しました。
    * Engrampa 書庫マネージャ
    * MATE アプレット
    * MATE ネットブック
    * MATE ユーザー共有
  * 多数のバグと非推奨事項が修正されています。
  * 翻訳が更新されました。*翻訳者のチームに感謝します！*

MATE デスクトップ 1.16 の各種コンポーネントは、次の場所からダウンロードできます。

  * <https://pub.mate-desktop.org/releases/1.16/>

## Changelog 変更点

変更点の詳細は以下のとおりです。

### mate-common

  * `mate-autogen` では、`autoconf`、`automake` のように `autoreconf` だけをチェック
    `libtool`、`gettext` は `autoreconf` ですでにチェックされています。

### mate-desktop

  * mate-bg: 不要な ignore-pending-change プロパティを削除 (Caja 1.14 でのフォント色修正によって不要)
  * GTK+3: 各種の非推奨事項を修正
  * distcheck: 現在選択されている GTK+ バージョンを明示的に使用
  * わずかなクリーンアップ
  * 翻訳の更新

### libmatekbd

  * libxklavier5.2 を要求し、そのイントロスペクションを使用
  * GTK+3: 一部の非推奨事項を修正
  * distcheck: 現在選択されている GTK+ バージョンを明示的に使用
  * 翻訳の更新

### libmatemixer

  * 翻訳の更新

### libmateweather お天気 MATE

  * 場所: エクアドル、キトーの ICAO コードを更新
  * 場所: ミンスク空港 (コード UMMS) の正しい時間帯に訂正
  * 翻訳の更新

### mate-icon-theme

  * 翻訳の更新

### Caja ファイルマネージャ

  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * Pathbar: 常に右矢印ボタンを表示
  * アイコンの異なるタブ間で切り替えた時、タスクバーアイコンが変わる問題を修正
  * `libcaja-extension` の文書ビルド時での多くの警告を修正
  * GTK+3: pathbar の要素にスタイルクラスを追加
  * GTK+3: fix 描画とデスクトップ背景の変更 >=3.21
  * GTK+3: 多量の非推奨事項を修正
  * **その他の改善**
  * 翻訳の更新

### mate-polkit

  * GTK+3 への移動 (GTK+ >= 3.14 が必要)、GTK+2 のコードと `--with-gtk` ビルオプションを削除
  * 翻訳の更新

### Marco ウィンドウマネージャ

  * 翻訳の更新
  * distcheck は現在選択されている GTK+ バージョンを使用

### mate-settings-daemon 

  * 既定のヒントスタイルを `hintslight` へ変更
  * 既定では 'rgba' (LCD サブピクセル) アンチエイリアスを使用
  * GTK+3: ハードコードされた色を使用する代わりに、OSD (MsdOsdWindow) に css のテーマを追加
  * GTK+3: fix 描画とデスクトップ背景の変更 >=3.21
  * GTK+3: 複数の非推奨事項を修正
  * 一部のビルド警告を修正
  * 翻訳の更新

### MATE セッションマネージャ

  * GTK+3 への移動 (GTK+ >= 3.14 が必要)、GTK+2 のコードと `--with-gtk` ビルオプションを削除
  * 翻訳の更新

### MATE メニュー

  * 翻訳の更新

### MATE パネル

  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * GTK+3: プロパティダイアログで GtkColorButton/GtkColorChooser を使用
  * GTK+3: 多数の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### mate-backgrounds 背景

  * 翻訳の更新

### MATE テーマ

  * GTK+3.20 および 3.22 の包括的なサポート

### MATE 通知デーモン

  * Build: 他のプロジェクトと同様に、m4 マクロには `macros` ではなく `m4` ディレクトリを使用
  * GTK+3 への移動 (GTK+ >= 3.14 が必要)、GTK+2 のコードと `--with-gtk` ビルオプションを削除
  * GNotification のサポートを追加
  * 特殊文字のエスケープを修正
  * GTK+ のさまざまな非推奨事項を修正
  * 翻訳の更新

### mate-control-center コントロールセンタ

  * Build: dconf 0.10 との互換性を削除
  * 外観: 既定のヒントスタイルを slight に変更し、そのスタイルを使用してアンチエイリアスサンプルをレンダリング
  * 外観: RGBAアンチエイリアスを使用してヒントサンプルをレンダリング
  * 外観: GTK+2 のときと一致するように、テーマ名を GTK+3 ビルドのテーマプレビューの下に配置
  * 外観: GTK+2 のときと一致するように、テーマ名を GTK+3 ビルドで中央に配置
  * 外観: GTK+3 ビルドではカスタマイズのテーマダイアログで色タブを非表示にします。テーマ色の変更は GTK+3 では機能しません。
  * GTK+3: appindicator サポートを有効にしてビルドを修正
  * GTK+3: glib2.49.6 でディスプレイのプロパティにモニタを表示するよう修正
  * GTK+3: 各種の非推奨事項を修正
  * 一部のコードをクリーンアップ
  * 翻訳の更新

### mate-screensaver スクリーンセーバ

  * スクリーンセーバーが既にアクティブになっているときのロックを修正
  * GTK+3: マルチモニタ設定で背景とロックを修正
  * GTK+3: 複数の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新
  * distcheck は現在選択されている GTK+ バージョンを使用

### mate-media

  * 翻訳の更新

### mate-power-manager MATE 電源管理

  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * `libmate-desktop` への依存関係を削除
  * プライマリデバイスの残り時間をコンテキストメニューの最初のエントリとして表示
  * ノートパソコンのバッテリが空の場合は、コンソールに警告を非表示
  * GTK+3: libunique を GtkApplication へ移植
  * GTK+3: OSD (MsdOsdWindow) 用の css テーマを追加
  * GTK+3: システムにバッテリがない場合の、トレイの空きスペースを修正
  * GTK+3: 多数の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新
  * distcheck は現在選択されている GTK+ バージョンを使用

### MATE システムモニタ

  * 翻訳の更新

### Atril 文書ビューア

  * Build: Poppler 0.18.0 が必要
  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * `libmate-desktop` と `--without-matedesktop` ビルドオプションへの依存関係を削除
  * `libegg` から `toolbar-editor` を更新
  * synctex を 1.18 へ更新
  * デュアルモードオプションを、左側に奇数ページと偶数ページのデュアルモードに分割して表示
  * 前後の検索結果に Ctrl+Up/Down キーバインドを追加
  * `caja-sendto` サポートを追加して、現在の文書を電子メールでリムーバブルデバイスなどに送信可能にしました。
  * `--named-dest` コマンドライン引数と dbus サポートで、名前付き宛先のサポートを改善
  * [dvi] t1フォントのマッピングファイルを使用
  * GTK+3: スタイルクラスを view へ追加
  * GTK+3: イントロスペクション有効時にビルドがクラッシュする問題を修正
  * GTK+3: 多数の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### Caja 拡張機能

  * open-terminal:
    * 名前に一重または二重引用符を使用して、リモートフォルダの端末を開く際の問題を修正
    * 一部のコードをクリーンアップ
  * 翻訳の更新

### Engrampa 書庫マネージャ

  * GTK+3 への移動 (GTK+ >= 3.14 が必要)、GTK+2 のコードと `--with-gtk` ビルオプションを削除
  * GtkApplication へ移植
  * ファイル名の並び替え時には自然な順序を使用
  * カスタムコードの代わりに GTK+ の App Chooser ダイアログを使用して "Open With" コマンドを実行
  * パスワードが指定されていない場合、"encrypt header" オプションを区別しません。
  * RAR アーカイブを処理する時、p7zip よりも unrar を優先
  * 7z: p7zip-rar >=15.14 のサポートを追加
  * 7z: '@' の接頭辞が付いたファイルに関する問題を修正
  * GTK+ の一部の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### Eye of MATE 画像ビューア

 * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
 * エラーメッセージ領域で発生する可能性がある、範囲外の書き込みを修正
 * 一部のクリーンアップ
 * 翻訳の更新

### MATE アプレット

  * Build: polkit 0.97 が必要
  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  - Netspeed: GtkColorButton/GtkColorChooser の使用
  - `libmate-desktop` への依存関係を削除
  - GTK+3: 各種の非推奨事項を修正
  - 一部のコードをクリーンアップ
  - 翻訳の更新

### MATE インジケーターアプレット

  * Build: 新しいスタイルのインジケータサポートの修正チェック
  * 翻訳の更新

### MATE ネットブック

  * Window Picker アプレット: `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * Window Picker アプレット: クラッシュの可能性を防止
  * mate-maximus: libunique から GApplication へ移植
  * `libmate-desktop` への依存関係を削除
  * 翻訳の更新

### MATE センサーアプレット

  * distcheck は現在選択されている GTK+ バージョンを使用
  * 翻訳の更新

### MATE 端末

  * GTK+3 へ移行、GTK+ 3.14 と VTE 0.38 (API2.91) が必要
  * GTK+2 のコードと `--with-gtk` ビルドオプションを削除
  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * `libmate-desktop` から dconf と gsettings ヘルパーをコピーし、`libmate-desktop` への依存関係を削除
  * X11 でのみ WM の変更に対応
  * 多数の GTK+ 依存関係を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### MATE ユーザー共有

  * Build: 他のプロジェクトと同様に、m4 マクロには `m4` ディレクトリを使用
  * GTK+3: libunique を GtkApplication へ移植
  * distcheck は現在選択されている GTK+ バージョンを使用
  * 翻訳の更新

### mate-polkit

  * GTK+3 への移動 (GTK+ >= 3.14 が必要)、GTK+2 のコードと `--with-gtk` ビルオプションを削除
  * 翻訳の更新

### mate-utils

  * コマンドラインのオプション `--version` を `mate-screenshot` へ追加
  * GTK+3: >= 3.21 での MATE 辞書のセグメンテーションエラーを修正
  * GTK+3: すべてのアプリケーションで、多数の非推奨事項を修正
  * 翻訳の更新

### Mozo メニューエディタ

  * プロパティと削除のボタンを追加
  * ドラッグ＆ドロップに関する複数の問題を修正
  * `.desktop` ファイル名にスラッシュを含むとき、クラッシュする問題を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### Pluma テキストエディタ

  * `MateAboutDialog()` の代わりに `GtkAboutDialog()` を使用
  * `libmate-desktop` と `--without-matedesktop` ビルドオプションへの依存関係を削除
  * GTK+3: 多数の非推奨事項を修正
  * その他の修正とクリーンアップ
  * 翻訳の更新

### caja-dropbox

  * 一部のコードをクリーンアップ

### python-caja

  * 例: 背景画像の拡張機能ロード時に Caja がクラッシュする問題を修正
  * 例: 各種の修正
  * 翻訳の更新
