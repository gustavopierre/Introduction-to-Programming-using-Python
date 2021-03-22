import sys

a = float(input("Enter a number: "))
b = float(input("Enter a number to divide by: "))

try:
    print(f"The answer is {a/b}.")
except:
    print(sys.exc_info()[0])
    print("This did not work. Did you try to divide by zero or something?")
else:
    print("You successfully used the division in Python.")
finally:
    print("Thank you for playing.")
    