
import csv

# 模拟一下你代码里的 list_city_stats 是什么样子
list_city_stats = [
    {"city": "北京", "cnt": 3, "total": 19997},  # 注意这里的键是 "cnt"
    {"city": "上海", "cnt": 3, "total": 21994},
    {"city": "广州", "cnt": 2, "total": 12996},
]

# 这是你现在设置的 fieldnames
fieldnames = ["city", "count", "total"]  # 注意这里写的是 "count"

print("=== 你准备写入的数据 ===")
print(list_city_stats)
print("\n=== 你指定的字段名 ===")
print(fieldnames)

print("\n=== 现在模拟 DictWriter 怎么写 ===")
# 临时写个文件看看
with open("demo_output.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_city_stats)

print("\n=== 实际写出来的 CSV 内容 ===")
with open("demo_output.csv", "r", encoding="utf-8") as f:
    print(f.read())
