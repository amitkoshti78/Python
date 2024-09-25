import os

os.remove("student.txt")

file1 = open("student.txt", "w")

""" print(file1.readline())
print(file1.readline())
print(file1.readline()) """

file1.write("fisrt_name\tlast_name\temail_id\tphone_number\n")
file1.write("Santosh\tBendre\tSantosh.Bendre@gmail.com\t910228259\n")
file1.write("Anmol\tJadhav\tAnmol.Jadhav@gmail.com\t9812341254\n")
file1.write("Amol\tKamble\tAmol.Kamble@gmail.com\t9142343257\n")
file1.write("Sameer\tPatil\tSameer.Patil@gmail.com\t9215368213\n")
file1.write("Omkar\tKulkarni\tOmkar.Kulkarni@gmail.com\t9372301917\n")
file1.write("Samara\tKhan\tSamara.Khan@gmail.com\t9850642264\n")
file1.write("Parthana\tJoshi\tParthana.Joshi@gmail.com\t9172183206\n")
file1.write("Sujit\tGavit\tSujit.Gavit@gmail.com\t9225060215\n")
file1.write("Akshay\tPatil\tAkshay.Patil@gmail.com\t9268001318\n")
file1.write("Viraj\tKamble\tViraj.Kamble@gmail.com\t9384397521\n")

file1.close()

file1 = open("student.txt", "r")

""" print(file1.readline())
print(file1.readline())
print(file1.readline()) """

data = file1.read()



""" for line in file1:
    print(line)
     """
domain1 = "gmail.com"
domain2 = "yahoo.com"

new_data = data.replace(domain1, domain2)

        
file1.close()

file1 = open("student.txt", "w")


file1.write(new_data)


file1.close()

file1 = open("student.txt", "r")


for line in file1:
    print(line)

file1.close()
    
with open("student.txt", "r+") as file2:
    
    print(file2.read())
    file2.write("Prakash\tBhandare\tPrakash.Bhandare@gmail.com\t913778850\n")
    

with open("student.txt", "r+") as file2:
    print(file2.read())