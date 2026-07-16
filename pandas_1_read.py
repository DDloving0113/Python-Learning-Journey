
import pandas as pd

# 1. 读入 CSV（一行搞定）
df = pd.read_csv("pandas_orders.csv")

# 2. 看看前几行（默认前5行）
print("=== 前3行 ===")
print(df.head(3))

# 3. 看看整体信息（有多少行多少列，每列类型是什么）
print("\n=== 数据信息 ===")
df.info()

# 4. 看看统计摘要（只对数值列有效）
print("\n=== 统计摘要 ===")
print(df.describe())

# 5. 看看有哪些列
print("\n=== 列名 ===")
print(df.columns.tolist())
