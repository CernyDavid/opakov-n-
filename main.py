number = 100
number = 69
website = "pslib.cz"

website = "google.com"

a = b = c = "Hello"
x, y, z = 1, 2, 3

PI = 3.14

abc = 0b01010

d = 9
e = 1+2j
f = [5, 10, 15, 20, 25, 30, 35, 40]
g = [1, 2.2, 'python']
h = (5, 'program', 1+3j)
i = "string"
j = """multiline
sting"""
k = {5, 10, 9, 6, 77, 4}
l = {1, 1, 2, 2, 3, 3}
m = {1: 'value', 'key':2}
n = dict([[1, 2], [3, 4]])
{1: 2, 3: 4}

o = 20
p = 10
print("o + p = ", o+p)
print("o - p = ", o-p)
print("o * p = ", o*p)
print("o / p = ", o/p)
print("o // p = ", o//p)
print("o ** p = ", o**p)

print("o > p is", o>p)
print("o < p is", o<p)
print("o == p is", o==p)

q = True
r = False
print("q and r is", q and r)
print("q or r is", q or r)
print("not r is", not r)
s = 5
t = s + 5
u = s - 3
v = s * t

x1 = 5
x2 = 5
y1 = 7
y2 = 7

x3 = "Hello there"

w = 10
print("id(w) is", id(w))

def printHello():
  print("hello there")

ab = printHello

ab()

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print("a =", a)

def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)