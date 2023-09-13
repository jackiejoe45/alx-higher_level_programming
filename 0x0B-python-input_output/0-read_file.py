#!/usr/bin/python3
"""
A function which prints the contents of a file
"""
def read_file(filename=""):
	with open(filename) as file:
		content = file.read()
	print(content, end="")
