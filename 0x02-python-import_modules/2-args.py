#!/usr/bin/python3
import sys
if __name__ == "__main__":
    # Get all the command-line arguments except the script name
    args = sys.argv[1:]

    # Print the number of arguments
    arg_count = len(args)
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(arg_count, "Arguments:")

    # Print the list of arguments
    if arg_count > 0:
        for i, arg in enumerate(args, 1):
            print(i, ":", arg)

    # If no arguments were passed, print a period and a newline
    else:
        pass
