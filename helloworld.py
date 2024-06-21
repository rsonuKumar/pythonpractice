# Introduction
print("hello , world")
print("----------------------------------")
#To get the version
import sys
print(sys.version)
print("----------------------------------")
# indentation 
 # @ without error
if 10>2:
    print("Number 10 is greater then 2")
print("----------------------------------")

if(20<10):
    print("20 is smaller")
else:
    print("10 is smaller")
print("----------------------------------")

# variable
x,y=20,40
print(x,y)
print("----------------------------------")

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x=5000
print(x)
x="Practice,Python"
print(x)
print("----------------------------------")

#Casting

x=int(3)
print(type(x))
x="Practice Python" #casted to  string type
print(x)
print(type(x))
print("----------------------------------")
# You can also use the + operator to output multiple string variables:
x="+ operator "
y=" used to "
z="concatinate"
print(x + y + z)
print("----------------------------------")

# The best way to output multiple variables in the print() function is to separate them with commas,
#  which even support different data types:
x=5
y="practice"
print(x,y)
print("----------------------------------")
# random number
import random

print(random.randrange(1,10))