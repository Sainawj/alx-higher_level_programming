#!/usr/bin/python3
import sys
import hidden_4 as hidden

if __name__ == "__main__":
    names = [name for name in dir(hidden) if not name.startswith("__")]
    for name in names:
        print(name)
