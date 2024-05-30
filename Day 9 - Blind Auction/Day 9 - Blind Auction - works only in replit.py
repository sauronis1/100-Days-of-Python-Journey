from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the blind auction program.")



def auction():
  bids = {}
  another_round = True
  while another_round is True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    again = input("Are there any more bidders? Type 'yes' or 'no'.")
    if again == "yes":
      another_round = True
    elif again == "no":
      another_round = False
    clear()
    
  highest_bid = 0
  highest_bidder = ""
  for key in bids:
    if bids[key] > highest_bid:
      highest_bid = bids[key]
      highest_bidder = key
  if highest_bid == 0:
    print("We're not giving shit out for free.")
  else:
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
auction()
  
