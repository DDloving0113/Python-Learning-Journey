
import csv

print("===== 情况 1：字典里的键比 fieldnames 少 =====")
data1 = [
    {"city": "北京", "count": 3}  # 字典里没有 "total"
]
fieldnames1 = ["city", "count", "total"]
with open("case1.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames1)
    writer.writeheader()
    writer.writerows(data1)
with open("case1.csv", "r", encoding="utf-8") as f:
    print(f.read())

print("\n===== 情况 2：字典里的键比 fieldnames 多（默认报错） =====")
try:
    data2 = [
        {"city": "北京", "cnt": 3, "total": 19997}  # 有 "cnt"，但 fieldnames 里没有
    ]
    fieldnames2 = ["city", "count", "total"]
    with open("case2.csv", "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames2)
        writer.writeheader()
        writer.writerows(data2)
    with open("case2.csv", "r", encoding="utf-8") as f:
        print(f.read())
except Exception as e:
    print(f"报错了：{type(e).__name__}: {e}")

print("\n===== 情况3：字典里的键比 fieldnames 多，用 extrasaction='ignore' =====")
data3 = [
    {"city": "北京", "cnt": 3, "total": 19997}  # 有 "cnt"
]
fieldnames3 = ["city", "count", "total"]
with open("case3.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames3,
        extrasaction="ignore"  # 忽略字典里 fieldnames 没有的键
    )
    writer.writeheader()
    writer.writerows(data3)
with open("case3.csv", "r", encoding="utf-8") as f:
    print(f.read())

print("\n===== 情况4：键完全对应 =====")
data4 = [
    {"city": "北京", "count": 3, "total": 19997}
]
fieldnames4 = ["city", "count", "total"]
with open("case4.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames4)
    writer.writeheader()
    writer.writerows(data4)
with open("case4.csv", "r", encoding="utf-8") as f:
    print(f.read())
