from replit import clear
from art import logo,ascii_logo,congratulations

print(logo)
print(ascii_logo)

#Creating a empty dictionary as bids
bids = {}
bidding_finished = False

#Comparing bids and declare the winner
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The Winner is {winner.upper()} with a bid of ${highest_bid}.")

#Check if bidding is finished or if not finished yet continue to add bidder
while not bidding_finished:
  name = input("What's your name:")
  price  = int(input("What's your bid: $"))
  bids[name] = price
  should_continue = input("Are there any bidders? Please type 'yes' or 'no'. \n")
  
  if should_continue == "no":
    bidding_finished = True
    clear()
    print(congratulations)
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()



