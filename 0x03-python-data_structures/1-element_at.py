#!/usr/bin/python3
def element_at(my_list, idx):
    try:
        return my_list[idx]
    except IndexError:
        return 'None'
