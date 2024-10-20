
      
try:
    file_handle = open("records.txt", "a+")
        
       
    records = "Sakshi;Gurme;sakshi.gurme@gmail.com;9312305544\n"
    file_handle.write(records)
        
    file_handle.seek(89)
    print(file_handle.tell())
    records = file_handle.read()
    print(records)
        
    """for _ in range(0,30):
           line = file_handle.readline()
           print(line)"""
       
    #print(file_handle.tell())
    
except FileNotFoundError:
    print("File does not exists")
except FileExistsError:
    print("File already exists")
except Exception as err:
    print(f"Error occuered while opening a file in write mode {err}")

finally:
    
    print("Program ended")
    