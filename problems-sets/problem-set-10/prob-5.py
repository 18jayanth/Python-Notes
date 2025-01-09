"""5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railway"""
import random
class train:
    def __init__(self,trainno,form,to):
        self.trainno=trainno
        self.form=form
        self.to=to
    def book(self):
        print(f"Train is with train no:{self.trainno}is booked from {self.form} to {self.to}")
    def status(self):
        print(f"Train no {self.trainno}is booked at this time")
    def fare(self):
        print(f"The Fare amount from {self.form} to{self.to} is {random.randint(222,555)}")
"""harry=train("12345")
harry.book("pathapatnam","srikakulum") #Train is with train no:12345is booked from pathapatnam to srikakulum
harry.status()#Train no 12345is booked at this time
harry.fare("pathapatnam","srikakulum")#The Fare amount from pathapatnam tosrikakulum is 299"""
harry=train("12345","pathapatnam","srikakulum")
harry.book()
harry.status()
harry.fare()
#both gives the same result we can put all parameters in init or keep it individually

