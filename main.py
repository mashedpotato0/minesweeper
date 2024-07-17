import numpy as np
import tkinter as tk
from tkinter import messagebox


class MinesweeperGame:
    def __init__(self, rows=16, cols=32, num_mines=64):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.mainmap = np.zeros((self.rows, self.cols), dtype=int)
        self.state = np.full((self.rows, self.cols), 'hidden', dtype='<U10')
        self.generate_mines()
        self.calculate_adjacent_mines()

    def generate_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = np.random.randint(0, self.rows)
            col = np.random.randint(0, self.cols)
            if self.mainmap[row, col] == 0:
                self.mainmap[row, col] = -1
                mines_placed += 1

    def calculate_adjacent_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mainmap[row, col] == -1:
                    continue
                mine_count = 0
                for i in range(max(0, row - 1), min(self.rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.cols, col + 2)):
                        if self.mainmap[i, j] == -1:
                            mine_count += 1
                self.mainmap[row, col] = mine_count

    def reveal_cell(self, row, col):
        if self.state[row, col] == 'hidden':
            self.state[row, col] = 'revealed'
            if self.mainmap[row, col] == 0:
                for i in range(max(0, row - 1), min(self.rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.cols, col + 2)):
                        if self.state[i, j] == 'hidden':
                            self.reveal_cell(i, j)

    def flag_cell(self, row, col):
        if self.state[row, col] == 'hidden':
            self.state[row, col] = 'flagged'
        elif self.state[row, col] == 'flagged':
            self.state[row, col] = 'hidden'

    def display_map(self):
        display = np.full((self.rows, self.cols), ' ')
        for row in range(self.rows):
            for col in range(self.cols):
                if self.state[row, col] == 'hidden':
                    display[row, col] = '.'
                elif self.state[row, col] == 'flagged':
                    display[row, col] = 'F'
                elif self.state[row, col] == 'revealed':
                    if self.mainmap[row, col] == -1:
                        display[row, col] = 'M'
                    else:
                        display[row, col] = str(self.mainmap[row, col])
        for row in display:
            print(" ".join(row))


class MinesweeperGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.buttons = {}
        self.create_widgets()

    def create_widgets(self):
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                btn = tk.Button(self.master, width=2, command=lambda r=row, c=col: self.reveal(r, c))
                btn.bind("<Button-3>", lambda e, r=row, c=col: self.flag(r, c))
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

        reset_btn = tk.Button(self.master, text="Reset", command=self.reset_game)
        reset_btn.grid(row=self.game.rows, column=0, columnspan=self.game.cols, sticky="ew")

    def reveal(self, row, col):
        if self.game.state[row, col] in ('revealed', 'flagged'):
            return

        self.game.reveal_cell(row, col)
        self.update_buttons()

        if self.game.mainmap[row, col] == -1:
            messagebox.showinfo("Game Over", "You hit a mine!")
            self.master.destroy()

    def flag(self, row, col):
        self.game.flag_cell(row, col)
        self.update_buttons()

    def update_buttons(self):
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                btn = self.buttons[(row, col)]
                state = self.game.state[row, col]
                if state == 'hidden':
                    btn.config(text="", state="normal")
                elif state == 'flagged':
                    btn.config(text="F", state="normal")
                elif state == 'revealed':
                    if self.game.mainmap[row, col] == -1:
                        btn.config(text="M", state="disabled", disabledforeground="red")
                    else:
                        btn.config(text=str(self.game.mainmap[row, col]), state="disabled")

    def reset_game(self):
        self.master.destroy()
        root = tk.Tk()
        root.title("Minesweeper")
        game = MinesweeperGame()
        gui = MinesweeperGUI(root, game)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = MinesweeperGame()
    gui = MinesweeperGUI(root, game)
    root.mainloop()
