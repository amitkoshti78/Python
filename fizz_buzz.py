#fizz buzz 
# if input is divisible by 3 then print fizz
# if input is divisible by 5 then print buzz
# if input is divisible by 3 and 5 then print fizzbuzz
# if input is not divisible by 3 and 5 then print blabla           

answer = int(input("Enter a number : "))

if (answer % 3 == 0) and (answer % 5 == 0) :
    print("FizzBuzz")
elif (answer % 3 == 0):
    print("Fizz")
elif (answer % 5 == 0):
    print("Buzz")
else:
    print("Blabla")   
 