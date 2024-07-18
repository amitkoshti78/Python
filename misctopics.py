import random

#to multiply string number of times
for i in range(1,6):
    print(i, (i * "#"))

# Randoum choice from a list
my_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
print(random.choice(my_list))

# for else construct and random number
for i in range(1, 4, 1):
    random_num = random.randint(0,50)
    print("Attempt" , i, ("." * i))
    guess_num = int(input("Enter a number to guess (0 to 50) : "))
    if random_num == guess_num:
        print("Your guess is correct!! You won")
        break
else:
    print("Attempts over!! Your guess is wrong!! You Lost. Winning number is", random_num )


# nested loops
for x in range(0,5):
    for y in range(0,5):
        print(f"({x}, {y})")


letter_list = ["A", "B", "C", "D"]
number_list = [1, 2, 3, 4]
repeat_list = [0] * 5



final_list = letter_list + number_list + repeat_list
print(final_list)
print("Count : " , final_list.count(0))

final_list = [letter_list, number_list, repeat_list]
print(final_list)

range_list = list(range(0,50,3))
print(range_list)

char_list = list("Python Programming")
print(char_list)

topper_list = ["Anurag", "Omakr", "Sakshi", "Tanvi", "Avinash", "Viraj"]
first, second, *other = topper_list
print("First : " , first)
print("Second : ", second)
print("Other : ", other)

first, *other, last = topper_list
print("First : " , first)
print("Last : ", last)
print("Other : ", other)

for index, name in enumerate(topper_list):
    print(index, name)

topper_list.append("Amit")
topper_list.insert(2, "Akshara")
topper_list.remove("Viraj")
print(topper_list)
topper_list1 = topper_list.copy()

print("Index for Tanvi" , topper_list.index("Tanvi"))

topper_list.extend("Hitesh")
print(topper_list)

topper_list.clear()
print(topper_list)
print(topper_list1)




# Program to illustrate if else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


# game
  
# Rock beats scissors, scissors beat paper, and paper beats rock
  
#  rock = 0
#  scissors = 1
#  paper = 2

# user   computer
#  0      0                        
#  0      1  
#  0      2           
#  1      0
#  1      1 

#  2      0       
  

         

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")



# functuion parameters and scope of variables, enumerate, tuples, boolean operations, __main__ , isdigit, not operator, 

#fizz buzz 
# if input is divisible by 3 then print fizz
# if input is divisible by 5 then print buzz
# if input is divisible by 3 and 5 then print fizzbuzz
# if input is not divisible by 3 and 5 then print blabla           