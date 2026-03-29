# 1. 处理嵌套数据：
from operator import concat

users = [{"name":"Alice", "hobbies":["reading", "running"]}, {"name":"Bob", "hobbies":["gaming", "cooking"]}]
#打印 Alice 的第二个爱好
# 直接通过索引访问（适合确定Alice在列表第一个位置的情况）
alice_hobby = users[0]["hobbies"][1]
print("Alice hobby is :", alice_hobby)
# 遍历users
for user in users:
    if user["name"] == "Alice":
        print(user["hobbies"][1])



# 2. 用字典统计列表中各元素出现次数
list1 = ["apple", "banana", "apple", "orange", "banana", "apple"]
clean_list1 = [i.strip() for i in list1]
std_fruit = list(set(clean_list1))
# 方法一.遍历列表
dict_fruit={}
for i in clean_list1:
    if i not in dict_fruit:
        dict_fruit[i] = 1
    else :
        dict_fruit[i] += 1
print(dict_fruit)
# 方法二.字典推导式
dict_fruit2 = {i : clean_list1.count(i) for i in std_fruit}
# 小列表用字典推导式（方法 2）更简洁，大列表用循环（方法 1）更高效。



# 3. 合并两个字典：
# dict1 = {"a":1}, dict2 = {"b":2}，合并为 {"a":1, "b":2}
dict1 = {"a":1}
dict2 = {"b":2}
concat_dict = {**dict1, **dict2}
print(concat_dict)
concat_dict1 = dict1 | dict2
print(concat_dict1)




# 4.建议项目：编写 “单词统计工具”，接收用户输入的一段英文文本，统计每个单词出现的次数（忽略大小写，用空格分割单词）
# 步骤分解
def word_frequency_count():
    print("===单词统计工具===")
    text = input("请输入一段英文文本（按回车结束）：\n")
    # 统一小写
    lower_text = text.lower()
    # 空格来分隔单词
    raw_words = lower_text.split(" ")
    #  过滤掉分割后产生的空字符串（比如连续空格、首尾空格导致的空元素）
    clean_words = [word for word in raw_words if word.strip() != ""]
    frequency_dict = {}
    for word in clean_words:
        if word  in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    print("\n===统计单词结果===")
    if not frequency_dict:
        print("未检测到有效单词")
    else:
        sorted_words = sorted(frequency_dict.items(), key=lambda x:x[1], reverse=True)
        for key, value in sorted_words:
            print(f"单词：{key}， 出现{value}次")


        # 不解包的写法（效果和解包一样，但更麻烦）
        # for item in sorted_words:
        #     key = item[0]  # 取元组第一个元素（单词）
        #     value = item[1]  # 取元组第二个元素（次数）
        #     print(f"单词：{key}， 出现{value}次")


if __name__ == "__main__":
    word_frequency_count()

