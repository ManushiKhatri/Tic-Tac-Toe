import random

# Initialize the board as a list of lists
board = [["-" for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_input():
    while True:
        try:
            position = int(input("Enter a number 1-9: ")) - 1
            if 0 <= position <= 8 and board[position // 3][position % 3] == "-":
                return position
            else:
                print("Oops! Invalid input or position already taken. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(cell != "-" for row in board for cell in row)

def switch_player(current):
    return "X" if current == "O" else "O"

def computer_move():
    return random.randint(0, 8)

def clear_screen():
    print("\033[H\033[J")  # ANSI escape codes to clear the terminal screen

# Main game loop
current_player = "X"
players = int(input("How many players? (1 or 2): "))
clear_screen()

while True:
    display_board(board)

    if current_player == "X" or (current_player == "O" and players == 2):
        position = player_input()
    else:
        position = computer_move()

    row, col = position // 3, position % 3
    board[row][col] = current_player

    if check_winner(board, current_player):
        display_board(board)
        print(f"The winner is {current_player}!")
        break
    elif check_tie(board):
        display_board(board)
        print("It's a Tie!")
        break

    current_player = switch_player(current_player)
    clear_screen()
