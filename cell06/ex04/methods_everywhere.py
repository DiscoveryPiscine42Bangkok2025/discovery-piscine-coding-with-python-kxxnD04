"""multiple methods in a single file"""
from sys import argv
def shrink(s):
    print(s[:8])
def enlarge(s):
    print(s + (8 - len(s)) * "Z")

if len(argv) < 2:
    print("none")
else:
    for param in argv[1:]:
        if len(param) < 8:
            enlarge(param)
        else:
            shrink(param)
