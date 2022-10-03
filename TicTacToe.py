


# Tic Tac Toe game with 2 players

# Step 1 : Create the map and decide who goes first, player one or two


def show_board(Board):
    print(f"{Board['1,1']}|{Board['2,1']}|{Board['3,1']} \n"
          f"-----------\n"
          f"{Board['1,2']}|{Board['2,2']}|{Board['3,2']} \n"
          f"-----------\n"
          f"{Board['1,3']}|{Board['2,3']}|{Board['3,3']}")


# Step 2 : each player takes a turn filling in a spot
def X_Turn(Locations):
    valid_input = False
    while valid_input != True:
        try:
            X_COL = int(input('Player X, Which Column do you want to put your X in? \n'
                      'Input 1,2 or 3 \n'))
        except ValueError:
            print('invalid selection, try again.')

        try:
            X_ROW = int(input('Player X, Which Row do you want to put your X in? \n'
                      'Input 1,2 or 3 \n'))
        except ValueError:
            print('invalid selection, try again.')


        if X_COL >3 or X_ROW >3:
            print('invalid selection, try again.')
        else:
            X_COR = str(f'{X_COL},{X_ROW}')
            print(X_COR)


            if Locations[X_COR] != '   ':
                print('you have not made a valid selection')
            else:
                Locations[X_COR] = ' X '
                valid_input = True
    return Locations

def O_Turn(Locations):
    valid_input = False
    while valid_input != True:
        try:
            O_COL = int(input('Player O, Which Column do you want to put your O in? \n'
                      'Input 1,2 or 3 \n'))
        except ValueError:
            print('invalid selection, try again.')

        try:
            O_ROW = int(input('Player O, Which Row do you want to put your O in? \n'
                      'Input 1,2 or 3 \n'))
        except ValueError:
            print('invalid selection, try again.')


        if O_COL >3 or O_ROW >3:
            print('invalid selection, try again.')
        else:
            O_COR = str(f'{O_COL},{O_ROW}')


            if Locations[O_COR] != '   ':
                print('you have not made a valid selection')
            else:
                Locations[O_COR] = ' O '
                valid_input = True
    return Locations

def checkforwin(Locations):
    if Locations['1,1'] == Locations['1,2'] and Locations['1,1'] == Locations['1,3']:
        if Locations['1,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['2,1'] == Locations['2,2'] and Locations['2,1'] == Locations['2,3']:
        if Locations['2,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['3,1'] == Locations['3,2'] and Locations['3,1'] == Locations['3,3']:
        if Locations['3,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['1,1'] == Locations['2,1'] and Locations['1,1'] == Locations['3,1']:
        if Locations['1,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['1,2'] == Locations['2,2'] and Locations['1,2'] == Locations['3,2']:
        if Locations['1,2'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['1,3'] == Locations['2,3'] and Locations['1,3'] == Locations['3,3']:
        if Locations['1,2'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['1,1'] == Locations['2,2'] and Locations['1,1'] == Locations['3,3']:
        if Locations['1,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif Locations['3,1'] == Locations['2,2'] and Locations['3,1'] == Locations['1,3']:
        if Locations['3,1'] != '   ':
            print('There is a winner!')
            return False
        else :
            return True

    elif '   ' not in Locations.values():
        print('There is a stalemate!')
        return False
    else:
        return True


def gaming_time():
    Locations = {
        '1,1': '   ', '2,1': '   ', '3,1': '   ',
        '1,2': '   ', '2,2': '   ', '3,2': '   ',
        '1,3': '   ', '2,3': '   ', '3,3': '   '}
    show_board(Locations)
    game_on = True
    while game_on:
        Locations = X_Turn(Locations)
        show_board(Locations)
        game_on = checkforwin(Locations)
        if game_on != True:
            break
        Locations = O_Turn(Locations)
        show_board(Locations)
        game_on = checkforwin(Locations)
        if game_on != True:
            break

gaming_time()

ga = input('Would you like to play again? \n').upper()
if ga == 'Y':
    gaming_time()
