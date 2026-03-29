"""
题目：Ex27 - 文件的读写操作 (File I/O)

目标：学习如何用 Python 创建文件、写入内容、并重新读取出来。

知识点预习：
在 Python 中，操作文件通常使用 `with open()` 语句。这叫“上下文管理器”，它的好处是：当你操作完文件后，它会自动帮你把文件关闭（就算中间报错了也会安全关闭）。

常见的文件模式 (mode)：
- "w" (write)：写入模式。如果文件不存在会创建，如果存在会【清空】原来的内容再写。
- "a" (append)：追加模式。如果文件不存在会创建，如果存在会在文件【末尾】接着写。
- "r" (read)：读取模式。只能读，不能写。（默认模式）

要求：
1) 写入文件：
   - 使用 "w" 模式打开一个名为 `my_diary.txt` 的文件。
   - 往里面写入两行文字（提示：写入换行需要自己加上 \n）：
     "这是我的第一篇日记。"
     "今天学习了 Python 的文件读写。"

2) 追加文件：
   - 使用 "a" 模式再次打开 `my_diary.txt`。
   - 往里面追加一行："继续加油！"

3) 读取文件：
   - 使用 "r" 模式打开 `my_diary.txt`。
   - 把里面的所有内容读取出来，并打印到控制台。
"""

def write_diary():
    # 1. 在这里写代码，用 "w" 模式写入前两行
    with open("./my_diary.txt","w",encoding="utf-8") as f:
        f.write("这是我的第一篇日记。\n今天学习了Python的文件读写")


def append_diary():
    # 2. 在这里写代码，用 "a" 模式追加一行
    with open("./my_diary.txt","a",encoding ="utf-8")as f:
        f.write("\n继续加油")



def read_diary():
    # 3. 在这里写代码，用 "r" 模式读取并打印全部内容
    with open("./my_diary.txt","r", encoding ="utf=8") as f:
        content = f.read()
        print(content)


if __name__ == "__main__":
    # 执行顺序
    print("--- 正在写入 ---")
    write_diary()
    
    print("--- 正在追加 ---")
    append_diary()
    
    print("--- 正在读取 ---")
    read_diary()
