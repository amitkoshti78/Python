try:
    with open("records.txt", "r") as file_handle :
        
        for _ in range(0,30):
           line = file_handle.readline()
           print(line)
       
        
       
        #print(file_handle.tell())
    
except FileNotFoundError:
    print("File does not exists")
except FileExistsError:
    print("File already exists")
except Exception as err:
    print(f"Error occuered while opening a file in write mode {err}")

finally:
    print("Program ended")
    