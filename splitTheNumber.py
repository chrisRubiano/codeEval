#!/usr/bin/python
import sys

def sum(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        strings = test.split(" ")
        if '+' in strings[1]:
            ind = strings[1].index('+')
            x = int(strings[0][:ind])
            y = int(strings[0][ind:])
            result = sum(x,y)
        if '-' in strings[1]:
            ind = strings[1].index('-')
            x = int(strings[0][:ind])
            y = int(strings[0][ind:])
            result = sub(x,y)
        print(str(result))
    test_cases.close()


if __name__ == '__main__':
    main()