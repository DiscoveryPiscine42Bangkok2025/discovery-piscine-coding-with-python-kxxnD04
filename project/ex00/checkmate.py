"""Check if the king is in checkmate or not."""
"""Rules: 1. all pieces contain Pawns, Bishops, Rooks, Queens and a King.
          2. The valid board is a square (N x N).
          3. All pieces against the King.
          4. A piece can only capture the first possible piece that stands on its path.
"""
R_DIREC = [(1, 0), (-1, 0), (0, 1), (0, -1)]
B_DIREC = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
Q_DIREC = R_DIREC + B_DIREC

def check_direc(direc, board, start, king_pos):
    rows = len(board)
    cols = len(board[0])
    for d in direc:
        x, y = start
        x += d[0]
        y += d[1]
        while 0 <= x < rows and 0 <= y < cols:
            if (x, y) == king_pos:  # เจอ King
                return True
            if board[x][y] != '.':  # เจอหมากอื่น
                break
            x += d[0]
            y += d[1]
    return False

def find_king(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'K':
                return (i, j)
    return None

def checkmate(board: str):
    king_count = board.count('K')
    board = [list(row.strip()) for row in board.splitlines()]
    rows = len(board)

    for r in range(rows):
        if len(board[r]) != rows:
            return "Error: The board is not a square."

    king_pos = find_king(board) # tuple (x, y)
    if not king_pos:
        return "Error: No King on the board."
    
    if king_count > 1:
        return "Error: More than one King on the board."

    enemy_pieces = ['R', 'B', 'Q', 'P']
    is_found = 0
    for i in range(rows):
        for j in range(rows):
            piece = board[i][j]
            if piece in enemy_pieces:
                if piece == 'R':  # แนวตั้งแนวนอน
                    if check_direc(R_DIREC, board, (i, j), king_pos):
                        is_found += 1
                elif piece == 'B':  # แนวทแยง
                    if check_direc(B_DIREC, board, (i, j), king_pos):
                        is_found += 1
                elif piece == 'Q':  # แนวตั้งแนวนอนและทแยง (8 ทิศ)
                    if check_direc(Q_DIREC, board, (i, j), king_pos):
                        is_found += 1
                elif piece == 'P':  # 2 ช่องแนวทแยงด้านหน้า
                    if (i - 1, j - 1) == king_pos or (i - 1, j + 1) == king_pos:
                        is_found += 1

    if is_found > 0:
        return print("Success")
    return print("Fail")
