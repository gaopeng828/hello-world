# AGENT.md

## 本次实践注意事项（2026-02-16）

## 1. Python 解释器与启动注意
- 可用 Python 解释器（已验证可执行）：
  - `C:\Users\gaope\python-sdk\python3.13.2\python.exe`
- `python` 命令默认指向：
  - `C:\Users\gaope\AppData\Local\Microsoft\WindowsApps\python.exe`
  - 该路径在当前环境下不可直接用于运行测试（会报无法访问）。
- `py -3` 在当前环境下不可用（提示未安装 Python）。

## 2. 本项目推荐命令
- 运行游戏：
  - `C:\Users\gaope\python-sdk\python3.13.2\python.exe snake_game.py`
- 运行单元测试：
  - `C:\Users\gaope\python-sdk\python3.13.2\python.exe -m unittest discover -s tests -v`
- 统计覆盖率（标准库 trace）：
  - `C:\Users\gaope\python-sdk\python3.13.2\python.exe -m trace --count --summary -C .trace --module unittest discover -s tests -v`

## 3. Python 标准库位置（已验证）
- Python 标准库根目录：
  - `C:\Users\gaope\python-sdk\python3.13.2\Lib`
- 本项目用到的标准库模块（无需 pip 安装）：
  - `tkinter`（GUI）
  - `unittest`（测试）
  - `trace`（覆盖率统计）
  - `dataclasses`、`enum`、`typing`、`random`

## 4. Git 与提交流程注意
- 提交前建议排除临时文件：`__pycache__/`、`*.pyc`。
- 当前仓库已使用本地 git 身份配置：
  - `user.name=gaopeng828`
  - `user.email=gaopeng828@users.noreply.github.com`
- 在受限网络环境下，`git push` 可能失败；需要在允许联网后重试。

## 5. 文档与代码位置
- 游戏主程序：`snake_game.py`
- 测试代码：`tests/test_snake_game.py`
- 文档目录：`docs/`
  - `docs/PROJECT.md`
  - `docs/TESTING.md`
  - `docs/COVERAGE.md`
  - `docs/USER_GUIDE.md`
