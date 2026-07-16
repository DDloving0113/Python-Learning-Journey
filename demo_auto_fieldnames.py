
import csv

# 你的列表
list_city_stats = [
    {"city": "北京", "cnt": 3, "total": 19997},
    {"city": "上海", "cnt": 3, "total": 21994},
]

# 自动取第一个字典的键作为 fieldnames
if list_city_stats:  # 先判断列表非空
    fieldnames = list(list_city_stats[0].keys())  # 取第一个字典的所有键
else:
    fieldnames = []

print(f"自动生成的 fieldnames: {fieldnames}")

# 然后正常写入
with open("auto_fieldnames.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_city_stats)

print("\n写出来的 CSV:")
with open("auto_fieldnames.csv", "r", encoding="utf-8") as f:
    print(f.read())
