# 题目：
# 使用 filter 和 lambda 表达式完成以下任务：
# 1. 给定一个数字列表，过滤出所有的偶数。
# 2. 给定一个字符串列表，过滤出所有长度大于 3 的字符串。
# 3. 给定一个字典列表（用户数据），过滤出所有年龄大于 18 岁的用户。

# 数据准备
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["hi", "hello", "py", "python", "code", "ai"]
users = [
    {"name": "Alice", "age": 15},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 10},
    {"name": "David", "age": 25}
]

def filter_even_numbers(nums):
    """
    过滤出偶数
    提示：lambda x: x % 2 == 0
    """
    # 请在此处实现代码，使用 filter 和 lambda
    data = filter(lambda x: x % 2 == 0, nums)
    return list(data)

def filter_long_words(word_list):
    """
    过滤出长度大于 3 的单词
    提示：lambda x: len(x) > 3
    """
    # 请在此处实现代码
    len_3 = filter(lambda x:len(x)>3, word_list)
    return list(len_3)

def filter_adults(user_list):
    """
    过滤出年龄 > 18 的用户
    提示：lambda x: x["age"] > 18
    """
    # 请在此处实现代码
    adult_list = filter(lambda x: x["age"] > 18, user_list)
    return list(adult_list)

if __name__ == "__main__":
    # 1. 偶数
    evens = filter_even_numbers(numbers)
    # 注意：filter 返回的是迭代器，需要用 list() 转一下才能打印看到内容
    print(f"偶数列表: {(evens) if evens else '未实现'}")

    # # 2. 长单词
    long_words = filter_long_words(words)
    print(f"长单词: {(long_words) if long_words else '未实现'}")
    #
    # # 3. 成年人
    adults = filter_adults(users)
    print(f"成年人: {(adults) if adults else '未实现'}")
