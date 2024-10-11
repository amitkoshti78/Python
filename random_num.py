import random
# Randoum choice from a list
my_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
print(random.choice(my_list))

# for else construct and random number
answer = 'y'

while answer == 'y' or answer == 'Y':
    for i in range(1, 4, 1):
        # randint function inside random package generates random number within range. 
        # here we have given range between 0 to 50 including both numbers
        random_num = random.randint(0,50)
        print("Attempt" , i, ("." * i))
        guess_num = int(input("Enter a number to guess (0 to 50) : "))
        if random_num == guess_num:
            print("Your guess is correct!! You won")
            break
        
    # this else is part of for ...else construct in python. 
    # this else only get executed once for loop is over
    else:
        print("Attempts over!! Your guess is wrong!! You Lost. Winning number is", random_num )

    print("\n Do you want to play again y/n :", end=' ')
    answer = input()
    
  
        
    