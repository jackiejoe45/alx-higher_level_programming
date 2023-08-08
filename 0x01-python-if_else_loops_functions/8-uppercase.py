#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_code = ord(char)
        if ord('a') <= char_code <= ord('z'):
            char_code -= ord('a') - ord('A')
        print("{}".format(chr(char_code)), end="")
    print("")
