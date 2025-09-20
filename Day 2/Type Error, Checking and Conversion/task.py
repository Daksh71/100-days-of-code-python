name=input("enter your name pls \n")
# length = len(name)
length=str(len(name))
print("Number of letters in your name: " + length)



# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()