#!/usr/bin/env python
# coding:utf-8
"""
img2ascii.py
image to ascii art.
"""
import sys
from PIL import Image
import numpy as np


class img_to_ascii(object):
    """img to ascii art class
    """

    def __init__(self):
        self.__char_pixel = [[]]
        self.__width = 5
        self.__height = 5
        self.__img_pixels = np.zeros((5, 5))
        self.__ascii_palette = {0.000000: ' ', 0.024761: '`', 0.038025: '.',
                                0.039794: '\\', 0.054827: ', ', 0.058806: '_',
                                0.059248: '-', 0.076050: ':', 0.077819: '~',
                                0.084009: '"', 0.085188: '^', 0.089167: '!',
                                0.092852: ';', 0.108327: '/', 0.108475: '<',
                                0.108622: '\\\\', 0.109211: '>', 0.111275: '+',
                                0.113338: '|', 0.114370: ')', 0.115402: '(',
                                0.125718: '=', 0.127929: 'L', 0.131172: 'v',
                                0.136035: '?', 0.138541: 'T', 0.138836: 't',
                                0.141046: '7', 0.142962: 'r', 0.144289: '}',
                                0.145763: 'x', 0.147089: 'z', 0.147826: 'c',
                                0.148121: 'i', 0.148268: '[', 0.148563: ']',
                                0.150332: 'Y', 0.150774: 'l', 0.151216: '{',
                                0.152100: 'f', 0.154164: 'I', 0.157259: 'n',
                                0.157553: 'u', 0.159617: '*', 0.159764: 's',
                                0.160648: 'J', 0.164480: 'y', 0.164923: 'j',
                                0.165070: 'F', 0.166544: '1', 0.168755: '4',
                                0.172144: 'o', 0.174945: 'V', 0.180693: 'h',
                                0.182167: 'a', 0.183493: 'e', 0.185999: 'k',
                                0.188504: '2', 0.190125: 'Z', 0.194547: 'X',
                                0.198379: '9', 0.199116: 'P', 0.199705: 'A',
                                0.200295: 'C', 0.200884: '6', 0.205601: '3',
                                0.206338: 'w', 0.206780: 'U', 0.208548: 'E',
                                0.208696: 'p', 0.210022: 'K', 0.210906: 'm',
                                0.213117: 'b', 0.213559: 'H', 0.213707: 'q',
                                0.214886: '5', 0.217981: 'd', 0.222697: 'S',
                                0.226824: '@', 0.231393: '#', 0.233604: 'O',
                                0.237583: 'D', 0.238025: 'R', 0.238172: 'G',
                                0.239057: '%', 0.242152: 'N', 0.245689: '&',
                                0.251437: '8', 0.252174: 'g', 0.253206: 'W',
                                0.257922: '0', 0.258217: 'B', 0.265144: 'Q',
                                0.267207: 'M', 0.268091: '$'}

    def load_img(self, filename):
        """load img method

        Arguments:
            filename {str} -- image file name

        Returns:
            np.array -- image's pixel array
        """
        img = Image.open(filename)
        self.__width, self.__height = img.size
        gray_img = img.convert('L')
        self.__img_pixels = []
        for y in range(self.__height):
            tmp_list = []
            for x in range(self.__width):
                # pixel / 255 * 0.268 ってしてる最後の0.268091はマジックナンバーっぽい?．
                tmp_list.append(gray_img.getpixel((x, y)) / 255.0 * 0.268091)
            self.__img_pixels.append(tmp_list)
        self.__img_pixels = np.array(self.__img_pixels)

    def pixel_to_char(self):
        """pixel to char
        """
        out_str_list = []
        for x in range(self.__width):
            str_line = ''
            for y in range(self.__height):
                str_line += self.__get_near_value(self.__img_pixels[x][y])
            str_line += '\n'
            out_str_list.append(str_line)
        return out_str_list

    def __get_near_value(self, num):
        """get nearest value

        Arguments:
            num {float} -- target value

        Returns:
            float -- nearest value
        """
        keys_list = list(self.__ascii_palette.keys())
        idx = np.abs(np.asarray(keys_list) - num).argmin()
        return self.__ascii_palette[keys_list[idx]]


def main():
    """main function
    """
    ascii_img = img_to_ascii()
    ascii_img.load_img(sys.argv[1])
    ascii_art = ascii_img.pixel_to_char()
    for s in ascii_art:
        print(s, end='')


if __name__ == '__main__':
    main()
