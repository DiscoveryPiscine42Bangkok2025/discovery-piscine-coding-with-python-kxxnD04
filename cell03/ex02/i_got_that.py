"""this is a while loop program that stop when user input is STOP"""
def main():
    user_input = input("What you gotta say? : ")
    while user_input != "STOP":
        user_input = input("I got that! Anything else? : ")
main()
