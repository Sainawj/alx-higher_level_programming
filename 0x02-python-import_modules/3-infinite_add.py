#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            result += int(i)
        print(result)
