def fun_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
number_list = [i for i in range(1,51)]    
even_list = list(filter(fun_even, number_list))
print("\n", even_list)

even_list = list(map(fun_even, number_list))
print("\n", even_list)

even_list = list(filter(lambda x : x % 3 == 0, number_list))
print("\n", even_list)

text = "Python is very powerfull language"
word_list = [word for word in text.split() if 'o' in word]
print("\n", word_list)








