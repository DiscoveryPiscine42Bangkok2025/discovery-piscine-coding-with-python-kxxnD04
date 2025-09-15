"""Advanced multiplication table script."""
def main():
    """Main function to display advanced multiplication table."""
    i = 0
    j = 0
    while i < 11:
        print(f"Table de {i}: ", end="")
        while j < 11:
            print(i*j, end=" ")
            j += 1
        print()
        i += 1
        j = 0
main()
