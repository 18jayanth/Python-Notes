""" 3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams. """
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"

spamtest=input("Enter a message::")
if(p1 in spamtest or p2 in spamtest or p3 in spamtest): # in function will see if the word is there is messgae
   print("spam")
else:
   print("YOu are safe")

