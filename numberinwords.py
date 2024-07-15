number = int(input("Enter Number :"))

number_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
decade_list = ["TEN", "TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY",  "NINETY" ]
decade_list_num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
century_list = ["HUNDRED", "THOUSAND", "LAKH", "CRORE"]
century_list_num = [100, 1000, 10000,  ]

remainder   = 0
sav_number  = number
word_list   = []
temp_number = 0
zero_count = 0
divisor = 1000


while number > 0 :
    remainder = number % 10
    number    = number // 10
    
    
    if remainder == 0:
        zero_count = zero_count + 1
        word = 
        
    print(f'Remainder : {remainder} and number of zeros : {zero_count} and number : {number}')

    if remainder != 0:
        temp_number = remainder
        for i in range(zero_count):
            temp_number = temp_number * 10
            print(f'temp number : {temp_number}')
        
    if zero_count >= 7:       #crore

    
    elif zero_count >= 6:     # 10 lakhs
    
    elif zero_count >= 5:     # 1 lakh

    elif zero_count >= 4:     # 10 thousand
    
    elif zero_count >= 3:    # 1 thousand

    elif zero_count >= 2:    # 1 hundred

    elif zero_count >= 1:    # ten
        word_list.append(number_list[remainder - 1] + decade_list[remainder - 1 ])
    else:
        word_list.append(number_list[remainder - 1])


    zero_count = 0    
        
    
        word_list.append(temp_number)

    print(temp_number)

print(word_list)

for number in word_list:
    if number   >= 1000:
        
    elif number >= 900:
    
    elif number >= 800:
    
    elif number >= 700:
    
    elif number >= 600:

    elif number >= 500:
    
    elif number >= 400:

    elif number >= 300:
    
    elif number >= 200:
    
    elif number >= 100:
    
    elif number 

