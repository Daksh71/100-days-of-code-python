print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
    print("Small pizza")
elif size == "M":
    bill += 20
    print("medium pizza")
elif size == "L":
    bill += 25
    print("large pizza")
else :
    print("wrong choice ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
else:
    bill+= 0
if extra_cheese == "Y":
    if size == "S":
        bill +=1
    else:
       bill += 3
else:
    bill+=0

print(f"(the final prize of the bill is ${bill}")

