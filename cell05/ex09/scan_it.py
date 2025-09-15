"""This program reads two parameters and checks if the first one is in the second one"""
from sys import argv
from re import findall
def main():
    if len(argv) == 3:
        if argv[1] in argv[2]:
            print(len(findall(argv[1], argv[2])))
        else:
            print("none")
    else:
        print("none")
main()
