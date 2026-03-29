"""
题目：Ex29 - 异常处理 (Exception Handling)

目标：学习如何使用 try...except 来让程序在遇到错误时不会直接崩溃，而是优雅地处理错误。

知识点预习：
在写代码时，很多时候我们会遇到不可预知的错误（比如：用户输入了字母而不是数字，或者我们要读取的文件不存在）。
如果不处理，程序就会直接报错退出（崩溃）。
我们可以用 try...except 块来“接住”这些错误：

语法结构：
try:
    # 尝试执行可能会报错的代码
    ...
except ValueError:
    # 如果发生了 ValueError（值错误，比如把 "abc" 转成整数），就执行这里的代码
    ...
except FileNotFoundError:
    # 如果发生了 FileNotFoundError（文件找不到），就执行这里的代码
    ...
except Exception as e:
    # 兜底：如果发生了其他任何未知的错误，接住它，并且把错误信息保存到变量 e 中
    print(f"发生了一个未知错误: {e}")
finally:
    # 无论有没有发生错误，最后都一定会执行的代码（通常用来清理资源）
    ...

要求：
请完成下面这个计算器函数 `safe_divide()`。
它接收两个字符串参数（模拟用户从键盘输入的内容），需要将它们转换为浮点数并相除。
您需要处理以下几种可能发生的错误：
1. 如果无法转换为浮点数（比如输入了 "abc"），捕获 ValueError，打印 "错误：请输入有效的数字！"
2. 如果除数为 0，捕获 ZeroDivisionError，打印 "错误：除数不能为 0！"
3. 如果计算成功，打印 "计算结果是：[结果]"
4. 无论成功还是失败，最后都要打印 "--- 此次计算结束 ---"
"""

def safe_divide(num1_str, num2_str):
    # 请在这里使用 try...except...finally 结构来完成要求
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = num1/num2
        print(f"计算结果是：{result}")
    except ValueError:
        print("错误，请输入有效的数字")
    except ZeroDivisionError:
        print("错误，除数不能为0")
    finally:
        print("----此次计算结束")


if __name__ == "__main__":
    # 测试用例 1：正常情况
    print("测试 1: 10 / 2")
    safe_divide("10", "2")
    print("\n")

    # 测试用例 2：除数为 0
    print("测试 2: 10 / 0")
    safe_divide("10", "0")
    print("\n")

    # 测试用例 3：输入了非数字
    print("测试 3: 10 / abc")
    safe_divide("10", "abc")
    print("\n")
