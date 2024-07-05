_chessboard = {i: 0 for i in range(1, 65)}

def cells_under_attack(chessboard, x, y):
    # Calculate the cell number from the row and column numbers
    cell_number = (x - 1) * 8 + y

    # Mark cells under attack horizontally
    for i in range(1, 9):
        if i!= y:
            chessboard[(x - 1) * 8 + i] = -1

    # Mark cells under attack vertically
    for i in range(1, 9):
        if i!= x:
            chessboard[(i - 1) * 8 + y] = -1

    # Mark cells under attack diagonally (top-left to bottom-right)
    for i, j in zip(range(x - 1, 0, -1), range(y - 1, 0, -1)):
        chessboard[(i - 1) * 8 + j] = -1

    # Mark cells under attack diagonally (bottom-left to top-right)
    for i, j in zip(range(x + 1, 9), range(y + 1, 9)):
        chessboard[(i - 1) * 8 + j] = -1

    # Mark cells under attack diagonally (top-right to bottom-left)
    for i, j in zip(range(x - 1, 0, -1), range(y + 1, 9)):
        chessboard[(i - 1) * 8 + j] = -1

    # Mark cells under attack diagonally (bottom-right to top-left)
    for i, j in zip(range(x + 1, 9), range(y - 1, 0, -1)):
        chessboard[(i - 1) * 8 + j] = -1

    # Place the queen on the specified cell
    chessboard[cell_number] = 1
    print_chessboard(_chessboard)

def print_chessboard(chessboard):
    """
    Prints the chessboard as an 8x8 matrix.

    Args:
        chessboard (dict): The chessboard dictionary, where keys are square numbers (1-64) and values are 0 (empty), 1 (queen), or -1 (under attack).

    Returns:
        None
    """
    for i in range(8):
        row = []
        for j in range(8):
            square_num = i * 8 + j + 1
            if chessboard[square_num] == 0:
                row.append('.')
            elif chessboard[square_num] == 1:
                row.append('Q')
            elif chessboard[square_num] == -1:
                row.append('*')
        print(' '.join(row))
    return None

cells_under_attack(_chessboard, 5,2)