"""
题目：Ex30 - 模块与导入 (Modules & Imports)

目标：学习如何将代码拆分到多个文件中，并在另一个文件里导入并使用它们。
同时，真正理解 `if __name__ == "__main__":` 到底有什么用。

知识点预习：
在 Python 中，每一个 `.py` 文件都是一个“模块 (Module)”。
如果你在 `A.py` 里写了一个好用的函数，你想在 `B.py` 里使用它，只需要在 `B.py` 开头写：
`import A`  或者  `from A import 某个函数`

要求：
我已经为您创建了另一个文件：`ex30_helper.py`。
那个文件里有两个现成的工具函数：`greet()` 和 `add_numbers()`。

请在这个文件（ex30_main.py）中：
1. 导入 `ex30_helper` 模块。
2. 使用导入的函数，给 "Alice" 打个招呼并打印出来。
3. 使用导入的加法函数，计算 10 + 20 并打印结果。
"""

# 1. 在这里写导入语句 (import)
import ex30_helper as hp

def run_main():
    # 2. 在这里调用导入的 greet 函数并打印
    print(hp.greet("Alice"))

    # 3. 在这里调用导入的 add_numbers 函数并打印
    print(hp.add_numbers(10,20))

if __name__ == "__main__":
    print("--- 启动主程序 ---")
    run_main()
