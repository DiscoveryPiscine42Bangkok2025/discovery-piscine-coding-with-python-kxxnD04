"""This program will run on cmd line with 0 or multiple parameters and display their length"""

import sys

def main():
    if len(sys.argv) == 1: # only the script name is present
        print("None")
    else:
        for arg in sys.argv[1:]:
            print(arg, len(arg), sep=": ")
main()
