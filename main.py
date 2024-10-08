import random
from art import logo

def print_board(board):
    # Board with players inputs
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def print_labeled_board():
    # Board with labeled positions
    labeled_board = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9'
    ]

    print(f"{labeled_board[0]} | {labeled_board[1]} | {labeled_board[2]}")
    print("--+---+--")
    print(f"{labeled_board[3]} | {labeled_board[4]} | {labeled_board[5]}")
    print("--+---+--")
    print(f"{labeled_board[6]} | {labeled_board[7]} | {labeled_board[8]}")


def check_winner(board, player):

    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_board_full(board):

    return all([spot != ' ' for spot in board])


def player_move(board):

    while True:
        try:
            position = int(input("Choose a position (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                return position
            else:
                print("Invalid or occupied position, try again.")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")


def ai_move(board):

    available_positions = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_positions)


def tic_tac_toe():

    board = [' '] * 9
    current_player = 'X'


    game_mode = input("Do you want to play against another player (P) or AI (A)? \n").strip().upper()


    while True:
        print_board(board)

        if current_player == 'X':
            print("Player X's turn.")
            position = player_move(board)
        else:
            if game_mode == 'P':
                print("Player O's turn.")
                position = player_move(board)
            else:
                print("AI O's turn.")
                position = ai_move(board)

        board[position] = current_player


        if check_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print("Player X wins!")
            else:
                print("Player O (AI) wins!" if game_mode == 'A' else "Player O wins!")
            break


        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


print(logo)
print_labeled_board()
print("\n^ Reference the above board to see positions labeled ^\n")
tic_tac_toe()
