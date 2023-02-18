"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
        #define variables
    countX, countO = 0, 0
        #check for number of X and O on board
    for i in range(3):
        for j in board:
            if j[i] == X:
                countX +=1
            elif j[i] == O:
                countO += 1
            else:
                pass
        #return whose turn it is
    if countX>countO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.append((i,j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currentPlayer = player(board)
    newboard = copy.deepcopy(board)
    print(action[0])
    xPos = action[0]
    yPos = action[1]

    newboard[xPos][yPos] = player(board)
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkHorizontal(board) != None:
        return checkHorizontal(board)
    elif checkVertical(board) != None:
        return checkVertical(board)
    elif checkDiagonal !=None:
        return checkDiagonal(board) 

def checkHorizontal(board):
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        else:
            return None

def checkVertical(board):
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
        else:
            return None

def checkDiagonal(board):
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O
    else:
        return None
def isDraw(board):
    countNone = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                countNone+=1
    if countNone == 0:
        return True
    else:
        return False
            
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if checkHorizontal(board) != None or checkVertical(board) != None or checkDiagonal(board) != None or isDraw(board) == True:
        return True
    else:
        False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    result = None
    value = None
    if terminal(board):
        return None
    elif player(board) == X:
        value, result = maximize(board)
        return result
    elif player(board) == O:
        value, result == minimize(board)
        return result

def maximize(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        a,b = minimize(result(board,action))
        if  a > v:
            v = a
            move = action
            if v == 1:
                return v,move
    return v,move

def minimize(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        a,b = maximize(result(board,action))
        if  a < v:
            v = a
            move = action
            if v == -1:
                return v, move
    return v, move

    """
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
    """




