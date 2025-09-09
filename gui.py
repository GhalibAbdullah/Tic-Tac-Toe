# gui.py
import tkinter as tk
from tkinter import messagebox
from model import AlphaBetaPruning, is_winner

BOARD_SIZE = 3

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (Alpha-Beta)")
        self.state = ['-'] * 9
        self.game = AlphaBetaPruning(depth=9, game_state=self.state, player='X')  # AI = 'X', You = 'O'
        self.buttons = []
        self.status_var = tk.StringVar(value="Your turn (You = O). Click a cell.")
        self.build_ui()

    def build_ui(self):
        status = tk.Label(self.root, textvariable=self.status_var, font=("Segoe UI", 12))
        status.grid(row=0, column=0, columnspan=BOARD_SIZE, pady=(10, 6))

        grid_frame = tk.Frame(self.root)
        grid_frame.grid(row=1, column=0, padx=10, pady=10)

        for r in range(BOARD_SIZE):
            row_buttons = []
            for c in range(BOARD_SIZE):
                idx = r * BOARD_SIZE + c
                b = tk.Button(
                    grid_frame, text=" ", width=6, height=3,
                    font=("Segoe UI", 18, "bold"),
                    command=lambda i=idx: self.handle_player_move(i)
                )
                b.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(b)
                self.buttons.append(b)

        controls = tk.Frame(self.root)
        controls.grid(row=2, column=0, pady=(0, 10))
        tk.Button(controls, text="Restart", font=("Segoe UI", 11), command=self.reset).pack()

    def handle_player_move(self, idx):
        if self.state[idx] != '-' or self.is_game_over():
            return
        # Player move ('O')
        self.state[idx] = 'O'
        self.update_buttons()

        if is_winner(self.state, 'O'):
            self.end_game("You win! 🎉")
            return
        if '-' not in self.state:
            self.end_game("It's a draw.")
            return

        # AI move ('X')
        self.status_var.set("AI is thinking…")
        self.root.after(50, self.ai_move)  # slight delay for UI feel

    def ai_move(self):
        new_state = self.game.best_move(self.state[:])  # pass a copy
        if new_state is None:
            # No moves (shouldn't happen here), treat as draw
            self.end_game("It's a draw.")
            return
        self.state = new_state
        self.update_buttons()

        if is_winner(self.state, 'X'):
            self.end_game("AI wins! 🤖")
            return
        if '-' not in self.state:
            self.end_game("It's a draw.")
            return

        self.status_var.set("Your turn (You = O). Click a cell.")

    def update_buttons(self):
        for i, val in enumerate(self.state):
            self.buttons[i]['text'] = ' ' if val == '-' else val

    def end_game(self, msg):
        self.update_buttons()
        self.status_var.set(msg)
        # Disable all buttons
        for b in self.buttons:
            b['state'] = tk.DISABLED
        messagebox.showinfo("Game Over", msg)

    def is_game_over(self):
        return is_winner(self.state, 'O') or is_winner(self.state, 'X') or '-' not in self.state

    def reset(self):
        self.state = ['-'] * 9
        self.game = AlphaBetaPruning(depth=9, game_state=self.state, player='X')
        for b in self.buttons:
            b['state'] = tk.NORMAL
        self.update_buttons()
        self.status_var.set("Your turn (You = O). Click a cell.")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeGUI(root)
    root.resizable(False, False)
    root.mainloop()
