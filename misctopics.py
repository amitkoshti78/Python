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



# functuion parameters and scope of variables, enumerate, tuples

#fizz buzz 
# if input is divisible by 3 then print fizz
# if input is divisible by 5 then print buzz
# if input is divisible by 3 and 5 then print fizzbuzz
# if input is not divisible by 3 and 5 then print blabla           