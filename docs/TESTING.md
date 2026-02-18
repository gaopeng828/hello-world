# 测试文档

## 1. 测试目标
验证贪吃蛇核心规则正确性，避免逻辑回归。

## 2. 测试框架
- `unittest`（Python 标准库）

## 3. 测试用例列表
- `test_board_too_small_raises_error`：棋盘尺寸下限校验
- `test_initial_state`：初始化状态（长度、方向、食物位置）
- `test_step_moves_forward`：正常前进一步
- `test_cannot_reverse_direction`：禁止 180° 反向
- `test_eat_food_grows_snake_and_scores`：吃食物后增长与计分
- `test_wall_collision_ends_game`：撞墙判负
- `test_self_collision_ends_game`：撞自身判负
- `test_fill_last_cell_triggers_game_over`：填满最后空格后的结束逻辑

## 4. 执行命令
```bash
python3 -m unittest discover -s tests -v
```

## 5. 最近一次测试结果
- 结果：`Ran 8 tests ... OK`
- 通过率：100%（8/8）
