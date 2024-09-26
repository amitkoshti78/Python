file_handle = open("msg1.txt", "w+")

file_data = file_handle.read()
print(file_data)

file_handle.write("End the lines\n")


#file_handle = open("msg.txt", "r")
""" file_data = file_handle.read()
print(file_data) """

file_handle.close()

"""with open("msg.txt", "r") as file_handle1:
    print(file_handle1.read())"""

with open("msg.txt", "a+") as file_handle2:
    
    file_handle2.write("Append the line at the end\n")
    

print("file closed")
with open("msg.txt", "r") as file_handle1:
    
    for line in file_handle1:
        print(line)


