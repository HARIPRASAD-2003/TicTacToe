"""
Tic Tac Toe Player
"""
import math
X = "X"
O = "O"
EMPTY = None
user=0
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
    turn=int(1)
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                continue
            else:
                turn+=int(1)
    if turn%int(2)==int(0):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                b=(i,j)
                a.add(b)
    if len(a)!=int(0):
        return a
    else:
        return None

def result(board,action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=board
    if action!=None:
        (i,j)=action
        if board[i][j]==EMPTY:
            new_board[i][j]=player(board)
            return new_board
        else:
            return board
    else:
        return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board: #row winner
        if i[0]!=None:
            if i[0]==i[1]:
                if i[1]==i[2]:
                    return i[1]
    else:
        for j in range(3): #column winner
            if board[0][j]!=None:
                if board[0][j]==board[1][j]:
                    if board[1][j]==board[2][j]:
                        return board[0][j]
        else:
            if board[1][1]!=None: #diagonal winner
                if board[0][0]==board[1][1]==board[2][2]:
                    return board[0][0]
                elif board[0][2]==board[1][1]==board[2][0]:
                    return board[1][1]
            else:
                return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    c=int(0)
    for i in range(3):
        for j in board[i]:
            if j==EMPTY:
                c+=int(1)
    if c!=int(0):
        if winner(board)==X or winner(board)==O: 
            return True
        else:
            return False
    else:
        if winner(board)==X or winner(board)==O:
            return True
        elif c==int(0): 
            return True
        else:
            return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if user==1:
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1 
        elif terminal(board):
            return 0
    else:
        if winner(board)==X:
            return -1 
        elif winner(board)==O:
            return 1 
        elif terminal(board):
            return 0

def undo(action,board):
    new_board=board
    if action!=None:
        (i,j)=action
        if board[i][j]!=EMPTY:
            new_board[i][j]=EMPTY
            return new_board


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global user
    if board==initial_state():
        user=1
    
    bestScore = -math.inf
    bestMove = None
    for action in actions(board):
        board=result(board,action)
        score = best_move(False,board)
        board=undo(action,board)
        if (score > bestScore):
            bestScore = score
            bestMove = action
    if terminal(result(board,bestMove)):
        user=0
    return bestMove

def best_move(isMaxTurn,board):
    if terminal(board):
        return utility(board)

    if isMaxTurn:
        bestScore = -math.inf
        for action in actions(board):
            board=result(board,action)
            score = best_move(False,board)
            board=undo(action,board)
            if (score > bestScore):
                bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for action in actions(board):
            board=result(board,action)
            score = best_move(True,board)
            board=undo(action,board)
            if (score < bestScore):
                bestScore = score
        return bestScore