# 练习题 1：列表基础 - 筛选并排序数字
# 题目要求
# 给定一个包含数字和空值的列表 nums = [15, '', 8, 32, '', 9, 21, '', 5]，完成两个操作：
# 过滤掉列表中的空字符串 ''；
# # 将过滤后的数字列表按从小到大排序。

nums = [15, '', 8, 32, '', 9, 21, '', 5]
clean_num = [i for i in nums if i != '']
sort_num = sorted(clean_num)
print(sort_num)


# 练习题 2：字典基础 - 整理学生成绩
# 题目要求
# 给定一个学生成绩的原始数据（姓名：分数）：{"小明": 85, "小红": 92, "小刚": 78, "小丽": 92}，
# 统计分数为 90 分及以上的学生，生成新字典；
# 输出每个高分学生的姓名和分数（格式：小红：92分）。


stu_dict = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 92}
new_stu = {}
for key, value in stu_dict.items():
    if value > 90:
        new_stu[key] = value
for key, value in new_stu.items():
    print(f"{key}: {value}分")

# 解题思路
# 遍历原字典的键值对，用条件判断筛选高分；
# 字典推导式快速生成新字典

# 练习题 3：集合基础 - 找两个列表的共同元素
# 题目要求
# 给定两个爱好列表：
hobby1 = ["reading", "running", "gaming", "cooking"]
hobby2 = ["gaming", "swimming", "cooking", "hiking"]
# 找出两个列表中共同的爱好（去重且不重复显示）。
# 解题思路
# 列表转集合（自动去重，且集合支持 “交集” 操作）；
common_hobby = set(hobby1)&set(hobby2)
print(common_hobby)
# 用 & 或 intersection() 找两个集合的共同元素，|符合是并集

# 练习题 4：列表 + 字典综合 - 统计商品销量
# 题目要求
# 给定商品销售记录列表
sales = ["苹果", "香蕉", "苹果", "橙子", "香蕉", "苹果", "香蕉", "橙子", "橙子", "橙子"]
# 用字典统计每个商品的销量；
fruit_dict = {}
for i in sales:
    if i in fruit_dict:
        fruit_dict[i] += 1
    else:
        fruit_dict[i] = 1

# 方法二  fruit_dict[i] = fruit_dict.get(i, 0) + 1
# 1. 先查字典里有没有 i 这个键；
# 2. 如果有，取它的值（比如 3）；如果没有，取默认值 0；
# 3. 把值 + 1，再赋给 fruit_dict[i]。



# 找出销量最高的商品（输出：销量最高的商品是：橙子，销量：4）
# .items()的方法
max_product = max(fruit_dict.items(),key=lambda x: x[1])
print(f"销量最高的商品是:{max_product[0]},销售:{max_product[1]}")


# 练习题 5：列表 + 字典 + 集合综合 - 清洗用户数据
# 题目要求
# 给定用户数据列表（包含重复和无效数据）：
users = [ {"name": "Alice", "age": 25}, {"name": "Bob", "age": ""}, {"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}, {"name": "", "age": 28} ]
# 完成：
# 过滤掉「姓名为空」或「年龄为空」的无效用户；
valid_user = []
for user in users:
    if user["age"] != "" and user["name"] != "":
        valid_user.append(user)
print(valid_user)
# 去重（姓名和年龄都相同的视为重复用户）；
# 步骤2：去重（将字典转元组存入集合，再转回字典）
# 元组是可哈希的，能存入集合；字典不可哈希，需转换
# 你可能会问：为什么不直接把用户字典加入集合？
# 集合要求里面的元素必须是「可哈希（不可变）」的，而字典（dict）是「可变类型」，不能直接加入集合（会报错 TypeError: unhashable type: 'dict'）；
# 元组（tuple）是「不可变类型」，可以作为集合的元素，所以我们把字典里的关键信息（姓名 + 年龄）拼成元组，再加入集合实现去重。
user_set  = set()
unique_user_list = []
for user in valid_user:
    info =(user["name"], user["age"])
    if info not in user_set:
        user_set.add(info)
        unique_user_list.append(user)
print(unique_user_list)
# 将最终的有效用户按年龄从小到大排序。

sorted_users = sorted(unique_user_list, key=lambda x: x["age"])
print(sorted_users)


