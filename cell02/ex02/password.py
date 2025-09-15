"""This script checks if a password is correct or not."""
def main():
    """Main function to check if a password is correct."""
    password = "Python is awesome"
    user_input = input("Enter the password: ").strip()
    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
main()
