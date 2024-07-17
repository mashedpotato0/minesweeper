# Minesweeper Game

This is a simple implementation of the classic Minesweeper game using Python and Tkinter for the graphical user interface. 

## Features

- **Customizable Grid**: Default grid size is 16x32 with 64 mines.
- **Flagging**: Right-click to flag cells suspected to contain mines.
- **Automatic Revealing**: Reveals neighboring cells automatically when empty cells are clicked.
- **Reset Functionality**: Allows the game to be reset at any time.
- **Game Over and Winning Conditions**: Notifies the player when they hit a mine or successfully clear all non-mine cells.

## Requirements

- Python 3.x
- NumPy
- Tkinter (usually included with Python)



## How to Play

1. **Run the game**:
    ```bash
    python main.py
    ```

2. **Gameplay**:
    - Left-click on a cell to reveal it.
    - Right-click on a cell to flag or unflag it as a mine.
    - The game ends when you reveal a mine.
    - Reveal all non-mine cells to win the game.

## Code Overview

### `MinesweeperGame` Class

- **`__init__(self, rows=16, cols=32, num_mines=64)`**: Initializes the game with a grid and places mines randomly.
- **`generate_mines(self)`**: Places mines randomly on the grid.
- **`calculate_adjacent_mines(self)`**: Calculates the number of adjacent mines for each cell.
- **`reveal_cell(self, row, col)`**: Reveals the specified cell and recursively reveals neighboring cells if the cell is empty.
- **`flag_cell(self, row, col)`**: Flags or unflags the specified cell.
- **`display_map(self)`**: Prints the current state of the game grid to the console.

### `MinesweeperGUI` Class

- **`__init__(self, master, game)`**: Initializes the GUI with a grid of buttons corresponding to the game cells.
- **`create_widgets(self)`**: Creates the grid of buttons and the reset button.
- **`reveal(self, row, col)`**: Reveals the cell at the specified coordinates.
- **`flag(self, row, col)`**: Flags or unflags the cell at the specified coordinates.
- **`update_buttons(self)`**: Updates the text and state of the buttons based on the game state.
- **`reset_game(self)`**: Resets the game.

