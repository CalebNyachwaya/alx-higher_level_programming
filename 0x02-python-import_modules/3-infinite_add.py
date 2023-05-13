#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for number in range(len(argv)):
        if number == 0:
            pass
        else:
            sum += int(argv[number])
    print("{}".format(sum))
