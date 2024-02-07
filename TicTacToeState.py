### State representing a Tic-Tac-Toe board. ' ' is used for unfilled squares.
from copy import deepcopy


class TicTacToeState():
    def __init__(self, board=None):
        self.score = 0
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]

    def __repr__(self):
        return self.board.__repr__()


def is_goal(state):
    if rowWin(state.board) or colWin(state.board) or diagonalWin(state.board):
        return True
    elif boardFull(state.board):
        return True
    else:
        return False


# player is either 'x' or 'o'
def successors(state, player):
    successor_states = []
    for i in range(3):
        for j in range(3):
            if state.board[i][j] == ' ':
                newstate = deepcopy(state)
                newstate.board[i][j] = player
                successor_states.append(newstate)
    return successor_states


# win for x = 1, win for o = -1, tie=0
def score_state(state) :
    winner = rowWin(state.board) or colWin(state.board) or diagonalWin(state.board)
    if winner and winner == 'x' :
        return 1
    elif winner and winner == 'o' :
        return -1
    else :
        return 0

#############
## TicTacToeState

### Helper functions to determine whether we are at a leaf node.
# if there is a row winner, return their letter
def rowWin(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return False


def colWin(board):
    for i in range(3):
        col = [item[i] for item in board]
        if len(set(col)) == 1 and col[0] != ' ':
            return col[0]
    return False


def diagonalWin(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]
    else:
        return False

def boardFull(board):
    if any(x == ' ' for x in board[0]) or any(x == ' ' for x in board[1]) or any(x == ' ' for x in board[2]):
        return False
    else:
        return True


def flipPlayer(player) :
    if player == 'x' :
        return 'o'
    else :
        return 'x'

##  player will be x or o.

## you implement this.
def minimax(current_state, player) :
    pass


