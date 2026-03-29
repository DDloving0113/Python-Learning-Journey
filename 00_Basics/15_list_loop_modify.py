# 练习题 1：基础循环 + 列表 - 批量修改数值
# 题目要求
# 给定数字列表
nums = [3, 7, 9, 12, 15, 18]
# 通过循环完成：
# 将列表中所有大于 10 的数字乘以 2；
q1_num = []
q2_num = []
for num in nums:
    q1_num.append(2*num)
print(q1_num)
# 小于等于 10 的数字保持不变；
for num in nums:
    if num <= 10:
        q2_num.append(num)
    else:
        q2_num.append(2*num)
print(q2_num)



# 题目要求
# 给定商品价格字典
prices = {"苹果": 5, "香蕉": 3, "橙子": 4, "草莓": 15, "西瓜": 8}
# 通过循环完成：
# 筛选出价格≥8 的商品；
dict_filter = {}
for key, value in prices.items():
    if value >= 8:
        dict_filter[key] = value
print(dict_filter)


# 练习题 3：循环 + 集合 - 找列表中重复的元素
# 题目要求
# 给定列表
count_dict = {}
words = ["cat", "dog", "cat", "bird", "dog", "fish", "cat"]
for word in words:
    if word not in count_dict:
        count_dict[word] = 1
    else:
        count_dict[word] += 1
print(count_dict)
# 通过循环 + 集合完成：
# 找出列表中重复出现的元素（只显示一次）；
# 输出重复元素的集合。
singelnum_list = []
for key, value in count_dict.items():
    if value >= 2:
        singelnum_list.append(key)
print(singelnum_list)

# 方法二：第一次遍历的放集合A，2次以上遍历的放集合B
first_seen = set()
duplicate_set = set()
for word in words:
    if word not in first_seen:
        first_seen.add(word)
    else:
        duplicate_set.add(word)
print(f'重复的元素包括：{duplicate_set}')

# 练习题 4：嵌套循环 + 嵌套列表 - 二维列表求和
# 题目要求
# 给定二维数字列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ，通过嵌套循环完成：
# 计算二维列表中所有数字的总和；
# 计算每一行的和，生成 “行和列表”。
sum_list = []
for list1 in matrix :
    sum_list.append(sum(list1))
print(sum(sum_list))

# 练习题 5：循环 + 字典 + 列表 - 统计用户行为
# 题目要求
# 给定用户行为日志列表
logs = [ {"user": "user1", "action": "login"}, {"user": "user2", "action": "logout"}, {"user": "user1", "action": "view"}, {"user": "user2", "action": "login"}, {"user": "user1", "action": "login"}, {"user": "user3", "action": "login"} ]
# 统计每个用户的操作次数（字典：用户→次数）；
log_dict = {}
for log in logs :
        log_dict[log["user"]]= log_dict.get(log["user"],0)+1
print(log_dict)
# 统计每种操作的次数（字典：操作→次数）
operation_dict = {}
for log in logs :
        operation_dict[log["action"]]= log_dict.get(log["action"],0)+1
print(operation_dict)
# get() 的正确用法：字典.get(键, 默认值) 是 “取值”，不是 “赋值”，需结合赋值语句使用；
# 新手可先写 if-else 理清逻辑，熟练后用 get() 简化代码（一行搞定计数）
# if-else方法
log_dict1 = {}
for log in logs :
    if log["user"] not in log_dict1:
        log_dict1[log["user"]] = 1
    else:
        log_dict1[log["user"]] += 1
print(log_dict1)

# 练习题 6：循环 + 数据结构综合 - 模拟购物车结算
# 题目要求
# 给定购物车列表
cart = [
    {"name": "牛奶", "price": 6, "count": 2, "discount": 0.9},
    {"name": "面包", "price": 4, "count": 3, "discount": 1.0},
    {"name": "鸡蛋", "price": 1, "count": 10, "discount": 0.8}
]
# 计算每个商品的折后总价（单价 × 数量 × 折扣）；
goods_dict = {}
for cart in cart :
    goods_dict[cart["name"]] = goods_dict.get(cart["name"],cart["count"]*cart["price"]*cart["discount"])
print(goods_dict)
# 计算购物车总金额；
good_sum = 0
for goods in goods_dict :
    good_sum += goods_dict[goods]
print(good_sum)
# 筛选出折后总价≥10 的商品，生成 “高价商品列表”。
high_price_good = []
for  goods in goods_dict :
    if goods_dict[goods] >= 10 :
        high_price_good.append(goods)
print(high_price_good)


