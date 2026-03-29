"""
这是 Ex30 的被导入模块（助手文件）。
在这个文件里，我们定义一些好用的工具函数。
"""

def greet(name):
    """打招呼函数"""
    return f"Hello, {name}! Welcome to Python Modules."


def add_numbers(a, b):
    """加法函数"""
    return a + b


# 思考题：如果不加这行 if __name__ == "__main__":，
# 下面的测试代码在被别人 import 的时候会自动运行吗？
if __name__ == "__main__":
    print("【内部测试】模块 ex30_helper 运行正常！")
    print(greet("TestUser"))
