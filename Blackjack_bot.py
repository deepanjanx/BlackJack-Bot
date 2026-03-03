import Blackjack_Game as bj

def WinStar(player,dealer):
    ph=bj.deckSum(player)
    dh=bj.deckSum(dealer)
    if (ph>=12) and (ph<=16) and (dh>=2) and (dh<=6):
        return "S"
    elif (ph>=12) and (ph<=16) and (dh>=7) and (dh<=11):
        return "H"
    else:
        return "S"
def runbot():
    r=bj.playgame(WinStar)
    return r