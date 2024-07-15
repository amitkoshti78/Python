number = input("Enter number : ")

if number == number[::-1]:
   print(number, "is palindrome")
else:
   print(number, "is not palindrome")

if ((lambda x: x == x[::-1])(input("Enter number : "))):
   print("Number is palindrome")
else:
   print("Number is not palindrome") 