# This list is created to form the board

board = [

["-","-","-"],
["-","-","-"],
["-","-","-"]

]

def print_board():
    for row in board:
        for slot in row:
            print(f"{slot} ",end='')
        print()

# function to make a play
def play(x,y, player):
    x = int (x)
    y = int(y)
    board[x][y] = player
    return "success"
# function to check if space is occupied
def is_space_occupied(x, y):
    x = int (x)
    y = int(y)
    if board[x][y] != "-":
        return True
    return False

# This is to check if any player won the round

def check_win_player(player):
  # Checks if there is a winner along the horizontals
        for i in range(3):
            if player == board[i][0] and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return True
            # Checks if there is a winner along the verticals
            elif player == board[0][i] and board[0][i] == board[1][i] and board[1][i] == board[2][i]  :
                return True

        # Checks if there is a winner along the left diagonal
        if player == board[0][0] and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True

        # Checks if there is a winner along the right diagonal
        if player == board[0][2] and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True
        return False

# Function to check if there is no more moves to play i.e board is full,hence a tie
def no_more_play():
    total = 0
    for i in board:
        for j in i:
            if j != '-':
                total += 1
    if total < 9:
        return False
    else:
        return True, "It's a Tie!"

def switch_player(player):
    if player == "x":
        return "o"
    elif player == "o":
        return "x" 
        
player = "x"
while no_more_play() == False:
    print_board()

    print(f"Player {player}'s turn.")

    one = input("index one: ")
    two = input("index two: ")

    if is_space_occupied(one, two):
        player = switch_player(player)

    if not is_space_occupied(one, two):
        print(play(one, two, player))

    if check_win_player(player) == True:
        print_board()
        print (f"Player {player} wins!")
        break
   
    player = switch_player(player)

print (no_more_play()[1])





    

