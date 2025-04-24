# Tetris2048

# Tetris 2048 🎮🧩

A unique puzzle game that blends the mechanics of **Tetris** and **2048** into a single, fun, and challenging experience.

## 🔍 Game Concept

- **Tetris** mechanics: Move, rotate, and drop tetrominoes onto the grid.
- **2048** mechanics: Each tile within a tetromino has a number (2 or 4). When tiles with the same number collide vertically, they merge into one with double the value.
- Score is calculated by:
  - The value of merged tiles (like in 2048).
  - The total value of cleared rows (like in Tetris).
- The game ends if a tile lands above the top of the grid, or it is won when a tile reaches 2048.

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬅️   | Move left |
| ➡️   | Move right |
| ⬇️   | Soft drop |
| ⬆️   | Rotate clockwise |

## 🖥️ Requirements

- Python 3.10 or higher
- `pygame` library

Install with:
pip install pygame

-----------------------------------------------------

🚀 How to Run:

Clone the repo and run the game:
git clone https://github.com/sude-1/Tetris2048
cd Tetris2048
python main.py


------------------------------------------------------

🧱 Features

Smooth animations with colorful tiles

Merging logic based on 2048

Row-clearing logic based on Tetris

Score tracking and game over screen

Custom fonts and themes

-------------------------------------------------------

📁 Project Structure

Tetris2048/
├── main.py             # Game loop and rendering
├── grid.py             # Grid management, merging and line clearing
├── tetromino.py        # Tetromino class and rotation logic
├── settings.py         # Constants and configuration
├── assets/             # (Optional) Fonts, images, etc.
└── README.md

--------------------------------------------------------

🧡 Author
Hatice Sude
GitHub: @sude-1

Enjoy the game and feel free to fork, star ⭐ and contribute!

