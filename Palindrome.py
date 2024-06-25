str_number = input("Enter number : ")
str_len = len(str_number)
print("Lenght of number : ", str_len , "\n")

number = int(str_number)
sav_num = number 
reverse = 0

for i in range(0,str_len):
    remainder = number % 10
    print("Remainder :" , number , "% 10 =", remainder )
    print("Reverse = (", reverse , " * 10 ) + ", remainder )
    reverse = (reverse * 10) + remainder
    print("Reverse : ", reverse)
    print(number, "/ 10")  
    number = number // 10
    print("Divison : " , number)

if sav_num == reverse:
    print("Number", sav_num  , "and Reverse", reverse,  "is palindrome")
else:
    print("Number", sav_num  , "and Reverse", reverse, "is not palindrome")