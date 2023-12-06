#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        for i in roman_string:
             y = d[i]
            n += y if n < y * 5 else -n
        return n
    return 0
