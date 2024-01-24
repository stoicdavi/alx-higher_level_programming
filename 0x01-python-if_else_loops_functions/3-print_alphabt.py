#!/usr/bin/python
for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end="")