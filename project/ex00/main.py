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
    checkmate(board1)
    checkmate(board2)
    checkmate(board3)
    checkmate(board4)
    checkmate(board5)
if __name__ == "__main__":
    main()
