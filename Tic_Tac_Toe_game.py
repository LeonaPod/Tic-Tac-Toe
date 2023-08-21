import os

field_on_the_board = [0,1,2,3,4,5,6,7,8,9]

def Game_status():

    """
    A function that checks if the game has ended.
    The function returns 1 (one) if the game is over and oneplayer has won.
    The function returns 0 (zero) if the game is over and there is a tie. Nobody won.
    The function returns -1 (minus one) if the game is still in progress,
    there are free spaces on the board where a player can place his marker.
    """
    if field_on_the_board[1] == field_on_the_board[2] and field_on_the_board[2] == field_on_the_board[3]:
        return 1
    elif field_on_the_board[4] == field_on_the_board[5] and field_on_the_board[5] == field_on_the_board[6]:
        return 1
    elif field_on_the_board[7] == field_on_the_board[8] and field_on_the_board[8] == field_on_the_board[9]:
        return 1
    elif field_on_the_board[1] == field_on_the_board[4] and field_on_the_board[4] == field_on_the_board[7]:
        return 1
    elif field_on_the_board[2] == field_on_the_board[5] and field_on_the_board[5] == field_on_the_board[8]:
        return 1
    elif field_on_the_board[3] == field_on_the_board[6] and field_on_the_board[6] == field_on_the_board[9]:
        return 1
    elif field_on_the_board[1] == field_on_the_board[5] and field_on_the_board[5] == field_on_the_board[9]:
        return 1
    elif field_on_the_board[3] == field_on_the_board[5] and field_on_the_board[5] == field_on_the_board[7]:
        return 1
    
    # If there are NO more free fields and no one has won, it means the game is over and it's a tie.
    elif (field_on_the_board[1] != 1 and
          field_on_the_board[2] != 2 and
          field_on_the_board[3] != 3 and
          field_on_the_board[4] != 4 and
          field_on_the_board[5] != 5 and
          field_on_the_board[6] != 6 and
          field_on_the_board[7] != 7 and
          field_on_the_board[8] != 8 and
          field_on_the_board[9] != 9):
        return 0
    
    # If none of the above conditions are met, it means that no one won,
    # and thete are free fields, so the game is still CONTINUING.
    else:
        return -1
    
def Draw_the_board():

    """
    A function that draws a board. later we will use it to draw the board, 
    but with graphic elements.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n\n\t LeonaPod')
    print('\n\t Tis Tac Toe \n\n')

    print('Player 1 (X)  -  Player 2 (O)' )
    print()

    print('\t     |     |     ')
    print('\t ' ,field_on_the_board[1] , ' | ' ,field_on_the_board[2] ,' | ' ,field_on_the_board[3] )

    print('\t_____|_____|_____')
    print('\t     |     |     ')

    print('\t ' ,field_on_the_board[4] ,' | ' ,field_on_the_board[5] ,' | ' ,field_on_the_board[6] )

    print('\t_____|_____|_____')
    print('\t     |     |     ')

    print('\t ' ,field_on_the_board[7] ,' | ' ,field_on_the_board[8] ,' | ' ,field_on_the_board[9] )

    print('\t     |     |     ' )

player = 1
game_status = -1

while game_status == -1:
    Draw_the_board()

    if player % 2 == 1:
        player = 1
    else:
        player = 2

    print('\n\n Player', player)
    selected_field = int(input('Enter the field number on the board: '))

    # Let's assign a tag to the active payer.
    if player == 1:
        player_tag = 'X'
    else:
        player_tag = 'O'

    # Player's move.
    if selected_field == 1 and field_on_the_board[1] == 1:
        field_on_the_board[1] = player_tag
    elif selected_field == 2 and field_on_the_board[2] == 2:
        field_on_the_board[2] = player_tag
    elif selected_field == 3 and field_on_the_board[3] == 3:
        field_on_the_board[3] = player_tag
    elif selected_field == 4 and field_on_the_board[4] == 4:
        field_on_the_board[4] = player_tag
    elif selected_field == 5 and field_on_the_board[5] == 5:
        field_on_the_board[5] = player_tag
    elif selected_field == 6 and field_on_the_board[6] == 6:
        field_on_the_board[6] = player_tag
    elif selected_field == 7 and field_on_the_board[7] == 7:
        field_on_the_board[7] = player_tag
    elif selected_field == 8 and field_on_the_board[8] == 8:
        field_on_the_board[8] = player_tag
    elif selected_field == 9 and field_on_the_board[9] == 9:
        field_on_the_board[9] = player_tag
    else:
        print('WRONG MOVE!')
        pause_the_game = input('To continue the game, press the <ENTER> key...')
        player -= 1

    # Game check.
    game_status = Game_status()
    player += 1

# END of the game -> display the result and end the program.
Draw_the_board()
print('\n\n THE RESULT')
if game_status == 1:
    print('Player',player-1,'has won! \n\n')
else:
    print("It's a tie. \n\n")


