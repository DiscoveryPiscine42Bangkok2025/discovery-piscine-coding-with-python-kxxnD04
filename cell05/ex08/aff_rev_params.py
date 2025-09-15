"""This program display all parameters in reverse order or None"""
from sys import argv
def main():
    if len(argv) >= 2:
        for param in reversed(argv[1:]):
            print(param)
    else:
        print("none")
main()
