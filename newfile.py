square_list = []

for element in range(1,21):
    square_list.append(element * element)

print(f'\nList of squares{square_list}')

square_list.clear()

print(f'\nEmpty List {square_list}')

square_list = [element * element for element in range(1,21)]

print(f'\nList of squares{square_list}')
      

matirx_list = []
for i in range(1,4):
    row_list = []
    for row in range(1,4):
        row_list.append(row * i)

    print(f'\n Row {i} : {row_list}')
    matirx_list.append(row_list)

print(f'\n Matrix List {matirx_list}')

matirx_list = [ [row * i for row in range(1,4)] for i in range(1,4)]
print(f'\n Matrix List {matirx_list}')

my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(f'\n Tuple {my_tuple}')

my_tuple1 = tuple(element * element for element in range(1,11))
print(f'\n Tuple {my_tuple1}')


from math import pi

print(pi)
circle_area_set = set()
range_from = 1
range_to = 8 
for r in range(range_from,range_to):
    circle_area_set.add((r ** 2) * pi)

print(f'\n Area of cirlcle {circle_area_set}')

circle_area_set = {(r ** 2) * pi for r in range(range_from,range_to) }
print(f'\n Area of cirlcle {circle_area_set}')

circle_area_set = set((r ** 2) * pi for r in range(range_from,range_to))
print(f'\n Area of cirlcle {circle_area_set}')


petrol_price = 103.44
range_from = 1
range_to = 31

amount_tobe_paid = {}
for litre in range(range_from, range_to):
    amount_tobe_paid[litre] = petrol_price * litre

print(f'\n Amount to be paid : {amount_tobe_paid}')

amount_tobe_paid = {litre : petrol_price * litre for litre in range(range_from, range_to ) }
print(f'\n Amount to be paid : {amount_tobe_paid}')


list_of_sets = [{1,2,3}, {2,1,8,4,6,7,0,3,9}, {"Amit", "Koshti"}, {'A', 'B', 'C'}]
print(f'\n List of sets : {list_of_sets}')

set1 = list_of_sets[2]
print(f'\n List of set1 : {set1}')

for element in list_of_sets[3]:
    print(f'\n Element of 4th set : {element}')

set2 = list_of_sets[1]
print(f'\n Set2 before pop: {set2}')
print(f'\npopped item : {set2.pop()}')
print(f'\n Set2 after pop : {set2}')

list_of_tuple = [(1,2,3), (1,4,6),(1,8,18)]
print(f'\n List of tuples : {list_of_tuple}')

list_of_student_info = {
        101 :   [  "Amit", "TY", {  "Math" : 78, 
                                    "ML"   : 89, 
                                    "AI"   : 72 }
                ]
    ,
     
        102 :   [  "Anurag", "FY", { "Math" : 98, 
                                     "ML"   : 90, 
                                     "AI"   : 84 }
                ]
    ,
        103 :   [  "Neha", "SY", {  "Math" : 87, 
                                    "ML"   : 93, 
                                    "AI"   : 80 }
                ]
    ,

        104 :   [  "Tanvi", "FY", {  "Math" : 84, 
                                     "ML"   : 94, 
                                     "AI"   : 90 }
                ]
    , 
     
     
        105 :   [  "Omkar", "SY", {  "Math" : 86, 
                                     "ML"   : 86, 
                                     "AI"   : 72 }
                ]
    , 

    
        106 :   [  "Varad", "TY", {  "Math" : 78, 
                                     "ML"   : 89, 
                                     "AI"   : 72 }
                ]
    } 




student_info_list = list_of_student_info[102]

print(student_info_list)

subject_dict = student_info_list[2]

print(subject_dict)

math_marks = subject_dict["Math"]

print(math_marks)

roll_no_list = []
student_list = []
for roll_no, values in list_of_student_info.items():
    roll_no_list.append(roll_no)
    student_list.append(values)

print(roll_no_list)
print(student_list)  

marks_list = []
for marks in student_list:
    marks_list.append(marks[2])

print(marks_list)

math_list = []
ml_list = []
ai_list = []
for sub_marks in marks_list:
    math_list.append(sub_marks['Math'])
    ml_list.append(sub_marks['ML'])
    ai_list.append(sub_marks['AI'])

print(math_list)
print(ml_list)
print(ai_list)


