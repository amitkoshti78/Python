list_of_article_info = {
# Article No   Name       color            size and its price
    1001 :  [ "Shirt",   "Red",   { "S" : 1250, "M" : 1400, "L" : 1500 } ],
    1002 :  [ "Shirt",   "Blue",  { "S" : 1350, "M" : 1450, "L" : 1550 } ],
    2001 :  [ "Jeans",   "Blue",  { "S" : 1600, "M" : 1700, "L" : 1800 } ],
    2002 :  [ "Jeans",   "Black", { "S" : 1500, "M" : 1600, "L" : 1700 } ],
    3001 :  [ "T-Shirt", "Black", { "S" :  650, "M" :  750, "L" :  850 } ],
    3002 :  [ "T-Shirt", "Gray",  { "S" : 2150, "M" : 3150, "L" : 4150 } ],
    4001 :  [ "Shoes",   "White", { "S" : 4500, "M" : 5500, "L" : 6500 } ], 
    4002 :  [ "Shoes",   "Black", { "S" : 6750, "M" : 7750, "L" : 8750 } ], 
    5001 :  [ "Cap",     "White", { "S" :  275, "M" :  375, "L" :  475 } ],
    5002 :  [ "Cap",     "Blue",  { "S" :  275, "M" :  375, "L" :  475 } ]
    } 

customer_list = {
# Cust No        Name       Address          email id     
    "C001" :  [  "Amit",    "Pune",         "amit@gmail.com"   ],
    "C002" :  [  "Omkar",   "Chinchwad",    "omkar@gmail.com"  ],
    "C003" :  [  "Neha",    "Baner",        "neha@gmail.com"   ],
    "C004" :  [  "Varad",   "Akurdi",       "varad@gmail.com"  ],
    "C005" :  [  "Anurag",  "Nigadi",       "anurag@gmail.com" ]
}  

shopping_list = {
# Cust No        Shoping list with Article no and size
    "C001"  : [ (1001, "M"), (2002, "S"), (5001, "L"), (4002, "M")], 
    "C002"  : [ (3001, "M"), (5002, "S"), (1001, "L")],
    "C003"  : [ (5001, "M"), (2001, "S"), (5002, "S"), (3002, "M"),(4001, "S") ],
    "C004"  : [ (1002, "L"), (4002, "S"), (3002, "L")],
    "C005"  : [ (1001, "M"), (1001, "S"), (2001, "S"), (2002, "S")]       
}   

# output expected for each customer from shopping list. So you need print
# below information for each customer. 
'''
-------------------------------------------------------------------
                     Customer Bill
Customer Number : C0001         Customer Address : Pune
Customer Name   : Amit          Customer email   : amit@gmail.com
-------------------------------------------------------------------
SNo  Article_Nr  Article_Name   Color    Size      Price   
-------------------------------------------------------------------
1      1001       Shirt         Red       M         1400
2      2002       Jeans         Black     S         1500
3      5001       Cap           White     L          475
4      4002       Shoes         Black     M         7750
-------------------------------------------------------------------
                                    Total Rs. :     11125 
'''

# Function to print bill for a customer
def print_customer_bill(customer_id):
    customer_info = customer_list[customer_id]
    shopping_items = shopping_list[customer_id]
    
    print("-------------------------------------------------------------------")
    print("                     Customer Bill")
    print(f"Customer Number : {customer_id}         Customer Address : {customer_info[1]}")
    print(f"Customer Name   : {customer_info[0]}          Customer email   : {customer_info[2]}")
    print("-------------------------------------------------------------------")
    print("SNo  Article_Nr  Article_Name   Color    Size      Price")
    print("-------------------------------------------------------------------")
    
    total_price = 0
    for index, (article_id, size) in enumerate(shopping_items):
        article_info = list_of_article_info[article_id]
        article_name = article_info[0]
        color = article_info[1]
        price = article_info[2][size]
        total_price += price
        
        print(f"{index + 1}      {format(article_id)}        {article_name}       {color}       {size}      {price}")
    
    print("-------------------------------------------------------------------")
    print(f"                                     Total Rs. :     {total_price}")

# Print bill for each customer
for customer_id in shopping_list.keys():
    print_customer_bill(customer_id)
    print("\n")