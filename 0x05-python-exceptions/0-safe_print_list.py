#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for index, item in enumerate(my_list):
        if count >= x:
            break
        try:
            print("{:d}".format(item), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
