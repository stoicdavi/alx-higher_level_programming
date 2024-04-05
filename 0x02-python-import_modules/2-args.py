#!/usr/bin/python3
import sys
#getting number of arguments
arguments = len(sys.argv) - 1 # subtracting 1 because the first argument is the name of the file
if arguments == 0:
    print(":")
elif arguments == 1:
    print("{}: {} argument".format(arguments, sys.argv[1]))
else:
    print("{} arguments:".format(arguments))
    for i in range(1, arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))

