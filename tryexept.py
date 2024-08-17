import logging
logging.basicConfig(filename='/Users/amitkoshti/Downloads/Sessions/Python/log.txt')

values_list = [9, 45, 0, "A", 3, "Amit", 89, 2, "45", 76 ]
result_list = []
for number in values_list:
    try:
        result = 100 / int(number)
    except ZeroDivisionError:
    #    pass
        print("Division by Zero not allowed", number)
    #except TypeError:
    #    pass
    #    print("Invalid numeric value", number)
    except Exception as err:
        logging.error(msg=f'{err} : Ocuured due to {number}')
        #print(err)
    else:    
        #print("Division successful", number)
        result_list.append(round(result,2))
    finally:
        pass
        #print("Hello")
    
#print("\n Fianl List", result_list)    

First = "Neha"
Second = "Marathe"
Teacher = "Amit"
msg = f'Dear {First} {Second}, \n\tWelcome to python Course. \nThis is our new designed course which will make you proficient in python programming. \nBest regards,\n {Teacher}'

print(msg)

msg = msg.replace('python', 'ANSI C') 

print(msg)

print('Dear', First, Second , ",\n\tWelcome to python Course. \nThis is our new designed course which will make you proficient in python programming. \nBest regards,\n " , Teacher)
