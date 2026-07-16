"""
进阶练习：订单数据分析 + CSV读写
综合运用：CSV读取、字典操作、多维度分组统计、CSV写入
"""

import csv

def load_orders(filename):
    """读取订单CSV文件，返回字典列表"""
    orders = []
    # TODO: 使用 csv.DictReader 读取文件
    # 注意：amount 和 price 是字符串，需要转换成整数
    with open(filename, newline='',mode="r",encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["amount"] = int(row["amount"])
            row["price"] = int(row["price"])
            orders.append(row)
    return orders

print("===== 第一步：读取订单数据 =====")
orders = load_orders("orders.csv")
print(f"成功读取 {len(orders)} 条订单")
for order in orders[:3]:  # 只打印前3条看看
    print(order)

print("\n===== 第二步：按城市分组统计 =====")
# TODO: 统计每个城市的订单数和总金额
city_stats = {}
for order in orders:
    order_city = order["city"]
    if order_city not in city_stats:
        city_stats[order_city] = {
            "cnt" : 1,
            "total" : order["amount"]*order["price"]
        }
    else:
        city_stats[order_city]["cnt"] += 1
        city_stats[order_city]["total"] += order["amount"]*order["price"]
print(f"城市统计: {city_stats}")

print("\n===== 第三步：按产品分组统计销量 =====")
# TODO: 统计每个产品的总销量
product_sales = {}
for pct in orders:
    product = pct["product"]
    if product not in product_sales:
        product_sales[product] = pct["amount"]
    else:
        product_sales[product] += pct["amount"]
print(f"产品销量: {product_sales}")

print("\n===== 第四步：找出金额最大的订单 =====")
# TODO: 找出金额最大的订单
max_revenue = 0
max_order = {}
for ods in orders:
    revenue = ods["amount"]*ods["price"]
    if revenue >= max_revenue:
        max_revenue = revenue
        max_order = ods
print(f"最大订单: {max_order}")

print("\n===== 第五步：把城市统计结果写入 city_stats.csv =====")
# TODO: 使用 csv.DictWriter 把 city_stats 写入文件
# 提示：先把 city_stats 转成适合写入的列表格式
list_city_stats = []
for city ,stat in city_stats.items():
    list_city_stats.append({
        "city" : city,
        "cnt" : stat["cnt"],
        "total" : stat["total"],
    }
                           )
fieldnames = ["city", "cnt", "total"]

with open("city_stats.csv", "w", newline='',encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(list_city_stats)
print("===== 分析完成，结果已保存！=====")

