import random
computer_choice=random.choice(['Rock','Paper','Scissors'])
user_choice=input("Do you want Rock,Paper or Scissors?\n")
print("Computer Choice is "+computer_choice)
if user_choice == computer_choice:
    print("TIE")
elif user_choice=='Rock' and computer_choice=='Scissors':
    print("You WIN")
elif user_choice=='Paper' and computer_choice=='Rock':
    print('You WIN')
elif user_choice=='Scissors' and computer_choice=='Paper':
    print('You WIN')
else:

    print('You lose!!  Computer Wins ')