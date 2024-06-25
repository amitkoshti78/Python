import calendar

birthdate = input("\n Enter your birth date dd/mm/yyyy foramt: ")
#                                           0123456789
birth_day   = int(birthdate[0:2])
birth_month = int(birthdate[3:5])
birth_year  = int(birthdate[6:10])

month_list = [ "Jan" , "Feb", "Mar",  "Apr",  "May" , "Jun" , "Jul" ,  "Aug" , "Sep" , "Oct" , "Nov" , "Dec" ]
#                0       1      2       3       4       5       6        7       8       9      10      11 

print("\n Bith date is : ", birth_day, "/", month_list[birth_month - 1], "/", birth_year )
print("\n Age is : " , 2024 - birth_year , "\n" )