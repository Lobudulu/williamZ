class Card:
    def __init__(self,number,suit):
        self.number=number
        self.suit=suit
    def string(self):
        if self.number==12:
            value="queen"
        if self.number==13:
            value="king"
        if self.number==11:
            value="jack"
        if self.number==1:
            value="Ace"
        else:
            value=self.number
        print(value,"of",self.suit)