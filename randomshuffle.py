import random

number_list = [2, 66, 91, 27, 12, 1, 0, 98]
number_list = sorted(number_list)
print(number_list)
random.shuffle(number_list)
print(number_list)
print(random.choice(number_list))
print(random.choice(number_list))
print(random.choice(number_list))
number_list.remove(91)
print(number_list)