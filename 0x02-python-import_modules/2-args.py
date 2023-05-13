#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))
    for number in range(len(argv)):
        if number == 0:
            pass
        else:
            print("{}: {}".format(number, argv[number]))
