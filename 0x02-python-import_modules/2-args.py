#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    arg_str = "{:d} argument".format(arg_count)
    if arg_count != 1:
        arg_str += "s"
    arg_str += ":"
    print(arg_str)

    for i, arg in enumerate(sys.argv[1:], 1):
        print("{:d}: {:s}".format(i, arg))
