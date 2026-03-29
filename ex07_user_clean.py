users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": ""},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "", "age": 28},
]

# 要求：
# 1. 写函数 clean_users(users)：
#    - 过滤掉姓名为空或年龄为空的记录
#    - 返回有效用户列表
# 2. 写函数 dedup_users(users)：
#    - 把“姓名 + 年龄”完全相同的视为重复，只保留一条
#    - 返回去重后的列表
# 3. 写函数 sort_users_by_age(users)：
#    - 按年龄从小到大排序，返回排序后的列表
# 主程序中组合调用三个函数，输出最终“干净并按年龄排序”的用户列表。

def clean_users(users):
    temp_list = []
    for i in users:
        if i["name"] != "" and i["age"] != "":
            temp_list.append(i)
    return temp_list

def dedup_users(users):
    # 请在此处实现代码
    temp_list = []
    for i in users:
        if i in temp_list:
            continue
        else:
            temp_list.append(i)
    return temp_list

def sort_users_by_age(users):
    # 请在此处实现代码
    users.sort(key=lambda x: x["age"])
    return users

if __name__ == "__main__":
    # 在这里调用函数并打印结果
    clean_data = clean_users(users)
    dedup_data = dedup_users(clean_data)
    sorted_data = sort_users_by_age(dedup_data)