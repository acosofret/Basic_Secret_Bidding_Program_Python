from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.\n")
bids = {}
ask_input = True
while ask_input:
	bid_name = input("What is your name?: ")
	bid_amount = int(input("What's your bid?: £"))
	continuation = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
	bids[bid_name] = bid_amount
	ask_input_check = True
	while ask_input_check:
		if continuation == 'yes':
			ask_input = True
			ask_input_check = False
		elif continuation == 'no':
			ask_input = False
			ask_input_check = False
		else:
			print("The value you entered is incorrect.\n")
			continuation = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
	clear()

winner = max(bids, key=bids.get)
print(f"The winner is {winner}")

# Optionally we can record & show the amount of the winner as: winning_amount = bids[max(bids, key=bids.get)]

# Further possible improvements:
# * full debugging for various scenarios that may not work
# * Auto-capital letters on name input
# * Repeat amount request in case of invalid input
# * Allow for decimals on amount input
