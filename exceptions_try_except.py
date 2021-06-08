try:
    x = int(input("Enter the denominator: "))
    y = 1/x
    raise Exception
    print(y)
except ZeroDivisionError:
    print("Cannot divide by zero, sorry!")
except ValueError:
    print("You must enter an integer value.")
except:
    print("oh, oh, something went wrong but I don't know what")
    