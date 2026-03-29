# 题目：Ex18 - 数据清洗流水线 (The Data Refinery)
#
# 在现实世界中，数据通常是“脏”的：格式不统一、有空格、有缺失值。
# 你的任务是使用“列表推导式”和“字典推导式”构建一个数据清洗流水线。
#
# 原始数据 (raw_data) 是一个字符串列表，格式混乱：
# "  Alice: 85 ", "bob: 59", "  Charlie: 90", "david: 60 ", "Eve: ??"

import pprint

raw_data = [
    "  Alice: 85 ",
    "bob: 59",
    "  Charlie: 90",
    "david: 60 ",
    "Eve: ??",
    "Frank: 75",
    "  grace: 88 "
]

def clean_data(data_list):
    """
    步骤 1: 基础清洗
    目标：
    1. 去除字符串两端的空格 (.strip())
    2. 忽略包含 "??" 的无效数据
    3. 将剩下的字符串按 ": " 分割
    
    返回列表：[['Alice', '85'], ['bob', '59'], ...]
    提示：使用列表推导式，配合 if 条件
    """
    # TODO: 请实现
    # 1. 使用 data_list 参数而不是 raw_data 全局变量
    # 2. 加上 if 条件过滤掉 "??"
    # 3. 使用 split(": ") 处理分割后的空格
    return [item.strip().split(": ") for item in data_list if "??" not in item]

def format_data(cleaned_list):
    """
    步骤 2: 格式化与转换
    目标：
    1. 将名字转为首字母大写 (.title())
    2. 将分数转为整数 (int())
    3. 构建字典 {名字: 分数}
    
    返回字典：{'Alice': 85, 'Bob': 59, ...}
    提示：使用字典推导式 {name.title(): int(score) for name, score in ...}
    """
    # TODO: 请实现
    # 使用 .title() 让名字首字母大写 (如 Bob)，而不是全大写 (BOB)
    # 使用 name, score = item 解包会让代码更易读
    return {item[0].title(): int(item[1]) for item in cleaned_list}

def filter_high_scores(score_dict, threshold=80):
    """
    步骤 3: 筛选高分
    目标：返回分数 >= threshold 的学生字典
    """
    # TODO: 请实现 (字典推导式)
    # 修正：这是一个集合推导式 {val}，我们需要的是字典推导式 {key: val}
    # 并且判断条件应该放在后面 if
    return {k: v for k, v in score_dict.items() if v >= threshold}

if __name__ == "__main__":
    print("--- 原始数据 ---")
    pprint.pprint(raw_data)
    
    # 1. 基础清洗
    step1 = clean_data(raw_data)
    print("\n--- 1. 清洗后 (列表) ---")
    pprint.pprint(step1)
    
    # 2. 格式化
    step2 = format_data(step1)
    print("\n--- 2. 格式化后 (字典) ---")
    pprint.pprint(step2)
    
    # 3. 筛选高分
    step3 = filter_high_scores(step2, 80)
    print("\n--- 3. 高分学生 (>=80) ---")
    pprint.pprint(step3)
