# Define game board as a list
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
  for i in range(3):
    print('|' + '|'.join(board[i*3:(i*3)+3]) + '|')

# Function to check if a player has won
def check_win(player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

# Function to check if the board is full
def is_board_full():
  return all(x != ' ' for x in board)

# Function for player turn
def player_turn(player):
  while True:
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if 0 <= move <= 8 and board[move] == ' ':
      board[move] = player
      break
    else:
      print("Invalid move. Try again.")

# Main game loop
game_on = True
current_player = 'X'

while game_on:
  print_board()
  player_turn(current_player)

  # Check for win
  if check_win(current_player):
    print_board()
    print(f"Player {current_player} wins!")
    game_on = False
  
  # Check for tie
  elif is_board_full():
    print_board()
    print("It's a tie!")
    game_on = False

  # Switch turns
  current_player = 'O' if current_player == 'X' else 'X'
