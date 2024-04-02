#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for i in range(x):
            try:
                value = my_list[i]
                if isinstance(value, int):
                    print("{:d}".format(value), end=' ')
                    integers_printed += 1
            except IndexError:
                break
        print()
        return integers_printed
    except TypeError:
        return integers_printed
