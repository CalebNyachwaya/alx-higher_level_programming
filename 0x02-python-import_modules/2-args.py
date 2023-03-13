#!/usr/bin/python3
if __name__ == "__main__":
    import sys
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
        for i in range(1,arg_count + 1):
            print('{:d}: {:s}'.format(i, sys.argv[i]))

    # If no arguments were passed, print a period and a newline
    else:
        pass
