"""This program will run on cmd line with 0 or 1 parameters"""

import sys

def main():
    if len(sys.argv) == 1: # only the script name is present
        print("None")
    else:
        user_input = input("What was the parameter? ")
        if user_input == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
main()
