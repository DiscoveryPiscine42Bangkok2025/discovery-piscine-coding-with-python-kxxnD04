"""display the first parameter in uppercase or None"""
from sys import argv
def main():
    if len(argv) > 1:
        print(argv[1].upper())
    else:
        print("none")
main()
