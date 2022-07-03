"""
    Markdown のリンクからなるリストをソートする
"""
import sys
import re


def de_mark(txt: str) -> str:
    """
    Markdown のリンクから URL を返す
    """
    res = re.sub(r"^\[|\)$", "", txt)
    res = res.split("](")
    return res[1]


def mark_sort(foo: list) -> list:
    """
    Markdown のリンクからなるリストを URL の順番でソートする
    """
    bar: list = sorted(foo, key=lambda x: de_mark(x))
    return bar


if __name__ == "__main__":
    PATH: list = list(set(sys.stdin.readlines()))
    RES: list = mark_sort(PATH)

    for INDEX in RES:
        print(INDEX.strip())
