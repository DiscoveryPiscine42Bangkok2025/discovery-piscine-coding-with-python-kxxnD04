"""display all parameters in lowercase or None"""
from sys import argv
def downcase_all(s): 
    return s.lower()
if len(argv) >= 2:
    for param in argv[1:]:
        print(downcase_all(param))
else:
    print("none")
