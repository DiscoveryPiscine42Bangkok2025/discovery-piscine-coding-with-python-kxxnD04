"""This script checks if a number is negative, positive or both."""
def main():
    """Main function to check if a number is negative, positive or both."""
    number = int(input())
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
main()
