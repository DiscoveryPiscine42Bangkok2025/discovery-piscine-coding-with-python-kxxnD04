"""This script asks for your name, lastname and prints it."""
def main():
    """Main function to ask for name and lastname."""
    first_name = input("Hey, what's your first name? : ").strip()
    last_name = input("And your last name? : ").strip()
    print("Well, pleased to meet you,", first_name, last_name + '.')
main()
