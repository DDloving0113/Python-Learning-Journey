# 题目：Ex16 - Python 的“魔法”列表推导式 (List Comprehension)
#
# 以前我们写代码：
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n * 2)
#
# 现在用列表推导式，只需要一行：
# new_list = [n * 2 for n in numbers]
#
# 任务：请把下面三个“笨重”的循环代码，改写成“优雅”的列表推导式。

# 数据准备
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["alice", "bob", "charlie", "david"]

def task1_squares(nums):
    """
    任务1：计算平方
    目标：返回 [1, 4, 9, 16, ...]
    """
    # --- 原始代码 (供参考) ---
    # result = []
    # for n in nums:
    #     result.append(n * n)
    # return result
    
    # TODO: 请用列表推导式实现 (一行代码)
    # 提示：[n * n for n in nums]
    return [i**2 for i in nums]

def task2_evens(nums):
    """
    任务2：筛选偶数
    目标：返回 [2, 4, 6, 8, 10]
    语法提示：[n for n in nums if 条件]
    """
    # --- 原始代码 (供参考) ---
    # result = []
    # for n in nums:
    #     if n % 2 == 0:
    #         result.append(n)
    # return result

    # TODO: 请用列表推导式实现
    return [i for i in nums if i % 2 == 0]

def task3_upper_names(name_list):
    """
    任务3：名字转大写
    目标：返回 ['ALICE', 'BOB', ...]
    """
    # TODO: 请用列表推导式实现
    # 提示：字符串大写方法是 .upper()
    return [ustr.upper() for ustr in name_list]

if __name__ == "__main__":
    print("--- 任务1：平方 ---")
    print(task1_squares(numbers))
    
    print("\n--- 任务2：偶数 ---")
    print(task2_evens(numbers))
    
    print("\n--- 任务3：大写名字 ---")
    print(task3_upper_names(names))
