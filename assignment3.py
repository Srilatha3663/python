"""
WHat is boolean.
and all the inbuild funtions for boolean
use condition statements for the operators:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""

a = 10
b = 11

if (a > b):
    print("statement is true")
else:
    print("warning")

print(11, bool(10))


def someFun():
    return False

if(someFun()):
    print("funtion undi")
else:
    print("funtion ledu")

x = "200"
print(isinstance(x, str))
a= 4.5
if (a%2 == 0):
    print("it is even")
elif(a%2==1):
    print("it is odd")
else:
    print("number is not a whole number")

x= 6
if (x<5 or x< 3):
    print("the number is less than 3")
elif(x>5 or x< 3):
    print("number is greated than 5")
else:
    print("number is in  between 3 and 5")


animals = ["cat","dog"]
if ("cate" not in animals):
    print("true")
else:
    print("flase")

