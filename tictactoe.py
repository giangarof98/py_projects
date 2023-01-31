# create the variable
# loop the variable in a range from 0 to 9 with an empty string
board = [" " for x in range(9)]

# format the board into a string
def create_board():
    row1 = "{} | {} | {}".format(board[0], board[1], board[2])
    row2 = "{} | {} | {}".format(board[3], board[4], board[5])
    row3 = "{} | {} | {}".format(board[6], board[7], board[8])

    print(row1)
    print(row2)
    print(row3)

# player movement
def move_player(icon):
    # assign a number to each player
    if icon == 'x':
        number = 1
    elif icon == 'o':
        number = 2
    # based on the selection, the choice will be formatted 
    print("your turn player {}".format(number))
    choice = int(input('enter yout move (1-9)').strip())

    # if the space is taken or not
    # i set the 'choice - 1' to set the range between 0 - 8, and not till 9
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print('that space is taken!')

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    create_board()
    move_player('x')
    if is_victory('x'):
        print('X wins! congrats!')
    elif is_draw():
        print('draw...')
        break
    move_player('o')
    if is_victory('o'):
        print('O wins! congrats!')
    elif is_draw():
        print('draw...')
        break
