#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    args = sys.argv[:]
    if len(sys.argv) == 4:
        a = int(args[1])
        operator = args[2]
        b = int(args[3])
        if args[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif args[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif args[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif args[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
