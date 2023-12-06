#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    u = list(uniq)
    n = u[0]
    for i in range(1, len(u)):
        n += u[i]
    return n
