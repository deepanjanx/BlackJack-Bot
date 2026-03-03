import Blackjack_bot as bb

win=0
lose=0
for i in range(1000000):
    r=bb.runbot()
    if r=="W":
        win+=1
    elif r=="L":
        lose+=1
    else:
        pass
print(f"{win/10000:.2f}% is the winrate")