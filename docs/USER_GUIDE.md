# User Guide

## 1. Prerequisites
- Python 3.x
- tkinter available (comes with standard Python on most desktop installs)

## 2. Start Game
Run in project root:
```bash
python3 snake_game.py
```

If you are in the provided Windows environment, you can also run:
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe snake_game.py
```

## 3. Controls
- Arrow Up: Move up
- Arrow Down: Move down
- Arrow Left: Move left
- Arrow Right: Move right
- `R`: Restart (after game over)

## 4. Rules
- Eat red food to grow and gain score.
- Hitting wall ends the game.
- Hitting snake body ends the game.
- Reversing direction directly is not allowed.
- Filling the entire board triggers game over after score updates (all cells occupied).

## 5. Run Tests
```bash
python3 -m unittest discover -s tests -v
```

## 6. Known Limitation
Automated tests focus on core logic. GUI rendering and manual play experience are verified by manually running the game.
