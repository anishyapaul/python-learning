import random

roll=random.randint(1,6)

user_roll=input("Guess the Dice Roll \n")

if user_roll==roll:
    print("Correct!! They Rolled "+str(roll))
else:
     print("Incorrect!! They Rolled "+str(roll))