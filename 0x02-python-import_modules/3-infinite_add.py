#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    sum = 0
    for i in arguments:
        sum += int(i)
    print(sum)