
import pandas as pd

print("===== 核心原因：它们都在表示同一张表格 =====")
print("（用不同的数据结构，描述的是同一个基金信息表）")
print("\n")

# 同一张表格的不同表示方式
print("===== 表示方式1：字典列表（按行存） =====")
by_row = [
    {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "company": "易方达基金"},
    {"fund_code": "F002", "fund_name": "广发双擎升级", "company": "广发基金"},
]
print(by_row)
print("\n")

print("===== 表示方式2：列字典（按列存） =====")
by_col = {
    "fund_code": ["F001", "F002"],
    "fund_name": ["易方达蓝筹精选", "广发双擎升级"],
    "company": ["易方达基金", "广发基金"],
}
print(by_col)
print("\n")

print("===== 表示方式3：二维列表（纯数据，列名单独给） =====")
by_2d_list = [
    ["F001", "易方达蓝筹精选", "易方达基金"],
    ["F002", "广发双擎升级", "广发基金"],
]
cols = ["fund_code", "fund_name", "company"]
print("数据：", by_2d_list)
print("列名：", cols)
print("\n")

print("===== pandas 说：不管你怎么存，我都能帮你转成统一的表格形式 =====")
df1 = pd.DataFrame(by_row)
df2 = pd.DataFrame(by_col)
df3 = pd.DataFrame(by_2d_list, columns=cols)

print("--- 转出来的 DataFrame 都是一样的（看前2行）： ---")
print(df1.head(2))
print("\n... 所以 pandas 愿意接受这么多结构，因为它们的本质都是表格数据！")
