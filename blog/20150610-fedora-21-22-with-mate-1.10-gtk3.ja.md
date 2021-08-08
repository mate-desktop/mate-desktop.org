<!--
.. link:
.. description:
.. tags: Releases,Fedora
.. date: 2015-06-11 22:30:30
.. title: MATE 1.10 で Fedora 21/22 が GTK3対応に
.. slug: 2015-06-11-mate-1-10-with-gtk3-for-fedora-21-22
.. author: Wolfgang Ulbrich
-->

Fedora プロジェクトの MATE デスクトップメンテナ等は、実験的な GTK3 ビルドが Fedora 21 と Fedora 22 でテスト可能となったことを発表しました。これらのGTK3 ビルドは動作しますが、複数の小さなレンダリング問題があるので、みなさんのフィードバックが大切です。

## インストール

repo ファイルをインストールし、`yum update` を実行してください。

### Fedora 22

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-22/raveit65-Mate-GTK3-fedora-22.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-22.repo /etc/yum.repos.d/
    $ sudo yum update

### Fedora 21

    $ wget https://copr.fedoraproject.org/coprs/raveit65/Mate-GTK3/repo/fedora-21/raveit65-Mate-GTK3-fedora-21.repo
    $ sudo cp raveit65-Mate-GTK3-fedora-21.repo /etc/yum.repos.d/
    $ sudo yum update

あるいは `dnf` コマンドを使ってください。

    $ sudo dnf copr enable raveit65/Mate-GTK3
    $ sudo dnf update

## 問題を報告するには

GitHub の MATE デスクトップ issue tracker を使い、'GTK3 and Fedora' を件名に含めてください。

  * https://github.com/mate-desktop

いくつかの注意点:

  * Compiz はウィンドウ装飾として `emerald` だけで動作します。
  * Fedora stable の GTK2 パッケージと上記のリポジトリの GTK3 パッケージを混在させて使用しないでください。
  .
  * 次の MATE アプリケーションは、GTK3 ビルドの MATE と一緒に使用しないでください。GTK3 へ移植されていないからです。
    * mintMenu および MATE Menu
    * mate-applet-streamer
    * mate-applet-lockkeys
    * mate-applet-softupd
    * caja-terminal
