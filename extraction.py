#!/usr/bin/env python
# coding=UTF-8
"""
upper case <-> lower case script
"""

import sys


def extraction(text, mode):
    """
    extraction

    Parameters
    ----------
    text : str
        target text
    mode : str
        extraction mode (big: upper case, little: lower case)
    Returns
    -------
    output : str
        extraction text
    """

    output = ""
    for s in text:
        print(s)
        if mode == "big":
            if ("A" <= s <= "Z")or(s == "{")or(s == "}")or(s == "_"):
                output += s
        elif mode == "little":
            if ("a" <= s <= "z")or(s == "{")or(s == "}")or(s == "_"):
                output += s
    return output


def main():
    """
    main

    Parameters
    ----------
    none
    Returns
    -------
    none
    """

    args = sys.argv
    file_name = args[1]
    mode = args[2]
    with open(file_name, "r", encoding="UTF-8") as f:
        text = f.read()

    print(extraction(text, mode))


if __name__ == '__main__':
    main()
