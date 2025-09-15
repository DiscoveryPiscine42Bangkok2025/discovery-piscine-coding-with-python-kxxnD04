"""This program iterates through an array and adds 2 to each element if that element is greater than or equal to 5"""
def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    new_arr = []
    print("Original array:", arr)
    for i in range(len(arr)):
        if arr[i] >= 5:
            new_arr.append(arr[i] + 2)
    print("New array:", new_arr)
main()
