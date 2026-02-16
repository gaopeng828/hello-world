# 项目文档（Snake Game）

## 1. 项目简介
本项目新增了一个使用 Python 开发的贪吃蛇小游戏，采用 `tkinter` 实现图形界面，采用 `unittest` 实现自动化测试。

## 2. 目录结构
- `snake_game.py`：游戏主程序（核心逻辑 + GUI）
- `tests/test_snake_game.py`：单元测试
- `docs/PROJECT.md`：项目文档
- `docs/TESTING.md`：测试文档
- `docs/COVERAGE.md`：覆盖率文档
- `docs/USER_GUIDE.md`：用户手册

## 3. 技术栈
- Python 3.13
- tkinter（标准库 GUI）
- unittest（标准库测试框架）
- trace（标准库覆盖率统计）

## 4. 功能清单
- 蛇的移动（方向键控制）
- 食物随机生成
- 吃到食物后长度增长、分数加一
- 禁止反向移动
- 撞墙判负
- 撞自身判负
- `R` 键重开

## 5. 运行方式
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe snake_game.py
```
