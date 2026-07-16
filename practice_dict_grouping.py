"""
练习：字典操作与分组统计（独立完成练习）

任务1：复习字典的 3 种遍历方式
任务2：分组统计练习
"""

print("===== 练习1：字典遍历 =====")

# 给你一个销售数据字典
sales_data = {
    "2026-07-01": {"product": "苹果", "amount": 100, "price": 5.5},
    "2026-07-02": {"product": "香蕉", "amount": 150, "price": 3.0},
    "2026-07-03": {"product": "苹果", "amount": 200, "price": 5.5},
    "2026-07-04": {"product": "橙子", "amount": 80, "price": 4.0},
    "2026-07-05": {"product": "香蕉", "amount": 120, "price": 3.0},
}

# TODO: 1. 使用 for key in dict 遍历，计算每天的销售额（amount * price），并打印出来

for date in sales_data:
    revenue = sales_data[date]["price"]*sales_data[date]["amount"]
    print(f"日期：: {date},当天营业额: {revenue}")
# TODO: 2. 使用 for key, value in dict.items() 遍历，做同样的事情
for date,info in sales_data.items():
    revenue = info["price"]*info["amount"]
    print(f"日期：{date},当天营业额: {revenue}")

print("\n===== 练习2：按产品分组统计 =====")

# TODO: 统计每种产品的总销量
# 目标结果：{"苹果": 300, "香蕉": 270, "橙子": 80}
product_stats = {}
for fruits in sales_data.values():
    if fruits["product"] not in product_stats:
        product_stats[fruits["product"]] = fruits["amount"]
    else:
        product_stats[fruits["product"]] += fruits["amount"]

print(f"产品总销量统计: {product_stats}")

print("\n===== 练习3：把字典的值转成列表 =====")

# TODO: 把 sales_data 的值转成列表，然后遍历打印每一条记录
sales_list = list(sales_data.values())
for record in sales_list:
    print(record)

print("\n===== 练习完成！=====")
