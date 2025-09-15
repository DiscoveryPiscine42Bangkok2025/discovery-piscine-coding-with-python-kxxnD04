"""This script get a number and display its multiplication table."""
def main():
    """Main function to display multiplication table of a number."""
    num = int(input("Enter a number\n"))
    for i in range(10):
        print(i, "x", num, "=", num * i)
main()
