"""this program append 'ism' at the end of the string passed as a parameter or None"""
from sys import argv
def main():
    if len(argv) >= 2:
        for param in argv[1:]:
            if not param.endswith("ism"):
                print(param + "ism")
    else:
        print("none")
main()
