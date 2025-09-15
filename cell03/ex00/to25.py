"""This script get a number and count from that number to 25."""
def main():
    """Main function to count from a number to 25."""
    num = int(input("Enter a number less than 25\n"))
    if num < 25:
        while num <= 25:
            print("Inside the loop, my variable is", num)
            num += 1
    else:
        print("Error")
main()
