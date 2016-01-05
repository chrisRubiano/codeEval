import sys


def is_divisible(x, y, n):
    result = ""
    for i in range(n):
        j = i + 1
        if j % x == 0 and j % y == 0:
            result += " FB"
        elif j % x == 0:
            result += " F"
        elif j % y == 0:
            result += " B"
        else:
            result += " "+str(j)
    return result


def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        x, y, n = [int(m) for m in test.split(' ')]
        print(is_divisible(x, y, n))
    test_cases.close()


if __name__ == '__main__':
    main()
