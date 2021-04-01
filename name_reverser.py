firstname = input("First name: ")
lastname = input("Last name: ")

# first solution
for count in range(len(firstname)-1, -1, -1):
    print(firstname[count], end="")
print(" ", end="")
for count in range(len(lastname)-1, -1, -1):
    print(lastname[count], end="")

# second solution
print(" ", firstname[::-1], lastname[::-1])
