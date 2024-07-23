

#to multiply string number of times
for i in range(1,6):
    print(i, (i * "#"))

print("\n")
# nested loops
for x in range(0,3):
    for y in range(0,3):
        print(f"({x}, {y})")

print("\n")
letter_list = ["A", "B", "C", "D"]
number_list = [1, 2, 3, 4]
repeat_list = [0] * 5

final_list = letter_list + number_list + repeat_list
print(final_list)
print("\nCount : " , final_list.count(0))

final_list = [letter_list, number_list, repeat_list]
print("\n")
print(final_list)

range_list = list(range(0,50,3))
print(range_list)

print("\n")
char_list = list("Python Programming")
print(char_list)

print("\n")
topper_list = ["Anurag", "Omakr", "Sakshi", "Tanvi", "Avinash", "Viraj"]
first, second, *other = topper_list
print("First : " , first)
print("Second : ", second)
print("Other : ", other)

print("\n")
first, *other, last = topper_list
print("First : " , first)
print("Last : ", last)
print("Other : ", other)

print("\n")
for index, name in enumerate(topper_list):
    print(index, name)

print("\n")
topper_list.append("Amit")
topper_list.insert(2, "Akshara")
topper_list.remove("Viraj")
print(topper_list)
topper_list1 = topper_list.copy()

print("\n")
print("Index for Tanvi" , topper_list.index("Tanvi"))

print("\n")
topper_list.extend("Hitesh")
print(topper_list)

print("\n")
topper_list.clear()
print(topper_list)
print(topper_list1)


# functuion parameters and scope of variables, enumerate, tuples, 
# boolean operations, __main__ , isdigit, not operator, lambda, regular expressions, sys.argv

print("\n")
number_list = [1, 4, 2, 3, 4, 5, 3, 4, 1]
print("Number occurs " , number_list.count(4), "times")
unique_list = []

for number in number_list:
    if number not in unique_list:
      unique_list.append(number)

print(unique_list)


# tuple are immutable means so we can not add or remove or modify items in the tuple

print("\n")
number_tuple = (3, 6, 7, 8, 9, 1, 5)
print(number_tuple)