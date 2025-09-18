import sys
from checkmate import *

def main():
    if len(sys.argv) < 2:
        print("No file was passed as argument")
        return

    for filename in sys.argv[1:]:
        if not filename.endswith(".chess"):
            print(f"Skipping {filename}: not a .chess file")
            continue

        try:
            with open(filename, "r") as f:
                board_str = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            continue

        result = checkmate(board_str)
        print(f"{filename}: {result}")

if __name__ == "__main__":
    main()