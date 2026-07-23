"""
题目：奶茶店多表合并分析（pandas merge / concat 入门）

项目背景：
你是一家连锁奶茶店的运营助理。总部给你两份数据：
1. sales.csv  —— 各门店每日销售记录（字段：sale_id, store_id, date, product, quantity, unit_price）
2. stores.csv —— 门店基本信息（字段：store_id, store_name, city, area_sqm, open_year）

你需要用 pandas 把两张表合并在一起，然后做分析。

任务目标：
1. 读取两个 CSV 文件。
2. 用 pd.merge() 按 store_id 把销售记录和门店信息合并（横向关联）。
3. 新增一列 revenue（revenue = quantity × unit_price）。
4. 按城市分组统计：每个城市的【总销售额】和【订单数】。
5. 按商品分组统计：每种商品的【总销量】和【总销售额】。
6. 用 pd.concat() 把"上海门店"和"南京门店"的销售数据纵向拼接，体会 merge 和 concat 的区别。
7. 把合并后的完整数据导出为 merged_sales.csv。

知识点提示：
- pd.merge(df1, df2, on="key")     → 按共同列合并（类似 SQL JOIN）
- how="inner"（默认）               → 只保留两边都有的 key
- how="left"                        → 左表全保留，右表没有的填 NaN
- df["col1"] * df["col2"]           → 列运算
- df.groupby("col").agg({...})      → 分组聚合
- pd.concat([df1, df2], ignore_index=True) → 纵向拼接（上下叠放）
- df.to_csv("xxx.csv", index=False) → 导出

merge vs concat 区别：
- merge 是"关联"：把两张表按某个 key 左右拼在一起（列变多）
- concat 是"追加"：把两张表上下叠在一起（行变多）

易错点：
- merge 时如果两边都有同名列（除 key 之外），pandas 会自动加 _x / _y 后缀
- concat 拼接后 index 可能重复，记得用 ignore_index=True
- on 参数指定的列必须在两个 DataFrame 中都存在
"""

import pandas as pd

# ========== 第 1 步：读取两个文件 ==========
sales = pd.read_csv("sales.csv")
stores = pd.read_csv("stores.csv")

print("===== 销售记录 =====")
print(sales)
print(f"\n形状：{sales.shape}")

print("\n===== 门店信息 =====")
print(stores)
print(f"\n形状：{stores.shape}")

# ========== 第 2 步：用 merge 合并两张表 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   想想 pd.merge() 需要哪几个参数？
#   两张表的共同列（key）是什么？
#   合并后把结果赋值给变量 merged

merged = pd.merge(sales,stores, on ="store_id")

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 合并后的数据 =====")
print(merged)
print(f"\n形状：{merged.shape}")

# ========== 第 3 步：新增 revenue 列 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   想想怎么给 DataFrame 新增一列？（之前 ex36 做过类似的）
#   revenue 的计算公式题目里已经给了
merged["revenue"] = merged["quantity"]*merged["unit_price"]

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 新增 revenue 后 =====")
print(merged[["sale_id", "store_name", "product", "quantity", "unit_price", "revenue"]])

# ========== 第 4 步：按城市分组统计 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   这一步用 groupby + agg，你在 pandas_4 里练过
#   注意：不同列要用不同的聚合方式（想想字典形式的 agg 怎么写）
city_stats = merged.groupby("city")["revenue"].agg(["count","sum"])

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 按城市统计 =====")
print(city_stats)

# ========== 第 5 步：按商品分组统计 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   和上一步几乎一样的套路，只是换了分组列和聚合列
#   这次要统计的是「总销量」和「总销售额」
product_stats = merged.groupby("product").agg({"quantity":"sum","revenue":"sum"})

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 按商品统计 =====")
print(product_stats)

# ========== 第 6 步：用 concat 纵向拼接（体会 merge 和 concat 的区别） ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   分三步走：
#   1. 用布尔筛选分别取出上海和南京的数据（pandas_2 练过）
#   2. 用 pd.concat() 把两个子表拼起来
#   3. 想想：为什么这里用 concat 而不是 merge？

sh_data = merged[merged["city"] == "上海"]
nj_data = merged[merged["city"] == "南京"]
combined = pd.concat([sh_data,nj_data],ignore_index=True)
# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== concat 拼接结果（上海 + 南京） =====")
print(combined[["sale_id", "store_name", "city", "product", "revenue"]])
print(f"\n上海 {len(sh_data)} 条 + 南京 {len(nj_data )} 条 = 共 {len(combined)} 条")

# ========== 第 7 步：导出合并后的完整数据 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   之前 ex36 最后一步也是导出，回忆一下 to_csv 的用法
#   注意文件名和 index 参数

combined.to_csv("merged_sales.csv",index = False)
# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 合并完成，结果已导出！ =====")
