# 测试文档

## 1. 测试目标
验证贪吃蛇核心规则的正确性，避免逻辑回归。

## 2. 测试框架
- `unittest`（Python 标准库）

## 3. 测试用例列表
- `test_initial_state`：验证初始化状态（长度、方向、食物位置）
- `test_step_moves_forward`：验证正常前进一步
- `test_cannot_reverse_direction`：验证禁止 180 度反向
- `test_eat_food_grows_snake_and_scores`：验证吃食物后的增长与计分
- `test_wall_collision_ends_game`：验证撞墙判负
- `test_self_collision_ends_game`：验证撞自身判负

## 4. 执行命令
```powershell
C:\Users\gaope\python-sdk\python3.13.2\python.exe -m unittest discover -s tests -v
```

## 5. 最近一次测试结果
- 时间：2026-02-16
- 结果：`Ran 6 tests ... OK`
- 通过率：100%（6/6）
