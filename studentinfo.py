list_of_student_info = {
        101 :   [  "Amit", "FY", {  "Math" : 78, 
                                    "ML"   : 89, 
                                    "AI"   : 72 }
                ]
    ,
     
        102 :   [  "Anurag", "FY", { "Math" : 98, 
                                     "ML"   : 90, 
                                     "AI"   : 84 }
                ]
    ,
        103 :   [  "Neha", "FY", {  "Math" : 87, 
                                    "ML"   : 93, 
                                    "AI"   : 80 }
                ]
    ,

        104 :   [  "Tanvi", "FY", {  "Math" : 84, 
                                     "ML"   : 94, 
                                     "AI"   : 90 }
                ]
    , 
     
     
        105 :   [  "Omkar", "FY", {  "Math" : 86, 
                                     "ML"   : 86, 
                                     "AI"   : 72 }
                ]
    , 

    
        106 :   [  "Varad", "FY", {  "Math" : 78, 
                                     "ML"   : 89, 
                                     "AI"   : 72 }
                ]
    } 




student_info_list = list_of_student_info[102]

print(f'\n Student with roll no 102 :', end = ' ')
print(student_info_list)


subject_dict = student_info_list[2]

print(f'\n Student marks with roll no 102 : ', end = ' ')
print(subject_dict)


math_marks = subject_dict["Math"]

print(f'\n Student marks in Maths roll no 102 :', end = ' ')
print(math_marks)


roll_no_list = []
student_list = []
for roll_no, values in list_of_student_info.items():
    roll_no_list.append(roll_no)
    student_list.append(values)

print(f'\n Student roll no list :', end = ' ')
print(roll_no_list)

print(f'\n Student info no list :')
print(student_list)  


marks_list = []
for marks in student_list:
    marks_list.append(marks[2])

print(f'\n Student marks list :')
print(marks_list)

math_list = []
ml_list = []
ai_list = []
for sub_marks in marks_list:
    math_list.append(sub_marks['Math'])
    ml_list.append(sub_marks['ML'])
    ai_list.append(sub_marks['AI'])

print(f'\n Student maths marks list :', end = ' ')
print(math_list)
print(f'\n Student ML marks list :', end = ' ')
print(ml_list)
print(f'\n Student AI marks list :', end = ' ')
print(ai_list)


