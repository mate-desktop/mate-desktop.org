<!--
.. link:
.. description:
.. tags: Releases
.. date: 2016-04-08 15:00:00
.. title: MATE 1.14 をリリースしました
.. slug: 2016-04-08-mate-1-14-released
.. author: Martin Wimpress
-->

5ヶか月の開発期間を経て、MATE デスクトップチームは MATE デスクトップ 1.14 のリリースを公表できたことをうれしく思います。すべての MATE 貢献者とユーザーに感謝します。

![about](/assets/img/blog/about-mate-1.14.png)

## MATE 1.14 で新しくなったこと

MATE デスクトップ 1.14 の主な変更点は次のとおりです。

  * MATE デスクトップ全体で GTK+3 のサポートが向上。
  * すべての MATE テーマで GTK 3.20 を完全にサポート。
  * クライアント側で装飾されたアプリケーションは、すべてのテーマで正しくレンダリングされます。
  * MATE システムモニタと Mozo は GTK+3 だけへ完全に移植。
  * タッチパッドの設定で、エッジスクロールと2本指スクロールを独立してサポートするようになりました。
  * Caja の Python 拡張機能は、個別に管理できるようになりました。
  * 3つのウィンドウフォーカス・モードはすべて選択可能です。
  * MATE パネルでは、メニューバーとメニュー項目のアイコンサイズの変更が可能になりました。
  * MATE ネットスピードアプレットは、MATE アプレット・パッケージへ統合されました。
  * MATE 端末は、GTK+3 用にビルドされた場合、VTE 2.91 API をサポートします。
  * モニタ画面の音量と明るさを有効 / 無効にできるようになりました。
  * 翻訳が更新されました。翻訳チームのみなさんに感謝します！  

MATE 1.14 の各種コンポーネントは、次の場所からダウンロードできます。

  * <https://pub.mate-desktop.org/releases/1.14/>

## スクリーンショット

  * [MATE 1.14 スクリーンショット](/gallery/1.14/)

## Changelog 変更点

変更点の詳細は以下のとおりです。

### mate-common

  * 廃止された MATE コンポーネントへの参照を除去

### mate-desktop

  * MateConf の移行スクリプトと古い `mate-conf-import` ツールを削除
  * GTK+3 でビルドされた `GtkHBox` と `GtkVBox` の非推奨使用を修正

### libmatekbd

  * MateConf 移行スクリプトの削除
  * イントロスペクションのビルド警告を軽減
  * GTK+3 の一部の非推奨事項を修正
  * 各種修正とクリーンアップ

### libmatemixer

  * PulseAudio 2.0 以降が必要
  * 各所のエラーチェックを改善
  * PulseAudio の音量制限を修正
  * その他の PulseAudio の修正
  * `alsa` と `oss` バックエンドの一部の修正と改善
  * 各種修正とクリーンアップ

### libmateweather お天気 MATE

  * 旧式のビルドフラグを削除
  * スキーマの小さな修正

### mate-icon-theme

  * `system-config-keyboard` アイコンの追加

### Caja

  * MateConf 移行スクリプトの削除
  * 中クリック時にタブを閉じることを許可
  * Python 拡張機能を拡張リストに個別にリスト
  * GTK+3: 複数のスタイルクラスを追加してテーマを簡単に
  * GTK+3: デスクトップ flash の問題を修正
  * GTK+3: 多数の非推奨関連の修正
  * 各種修正とクリーンアップ

### mate-polkit

  * GTK+3: 複数の非推奨事項を修正

### Marco

  * MateConf 移行スクリプトの削除
  * Chromium ウィンドウ最小化後に現れる視覚的な不具合を修正
  * compositing-fast-alt-tab GSettings キーの記述を訂正 (サムネイルが無効になることを明記)
  * GTK+3 のビルドで libmarco-private's sover をバンプ
  * GTK+3: コンポジタが有効な場合、Alt-Tab のサムネイルを表示する機能を再追加
  * GTK+3: 複数の非推奨事項を修正

### mate-settings-daemon 

  * MateConf 移行スクリプトの削除
  * media-keys: OSD を有効/無効にする設定を追加
  * touchpad: エッジスクロールと2本指スクロールを個別にサポート (個別の GSettings キーを使用)
  * xsettings: カーソルテーマとサイズの設定を追加
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-session-manager

  * MateConf 移行スクリプトの削除
  * GTK+3: 一部の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-menus

  * `mate-preferences-categories.menu` を `mate-control-center` から移動

このファイルは個別にパッケージ化できるので、ユーザーは設定メニューでカテゴリを使用するかどうかを決定できます。

### mate-panel

  * MateConf 移行スクリプトの削除
  * 「アプレットの再ロード」ダイアログに別の「削除」ボタンを追加して、「再ロードしない」ボタンを動作させます (今はアプレットを永久に削除しません)。
  * (サブメニューが作成される前に) メニュー内のブックマークの最大数を GSettings キーで設定できるようにしました。
  * GSettings キーを使用してメニュー項目のアイコンサイズを設定可能に
  * メニューバーアイコンの既定サイズを 22px に変更
  * *"Ubuntu hacks"* (`--enable-ubuntu` ビルドオプション) を Ubuntu がかなり前に削除したので廃止
  * GTK+3: 複数のスタイルクラスを追加
  * GTK+3: 3.20 用に複数の css 名を追加
  * GTK+3: 3.18 以降でカスタム背景のレンダリングを修正
  * GTK+3: 多数の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-themes

  * GTK 3.20 の完全サポート。
  * クライアント側で装飾されたアプリケーションは、すべてのテーマで正しくレンダリングされます。
  * すべてのテーマに対するさまざまな改善と細かな改良

### mate-notification-daemon

  * MateConf 移行スクリプトの削除
  * GTK+3: 通知テキストを明示的に50文字で折り返し
  * GTK+3: スライダテーマの fg/bg 色の反転を止めます (現在の GTK+ テーマの色をそのまま使用)。
    &nbsp;
  * GTK+3: スライダテーマの一部を修正
  * GTK+3: 一部の非推奨事項を修正

### mate-control-center

  * MateConf 移行スクリプトの削除
  * *"Ubuntu hacks"* (`--enable-ubuntu` ビルドオプション) を Ubuntu がかなり前に削除したので廃止
  * mate-preferences-categories.menu を mate-menus へ移動
  * タッチパッドの設定: エッジスクロールと2本指スクロールを独立してサポート
  * ウィンドウのプロパティ: 3 つのウィンドウフォーカスモードすべてを選択可能に
  * GTK+3: mate-appearance-properties でのテーマプレビューを修正
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-screensaver

  * MateConf 移行スクリプトの削除
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-media

  * GTK+3: 3.20 用に css 名 `GvcMixerDialog` を追加
  * GTK+3: 複数の非推奨事項を修正

### mate-power-manager

 - MateConf 移行スクリプトの削除
 - Xorg 関数の呼び出し失敗時に発生する可能性があるクラッシュを修正
 - GTK+3: 明るさアプレットの非推奨事項を修正
 - 各種修正とクリーンアップ

### mate-system-monitor

  * GTK+3 へ移行して、GTK+2 コードを廃止し、`--with-gtk` ビルドオプションを使用
  * 要求する最小限の GTK+ バージョンを 3.14 へと設定し、非推奨コードの一部を削除
  * `libgksu2.so` をロードする代わりに `gksu` バイナリを実行します (これは GTK+2 のみです)。
  * MateConf 移行スクリプトの削除
  * メインウィンドウ: 最大化された状態を gsettings に終了時保存し、起動時にロード
  * Disks: 複数の列幅とその表示/非表示を保存しロードする機能を追加
  * プロセスのプロパティ: cgroups を表示
  * プロセスのプロパティ: cgroups または selinux 非設定時には N/A を表示
  * プロセステーブル: CPU 時間が変化した時に実行状態を表示
  * グラフのグリッド線の色とパターンを変更
  * GTK+ 3.20 の問題を回避するために、グラフの背景を明示的に描画します
  * marco や vino のような一部の既知のアプリの不正なアイコンを修正
  * 各種修正とクリーンアップ

### Atril 

 * MateConf 移行スクリプトの削除
 * 著作権を更新し、Caja 拡張機能にて MATE チームを記述
 * スクリーンセーバーを無効にするには `org.gnome.SessionManager`DBus 名を使用します
 * GTK+3: atril-window スタイルクラスを最上位に追加
 * GTK+3: 3.20 用に EggToolbarEditor という css 名を追加
 * 各種修正とクリーンアップ

### Caja 拡張機能

  * MateConf 移行スクリプトの削除
  * GTK+3: 一部の非推奨事項を修正
  * 各種修正とクリーンアップ

### Engrampa

  * MateConf 移行スクリプトの削除
  * ""開く..."ダイアログでの不規則なクラッシュを修正
  * 7z: ファイル名の "?" 文字に係る問題を回避
  * 7z: p7zip 15.09+ に対するチェックを訂正
  * rar: 既存ファイルの上書きを無効にする時、"展開するファイルがありません" というメッセージを回避
  * tar: txz ファイルの内容の変更を許可 (.tar.xz ファイルの場合と同様)
  * unar: ファイル名の "?" 文字に係る問題を回避

### Eye of MATE

  * MateConf 移行スクリプトの削除
  * スクリーンセーバーを無効にするには `org.gnome.SessionManager`DBus 名を使用します
  * ファイルが変更された時、未変更の画像を自動的に再ロード
  * GTK+3: 最上位レベルに eom-window クラスを追加
  * GTK+3: 3.20 用に EggToolbarEditor という css 名を追加
  * GTK+3: SVG のレンダリングを修正
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### MATE アプレット

  * MateConf 移行スクリプトの削除
  * 最近ではビルドもできない `null_applet` を削除
  * GPL-2+ のもとでコマンドとタイマーアプレットを再ライセンス
  * mate-netspeed プロジェクト (およびその開発停止プロジェクト) の netspeed アプレットを統合
  * GTK+3: CPU 計測モニタのレンダリングを修正
  * GTK+3: 付箋アプレットのf g/bg 色とフォントタイプの設定を修正
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### mate-netbook

  * MateConf 移行スクリプトの削除
  * GTK+3: 一部の非推奨事項を修正
  * 各種修正とクリーンアップ

### MATE ネットスピード

  * MATE ネットスピードは `mate-applets` パッケージへ統合されました。

### mate-sensors-applet

  * 各種修正とクリーンアップ

### MATE 端末

  * GTK+3 ビルドでの VTE 2.91 API をサポート
  * MULTILINE オプションを使用して dingu の正規表現をコンパイル
  * コマンドラインオプションの説明および man ページの COLS と ROWS の誤った順序を修正
  * GTK+3: スタイルクラスを MATE 端末へ追加
  * GTK+3: 3.20 用のウィンドウサイズを修正
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### MATE ユーザー共有

  * MateConf 移行スクリプトの削除
  * .desktop ファイルのキーワード欄を翻訳しない
  * GTK+3: 一部の非推奨事項を修正

### mate-utils

  * MateConf 移行スクリプトの削除
  * -ai コマンドライン引数を使用して起動した時、mate-screenshot UI の効果と遅延オプションを無効にします
  * スクリーンショットのファイル名には、標準でコロンの代わりにハイフンを使用します。
  * GTK+3: 多くの非推奨事項と一部の UI 問題を修正
  * ビルド時に `-Werror` フラグを使わない
  * 各種修正とクリーンアップ

### Mozo

  * GTK+3 と GObject Introspection へ移植し、古い PyGTK 関連のコードを削除

### Pluma

  * MateConf 移行スクリプトの削除
  * 中クリックでタブを閉じる機能の実装
  * スペルチェックプラグイン用の新しい設定ダイアログボックスを追加
  * 外部ツールで `switch-c` ツールが動作します
  * 潜在的な shell-code インジェクションを修正
  * GTK+3: pluma-window と pluma-print-preview にスタイルクラスを追加
  * GTK+3: 複数の非推奨事項を修正
  * 各種修正とクリーンアップ

### caja-dropbox

  * わずかなクリーンアップ
