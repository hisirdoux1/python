# mines_game.py

import random
import transactions

# Constants for the game
ROWS, COLS = 5, 5
MIN_BET = 10
MAX_MINES = 24  # Maximum number of mines that can be set on the board

# Function to calculate multipliers based on number of mines
def calculate_multipliers(max_mines, rows, cols):
    multipliers = {}
    # Placeholder values for multipliers based on the provided images
    # You might want to adjust the values based on your game design
    multiplier_increments = {
        3: [1.11, 1.25, 1.43, 1.68, 1.96, 2.3],
        4: [1.17, 1.39, 1.68, 2.00, 2.48, 3.1]
    }
    
    for mines in range(1, max_mines + 1):
        if mines in multiplier_increments:
            multipliers[mines] = multiplier_increments[mines]
        else:
            # For mines not in the placeholder increments, let's extrapolate a bit
            # This is a naive extrapolation and should be replaced with actual game design data
            last_known = max(multiplier_increments.keys())
            step = (multiplier_increments[last_known][0] - 1) / last_known
            multipliers[mines] = [round(1 + step * mines, 2)]
    
    return multipliers

# Calculate the multipliers for the range of mines
mines_multipliers = calculate_multipliers(MAX_MINES, ROWS, COLS)

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_locations = set()
    while len(mine_locations) < mines:
        x, y = random.randint(0, cols-1), random.randint(0, rows-1)
        mine_locations.add((x, y))  # For simplicity, we don't check for duplicates here
    return board, mine_locations

def print_board(board, mines, show_mines=False):
    for y, row in enumerate(board):
        row_string = ''
        for x, cell in enumerate(row):
            if (x, y) in mines and show_mines:
                row_string += '[*]'
            elif cell == ' ':
                row_string += '[ ]'
            else:
                row_string += f'[{cell}]'
        print(row_string)
    print()

def get_move():
    try:
        row = int(input("Enter row number (1-5): ")) - 1
        col = int(input("Enter column number (1-5): ")) - 1
        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            print("That position is out of bounds. Try again.")
            return get_move()
        return row, col
    except ValueError:
        print("Invalid input, please enter numbers only.")
        return get_move()

def play_game(username):
    balance = transactions.get_balance(username)
    if balance < MIN_BET:
        print(f"You do not have enough balance to make the minimum bet of {MIN_BET}.")
        return False  # Go back to the main menu

    bet_amount = float(input(f"Enter your bet amount (minimum {MIN_BET}): "))
    if bet_amount < MIN_BET:
        print(f"The minimum bet amount is {MIN_BET}.")
        return True
    if bet_amount > balance:
        print("Insufficient funds for this bet.")
        return True

    num_mines = int(input(f"Enter the number of mines (1-{MAX_MINES}): "))
    if not 1 <= num_mines <= MAX_MINES:
        print(f"Please choose between 1 and {MAX_MINES} mines.")
        return True

    board, mines = initialize_board(ROWS, COLS, num_mines)
    multiplier = mines_multipliers[num_mines][0]  # Get the multiplier from the dictionary
    print(f"Setting {num_mines} mines. Multiplier for this game: x{multiplier}")

    revealed_spots = set()
    while True:
        print_board(board, mines)
        row, col = get_move()

        if (row, col) in revealed_spots:
            print("You've already picked this spot. Pick another one.")
            continue
        revealed_spots.add((row, col))

        if (row, col) in mines:
            print_board(board, mines, show_mines=True)
            print("Boom! You hit a mine!")
            transactions.update_balance(username, -bet_amount)
            return True  # Go back to the main menu
        else:
            board[row][col] = 'X'  # Update the board

        if len(revealed_spots) == ROWS * COLS - num_mines:
            print_board(board, mines, show_mines=True)
            print("Congratulations! You've cleared all the safe spots!")
            winnings = bet_amount * multiplier
            print(f"You win: {winnings}!")
            transactions.update_balance(username, winnings)
            return True  # Go back to the main menu

        # Cash out option
        if input("Press 'C' to cash out, or any other key to continue picking: ").upper() == 'C':
            print("Cashing out...")
            transactions.update_balance(username, bet_amount * multiplier)
            return True  # Go back to the main menu

# ... [Any additional functions or logic]
