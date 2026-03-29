# 题目：Ex17 - 字典推导式 (Dictionary Comprehension)
#
# 既然列表可以推导，字典当然也可以！
# 语法非常像，只是用花括号 {}，并且要写 key: value
#
# 语法示例：
# new_dict = {key: value for item in iterable if condition}

# 数据准备
numbers = [1, 2, 3, 4, 5]
scores = {'Alice': 85, 'Bob': 59, 'Charlie': 90, 'David': 60, 'Eve': 55}
lookup = {'a': 1, 'b': 2, 'c': 3}

def task1_square_dict(nums):
    """
    任务1：制作平方字典
    目标：返回 {1: 1, 2: 4, 3: 9, ...}
    提示：{n: n*n for n in nums}
    """
    # TODO: 请用字典推导式实现
    return {num:num**2 for num in nums}

def task2_pass_scores(score_dict):
    """
    任务2：筛选及格的学生 (>= 60)
    目标：返回 {'Alice': 85, 'Charlie': 90, 'David': 60}
    提示：{k: v for k, v in score_dict.items() if ...}
    """
    # TODO: 请用字典推导式实现
    return {k:v for k,v in score_dict.items() if v >= 60}

def task3_swap_lookup(lookup_dict):
    """
    任务3：键值对互换 (Key-Value Swap)
    目标：把 {'a': 1, ...} 变成 {1: 'a', ...}
    提示：{v: k for k, v in lookup_dict.items()}
    """
    # TODO: 请用字典推导式实现
    return {v:k for k,v in lookup_dict.items() }

if __name__ == "__main__":
    print("--- 任务1：平方字典 ---")
    print(task1_square_dict(numbers))
    
    print("\n--- 任务2：及格学生 ---")
    print(task2_pass_scores(scores))
    
    print("\n--- 任务3：键值互换 ---")
    print(task3_swap_lookup(lookup))
