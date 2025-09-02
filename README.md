# Tic Tac Toe with Alpha-Beta Pruning  

This project implements a **Tic Tac Toe AI** using the **Alpha-Beta Pruning algorithm**.  
The AI plays optimally against a human player by pruning unnecessary moves, ensuring efficient gameplay.  

---

## Features  
- Human vs AI gameplay (Player = `O`, AI = `X`)  
- Alpha-Beta Pruning optimization for faster decisions  
- Utility evaluation (`+1` AI win, `-1` player win, `0` draw)  
- Terminal state detection (win, lose, or draw)  
- Simple CLI board display  

---

## How to Play  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-alphabeta.git
   cd tic-tac-toe-alphabeta
   ```

2. Run the game:  
   ```bash
   python3 tictactoe.py
   ```

3. Enter a position (1–9) when prompted.  
   - Positions map as follows:  

   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

4. The AI (`X`) will respond with its best move.  
5. Play continues until a win or draw.  

---

## Example Gameplay  

```
Initial Board:
- | - | -
---------
- | - | -
---------
- | - | -

Your Turn! Enter position (1-9): 5
AI is making a move...
X | - | -
---------
- | O | -
---------
- | - | -
```

---

## Technologies Used  
- **Python 3**  
- **Alpha-Beta Pruning (Minimax Optimization)**  

---

## Future Improvements  
- Add GUI (Tkinter or Pygame)  
- Adjustable difficulty (depth limit)  
- Two-player mode  

---
