"""this program counts the length of parameters passed on the command line"""
from sys import argv
def main():
    print("Number of parameters:", len(argv) - 1)
main()
