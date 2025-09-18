"""Main program to test the checkmate function."""

from checkmate import *

def main():
    board1 = """\
    R...
    .K..
    ..P.
    ....\
    """

    board2 = """.........
.........
.........
.....R...
.....K...
.........
.........
.........
........."""
    # invalid board (not square)
    board3 = """\
    R...
    .K......
    ..P.
    ....\
    """
    # No king
    board4 = """\
    R...
    ....
    ..P.
    ....\
    """

    # more tha1n 1 king
    board5 = """\
    R...
    .K..
    ..P.
    ..K.\
    """
    print(checkmate(board1))
    print(checkmate(board2))
    print(checkmate(board3))
    print(checkmate(board4))
    print(checkmate(board5))
if __name__ == "__main__":
    main()
