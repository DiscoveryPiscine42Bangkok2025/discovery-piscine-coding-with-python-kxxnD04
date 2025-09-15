"""Basic calculator program with addition, subtraction, multiplication, and division."""
def main():
    """Main function to run the calculator."""
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
main()
