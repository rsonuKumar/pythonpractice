# Quotes Inside Quotes 
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's all rigt")
print("He is called 'jhonny'")
print('He is call "Ram"')
print("----------------------------------")
#Multiline String

address="""south of baba engineering, new mainpura, danapur cannt patna bihar
        near balaji nagar"""
print(address)
print("----------------------------------")
#String is a Array
name="Ranjan Kumar Sonu"
print(name[0],name[7],name[13])

#looping through string
for x in range(len(name)):
    print(name[x])

# Chaecking Text
print("Sonu" in name)

if "Son" in name:
    print("Yes")
else:
    print("NO")

# String Slicing
print(name[2:9])

#Slicing from Start
print(name[:10])
#Slicing from End
print(name[2:])
#Negative Indexing
print(name[-10:-2])

# Creating a String
age=30
Name= f"My Name is Ranjan Kumar Sonu {age*30}"
print(Name)
