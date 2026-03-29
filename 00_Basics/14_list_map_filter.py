# 练习题 1：列表进阶 - 批量修改 + 筛选
# 题目要求
# 给定数字列表
nums = [12, 5, 8, 23, 18, 3, 35, 9]
# 将列表中所有小于 10 的数字乘以 2；
nums = [i*2 for i in nums if i <10]
print(nums)
# 筛选出修改后大于等于 15 的数字，生成新列表；
new_list = [i for i in nums if i >= 15]
print(new_list)
sorted_list = sorted(new_list , reverse = True)
print(sorted_list)
# 对新列表按从大到小排序。
# 解题思路
# 遍历列表，用条件判断修改数字；
# 列表推导式筛选符合条件的元素；
# sorted() 加 reverse=True 降序排序。



# 练习题 2
# 给定学生信息字典（嵌套结构）：
students = {
    "001": {"name": "小明", "score": {"语文": 85, "数学": 92}},
    "002": {"name": "小红", "score": {"语文": 90, "数学": 88}},
    "003": {"name": "小刚", "score": {"语文": 78, "数学": 80}}
}
# 完成：
# 统计每个学生的总分（语文 + 数学），添加到对应学生字典中；
# 方法一：遍历
# for num, info in students.items():
#     # 第一步：先初始化total为0（关键！避免KeyError）
#     info["total"] = 0  # 等价于 students[num]["total"] = 0
#     for k , v in info.items():
#         if k == "score":
#             for subject in v.values():
#                 info["total"] += subject
# print(students)
# 方法二 ；求和
for num, info in students.items():
    # 直接取score字典的所有值，求和后赋值给total
    total_score = sum(info["score"].values())
    info["total"] = total_score  # 添加总分键

print(students)
# 找出总分最高的学生（输出：总分最高的学生：小红，总分：178）
score_list = list(students.values())
sort_list = sorted(score_list, key = lambda x: x["total"], reverse = True )
print(f"总分最高的学生： {sort_list[0]['name']}, 总分 ：{sort_list[0]['total']}")
# 用max()结合lambda找总分最高的学生





# 练习题 3：集合 + 列表 - 找 “只出现一次” 的元素
# 题目要求
words = ["cat", "dog", "cat", "bird", "dog", "fish", "rabbit"]  #找出列表中只出现一次的元素（去重显示）。
word_dict = {}
for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1
print(word_dict)

animal_list = []
for k,v in word_dict.items():
    if v == 1:
        animal_list.append(k)
print(set(animal_list))
# 解题思路
# 先用字典统计每个元素的出现次数；
# 再用集合 / 列表筛选出次数为 1 的元素；
# 集合去重（确保结果不重复）。

# 练习题 4：列表 + 字典 - 模拟购物车结算
# 题目要求
# 给定购物车列表（每个元素是商品字典）：
cart = [
    {"name": "牛奶", "price": 5, "count": 2},
    {"name": "面包", "price": 3, "count": 3},
    {"name": "鸡蛋", "price": 1, "count": 10}
]
# 完成：
# 计算每个商品的总价（单价 × 数量），添加到商品字典；
for goods in cart:
    goods["revenue"] = goods["price"] * goods["count"]
print(cart)
# 计算购物车总金额；
cart_sum = []
for goods in cart:
    cart_sum.append(goods["revenue"])
total_revenue = sum(cart_sum)
print(total_revenue)
# 筛选出总价≥10 的商品
good_names = []
for goods in cart:
    if goods["revenue"] >= 10:
        good_names.append(goods["name"])
        print(goods["name"],end= " ")

# 练习题 5：集合进阶 - 找 “对称差集”（只在 A 或只在 B 中）
hobby1 = ["reading", "running", "gaming", "cooking"]
hobby2 = ["gaming", "swimming", "cooking", "hiking"]
# 找出只在 hobby1 或只在 hobby2 中出现的爱好（即 “非共同爱好”）。
# 解题思路
# 集合的「对称差集」（^ 或 symmetric_difference()）：只在 A 或只在 B 中，不同时在两者中；
# 对称差集 = 并集 - 交集


s1 = set(hobby1)
s2 = set(hobby2)
dif_list =list(s1^s2)
print(dif_list)
# # 方法2：等价写法（并集 - 交集）
# # unique_hobby = (s1 | s2) - (s1 & s2)

# 练习题 6：综合实战 - 清洗并统计日志数据
# 题目要求
# 给定日志数据列表（包含无效数据、重复数据）：
logs = [
    "user1,login,2026-01-01",
    "user2,logout,2026-01-01",
    "user1,login,2026-01-01",
    "",
    "user3,login,2026-01-02",
    "  user2,login,2026-01-02  ",
    "user4,,2026-01-02"
]
# 完成：
# 清洗数据：过滤空行、去掉首尾空格、过滤 “操作字段为空” 的日志；
clean_logs = []
for log in logs:
    log_strip = log.strip()
    if not log_strip :
        continue
    split_log = log_strip.split(",")
    if len(split_log)>=2 and split_log[1]!= "":
        clean_logs.append(split_log)
print(clean_logs)
print("==================")
# 按 “用户名” 为键，统计每个用户有多少不唯一的日期；
# 方案 1：新手友好版（先存集合去重，再统计长度）
# 核心思路：
# 外层字典的键是 log[0]（用户名），值是「存储该用户日期的集合」（利用集合去重）；
# 遍历日志，把每个用户的日期 log[2] 加入对应集合（自动去重）；
# 最后遍历字典，获取每个集合的长度（就是唯一日期的数量）
manipulate_times = {}
for log in clean_logs:
    name = log[0]
    date_log = log[2]
    if name not in manipulate_times:
        manipulate_times[name] = set()
    manipulate_times[name].add(date_log)
sum_dict = {}
for name,time_log in manipulate_times.items():
    sum_dict[name] = len(time_log)
print(sum_dict)

# 方案 2：简洁版（一步到位，直接统计唯一数量）
# 核心思路：利用列表推导式提取每个用户的所有日期，再转集合去重后统计长度，代码更简洁
user_list = set(log[0]for log in clean_logs )
user_dic = {}
for user in user_list:
    log_list = set([log[2]for log in clean_logs if log[0]==user])
    user_dic[user] = len(log_list)
print(user_dic)