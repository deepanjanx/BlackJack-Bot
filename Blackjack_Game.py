import random

#deck geerator function
def deckgen():
    Base="A,2,3,4,5,6,7,8,9,10,J,Q,K"
    Deck=Base.split(",")*4
    random.shuffle(Deck)
    return Deck

#Deck Score Calc
def deckSum(deck: list):
    countA=0
    deckSum=0
    for card in deck:
        if card=="A":
            countA+=1
        elif card in "JQK":
            deckSum+=10
        else:
            deckSum+=int(card)
    for i in range(countA):
        if deckSum+11>21 or countA>1:
            deckSum+=1
        else:
            deckSum+=11
    return deckSum

def playgame(strategy=None):
    Deck=deckgen() #Deck Generation
    player=[] #player's hand
    dealer=[] #dealer's hand

    # Dealing the initial hands
    for i in range(2):
        player.append(Deck.pop())
        dealer.append(Deck.pop())
    Stand=False
    #show(player,dealer,Stand) #first #showcase after initial dealings

    while (not Stand) and (deckSum(player)<21): #Player's turn 
        ctrl=strategy(player,dealer[1:])
        if ctrl.startswith("H"):
            player.append(Deck.pop())
        elif ctrl.startswith("S"):
            Stand=True
        #show(player,dealer,Stand)

    #Dealer's chance
    playerhand=deckSum(player)
    while deckSum(dealer)<17 and playerhand<=21: #only enters if player not bust and dealer's hand less than 17

        Stand=True
        dealer.append(Deck.pop())
        #show(player,dealer,Stand)

    #Evaluation
    dealerhand=deckSum(dealer)
    if playerhand>21:
        return "L"
    elif dealerhand>21:
        return "W"
    elif playerhand<dealerhand:
        return "L"
    elif playerhand>dealerhand:
        return "W"
    else:
        return "D"
