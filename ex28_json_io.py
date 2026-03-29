"""
题目：Ex28 - 处理 JSON 数据 (JSON I/O)

目标：学习如何将 Python 中的列表/字典保存为 .json 文件，并重新读取回来。

知识点预习：
在 Python 中，处理 JSON 需要先导入内置模块：`import json`

核心方法：
1. json.dump(数据, 文件对象)：将 Python 数据写入到文件中（保存为 JSON 格式）。
2. json.load(文件对象)：从文件中读取 JSON 数据，自动转换回 Python 的字典或列表。

注意：
写入包含中文的 JSON 时，建议加上 `ensure_ascii=False`，否则中文会被转码。
例如：json.dump(data, f, ensure_ascii=False, indent=4) # indent=4 可以让保存的文件自动换行缩进，更好看。

要求：
1) 写入 JSON：
   - 题目已经为您准备好了一个名为 `students_data` 的列表（里面嵌套了字典）。
   - 请完成 `save_to_json` 函数：将这个列表保存为名为 `students.json` 的文件。

2) 读取 JSON：
   - 请完成 `read_from_json` 函数：从 `students.json` 中读取数据，并返回读取到的列表。
   - 遍历读取到的列表，打印出每个学生的名字和分数。
"""

import json

# 准备好的模拟数据
students_data = [
    {"id": "S001", "name": "Alice", "score": 95, "skills": ["Python", "Math"]},
    {"id": "S002", "name": "Bob", "score": 88, "skills": ["Java", "Physics"]},
    {"id": "S003", "name": "张三", "score": 92, "skills": ["C++", "Chemistry"]}
]

def save_to_json(data, filename):
    """将传入的 data 保存到 filename 中"""
    # 1. 在这里写代码（记得使用 with open，并调用 json.dump）
    with open(filename,"w",encoding = "utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)



def read_from_json(filename):
    """从 filename 中读取 JSON 数据并返回"""
    # 2. 在这里写代码（记得使用 with open，并调用 json.load）
    with open(filename,"r",encoding="utf-8")as f:
        result = json.load(f)
        return result


if __name__ == "__main__":
    # 1. 保存数据
    print("--- 正在保存为 JSON ---")
    save_to_json(students_data, "students.json")
    
    # 2. 读取数据并打印
    print("--- 正在从 JSON 读取 ---")
    loaded_data = read_from_json("students.json")
    
    # 3. 验证数据类型
    print("\n读取到的数据类型是:", type(loaded_data))
    
    # 4. 遍历打印
    for stu in loaded_data:
        print(f"学生姓名: {stu['name']}, 分数: {stu['score']}")
