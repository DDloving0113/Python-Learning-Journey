# 1. 处理嵌套数据：users = [{"name":"Alice", "hobbies":["reading", "running"]}, {"name ":"Bob", "hobbies":["gaming", "cooking"]}]，打印 Alice 的第二个爱好
users = [{"name":"Alice", "hobbies":["reading", "running"]}, {"name":"Bob", "hobbies":["gaming", "cooking"]}]
def print_hobby(users_list, name, idx):
    for i in users_list:
        if i["name"] == name :
            if idx <= len(i["hobbies"])-1:
                print(i["hobbies"][idx])
            else:
                print("索引超范围")
            return
    print("no such user")
print_hobby(users,"Bob",1)

# 2. 用字典统计列表[" apple", "banana", "apple", "orange", "banana", "apple"]中各元素出现次数
list1 = [" apple", "banana", "apple", "orange", "banana", "apple"]
count_dict ={}
for i in list1:
    clean_item = i.strip()
    if clean_item in count_dict:
        count_dict[clean_item] += 1
    else:
        count_dict[clean_item] = 1
print(f"各元素出现次数", count_dict)
# 合并两个字典： dict1 = {"a":1}, dict2 = {"b":2}，合并为 {" a":1, "b":2}
# 方法一：
dict1 = {"a":1}
dict2 = {"b": 2}
dict_merge = {}
for i in dict1.keys():
    dict_merge[i] = dict1[i]
for i in dict2.keys():
    dict_merge[i] = dict2[i]
print(dict_merge)
# 方法二 ：** 解包两个字典，合并为新字典
dict_merge2 = {**dict1, **dict2}
print(dict_merge2)
# 方法三 : Python3.9+ 专属 | 运算符（最简洁）
dict_merge3 = dict1 | dict2
print(dict_merge3)
# 方法四 :  update 方法
dict_merge4 = dict1.copy()
dict_merge4.update(dict2)
print(dict_merge4)

# 建议项目：编写 “单词统计工具”，接收用户输入的一段英文文本，统计每个单词出现的次数（忽略 大小写，用空格分割单词）