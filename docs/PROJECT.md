# 项目文档（Python 贪吃蛇）

## 1. 项目简介
本项目实现了一个基于 Python 标准库 `tkinter` 的桌面贪吃蛇游戏，包含：
- 可交互图形界面
- 完整的核心规则（移动、吃食物、成长、碰撞判负）
- `unittest` 自动化测试

## 2. 目录结构
- `snake_game.py`：游戏主程序（核心逻辑 + GUI）
- `tests/test_snake_game.py`：核心逻辑单元测试
- `docs/PROJECT.md`：项目说明
- `docs/USER_GUIDE.md`：用户使用文档
- `docs/TESTING.md`：测试说明
- `docs/COVERAGE.md`：覆盖率说明

## 3. 功能清单
- 方向键控制蛇移动
- 食物随机生成（不会刷到蛇身上）
- 吃到食物后：分数 +1，蛇长度 +1
- 禁止 180° 反向移动
- 撞墙判负
- 撞自身判负
- 棋盘填满后自动结束（视为通关）
- 游戏结束后按 `R` 键重开

## 4. 技术栈
- Python 3
- tkinter（标准库 GUI）
- unittest（标准库测试框架）
- trace（标准库覆盖率统计）

## 5. 快速运行
```bash
python3 snake_game.py
```

Windows 环境可使用：
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe snake_game.py
```
