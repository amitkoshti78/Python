def return_marks(marks):
    return marks[1]

number_list = [ ["Amit",  50], ["Swapnil" , 75], ["Omkar" , 95], ["Anurag" , 80], ["Vinit" , 45], ["Pushkar" , 65]]

number_list.sort(key=return_marks)
print(number_list)
number_list.sort(key=return_marks, reverse=True)
print(number_list)
