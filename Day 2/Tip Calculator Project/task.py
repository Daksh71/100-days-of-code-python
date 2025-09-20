print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = bill * (tip / 100)
total_amount = bill + tip_amount
amount_per_person = total_amount / people
print(f"the split btw{people} of {total_amount} will be {amount_per_person}")


