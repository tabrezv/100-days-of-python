from operator import truediv  # This line is unnecessary and can be removed
import art

print(art.logo)
print("Welcome to the secret auction program.")

# Function to find and print the highest bidder
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = int(bidding_dictionary[bidder])  # Convert to int to compare
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

# Main bidding logic
bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = input("What's your bid?: $")
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)  # Clears the screen
