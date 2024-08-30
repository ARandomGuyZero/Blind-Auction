"""
Auction Program

Author: Alan
Date: August 2024

This program allows users to place bids in an auction and determines the highest bidder.
"""

import art

# Print the logo from the art module
print(art.logo)

def store_bidders():
    """
    Collects bidder names and their respective bids, and stores them in a dictionary.
    
    The function continues to prompt for new bidders until the user decides to stop.
    """
    continue_bidding = True
    while continue_bidding:
        # Get the bidder's name
        name = input("What is your name?\n")
        
        # Get the bidder's bid amount and convert it to an integer
        bid = int(input("What is your bid?\n$"))
        
        # Save the data into the dictionary with the bidder's name as the key and bid as the value
        bidders_dictionary[name] = bid
        
        # Ask if there are more bidders who want to place bids
        option = input("Are there other bidders? Type 'yes' or 'no'\n").lower()
        if option == "no":
            continue_bidding = False
        
        # Clear the screen by printing 20 new lines to hide previous bids
        print("\n" * 20)

def find_highest_bidder():
    """
    Determines the highest bid from the dictionary of bidders and declares the winner.
    """
    highest_bid = 0
    winner = ""
    
    # Loop through the dictionary to find the highest bid and the corresponding bidder
    for bidder in bidders_dictionary:
        if bidders_dictionary[bidder] > highest_bid:
            highest_bid = bidders_dictionary[bidder]
            winner = bidder
    
    # Announce the winner and their bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Initialize an empty dictionary to store the bidders and their bids
bidders_dictionary = {}

# Start the bidding process
store_bidders()

# Find and announce the highest bidder
find_highest_bidder()
