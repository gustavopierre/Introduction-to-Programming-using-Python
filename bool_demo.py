x = 1
print("bool(x)=", bool(x))
y = 0
print("bool(y)=", bool(y))
print("\n")

if not None: print("None is False")
if not False: print("False is False")
if not (0 or 0.0 or 0j): print("Zero is False")
if not ("" or [] or ()): print("Empty sequences are False")
if not ({} or set([])): print("Empty mappings are False")
print("\n")

# Boolean OR returns first True or last False value
print("True or False returns ", True or False)
print("1 or 0 returns ", 1 or 0)
print("4 or 2 or 3 returns ", 4 or 2 or 3)
print("None or 0 returns ", None or 0)
print("0 or None returns ", 0 or None)
print("\n")