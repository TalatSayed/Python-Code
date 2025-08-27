
#new bids
def maximum_value(bidding_dictionary):
    highest_value = 0
    winner = ""
    for bidder in bidding_dictionary :
        bidder_amount = bidding_dictionary[bidder] #price is getting stored in the variable 
        if bidder_amount>highest_value:
            highest_value = bidder_amount
            winner = bidder

    print(f"The winner is {winner} with the bid of rupees {highest_value}")
   


bids={}
continue_bidding = True
while continue_bidding :
   
    name  = input("What is your name?:-")
    bid_price = int(input("What is your bid price ? :-"))
    bids[name] = bid_price
    new_bids = input("Are there anymore Bidders y fro yes and n for no \n").lower()
    if new_bids =="n" :
        continue_bidding = False
        maximum_value(bidding_dictionary=bids)
    elif new_bids =="y":
        print("\n"*10000)
     
  
