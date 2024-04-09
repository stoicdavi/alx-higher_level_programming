#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for i in argv:
        if argv.index(i) == 0:
            continue
        result += int(i)
    print(result)
