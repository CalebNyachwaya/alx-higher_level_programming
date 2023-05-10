#!/usr/bin/python3
for number in range(0, 100):
    if number <= 9:
        print("0" + str(number), end=', ')
    else:
        if number < 99:
            print(number, end=', ')
        else:
            print(number)
