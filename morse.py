#!/usr/bin/env python
# coding:utf-8

"""
morse.py
Morse Code Script
"""


class Morse():
    """
    Morse
    . : 1
    - : 11
    space : 0

    example
    ----------
    SOS : 101010001101101100010101

    Args
    ----------
    __morse_table :{"Character":"Code"}
        Morse Code Transform Table
    Attributes
    ----------
    method : return
        method_description
    """

    def __init__(self):
        self.__morse_table = {
            "A": "1011", "B": "11010101", "C": "101101", "D": "110101",
            "E": "1", "F": "10101101", "G": "1101101", "H": "1010101",
            "I": "101", "J": "1011011011", "K": "1101011", "L": "10110101",
            "M": "11011", "N": "1101", "O": "11011011", "P": "101101101",
            "Q": "1101101011", "R": "101101", "S": "10101", "T": "11",
            "U": "101011", "V": "10101011", "W": "1011011", "X": "110101011",
            "Y": "1101011011", "Z": "110110101", "0": "11011011011011",
            "1": "1011011011011", "2": "101011011011", "3": "10101011011",
            "4": "1010101011", "5": "101010101", "6": "1101010101",
            "7": "11011010101", "8": "110110110101", "9": "1101101101101",
            ".": "10110101101011", ",": "110110101011011", "?": "1010110110101",
            "!": "110101101011011", "-": "1101010101011", "/": "11010101101",
            "@": "10110110101101", "(": "110101101101", ")": "110101101101011"}

    def text_to_morse(self, text):
        """
        text_to_morse

        Parameters
        ----------
        text : str
            text
        Returns
        -------
        code : int
            morse code
        """
        code = ""
        text = text.upper()
        for s in text:
            if self.__morse_table.get(s) != None:
                code += self.__morse_table.get(s)
                code += "0"*3
            elif s == " ":
                code += "0"*4
        return code[:-3]

    def morse_to_text(self, code):
        """
        morse_to_text

        Parameters
        ----------
        code : str
            morse code
        Returns
        -------
        text : str
            text
        """

        text = ""
        tmp_code = ""
        code += "000"
        for s in code:
            tmp_code += s
            print(tmp_code)
            if tmp_code == "0000":
                text += " "
                tmp_code = ""
            elif tmp_code[-3:] == "000" and len(tmp_code) != 3:
                text += self.__get_char_from_code(tmp_code[:-3])
                tmp_code = ""
        return text

    def __get_char_from_code(self, code):
        char = [k for k, v in self.__morse_table.items() if v == code]
        if char:
            return char[0]
        return ""


def main():
    """
    main function

    Parameters
    ----------
    none
    Returns
    -------
    none
    """
    morse = Morse()
    code = morse.text_to_morse("SOS, test text.")
    text = morse.morse_to_text(code)
    print(code)
    print(text)


if __name__ == '__main__':
    main()
