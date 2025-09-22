# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
lets = {}


permission = "yes"
while permission.lower() == "yes":
    name = input("Enter your name: ")
    price = int(input("Enter your bid amount: "))
    print("\n" * 20)
    lets[name] = price
    permission = input("Do you want to add more bids? Type yes/no: ")


print("Final bids are:")
print(lets)


winner_name = ""
highest_bid = 0

for bidder, amount in lets.items():
    if amount > highest_bid:
        highest_bid = amount
        winner_name = bidder


print(f"\nThe winner is {winner_name} with a bid of ${highest_bid}.")






# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


