"""
What is string?
what is variable?
what are parameters?
what is integer?
what is funtion?
what is datatype?
what is slicing and print an example?
What is Modification and print an example?
what is concatination and print an example?
what is .format() and print with examples?
what is escape character and print all the escape examples?
"""

india = "it is a country from south asia and have largest population"

b = "hellO World"
print(b[6:8])
print(b[-3:-2])

print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace('W', "s"))
print(b.split("W"))

age = 26
siri = "Is a girl have {}"

print(siri.format(age))

txt = 'We are the so-called\t\'Vikings\' from the north.'
print(txt)
print(india.title())
print(india.zfill(100))

"""what is variable?
variable is a container to store the data values """
b = "hello"
print(b)

""" what is concatenation and print an example?
 combine two strings yoe can use + operation """
a = "siri"
b = "Yadav"
c = a + b
print(c)
"if we want space we can use add quotation  between + """
c = (a + " " + b)
print(c)
""""what is string?
string in python are surrounded by either single quotation or double quotation mark"""
"""we can display in string by print function """
print('siri')
print("siri")
"""what is data types
data types are """
a = int(2)  # int is whole num
b = float(2.0)  # float is num with decimal point
c = str("hello")  # str is ordered sequence  of character with quotation marked
d = complex(4j)


# function is block of code it works only when it call
def multi(a, b):
    return a * b


print("multiplication", multi(10, 7))

# you can return a range of character by using a slice syntax

a = "siri, yadav"
print(a[2:4])

x = "siri, yadav"
print(x.upper())
y = "SIRI, karthik"
print(y.lower())
z = "siri, yadav"
print(z.replace("i", "s"))
p = "srilu, yadav"
print(p.replace("s", "k"))
s = "siri, kadari"
print(s.split(","))

age = str(29)
age = str(30)
txt = "my name is srilu, i am" + age
print(txt)


txt = "My Name is Srilu, and I am age{}"
print(txt.format(age))


