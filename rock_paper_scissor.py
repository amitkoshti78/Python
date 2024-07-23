''' game
Rock beats scissors, paper beats rock and scissors beat paper.'''
  
#  rock = 0
#  paper = 1
#  scissors = 2

# user   computer  result
#  0      0        draw  
#  1      1        draw    
#  2      2        draw             

#  0      2        user wins   Rock beats scissors

#  1      0        user wins  paper beats rock
#  2      1        user wins   scissors beat paper

#  2      0        computer wins Rock beats scissors

#  0      1        computer wins paper beats rock
#  1      2        computer wins scissors beat paper 

import random


rock = '''
   ______  
---'   ___)
      (____)
rock  (____)
      (___)
---.__(__)
'''

paper = '''
    ________
---'   _____)____
          _______)
paper     ________)
         ________)
---.___________)
'''

scissors = '''
    _______
---'   ____)_____
          _______)__
 scissor____________)
      (_____)
---.__(____)
'''

game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("Your choice!! Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
    print("\n ### You chose ###")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(" ### Computer chose ###")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
    elif user_choice == 0 and computer_choice == 2:
        print("You win!! Computer lost Rock beats scissors")
    elif computer_choice == 0 and user_choice == 2:
        print("You lost Computer wins!! Rock beats scissors")
    elif computer_choice > user_choice:
        print("You lost!! Computer wins paper beats rock or scissors beat paper")
    elif user_choice > computer_choice:
        print("You win!! Computer lost paper beats rock or scissors beat paper")
    elif computer_choice == user_choice:
        print("It's a draw!! Same Choice")
    
    print("\n Do you want to play again y/n :", end=' ')
     
    if input().lower() == 'n':
        break


