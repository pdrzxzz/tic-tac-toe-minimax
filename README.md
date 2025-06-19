# 🎮 Tic-Tac-Toe with AI (Minimax Algorithm)  

A simple terminal-based Tic-Tac-Toe game in Python where a human player competes against an AI.  

## 🧠 About the AI  

- ✅ Unbeatable AI using Minimax with Alpha-Beta Pruning  
- 🎯 Prioritizes quick wins and avoids losses  
- ♻️ Backtracking logic to simulate all possible game outcomes  

## � How to Play  

Clone this repository:  

```bash
git clone https://github.com/yourusername/tic-tac-toe-ai.git  
```

Run the game:  

```bash
python game.py  
```  

1. Choose to play as **X** or **O**  
2. **X always moves first**  
3. Enter your moves using row and column indices (0 to 2), for example:  

```
Your move (row and column, from 0 to 2): 0 1  
```  

## 🧾 Code Structure  

- `play()` – Starts and manages the game loop  
- `minimax()` – Main recursive algorithm for optimal decision-making  
- `best_move()` – Finds the best move for the AI using Minimax  
- `isGameOver()` – Checks for a win or draw  
- `possible_moves()` – Returns available moves on the board  
- `show_board()` – Displays the board in the console  

## 🛠 Requirements  

- Python 3.6 or higher  
- No external libraries required  

---  

## 📷 Sample Output  

```
AI is thinking...  
 X | O | O  
-----------  
   | O | X  
-----------  
 O | X | X  
-----------  
O wins!  
```  

## 📄 License  

This project is **open-source** and free to use.  

Made by [pdrzxzz](https://github.com/pdrzxzz) | Computer Science Student 🎓  

![MuaKissGIF (2)](https://github.com/user-attachments/assets/2bc84399-8890-47c4-bca9-74546d5d07a6)  
