import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again == "Y" or roll_again == "y" or roll_again == "Yes" or roll_again == "YES" :
    print("\nRolling the dice !")
    time.sleep(2)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("The values are:")
    print("Dice1=", dice1)
    print("Dice2=", dice2)

    if dice1 == dice2 :
        print("You rolled a doubled !")
    else:
        print("Keep trying !")
    roll_again = input("\nRoll the dice again? (Y/N)")


