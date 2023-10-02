#A begineer level python programme to understand dictionaries

import art
print(art.logo)

bids = {}
name = input("What is your name ? :\t")
bid = int(input("What is your bid ? :\t"))

bids[name] = bid

flag = input("Are there any other bidders ? (Yes / No) :\t")

while(flag=="Yes"):
    name=input("What is your name ? :\t")
    bid=int(input("What is your bid ? :\t"))
    bids[name]=bid
    flag=input("Are there any other bidders ? (Yes / No) :\t")

highes = -1
highest_bidder = ""

for key in bids:
    if(bids[key]>highes):
        highes = bids[key]
        highest_bidder = key

print(f"Highest Bid {highes} , Highest Bidder {highest_bidder}")
