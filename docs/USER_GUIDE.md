# User Guide

## 1. Prerequisites
- Windows
- Python 3.13 available at:
  `C:\Users\gaope\python-sdk\python3.13.2\python.exe`

## 2. Start Game
Run in project root:
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe snake_game.py
```

## 3. Controls
- Arrow Up: Move up
- Arrow Down: Move down
- Arrow Left: Move left
- Arrow Right: Move right
- `R`: Restart after game over

## 4. Rules
- Eat red food to grow and gain score.
- Hitting wall ends the game.
- Hitting snake body ends the game.
- Reversing direction directly is not allowed.

## 5. Run Tests
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe -m unittest discover -s tests -v
```

## 6. Known Limitation
Automated tests focus on game logic. GUI rendering and manual play experience are verified by manual run.
