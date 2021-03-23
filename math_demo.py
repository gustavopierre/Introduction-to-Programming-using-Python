import math

x, y = 5.0, 10
print("x=", x, "y=", y, "\n")

pi = math.pi
e = math.e
print("The value of pi is: ", pi)
print("The round value of pi is: ", round(pi, 4))

pos_inf = float("inf")
neg_inf = float("-inf")
not_a_num = float("nan")

print("math.isinf(pos_inf) = ", math.isinf(pos_inf))
print("math.isinf(neg_inf) = ", math.isinf(neg_inf))
print("math.isnan(not_a_num) = ", math.isnan(not_a_num))
print("\n")

print("pos_inf*x=", pos_inf*x)
print("neg_inf/y=", neg_inf/y)
print("pos_inf + neg_inf = ", pos_inf + neg_inf)
print("not_a_num - y = ", not_a_num - y)
print("\n")

print("not_a_num == not_a_num = ", not_a_num == not_a_num)
print("\n")

print("math.factorial(5)=", math.factorial(5))
print("\n")

print("e=", e)
print("math.log(x)=", math.log(x))
print("math.log10(x)=", math.log10(x))
print("math.exp(x)=", math.exp(x))
print("math.pow(x, x)=", math.pow(x, x))
print("math.sqrt(25)=", math.sqrt(25))
print("\n")