'''
tic tac toe game
author: Luis A. Rojas
'''

def main():   
    wellcome() 
    player = next_player("")
    board = make_board()
    while not (winner(board) or draw(board)):
        show_board(board)
        select_position(player, board)
        player = next_player(player)
    show_board(board)
    print("Thanks for play")


def wellcome():
    print("Hi, Now we will playing tic tac toe")
    input()
    know = input("Do yu know how to play? (YES / NO): ")
    if know.lower() =="yes":
        print("Excellent, let's start")
    elif know.lower() =="no":
        print ("Instructions:")
        print("     You must choose a position number between 1 to 9") 
        print("     on the board to replace it with an 'O' or an 'X'")
        print("     depending on the symbol you use.")
    input()
    print("Are you ready?")
    input()
    print("Let's start")
    input()



def make_board():
    board = []
    for number in range(9):
        board.append(number + 1)
    return board
    
def show_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('--|---|--')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('--|---|--')
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def select_position(player, board):
    number_position = int(input(f"Turn of {player}, choose a number (1 - 9): "))
    board[number_position - 1] = player

def next_player(turn):
    if turn =="o" or turn =="":
        return "x"
    elif turn =="x":
        return "o"

def draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def winner(board):
    return (board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[6] == board[7] == board[8] or
            board[3] == board[4] == board[5] or
            board[0] == board[1] == board[2] or
            board[1] == board[4] == board[8] or
            board[6] == board[4] == board[2] 
             )

if __name__ == "__main__":
    main()