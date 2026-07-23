"""
题目：订单数据分析（pandas 新增列 + 排序 + 筛选）

数据文件：pandas_orders.csv
字段说明：order_id, city, product, amount, price, date

任务目标：
1. 读取 CSV 文件，生成 DataFrame。
2. 新增一列 total：表示每笔订单的总金额（= amount × price）。
3. 按 total 从高到低排序。
4. 筛选出 total > 5000 的订单，只展示 city、product、total 三列。

知识点提示：
- 新增列：df["新列名"] = df["列A"] * df["列B"]（整列批量运算）
- 排序：df.sort_values(by="列名", ascending=False)
  - ascending=True  → 从小到大（默认）
  - ascending=False → 从大到小
- 筛选 + 选列可以分步做，也可以链式写在一起
"""

import pandas as pd

# ========== 第 1 步：读取数据 ==========
df = pd.read_csv("pandas_orders.csv")

print("===== 原始数据 =====")
print(df)
print("\n")

# ========== 第 2 步：新增一列 total（amount × price） ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：一行搞定，df["total"] = ...
df["total"] = df["amount"] * df["price"]

# ========== 你需要写的逻辑到这里结束 ==========

print("===== 新增列后 =====")
print(df)
print("\n")

# ========== 第 3 步：按 total 从高到低排序 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：df = df.sort_values(...)
# 注意 ascending 参数
df = df.sort_values(by="total", ascending=False)

# ========== 你需要写的逻辑到这里结束 ==========

print("===== 按总金额从高到低排序 =====")
print(df)
print("\n")

# ========== 第 4 步：筛选 total > 5000，只展示 city、product、total ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   先筛选行：df[df["total"] > 5000]
#   再选列：[["city", "product", "total"]]
# 可以分两步写，也可以一行链式写
filter_df = df[df["total"]>5000]
result = filter_df[["city", "product", "total"]]

# ========== 你需要写的逻辑到这里结束 ==========

print("===== 总金额 > 5000 的订单 =====")
print(result)
