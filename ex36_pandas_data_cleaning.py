"""
题目：员工数据清洗与分析（pandas 综合练习）

项目背景：
你拿到了一份 HR 部门提供的员工数据 messy_employees.csv。
这份数据有不少问题：有缺失值、有重复记录、部门名大小写不统一。
你需要用 pandas 把这份"脏数据"清洗干净，然后做分组统计，最后导出结果。

任务目标：
1. 读取 messy_employees.csv，查看基本信息。
2. 检查并处理缺失值（isna / fillna / dropna）。
3. 去除重复行（drop_duplicates）。
4. 统一部门名称的大小写（str.lower / replace）。
5. 用部门薪资中位数填充 salary 的缺失值。
6. 新增一列 avg_dept_salary：该员工所在部门的平均薪资。
7. 按部门分组统计：人数、平均薪资、最高薪资。
8. 把清洗后的数据导出为 clean_employees.csv。

知识点提示：
- df.isna().sum()          → 查看每列有多少缺失值
- df.dropna(subset=[...])  → 删除指定列有缺失值的行
- df.drop_duplicates()     → 删除完全重复的行
- df["col"].str.lower()    → 把字符串列统一转小写
- df["col"].fillna(value)  → 用指定值填充缺失值
- df.groupby("col").transform("mean") → 分组计算后广播回原表
- df.to_csv(index=False)   → 导出时不要行索引
"""

import pandas as pd

# ========== 第 1 步：读取数据 ==========
df = pd.read_csv("messy_employees.csv")

print("===== 原始数据 =====")
print(df)
print(f"\n数据形状：{df.shape}")

# ========== 第 2 步：检查缺失值 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：用 df.isna().sum() 查看每列缺失值数量
# 然后用 df.dropna(subset=["name"]) 删除 name 为空的行（如果有的话）

# ========== 你需要写的逻辑到这里结束 ==========
print(df.isna().sum())
df = df.dropna(subset=["name"])
print("\n===== 处理缺失值后 =====")
print(df)

# ========== 第 3 步：去除重复行 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   先看看有没有重复：df.duplicated().sum()
#   然后去重：df = df.drop_duplicates()
print(# 只看 name 和 department 两列是否重复（忽略 id 和 salary）
print(df.duplicated(subset=["name", "department"]).sum()))
df = df.drop_duplicates()

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 去重后 =====")
print(df)

# ========== 第 4 步：统一部门名称（全转小写） ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：df["department"] = df["department"].str.lower()
# 注意：NaN 用 str.lower() 不会报错，会变成 NaN
df["department"] = df["department"].str.lower()
# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 统一部门名后 =====")
print(df)

# ========== 第 5 步：填充 salary 缺失值 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   先算出 salary 的中位数：median_val = df["salary"].median()
#   然后用 fillna 填充：df["salary"] = df["salary"].fillna(median_val)

# ========== 你需要写的逻辑到这里结束 ==========
# 先把 salary 转成数字，转不了的变成 NaN
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
median_val = df["salary"].median()
df["salary"] = df["salary"].fillna(median_val)
print("\n===== 填充薪资缺失后 =====")
print(df)

# ========== 第 6 步：新增 avg_dept_salary 列 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   用 groupby + transform 算出每个部门的平均薪资
#   dept_avg = df.groupby("department")["salary"].transform("mean")
#   然后赋值给新列：df["avg_dept_salary"] = dept_avg
#
# transform 的特点：计算结果的长度和原表一样，可以直接赋值成新列
dept_avg = df.groupby("department")["salary"].transform("mean")
df["avg_dept_salary"] = dept_avg

# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 新增部门平均薪资列后 =====")
print(df)

# ========== 第 7 步：按部门分组统计 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：
#   dept_stats = df.groupby("department")["salary"].agg(["count", "mean", "max"])
#   然后用 rename 重命名列：
#     count → emp_count
#     mean  → avg_salary
#     max   → max_salary
dept_stats = df.groupby("department")["salary"].agg(["count","mean","max"])
dept_stats = dept_stats.rename(columns={"count":"emp_count","mean":"avg_salary","max":"max_salary"})
# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 部门统计 =====")
print(dept_stats)

# ========== 第 8 步：导出清洗后的数据 ==========

# ========== 你需要写的逻辑从这里开始 ==========
# 提示：df.to_csv("clean_employees.csv", index=False)
# index=False 表示不把行号写进去
df.to_csv("clean_employees.csv",index = False)
# ========== 你需要写的逻辑到这里结束 ==========

print("\n===== 清洗完成，结果已导出！ =====")
