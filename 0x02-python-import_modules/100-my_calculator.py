#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    args = sys.argv[:]
    i = len(args)
    n = 0
    if i == 4:
        a = int(args[1])
        operator = args[2]
        b = int(args[3])
        if args[2] == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif args[2] == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif args[2] == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        elif args[2] == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
    else:

        print("usage: ./100-my_calculator.py <a> <operator> <b>")
