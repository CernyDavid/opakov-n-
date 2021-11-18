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

num = 3
if num > 0:
    print(num, "je kladné")
print("This is always printed")

num = -1
if num > 0:
    print(num, "je kladné")
print("This is also always printed")

number = 3
if number >= 0:
    print("kladné nebo nula")
else:
    print("záporné")

num = -4.5
if num > 0:
    print("kladné")
elif num == 0:
    print("nula")
else:
    print("záporné")

num = float(input("Zadejte číslo: "))
if num >= 0:
    if num == 0:
        print("Nula")
    else:
        print("Kladné")
else:
    print("záporné")

numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 5
for val in numbers:
    sum = sum+val

print("The sum is", sum)
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("I like", genre[i])

digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("Nic nezbylo")

student_name = "Standa Uzdichcal"

marks = {"James": 90, "Jules": 55, "Arthur": 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("Nenalezeno")

n = 15
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1 

print("The sum is", sum)

cislo = 0

while cislo < 3:
    print("Inside loop")
    cislo = cislo + 1
else:
    print("Inside else")

