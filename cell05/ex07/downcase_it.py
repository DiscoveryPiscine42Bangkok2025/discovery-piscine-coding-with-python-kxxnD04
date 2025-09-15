"""display the first parameter in lowercase or None"""
from sys import argv
def main():
    if len(argv) == 2:
        print(argv[1].lower())
    else:
        print("none")
main()
