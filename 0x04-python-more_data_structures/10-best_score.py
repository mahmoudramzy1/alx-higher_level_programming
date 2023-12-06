#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n = list(a_dictionary.values())[0]
        for i, m in a_dictionary.items():
            if m > n:
                n = m
                k = i
        return k
    return None
