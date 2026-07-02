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
        rope=f"{value} of {self.suit}"
        print(rope)
        if rope=="Ace of spades":
            print("🂡")
        if rope=="Ace of hearts":
            print("🂱")
        if rope=="Ace of diamonds":
            print("🃁")
        if rope=="Ace of clubs":
            print("🃑")
        if rope=="2 of spades":
            print("🂢")
        if rope=="2 of hearts":
            print("🂲")
        if rope=="2 of clubs":
            print("🃒")
        if rope=="2 of diamonds":
            print("🃂")
        if rope=="3 of spades":
            print("🂣")
        if rope=="3 of hearts":
            print("🂳")
        if rope=="3 of diamonds":
            print("🃃")
        if rope=="3 of spades":
            print("🃓")