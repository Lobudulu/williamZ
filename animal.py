class animal:
    def __init__(self,leg,pig,tail,eyes,a_lot_of_foods_to_eat):
        self.leg=leg
        self.pig=pig
        self.tail=tail
        self.eyes=eyes
        self.a_lot_of_foods_to_eat=a_lot_of_foods_to_eat
    def string(self):
        print(self.leg,self.pig,self.tail,self.eyes,self.a_lot_of_foods_to_eat)
x=input("does the animal have at least 1 leg ")
r=input("is the animal a pig ")
j=input("does the animal have a tail ")
q=input("does the animal have eyes ")
e=input("does the animal have a lot of foods to eat ")
if x=="yes":
    x="The animal has legs"
if x=="no":
    x="The animal does not have legs."
if r=="yes":
    r="The animal is a pig."
if r=="no":
    r="The animal is not a pig."
if j=="yes":
    j="The animal has a tail."
if j=="no":
    j="The animal does not have a tail."
if q=="yes":
    q="The animal has eyes."
if q=="no":
    q="The animal has eyes."
if e=="yes":
    e="The animal has a lot of foods to eat."
if e=="no":
    e="The animal does not have a lot of foods to eat."
l=animal(x,r,j,q,e)
l.string()