a1 = "Make a lot of money"
a2 = "buy now"
a3 = "subscribe this"
a4 = "click this"

message = input("Comment: ")

if(a1 in message or a2 in message or a3 in message or a4 in message):
    print("Message is inappropriate")
else:
    print(message)