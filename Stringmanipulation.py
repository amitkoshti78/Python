name = "      Amit     Koshti   "
name = name.strip()
print(name)

name = name.split("     ")
print("\n", name, "\n")

email = "amit.koshti@gmail.com"

domain = email.split("@")[-1]
print(domain)

name = email.split("@")[0]

name = name.split(".")
print(name)

firstname = name[0]
lastname = name[1]

print(firstname)
print(lastname)




