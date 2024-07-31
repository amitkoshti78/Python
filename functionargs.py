
def add_num(name, *numbers):
    sum = 0
    print(numbers)
    for num in numbers:
        sum = sum + num
    
    return sum, name.upper()

result, upp_name = add_num('amit', 1,3,7,8,2,7,56,12,78,90,12,45 )
print(f' Hi {upp_name} the sum of numbers is : {result}')


def student(**kwargs):

    print(kwargs)
    for info in kwargs.items():
        print(info)

    

student(first_name="Amit", rnr = 101, yy = 2024, sem = 3)


def student_marks(*marks, **kwargs):

    print(kwargs)
    print(marks)
    for info in kwargs.items():
        print(info)

    
    
student_marks(60, 80, 90, first_name="Amit", rnr = 101, yy = 2024, sem = 3)


dict_phone = {
                'Amit'      : 2345678989 ,
                'Omkar'     : 3456789120 ,
                'Tanvi'     : 9856789123 ,
                'Anurag'    : 9145675681 ,
                'Neha'      : 7857789147 ,
                'Varad'     : 3418902382 , 
}
print(dict_phone)

for key , value in dict_phone.items():
    print(key, value)


dict_phone['Amit'] = 0
print(dict_phone)

print(dict_phone.popitem())
print(dict_phone)

print(dict_phone.get('Neha'))

dict_phone['Avinash'] = 3457812794
print(dict_phone)






    