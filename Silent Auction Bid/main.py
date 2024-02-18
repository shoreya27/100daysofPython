from art import logo
import os

biding_on = True
bidders = []
# Add a Bidding Logo
print(logo)
print()

while biding_on:

    name = input("Enter your Name: ")
    bid_amount = int(input("Enter the bidding Amount: $"))

    user_bid_detail = {
        "name": name,
        "amount": bid_amount
    }

    bidders.append(user_bid_detail)
    add_more = input("Would you like to add other bidder details Y or N ?")

    if add_more == 'N':
        biding_on = False
    # clearing the screen
    os.system('clear')
    print(logo)
    print() 

def calculate_highest_bid(bidders):

    highest = -1
    winner = ''
    for bidder in bidders:
        if bidder["amount"] > highest:
            highest = bidder["amount"]
            winner = bidder["name"]
    
    print(f'Winner is {winner}, with highest bid of ${highest}')
    

calculate_highest_bid(bidders)