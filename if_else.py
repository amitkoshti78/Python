# Program to illustrate if else statements
# following program will print $ to be paid depending upon various options
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# first 'if' statement
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  
  # if elif else statment inside first 'if' statement
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
  if wants_photo.upper() == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
  
# this else statement is for first 'if' mentioned above
else:
  print("Sorry, you have to grow taller before you can ride.")
