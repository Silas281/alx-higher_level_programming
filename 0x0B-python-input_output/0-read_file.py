#!/usr/bin/python3


def read_file(filename=""):
    """Write a function that reads a text file (UTF8) and prints it to stdout

    args:
        filename(str) - file name/path to file to be read
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")


if __name__ == '__main__':
    read_file("testFile.txt")
