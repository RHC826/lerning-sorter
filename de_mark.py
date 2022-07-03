"""
    Markdown のリンクからなるリストをソートする
"""
import re
import sys


def de_mark(txt: str) -> str:
    """
    Markdown のリンクから URL を返す
    """
    txt = re.sub(r"^\[|\)$", "", txt)
    res = txt.split("](")
    return res[1]


def mark_sort(pre_sort: list) -> list:
    """
    Markdown のリンクからなるリストを URL の順番でソートする
    """
    res: list = sorted(pre_sort, key=de_mark)
    return res


if __name__ == "__main__":
    PATH: list = list(set(sys.stdin.readlines()))
    RES: list = mark_sort(PATH)

    for INDEX in RES:
        print(INDEX.strip())
