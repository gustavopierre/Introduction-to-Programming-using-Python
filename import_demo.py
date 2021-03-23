# Use separate namespace for "math" module
print("List of object names in __main__ namespace:")
print(dir())
import math
print("List of object names in __main__ namespace:", end=" ")
print("after 'import math' has executed:")
print(dir())
print("The value of pi is", math.pi)
print("The value of tangent of 1 is", math.tan(1))
print("\n")
del (math)

# Use separate aliased namespace for "math" module
print("List of object names in __main__ namespace:")
print(dir())
import math as fun
print("List of object names in __main__ namespace:", end=" ")
print("after 'import math as fun' has executed:")
print(dir())
print("The value of pi is", fun.pi)
print("The value of tangent of 1 is", fun.tan(1))
print("\n")
del (fun)

# Import selectively into __main__ namespace
print("List of object names in __main__ namespace:")
print(dir())
from math import tan, pi
print("List of object names in __main__ namespace:", end=" ")
print("after 'from math import tan, pi' has executed:")
print(dir())
print("The value of pi is", pi)
print("The value of tangent of 1 is", tan(1))
print("\n")
del (tan)
del (pi)

# Import selectively with aliases into __main__ namespace
print("List of object names in __main__ namespace:")
print(dir())
from math import tan as tangent, pi as pie
print("List of object names in __main__ namespace:", end=" ")
print("after 'from math import tan as tangent, pi as pie' has executed:")
print(dir())
print("The value of pi is", pie)
print("The value of tangent of 1 is", tangent(1))
print("\n")
del (tangent)
del (pie)
