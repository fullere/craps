# Elizabeth Fuller
# 10/21/19
# game of craps
import random


def roll_dice():
    # creates dice roll number
    roll = random.randint(2, 12)
    return roll


def create():
    # starts fresh game and fills in bankroll amount
    bankroll = int(input("Enter bankroll amount:\n> $"))
    while bankroll <= 0:
        print("Invalid amount. Enter valid amount")
        bankroll = int(input("> $"))
    game_rules()
    play_game(bankroll)
    return bankroll


def game_rules():
    print("Do you wish to read the rules? y/n")
    rules = input("> ")
    rules = rules.strip()
    rules = rules.lower()
    if rules == 'y':
        print("""Rules:\n\tYou will roll 2 dice then take the sum.
    If you rolled a 7 or 11 then you win.
    Rolling a 2, 3, or 12 results in a loss.
    Anything else will become your point.
    You will continue rolling both dice until either
    you roll the same as your point
    or roll a 7.
    Matching your point means you win while a 7 is a loss""")
    else:
        print("Then let us continue.")


def play_game(bankroll):
    bankroll_total = bankroll
    win = 0
    print("Lets play Craps.")
    # inform player of bankroll amount and ask for bet
    # make sure bet is <= bankroll or != 0, no negative bets
    print(f"You have ${bankroll_total}.")
    bet = int(input("Place bet\n> $"))
    while bet > bankroll or bet <= 0:
        print("Invalid amount. Enter valid amount")
        bet = int(input("> $"))
    # roll dice and print roll outcome; and determine win, lose, or point
    print("Rolling dice...")
    roll = roll_dice()
    print(f"You rolled a {roll}.")
    # rolled 7 or 11? win.
    if roll == 7:
        print("You Win!")
        win = 1
    elif roll == 11:
        print("You Win!")
        win = 1
    # rolled 2, 3, or 12? lose.
    elif roll == 2:
        print("You Lose!")
    elif roll == 3:
        print("You Lose!")
    elif roll == 12:
        print("You Lose!")
    # not a win or lose? create player point and continue.
    else:
        point = roll
        roll2 = 0

        print(f"Your point is {point}.") # inform player of their point
        # rolling to match point for a win or till a 7 for a loss
        check = 0
        while check == 0:
            roll2 = roll_dice()
            print(f"Rolling again...\nYou rolled a {roll2}.")
            if roll2 == point:
                check = 1
            elif roll2 == 7:
                check = 1
        if roll2 == point:
            print("You Win!")
            win = 1
        else:
            print("Craps! You Lose!")
    # if win add bet to bankroll, if lose subtract bet from bankroll
    if win == 1:
        bankroll_total = bankroll_total + bet
        print(f"Congrats your bankroll is now ${bankroll_total}.")
    else:
        bankroll_total = bankroll_total - bet
        print(f"Your bankroll is now ${bankroll_total}.")
    # check to see if player can still play/bet
    # if no ask if they want to start over with new bankroll or quit
    if bankroll_total == 0:
        print("You cannot continue due to insufficient bankroll.")
        print("Would you like to play again with a new bank roll? y/n")
        choice = input("> ")
        choice = choice.lower()
        choice = choice.strip()
        if choice == 'y':
            create()
        else:
            print("Thanks for playing!")
            print("""
            
            -------
            """)
            input("To start new game hit ENTER")
            create()
    # if yes ask if they want to keep playing or quit
    else:
        print("Play [1]\nQuit [2]")
        selection = int(input("> "))
        if selection == 1:
            print("Continuing")
            play_game(bankroll_total)
        elif selection == 2:
            print("Thanks for playing!")
            input("To start new game hit ENTER")
            create()


create()
