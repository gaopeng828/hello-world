# 测试覆盖率文档

## 1. 覆盖率统计方式
使用 Python 标准库 `trace` 统计行覆盖率。

## 2. 执行命令
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe -m trace --count --summary -C .trace --module unittest discover -s tests -v
```

## 3. 覆盖率结果（核心文件）
- `snake_game.py`：84 lines, 100%
- `tests/test_snake_game.py`：43 lines, 100%

> 说明：`trace` 输出会包含 Python 标准库模块，本文档仅关注项目内核心文件。

## 4. 覆盖范围说明
当前覆盖了游戏核心逻辑：
- 初始化
- 移动
- 方向切换约束
- 吃食物增长
- 撞墙与撞自身

## 5. 未覆盖项
- `tkinter` 图形界面渲染行为（`Canvas` 绘制、事件循环）
- 人机交互体验（手工测试项）
