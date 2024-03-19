#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = 0
    for i, arg in enumerate(sys.argv[1:], 1):
        result += int(arg)
        print(result)
