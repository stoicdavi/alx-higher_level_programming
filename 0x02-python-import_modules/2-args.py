#!/usr/bin/python3
from sys import argv

def main():
    argument_count = len(argv) - 1 # subtract 1 to exclude the script name
    if argument_count == 0:
        print("0 arguments.")
    elif argument_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument_count))
    for i in range(1, argument_count + 1):
        print("{}: {}".format(i, argv[i]))
if __name__ == "__main__":
    main()