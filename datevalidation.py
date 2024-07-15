
def leap_year(yyyy_j):
    
    if yyyy_j % 4 == 0 :
        if yyyy_j % 100 == 0 :
            if yyyy_j % 400 == 0 :
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

def date_validation(day_i, month_i, yyyy_i):

    if yyyy_i < 1 :
        return f'Year {yyyy_i} is invalid'

    if month_i < 1  or month_i > 12 :
        return f'Month {month_i} is invalid'
  
    

    if month_i == 4 or month_i == 6 or month_i == 9 or month_i == 11 :
        month_end_day = 30
    else:
        month_end_day = 31

    if month_i == 2 :
        month_end_day = leap_year(yyyy_i)
        if month_end_day == 29 :
            print(f'Year {yyyy_i} is a leap year')
        else:
           print(f'Year {yyyy_i} is a not leap year') 

    if day_i <= month_end_day and day_i > 0 :
        return f'Date {day_i}/{month_i}/{yyyy_i}  is valid'
    else:
        return f'Day {day_i} is invalid'
    
def main():

    date_str = input("Enter a date in dd/mm/yyyy format : ")
    date_list = date_str.split('/')
    int_dd   = int(date_list[0])
    int_mm   = int(date_list[1])
    int_yyyy = int(date_list[2])

    print(date_list)
    fstr_msg = date_validation(int_dd, int_mm, int_yyyy)

    print(fstr_msg)

if __name__ == '__main__' :
    main()