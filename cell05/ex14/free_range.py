"""This programs takes two numbers as parameters and displays the range of numbers between them"""
from sys import argv
def main():
    if len(argv) == 3 and argv[1].isdigit() and argv[2].isdigit():
        arr = []
        step = 1 if int(argv[1]) <= int(argv[2]) else -1
        for i in range(int(argv[1]), int(argv[2]) + step, step):
            arr.append(i)
        print(arr)
    else:
        print("none")
main()
