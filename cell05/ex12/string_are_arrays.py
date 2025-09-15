"""this program display 'z' for each occurrence of the character 'z' in the string passed as a parameter or None"""
from sys import argv
def main():
    if len(argv) == 2 and "z" in argv[1]:
        print("z" * argv[1].count("z"))
    else:
        print("none")
main()
