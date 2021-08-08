<!-- 
.. link: http://galculator.mnim.org/
.. description: galculator is replacing mate-calc in MATE 1.10
.. tags: News
.. date: 2014/03/17 07:38:45
.. title: galculator が MATE 1.10 に採用されます
.. slug: 2014-03-17-galculator-is-coming-to-mate
.. author: Martin Wimpress
-->

MATE チームは、[galculator](http://galculator.mnim.org/) チームと共同開発した結果、MATE1.10で `mate-calc` が galculator に置き換わるのを発表できてうれしく思います。

## galculator とは何ですか？

以下は galculator ウェブサイトの説明です。

> galculator は GTK 2 / GTK 3 ベースの電卓で、通常の表記/逆ポーランド表記 (RPN)、数式入力モード、異なる数値ベース (DEC、HEX、OCT、BIN)、および異なる角度単位 (DEG、RAD、GRAD) があります。4 桁精度の浮動小数点と 112 ビットの 2 進数演算をサポートしています。

galculator の主な特徴は次のとおりです。

  * 代数モード、RPN (逆ポーランド表記)、フォーミュラ入力およびペーパー・モード
  * 10進数、16進数、8進数、および 2進数ベース
  * Radiant、degree および grad をサポート
  * 基本モードと科学モード
  * ユーザー定義の定数と関数
  * 三角関数、べき乗、平方根、自然対数および常用対数、逆関数および双曲線関数
  * 設定可能なビット長と符号の二進演算
  * 四倍精度浮動小数点演算
  * 112 ビットの二進数演算
  * コピー＆ペースト
  * 20 種類以上の翻訳が用意されています。

MATE と同様、galculator は GTK2 および GTK3 にコミットしていて、メンテナンスされています。

## なぜ mate-calc を廃止したのですか？

`mate-calc` は実用的ですが、モダンなデスクトップ用電卓に必要とされる多くの機能が欠けています。MATE チームは規模が小さく、リソースも限られているため、可能な場合には、MATE に付加価値を与え、MATE チームの開発負担を軽減できるプロジェクトとの共同作業を試みています。galculator はこの点で最も適っています。

## galculator チームには何がありますか？

galculator は今後も完全に独立したプロジェクトであり続けますが、MATE に含まれることによって galculator のユーザー層が拡大し、galculator に対する関心が高まり、新たな貢献者が増えることを期待しています。そのために、MATE チームはgalculatorを[MATE transifex プロジェクト](https://www.transifex.com/organization/mate/dashboard/MATE)のリソースとして支援します。私たちは、~300人の立派な MATE 翻訳者が galculator を受け入れ、現在サポートする ~20の言語に追加できることを期待しています。

## 私はパッケージャです。これは私にどう影響しますか？

もしあなたが MATE パッケージのメンテナであれば、あなたのディストリビューション用の galculator パッケージが未だ存在していない場合には作成を開始し、MATE メタパッケージやパッケージグループに galculator を追加してください。MATE 1.10 のリリースは未だ先なので、時間は十分あります。

私たちがこのように考える理由を理解していただき、この協力関係での相互利益をご理解していただければ幸いです。コメント欄でご意見をお聞かせください。
