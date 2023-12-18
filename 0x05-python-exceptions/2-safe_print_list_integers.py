#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, c = 0, 0
    for i in range(x): 
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
        except (BaseException, IndexError):
            pass
        i += 1
    print()
    return c
