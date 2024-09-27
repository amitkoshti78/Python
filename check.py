try:
    file_handle = open("records.txt", "r+")
    print(file_handle.tell())
    lines = file_handle.read()
    #print(lines)
    file_handle.seek(10)
    file_handle.write("\nRecord 31")
    print(file_handle.tell())
    file_handle.seek(0)
    print(file_handle.tell())
    lines = file_handle.read()
    print(lines)
    print(file_handle.tell())
    
except FileNotFoundError:
    print("File does not exists")
except FileExistsError:
    print("File already exists")
except Exception as err:
    print(f"Error occuered while opening a file in read mode {err}")
else:
    file_handle.close()
finally:
    print("Program ended")
    