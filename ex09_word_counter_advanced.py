# 题目：Ex09 - 进阶单词计数器
#
# 给定一段英文文本，请完成以下步骤：
# 1. clean_text(text):
#    - 把所有单词转为“小写” (Hello -> hello)
#    - 去掉标点符号 (,.!?-等) -> 提示：可以用 replace 把标点变成“空格”
#    - 返回一个单词列表
#
# 2. count_words(word_list):
#    - 统计每个单词出现的次数
#    - 返回字典 {"hello": 5, "world": 3, ...}
#
# 3. get_top_3(word_counts):
#    - 找出出现频率最高的 3 个单词
#    - 返回列表 [("hello", 5), ("world", 3), ("test", 2)]

text = """
Python is an interpreted, high-level and general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use of significant indentation.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""

def clean_text(text):
    """
    1. 转小写
    2. 去掉标点 (比如 , . ! - ')
    3. 分割成列表
    """
    # 请在此处实现代码
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("'", "")
    text = text.replace("-", "")
    return text.split()


def count_words(word_list):
    """
    统计词频
    """
    # 请在此处实现代码
    count_dict = {}
    for word in word_list:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict

def get_top_3(word_counts):
    top_three = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)
    return top_three[:3]

if __name__ == "__main__":
    # 1. 清洗
    words = clean_text(text)
    print(f"清洗后的单词前10个: {words[:10] if words else 'None'}")

    # 2. 统计
    counts = count_words(words)
    print(counts)
    print(f"单词总数: {len(counts) if counts else 0}")
    #
    # # 3. Top 3
    top3 = get_top_3(counts)
    print(f"出现最多的3个词: {top3}")
