#Import modules
import random
# Describtion functions
def instruction():
    """Shows greeting and rules"""
    print("""\t\tWelcome to the ring of the greatest intellectual competition of all time!!!
Your brain and my processor will get in a fight at the game board \"Tic-tac-toe\"!
\t\tTo make a move, enter the number in range from 0 to 8. 
The numbers uniquely correspond to the fields of the board - as shown below:
\t\t\t\t\t\t\t\t0 | 1 | 2
\t\t\t\t\t\t\t\t---------
\t\t\t\t\t\t\t\t3 | 4 | 5
\t\t\t\t\t\t\t\t---------
\t\t\t\t\t\t\t\t6 | 7 | 8
Get ready to the fight, Pathetic squirrel man! The decisive battle will begin!!! """)

def playing_field(fields = [" ",] * 9):
    """Display the gaming field"""
    print("Gaming field:")
    print("\t\t\t\t\t\t\t\t",fields[0]," | ", fields[1] ," | ", fields[2],sep = '')
    print("\t\t\t\t\t\t\t\t---------")
    print("\t\t\t\t\t\t\t\t",fields[3]," | ", fields[4] ," | ", fields[5],sep = '')
    print("\t\t\t\t\t\t\t\t---------")
    print("\t\t\t\t\t\t\t\t",fields[6]," | ", fields[7] ," | ", fields[8],sep = '')

def first_move():
    """Define 'Who get the first move?''"""
    choice = None
    while choice != "1" and choice != "2":
        print("""Whose move the first?
I can give way to such a loser, ha!
\t\t1 - My move is the FIRST
\t\t2 - I'll give in to a miserable robot""")
        choice = input("Enter your choice: ")
        if choice == "1":
            user_move = 1
        elif choice == "2":
            user_move = 2
        else:
            print("\nYou entered something wrong:(/.\nTry again...\n")
            continue
    return user_move

def who_0_who_x(user_move):
    """define who play for 0, and who play for X"""
    if user_move == 1:
        player_token = "0"
        computer_token = "X"
    else:
        player_token = "X"
        computer_token = "0"
    return player_token,computer_token

def players_move(fields,player_token):
    """Start the player's move"""
    move_over = False
    while not move_over:
        print("\nNow it's the player's turn.")
        number_of_field = int(input("Enter the number of field: "))
        if fields[number_of_field] == " ":
            fields[number_of_field] = player_token
            move_over = True
        else:
            print("\nThis field is taken:/ Try again.\n")

def pc_move(fields,pc_token):
    """Start the player's move"""
    move_over = False
    print("\nNow it's the pc's turn.")
    while not move_over:
        number_of_field = random.randrange(9)
        if fields[number_of_field] == " ":
            fields[number_of_field] = pc_token
            move_over = True
        else:
            continue

def checking_player_win(fields,player_token):
    """Checking the player's winnings"""
    if (fields[0], fields[1], fields[2]) == (player_token,)*3:
        player_win = True
    elif (fields[3], fields[4], fields[5]) == (player_token,)*3:
        player_win = True
    elif (fields[6], fields[7], fields[8]) == (player_token,)*3:
        player_win = True
    elif (fields[0], fields[3], fields[6]) == (player_token,)*3:
        player_win = True
    elif (fields[0], fields[3], fields[6]) == (player_token,)*3:
        player_win = True
    elif (fields[1], fields[4], fields[7]) == (player_token,)*3:
        player_win = True
    elif (fields[2], fields[5], fields[8]) == (player_token,)*3:
        player_win = True
    elif (fields[0], fields[4], fields[8]) == (player_token,)*3:
        player_win = True
    elif (fields[2], fields[4], fields[6]) == (player_token,)*3:
        player_win = True
    else:
        player_win = False
    return player_win

def checking_pc_win(fields, pc_token):
    """Checking the pс's winnings"""
    if (fields[0], fields[1], fields[2]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[3], fields[4], fields[5]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[6], fields[7], fields[8]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[0], fields[3], fields[6]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[0], fields[3], fields[6]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[1], fields[4], fields[7]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[2], fields[5], fields[8]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[0], fields[4], fields[8]) == (pc_token,) * 3:
        pc_win = True
    elif (fields[2], fields[4], fields[6]) == (pc_token,) * 3:
        pc_win = True
    else:
        pc_win = False
    return pc_win
def end_game(pc_win, player_win):
    """End of the game. Praises the winner."""
    if pc_win:
        print(" You are lose, loser! My processor is winner.\n Get out of here, don't be embarrassed")
    elif player_win:
        print("You just got lucky. I can not believe. The next fight is inevitable!!!")
def tic_tac_toe():
    """Main code the tic-tac-toe"""
    # Create variable
    pc_win = False
    player_win = False
    fields = [" ",] * 9

    # Main
    instruction()
    user_move = first_move()
    player_token, pc_token = who_0_who_x(user_move)
    if user_move == 1:
        playing_field(fields)
        while pc_win == False or player_win == False:
            try:
                players_move(fields, player_token)
                player_win = checking_pc_win(fields, player_token)
                if player_win == True:
                    break
                playing_field(fields)
            except IndexError:
                print("\nThere is no such field.Try again:)\n")
                playing_field(fields)
                continue
            pc_move(fields, pc_token)
            pc_win = checking_pc_win(fields, player_token)
            if player_win == True:
                break
            playing_field(fields)
    else:
        while pc_win == False or player_win == False:
            pc_move(fields, pc_token)
            pc_win = checking_pc_win(fields, player_token)
            if pc_win == True:
                break
            lp = None
            while lp == None:
                try:
                    playing_field(fields)
                    players_move(fields, player_token)
                    player_win = checking_pc_win(fields, player_token)
                    if player_win == True:
                        break
                    playing_field(fields)
                    lp = 1
                except IndexError:
                    print("\nThere is no such field.Try again:)\n")
                    continue
    playing_field(fields)
    end_game(pc_win,player_win)
#Game tic-tac-toe
tic_tac_toe()
input("Click 'Enter' to exit")