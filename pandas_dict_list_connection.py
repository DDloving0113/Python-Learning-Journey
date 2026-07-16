
import pandas as pd

# 1. 这是你之前很熟悉的：字典列表
dict_list = [
    {"city": "北京", "cnt": 3, "total": 19996},
    {"city": "上海", "cnt": 3, "total": 21995},
    {"city": "广州", "cnt": 2, "total": 12996},
]

print("===== 1. 原始：字典列表（你之前很熟悉的结构） =====")
for item in dict_list:
    print(item)
print(f"类型：{type(dict_list)}")
print("\n")

# 2. 字典列表 → pandas DataFrame（一行搞定！）
df = pd.DataFrame(dict_list)

print("===== 2. 转换为：pandas DataFrame =====")
print(df)
print(f"类型：{type(df)}")
print("\n")

# 3. pandas DataFrame → 字典列表（又回来了！）
back_to_dict_list = df.to_dict("records")

print("===== 3. 又转回：字典列表 =====")
for item in back_to_dict_list:
    print(item)
print(f"类型：{type(back_to_dict_list)}")
print("\n")

print("===== 总结：异曲同工之妙 =====")
print("- csv.DictReader 读出来是字典列表")
print("- 你手动写的也是字典列表")
print("- 这种结构非常适合表示“表格”数据")
print("- pandas 可以直接把这种结构转成 DataFrame")
print("- DataFrame 也可以转回字典列表")
