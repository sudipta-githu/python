p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"
p5 = "link"
p6 = "hot"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message) or (p6 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")   