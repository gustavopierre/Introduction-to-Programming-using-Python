num = 7000
num2 = 3456

print("A variable {} in a string".format(num))

formatted = "A {0} {1} and a {0} {2}."
print(formatted.format("blue", "car", "truck"))

formatted = "{:d}"
print(formatted.format(num))

formatted = "{:,d}"
print(formatted.format(num))

formatted = "{:^15,d}"
print(formatted.format(num))

formatted = "{:*^15,d}"
print(formatted.format(num))
