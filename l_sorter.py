"""
    CUI で URL を整理するプログラム。
    パスを解釈して分けてくれる。非技術のページなども含むリストを大まかに振り分ける篩として用いる。
    クラスA
        - 公式ドキュメント、 MDN などのここから出発すべきもの
    クラスB
        - Qiita、Zenn 、 Stack Overflow、 各種フォーラムなどの公式ドキュメントなどではないテック系のサイト
    クラスC
        - はてなブログなど、とくにテック系であるとは限らないもの。

    追加時便利コマンド
        :'<,'>s/\(http.*\)/"\1\.*",/ | w | !black %
        :'<,'>sort u
"""
import sys

def main(lines: list) -> list:
    """
    投げたパスのリストをクラス分けして返す。
    """
    class_a: list = []
    class_b: list = []
    class_c: list = []
    class_a_list: list = [
        "https://developer.mozilla.org/",
        "https://doc.rust-jp.rs/",
        "https://docs.oracle.com/en/java/",
        "https://docs.python.org/ja/",
        "https://github.com/Microsoft/TypeScript-Handbook",
        "https://ja.reactjs.org/",
        "https://ja.reactjs.org/docs/getting-started.html",
        "https://nextjs-ja-translation-docs.vercel.app/",
        "https://nextjs.org/",
        "https://pptr.dev/",
        "https://www.typescriptlang.org/docs/",
    ]
    class_b_list: list = [
        "https://e-words.jp/",
        "https://github.com/",
        "https://it-trend.jp/words/",
        "https://ja.stackoverflow.com/",
        "https://jp.quora.com/",
        "https://js.studio-kingdom.com/typescript/handbook/",
        "https://pandoc-doc-ja.readthedocs.io/",
        "https://qiita.com/",
        "https://typescript-jp.gitbook.io/deep-dive/",
        "https://vim-jp.org/",
        "https://wa3.i-3-i.info/",
        "https://www.ipa.go.jp/security/",
        "https://www.otsuka-shokai.co.jp/words/",
        "https://www.sophia-it.com/",
        "https://www.tohoho-web.com/",
        "https://zenn.dev/",
    ]

    for line in iter(lines):
        if is_class_x(line, class_a_list):
            class_a.append(line)
        elif is_class_x(line, class_b_list):
            class_b.append(line)
        else:
            class_c.append(line)

    return [sorted(class_a), sorted(class_b), sorted(class_c)]


def is_class_x(path: str, class_x_list: list) -> bool:
    """
    あるパスがリストの中のパスとマッチするか調べる。
    """
    for condition in class_x_list:
        if condition in path:
            return True
    return False


if __name__ == "__main__":
    PATH: list = list(set(sys.stdin.readlines()))
    RES: list = main(PATH)

    for INDEX in range(len(RES)):
        for URL in RES[INDEX]:
            print(URL.strip())
