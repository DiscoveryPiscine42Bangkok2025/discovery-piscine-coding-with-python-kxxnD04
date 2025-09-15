"""This program print the first parameter passed to the script or None"""
from sys import argv
def main():
    if len(argv) == 2:
        print(argv[1])
    else:
        print("none")
main()
