"""6. Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects."""
import random
class train:
    def __init__(slf,trainno,form,to):
        slf.trainno=trainno
        slf.form=form
        slf.to=to
    def book(jayanth):
        print(f"Train is with train no:{jayanth.trainno}is booked from {jayanth.form} to {jayanth.to}")
    def status(pavan):
        print(f"Train no {pavan.trainno}is booked at this time")
    def fare(ajay):
        print(f"The Fare amount from {ajay.form} to{ajay.to} is {random.randint(222,555)}")
harry=train("12345","pathapatnam","srikakulum")
harry.book()
harry.status()
harry.fare()
#there is no change in results