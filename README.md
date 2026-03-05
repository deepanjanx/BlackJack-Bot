# BlackJack Bot
A Python-based Blackjack environment featuring a playable CLI game, an automated bot with editable strategies, and a high-volume testbench for win-rate analysis.
## 📂 Project Structure
The repository consists of four main files:
|**File**|**Description**|
|---|---|
|**`Blackjack the Game.py`**|A standalone, playable version of Blackjack. Run this in your terminal to understand the game mechanics and rules.|
|**`Blackjack_Game.py`**|The "Game Engine." It acts as the environment where the bot plays, stripped of manual inputs and unnecessary print statements for speed.|
|**`Blackjack_bot.py`**|The logic brain. It connects to the engine and contains the `WinStar` strategy function that decides whether to "Hit" or "Stand."|
|**`Testbench.py`**|The simulator. It runs the bot through **1,000,000** iterations (default) and calculates the final win rate.|

---
## 🚀 How to Use
### 1. Play the Game
If you want to play a round yourself:
``` bash
python "Blackjack the Game.py"
```
### 2. Run the Simulation
To see how the current strategy performs over a million games:
``` bash
python Testbench.py
```
---
## 🧠 Current Strategy
The bot currently uses a basic logic gate based on the player's hand vs. the dealer's visible card.
**Current Win Rate:** ~39.5%
### Editing the Strategy
You can modify the bot's behavior by editing the `WinStar` function in `Blackjack_bot.py`:
``` Python
def WinStar(player, dealer):
    ph = bj.deckSum(player)
    dh = bj.deckSum(dealer)
    
    # Example logic: Stand on 12-16 if dealer shows 2-6
    if (ph >= 12) and (ph <= 16) and (dh >= 2) and (dh <= 6):
        return "S"
    # Otherwise, Hit
    return "H"
```
---
## 🛠 Features
- **Aces Handling:** Automatically calculates if an Ace should be valued at 1 or 11.
- **High Performance:** The `Testbench` can process 1,000,000 games in seconds.
- **Modular Design:** Easy to swap the game engine or the bot logic without breaking the other.
