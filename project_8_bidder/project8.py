from art import logo
print(logo)

bid={}


# after generating dict we compare find the max value 
def max_bid(bid):
    max=0
    for i in bid:
        amount=bid[i]
        winner=i
        if amount>max:
            max=amount
        
    print(f"The winner is {winner} with a bid of ${max}")


# getting the bids and storing in a dictionary 
bidding=True
while bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid[name]=price
    to_continue  = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if to_continue=="no":
        bidding=False
        max_bid(bid)
    elif to_continue=="yes":
        bidding=True
    else:
        bidding=False

print(bid)
