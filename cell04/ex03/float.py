"""This script check that the input is a float or int number"""
def main():
    user_input = float(input("Give me a number: "))
    if user_input - (int(user_input)) == 0.00:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
main()
