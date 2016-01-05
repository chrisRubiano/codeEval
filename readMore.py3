def trim_line(line):
    if len(line) <= 55:
        return line
    elif len(line) > 55:
        line = line[0:40]
        if line.rfind(' ') != -1:
            line = line[0:line.rfind(' ')]
        return line + "... <Read More>"


def main():
    textFile = open("text.txt", "r")
    for line in textFile:
        print(trim_line(line))


if __name__ == '__main__':
    main()
