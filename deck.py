import random
from card import Card

def Create_deck():
    deck=[]
    for i in range(1,14):
        if i==13:
            i="king"
        if i==12:
            i="queen"
        if i==11:
            i="jack"
        if i==1:
            i="Ace"
        x=Card(i,"clubs")
        deck.append(x)
    for i in range(1,14):
        if i==13:
            i="king"
        if i==12:
            i="queen"
        if i==11:
            i="jack"
        if i==1:
            i="Ace"
        x=Card(i,"diamonds")
        deck.append(x)
    for i in range(1,14):
        if i==13:
            i="king"
        if i==12:
            i="queen"
        if i==11:
            i="jack"
        if i==1:
            i="Ace"
        x=Card(i,"spades")
        deck.append(x)
    for i in range(1,14):
        if i==13:
            i="king"
        if i==12:
            i="queen"
        if i==11:
            i="jack"
        if i==1:
            i="Ace"
        x=Card(i,"hearts")
        deck.append(x)
    return deck