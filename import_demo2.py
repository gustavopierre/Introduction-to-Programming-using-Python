import math

print(dir())
print(math.pi)
print(math.tan(1))
del(math)
print(dir())

import math  as fun

print(dir())
print(fun.pi)
print(fun.tan(1))
del(fun)
print(dir())

from math import pi, tan

print(dir())
print(pi)
print(tan(1))
del(pi)
del(tan)
print(dir())

from math import pi as pie, tan as tangent

print(dir())
print(pie)
print(tangent(1))
del(pie)
del(tangent)
print(dir())
