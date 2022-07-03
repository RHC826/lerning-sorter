# lerning-sorter

CUI で URL を整理するプログラム。

非技術のページなども含むリストを大まかに振り分ける篩として使用してください。

        $ cat url.txt | python l_sorter.py

設定されているサイトが上位に来るようにソートされます。

## 設定の基準

設定のリストはコードに書き込まれているのでシングルファイルで動作します。設定は必要に応じて自由に書き換えてください。

- クラスA
    - 公式ドキュメント、 MDN などのここから出発すべきもの
- クラスB
    - Qiita、Zenn 、 Stack Overflow、 各種フォーラムなどの公式ドキュメントなどではないテック系のサイト
- クラスC
    - はてなブログなど、とくにテック系であるとは限らないもの。

