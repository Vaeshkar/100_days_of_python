# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
# Get the input from the current user
user_name = input("What is your name?\n")
user_bid = int(input("Please, make a bid?\n"))

# Users bidding, saved in a dictionary, dict literal used
bidding_dict = {user_name: user_bid}
#print(bidding_dict)

# Generate a 'while' loop to keep on going.
program = True
while program:
    # Aks if someone else wants to bid?
    more_users = input("Are there more people who want to join? 'yes' or 'no'\n").lower()
    if more_users == "no":
        highest_bid = 0
        winner = ""
        for user, bid in bidding_dict.items():
            if bid >= highest_bid:
                highest_bid = bid
                winner = user
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
        program = False
    elif more_users == 'yes':
        # new_user_clean_screen
        print("\n" * 40)
        user_name = input("What is your name?\n")
        user_bid = int(input("Please, make a bid?\n"))
        bidding_dict[user_name] = user_bid
    else:
        print("Wrong input: Write yes or no.")
