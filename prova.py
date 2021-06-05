'''def add(x, y):
    return x + y

def mult(x, y):
    print(x * y)

add(1, 2)
print(add(2, 3))
mult(3, 4)
print(mult(4, 5))'''
'''colours = 'red'

def my_colour(color):
    colours = 'My favourite colour is %s.' % color
    return colours 

abc = my_colour('blue')

print(abc, 'Global variable: colours = ', colours)'''
'''def function1(a, b):
    return function2(a + b)

def function2(a):
    b = a * 5

print(function1(2, 3))'''

'''def function1(x, y):
    return function2(x + y)

def function2(a):
    return a * 5

print(function1(2, 3))
'''

'''cheese = 'cheddar'

def mix_and_cook():
    pass

def make_omelette():
    cheese = 'swiss'
    mix_and_cook()
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake1():
    global cheese
    cheese = 'Brie'
    mix_and_cook()
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def make_pancake2():
    mix_and_cook()
    pancake = 'a {} pancake'.format(cheese)
    return pancake
    
print(make_omelette())
print(make_pancake1())
print(make_pancake2())'''

'''cheese = 'gouda'

def make_omelette():
    global cheese
    cheese = 'very smelly cheese'
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake1():
    global cheese
    cheese = 'Brie'
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def make_pancake2():
    global cheese 
    pancake = 'a {} pancake'.format(cheese)
    return pancake

print(make_omelette())

print(make_pancake1())
print(make_pancake2())'''
'''def sq(func, x):
    y = x**2
    return func(y)

def f(x):
    return x**2

calc = sq(f, 2)
print(calc)'''
'''def always_sunny(t1, t2):
    """ t1, t2 are non empty """
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)

print(always_sunny( ('cloudy'), ('cold', ) ) )
'''

cheese = 'cheddar'

def make_omelette():
    cheese = 'swiss'
    omelette = 'a {} omelette'.format(cheese)
    return omelette

def make_pancake1():
    cheese = 'Brie'
    pancake = 'a {} pancake'.format(cheese)
    return pancake

def make_pancake2(): 
    pancake = 'a {} pancake'.format(cheese)
    return pancake

print(make_omelette())

print(make_pancake1())
print(make_pancake2())
