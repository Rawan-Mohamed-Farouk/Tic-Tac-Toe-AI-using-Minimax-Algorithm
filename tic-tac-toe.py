EMPTY = None

def result(board, action):
    new_board = [row[:] for row in board]
    row, col = action
    if new_board[row][col] == EMPTY:
        new_board[row][col] = 'X'  # Assuming 'X' always starts first
        return new_board
    else:
        return None

def winner(board):
    for row in board + list(zip(*board)) + [(board[0][0], board[1][1], board[2][2]), (board[0][2], board[1][1], board[2][0])]:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return f"Player {row[0]} is the winner"

def terminal(board):
    def all_same(lst):
        return len(set(lst)) == 1 and lst[0] != EMPTY
    
    for row in range(3):
        if all_same(board[row]):
            return True, board[row][0]

    for col in range(3):
        if all_same([board[row][col] for row in range(3)]):
            return True, board[0][col]
    
    if all_same([board[i][i] for i in range(3)]) or all_same([board[i][2-i] for i in range(3)]):
        return True, board[1][1]
    
    if all(cell != EMPTY for row in board for cell in row):
        return True, EMPTY
    
    return False, EMPTY

def utility(board):
    terminal_state, winner = terminal(board)
    if terminal_state:
        if winner == 'X':
            return 1
        elif winner == 'O':
            return -1
        else:
            return 0
    else:
        return EMPTY

def minimax(board):
    terminal_state, winner = terminal(board)
    if terminal_state:
        if winner == 'X':
            return 1, EMPTY
        elif winner == 'O':
            return -1, EMPTY
        else:
            return 0, EMPTY
