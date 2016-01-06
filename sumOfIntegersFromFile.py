import sys


def its_a_number(line):
    if ord(line[0]) < 48 or ord(line[0]) > 59:
        isValid = False
    else:
        isValid = True
    return isValid


def main():
    x = 0
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        if its_a_number(test):
            test = test.strip()
            x += int(test)
    print(x)
    test_cases.close()


if __name__ == '__main__':
    main()
