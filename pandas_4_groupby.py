"""
题目：订单分组统计（pandas groupby 入门）

数据文件：pandas_orders.csv
字段说明：order_id, city, product, amount, price, date

背景回顾：
你之前用字典手动做过"按部门分组统计"（ex33、ex34），
现在用 pandas 的 groupby，同样的事情一两行就能搞定。

任务目标：
1. 读取 CSV，新增 total 列（amount × price）。
2. 按 city 分组，统计每个城市的【订单数】和【总金额】。
3. 按 product 分组，统计每种商品的【平均单价】和【总销量（amount 之和）】。
4. 把城市统计结果转回字典列表，体会 DataFrame 和字典的互转换。

知识点提示：
- df.groupby("列名")  → 按该列分组，返回一个 GroupBy 对象
- .agg(统计方式)      → 对每组做聚合计算
  - "count"  → 计数（有几条）
  - "sum"    → 求和
  - "mean"   → 求平均
- 可以同时做多种聚合：.agg(["sum", "mean"])
- groupby 之后结果列名可能不够直观，可以用 rename() 重命名
"""

import pandas as pd

# ========== 第 1 步：读取数据 + 新增 total 列 ==========
df = pd.read_csv("pandas_orders.csv")
df["total"] = df["amount"] * df["price"]

print("===== 原始数据（含 total） =====")
print(df)
print("\n")

# ========== 第 2 步：按城市分组，统计订单数和总金额 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   第一步：city_group = df.groupby("city")
#   第二步：对 "total" 列做 agg，同时算 count 和 sum
#   例如：city_group["total"].agg(["count", "sum"])
#
# 注意：agg 返回的结果列名是 "count" 和 "sum"，不太直观
# 可以用 .rename(columns={"count": "order_count", "sum": "total_amount"}) 重命名
city_group = df.groupby("city")["total"].agg(["count","sum"])
city_stats = city_group.rename(columns = {"count":"order_count","sum":"total_amount"})

# ========== 你需要写的逻辑到这里结束 ==========

print("===== 按城市分组统计 =====")
print(city_stats)
print("\n")

# ========== 第 3 步：按商品分组，统计平均单价和总销量 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   按 "product" 分组
#   对 "price" 求 mean（平均单价）
#   对 "amount" 求 sum（总销量）
#
# 这次两列要分别做不同的聚合，写法是：
#   .agg({"列名1": "聚合方式1", "列名2": "聚合方式2"})
product_stats = df.groupby("product").agg({"price":"mean","amount":"sum"})



# ========== 你需要写的逻辑到这里结束 ==========

print("===== 按商品分组统计 =====")
print(product_stats)
print("\n")

# ========== 第 4 步：把 city_stats 转回字典列表 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：DataFrame → 字典列表用 .to_dict("records")
# 但 city_stats 的索引是城市名，不是普通列
# 需要先 .reset_index() 把索引变回普通列，再转

city_stats = city_stats.reset_index()
city_list = city_stats.to_dict("records")
# ========== 你需要写的逻辑到这里结束 ==========

print("===== 城市统计结果（字典列表形式） =====")
for item in city_list:
    print(item)
