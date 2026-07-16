
import pandas as pd

# 1. 先读入 DataFrame
df = pd.read_csv("pandas_orders.csv")

print("===== 1. 这是 DataFrame =====")
print(f"类型：{type(df)}")
print(df)
print("\n")

print("===== 2. 这是 Series（取单独一列） =====")
# 取单独一列，就是 Series
city_series = df["city"]
print(f"类型：{type(city_series)}")
print(city_series)
print("\n")

print("===== 3. 这也是 Series（取单独一行，用 loc） =====")
# 取单独一行，也是 Series
row_series = df.loc[0]
print(f"类型：{type(row_series)}")
print(row_series)
print("\n")

print("===== 4. 怎么判断你手里的是什么？ =====")
print(f"- 看类型：type(df) → {type(df)}")
print(f"- 看形状：df.shape → {df.shape}（行数, 列数）")
print(f"- 看类型：type(city_series) → {type(city_series)}")
print(f"- 看形状：city_series.shape → {city_series.shape}（只有长度，没有列数）")
print("\n")

print("===== 5. 简单总结：DataFrame vs Series =====")
print("- DataFrame：像一张 Excel 表，有行有列，是二维的")
print("- Series：像 Excel 里的一列或者一行，是一维的")
print("- 你可以把 DataFrame 理解成很多 Series 拼在一起")
