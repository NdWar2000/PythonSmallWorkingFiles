#Fruit Machine:
    #Write a program to simulate a Fruit Machine that displays three symbols
    #at random from Cherry, Bell, Lemon, Orange, Star, Skull.
    #The player starts with £1 credit, with each go costing 20p.
    #If the Fruit Machine “rolls” two of the same symbol, the user wins 50p.
    #The player wins £1 for three of the same and £5 for 3
    #Bells. The player loses £1 if two skulls are rolled and all of his/her money
    #if three skulls are rolled. The player can choose to quit with the winnings
    #after each roll or keep playing until there is no money left.

#display 3 symbols from list
import random

def display_cred(credit):
    print("\nCredit: £" + format(credit, ".2f"))
    return capture_input("Would you like to play again for £0.20?")

def capture_input(output_string = ""):
    captured = ""
    while captured == "":
        print("\n" + output_string)
        try:
            captured = input("(Y)es or (N)o? ").lower().strip()
            if captured == "y":
                return True
            elif captured == "n":
                return False
            else:
                raise Exception
        except:
            print("Error: Please enter a Y/N.\n")
            captured = ""

def play(credit):
    #Rolling reels
    symbols = ["Cherry", " Bell ", "Lemon ", "Orange", " Star ", "Skull "]
    reels = []

    print("\nReels rolling!\n\n| ", end = "")

    for i in range(3):
        #test
        #reels.append("Skull")
        reels.append(random.choice(symbols))
        print(reels[i], end = " | ")

    print()
    print()

    if reels[0] == reels[1] and reels[0] == reels[2]:
        #3 reels
        if reels[0] == "Bell":
            #big payout £5
            print("Three Bells! £5 won!")
            return 5
        elif reels[0] == "Skull":
            #dead!
            print("Three Skulls! You lose!")
            return credit * -1
        else:
            #little payout £1
            print("Three symbols! £1 won!")
            return 1
    elif reels[0] == reels [1] or \
    reels[1] == reels[2] or \
    reels[2] == reels[0]:
        if reels[0] == "Skull":
            #injury -£1
            print("Two Skulls! £1 lost!")
            return -1
        else:
            #tiny payout £.5
            print("Two symbols! £0.50 won!")
            return .5
    else:
        print("Sorry, no win here...")

    print("")
    print("")
    return 0

def cash_out(credit):
    print("You cashed out. \nCongratulations on walking out with £" + format(credit, ".2f"))
def ran_out():
    print("Sorry you've ran out of money. \nPlease restart to try again.")

def main():
    credit = 1
    keep_playing = True
    while keep_playing and credit >= .2:
        keep_playing = display_cred(credit)
        if keep_playing:
            credit -= .2
            credit += play(credit)

    if not keep_playing:
        cash_out(credit)
    else:
        ran_out()

main()
