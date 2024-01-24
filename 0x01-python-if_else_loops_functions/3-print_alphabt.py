#!/usr/bin/python3
# for letter in range(97, 123):
#     if letter != 101 and letter != 113:
#         print("{}".format(chr(letter)), end="")
for i in range(97, 123):
    if chr(i) not in ('q', 'e'):
        print("{}".format(chr(i)), end='')
