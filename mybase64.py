#!/usr/bin/env python
#coding:utf-8
""" Base64 Script """

import inspect

def str_to_bin(text):
	""" str -> binary """
	bin_text = ""
	for i in text:
		i_bin = format(ord(i), "b")
		bin_text += (i_bin if len(i_bin) == 8 else ("0" * (8 - len(i_bin))) + i_bin)
	return bin_text

def bin_to_str(bin_text):
	""" binary -> str """
	text = chr(int(bin_text, 2))
	return text

def split_n(text, n):
	""" split n """
	return [text[i: i+n] for i in range(0, len(text), n)]

def convert(text):
	""" convert by rule """
	dictionary = {"000000":"A", "000001":"B", "000010":"C", "000011":"D", "000100":"E", "000101":"F", "000110":"G", "000111":"H", "001000":"I", "001001":"J", "001010":"K", "001011":"L", "001100":"M", "001101":"N", "001110":"O", "001111":"P", "010000":"Q", "010001":"R", "010010":"S", "010011":"T", "010100":"U", "010101":"V", "010110":"W", "010111":"X", "011000":"Y", "011001":"Z", "011010":"a", "011011":"b", "011100":"c", "011101":"d", "011110":"e", "011111":"f", "100000":"g", "100001":"h", "100010":"i", "100011":"j", "100100":"k", "100101":"l", "100110":"m", "100111":"n", "101000":"o", "101001":"p", "101010":"q", "101011":"r", "101100":"s", "101101":"t", "101110":"u", "101111":"v", "110000":"w", "110001":"x", "110010":"y", "110011":"z", "110100":"0", "110101":"1", "110110":"2", "110111":"3", "111000":"4", "111001":"5", "111010":"6", "111011":"7", "111100":"8", "111101":"9", "111110":"+", "111111":"/"}

	conv_text = ""
	mode = inspect.currentframe().f_back.f_code.co_name
	if mode == "encode":
		text_list = split_n(text, 6)
		for i in text_list:
			conv_text += dictionary[i]
	else:
		for i in text:
			conv_text += [k for k, v in dictionary.items() if v == i][0]

	return conv_text

def encode(text):
	""" base64 encode function """
	bin_text = str_to_bin(text)
	print(bin_text)
	if len(bin_text) % 6 != 0:
		bin_text += ("0" * (6 - len(bin_text) % 6))
	conv_text = convert(bin_text)
	if len(conv_text) % 4 != 0:
		print(len(conv_text) % 4)
		conv_text = conv_text + ("=" * (4 - len(conv_text) % 4))

	return conv_text

def decode(text):
	""" base64 decode function """
	text = text.replace("=", "")
	bin_text = convert(text)
	print(bin_text)
	if len(bin_text) % 8 != 0:
		bin_text = bin_text[:-(len(bin_text) % 8)]
	bin_list = split_n(bin_text, 8)
	conv_text = ""
	for i in bin_list:
		conv_text += bin_to_str(i)

	return conv_text

def main():
	""" main function """

	text = input("text >>> ")
	mode = input("encode (e) or decode (d) >>> ")
	if mode == "e" or mode == "encode":
		print(encode(text))
	elif mode == "d" or mode == "decode":
		print(decode(text))

if __name__ == "__main__":
	main()
