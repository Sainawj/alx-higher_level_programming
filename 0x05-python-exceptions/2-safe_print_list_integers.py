#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    
    for item in my_list:
        if printed_count >= x:
            break
        
        if isinstance(item, int):
            print("{:d}".format(item), end="")
            printed_count += 1

    print()
    return printed_count
