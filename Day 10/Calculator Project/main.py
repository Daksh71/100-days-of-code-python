def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 // n2

n1 = int(input("pls enter the first digit you want to perform the calculation with "))
dec =input("pls enter what mathematical cal you want to perform add(addition) , sun(subtraction ,mul(multiply) or div(division))").lower()
n2= int(input("enter the second digit you want to perform operation"))

# if dec == "add":
#     print(add(n1,n2))
# elif dec == "sub":
#     print(sub(n1,n2))
# elif dec == "mul":
#     print(mul(n1, n2))
# elif dec == "div":
#     print(div(n1, n2))
# else:
#     print("print invalid input pls try again ")


operation = {
    "add" : add,
    "sub" : sub,
    "mul": mul,
    "div": div
}

if dec in operation :
    result=(operation[dec](n1, n2))
    print(f"The result of the operation {dec} is {result}")
else:
    print("pls retry to put the input . it looks like you entered wrong input ")


