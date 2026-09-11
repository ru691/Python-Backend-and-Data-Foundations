# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
total_bidders = {}

continue_bidding = "yes"
while continue_bidding == "yes":
    name = input("What is your name?: \n")
    bid_amount = int(input("What is your bid?: \n"))
    total_bidders[name] = bid_amount
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)

highest_bid = 0
winner = ""
for bidder in total_bidders:
    bids = total_bidders[bidder]
    if bids > highest_bid:
        highest_bid = bids
        winner = bidder
print(f"The winner is {winner} with a bid of {highest_bid}.")