import random
'''A basic BlackJack game we gonna build our bot on this but not exactly this as this has too many outputs'''
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

# Show of hands:
def show(P_Deck: list, D_Deck: list, S:bool=False):
    print("Player's Hand:")
    for card in P_Deck:
        print(card, end="   ")
    print("\nDealer's Hand:")
    D_Deckt=D_Deck
    if S==False:
        D_Deckt=D_Deck[1::]
        print("X",end="   ")
    for card in D_Deckt:
        print(card, end="   ")
    print("\n---x---")


# Main Game:
def playgame():
    Deck=deckgen() #Deck Generation
    player=[] #player's hand
    dealer=[] #dealer's hand

    # Dealing the initial hands
    for i in range(2):
        player.append(Deck.pop())
        dealer.append(Deck.pop())
    Stand=False
    show(player,dealer,Stand) #first showcase after initial dealings

    while (not Stand) and (deckSum(player)<21): #Player's turn 
        ctrl=input("Do you wish to Hit or Stand: ").capitalize()
        if ctrl.startswith("H"):
            print("Player Hits")
            player.append(Deck.pop())
        elif ctrl.startswith("S"):
            print("Player Stands")
            Stand=True
        else:
            print("Error! Please input either Hit or Stand")
        show(player,dealer,Stand)

    #Dealer's chance
    playerhand=deckSum(player)
    while deckSum(dealer)<17 and playerhand<=21: #only enters if player not bust and dealer's hand less than 17
        print("Dealer Hits")
        Stand=True
        dealer.append(Deck.pop())
        show(player,dealer,Stand)

    #Evaluation
    dealerhand=deckSum(dealer)
    if playerhand>21:
        print("Player Bust, hence Player looses")
    elif dealerhand>21:
        print("Dealer Bust, hence Player wins")
    elif playerhand<dealerhand:
        print("Dealer has a higher hand, hence Player looses")
    elif playerhand>dealerhand:
        print("Player has a higher hand, hence Player wins")
    else:
        print("Equal hands, hence game has been a tie")
WannaPlay=True
while WannaPlay:
    playgame()
    if input("Do you wanna play again(Y/N): ").capitalize().startswith("Y"):
        WannaPlay=True
    else:
        WannaPlay=False