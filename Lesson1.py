#Exersice 1
print("Hello world")
#Exersice 2
if(5 > 2):
    print("YES")
#Exersice 3
#This is a comment
"""
this is 
multilane comment
"""
#Exersice 4
carname = "Volvo"

#Exersice 5
x = 50

#Exersice 6
x = 5
y = 10
print(x + y)

#Exersice 7
x = 5
y = 10
z = x + y
print(z)

#Exersice 8
x,y,z = "apple","banan","cherry"

#Exersice 9
x = y = z = "orange"

#Exersice 10
def myfunc():
    global(x)
x = "fantastic"
 
#Exersice 11
x = 5
print(type(x))
int

#Exersice 12
x = "Hello world"
print(type(x))
str

#Exersice 13
x = 20.5
print(type(x))
float

#Exersice 14
x = ["apple", "banana", "cherry"]
print(type(x))
list

#Exersice 15
x = ("apple", "banana", "cherry")
print(type(x))
tuple

#Exersice 16
x = {"name" : "John", "age" : 36}
print(type(x))
dict

#Exersice 17
x = True
print(type(x))
bool

#Exersice 18
x = 5
x = float(x)

#Exersice 19
x = 5.5
x = int(x)

#Exersice 20
x = 5
x = complex(x)

#Exersice 21
x = "Hello world"
print(len(x))

#Exersice 22
txt = "Hello world"
x = txt[0]
print(x)

#Exersice 23
txt = "Hello world"
x = txt[2:5]
print(x)

#Exersice 24
txt = " Hello world "
x = txt.strip()
print(x)

#Exersice 25
txt = "Hello world"
x = upper(txt)

#Exersice 26
txt = "Hello world"
x = lower(txt)

#Exersice 27
txt = "Hello world"
x = txt.replace('H','J')

#Exersice 28
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))