"""This script get two numbers, multiplies them and checks if the result is negative, positive or zero."""
def main():
    """Main function to multiply two numbers and check the result."""
    num1 = int(input("Enter the first number: \n"))
    num2 = int(input("Enter the second number: \n"))
    result = num1 * num2
    print(f"{num1} X {num2} = {result}")
    if result < 0:
        print("The result is negative.")
    elif result > 0:
        print("The result is positive.")
    else:
        print("The result is zero.")
main()
