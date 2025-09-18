"""add real checkmate logic"""
R_DIREC = [(1, 0), (-1, 0), (0, 1), (0, -1)]
B_DIREC = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
Q_DIREC = R_DIREC + B_DIREC
KING_MOVES = [(0,0),(1,0),(-1,0),(0,1),(0,-1),
              (1,1),(1,-1),(-1,1),(-1,-1)]

def check_direc(direc, board, start):
    rows = len(board)
    cols = len(board[0])
    attacked = set()
    for d in direc:
        x, y = start
        x += d[0]
        y += d[1]
        while 0 <= x < rows and 0 <= y < cols:
            attacked.add((x, y))
            if board[x][y] != '.':
                break
            x += d[0]
            y += d[1]
    return attacked

def find_king(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'K':
                return (i, j)
    return None

def checkmate(board: str):
    board = [list(row.strip()) for row in board.splitlines()]
    rows = len(board)

    for r in range(rows):
        if len(board[r]) != rows:
            return "Error: The board is not a square."

    king_pos = find_king(board)
    if not king_pos:
        return "Error: No King on the board."

    enemy_pieces = ['R', 'B', 'Q', 'P']
    attacked = set()

    for i in range(rows):
        for j in range(rows):
            piece = board[i][j]
            if piece in enemy_pieces:
                if piece == 'R':
                    attacked |= check_direc(R_DIREC, board, (i,j))
                elif piece == 'B':
                    attacked |= check_direc(B_DIREC, board, (i,j))
                elif piece == 'Q':
                    attacked |= check_direc(Q_DIREC, board, (i,j))
                elif piece == 'P':
                    attacked |= {(i-1, j-1), (i-1, j+1)}

    king_zone = []
    for dx, dy in KING_MOVES:
        nx, ny = king_pos[0] + dx, king_pos[1] + dy
        if 0 <= nx < rows and 0 <= ny < rows:
            if board[nx][ny] == '.' or (nx,ny) == king_pos:
                king_zone.append((nx,ny))

    if king_pos not in attacked:
        return "Not in check"

    for pos in king_zone:
        if pos not in attacked:
            return "In check, but not checkmate"

    return "Checkmate!"

if __name__ == "__main__":
    board1 = """\
    R...
    .KQ.
    ..P.
    ....\
    """

    board2 = """.........
.........
.........
.....R...
.....KR..
.........
.........
.........
........."""
    print(checkmate(board1))
    print(checkmate(board2))
