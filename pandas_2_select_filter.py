
import pandas as pd

# 先手动创建一点数据（基金信息）
fund_data = [
    {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "company": "易方达基金", "strategy": "权益投资", "latest_nav": 1.589},
    {"fund_code": "F002", "fund_name": "广发双擎升级", "company": "广发基金", "strategy": "权益投资", "latest_nav": 2.234},
    {"fund_code": "F003", "fund_name": "华夏成长混合", "company": "华夏基金", "strategy": "固收+", "latest_nav": 1.945},
    {"fund_code": "F004", "fund_name": "南方优选成长", "company": "南方基金", "strategy": "固收+", "latest_nav": 1.299},
    {"fund_code": "F005", "fund_name": "汇添富创新医药", "company": "汇添富基金", "strategy": "权益投资", "latest_nav": 3.612},
]
df = pd.DataFrame(fund_data)

print("===== 原始数据 =====")
print(df)
print("\n")

print("===== 1. 选列：只看你关心的列 =====")
print("--- 方式1：选单列（df['列名']），返回 Series ---")
print(df["fund_name"])
print("\n")

print("--- 方式2：选多列（df[['列1', '列2']]），注意是两个方括号！ ---")
print(df[["fund_code", "fund_name", "latest_nav"]])
print("\n")

print("===== 2. 筛选行：只看符合条件的数据 =====")
print("--- 筛选1：找出所有权益投资的基金 ---")
equity_funds = df[df["strategy"] == "权益投资"]
print(equity_funds)
print("\n")

print("--- 筛选2：找出最新净值大于2的基金 ---")
high_nav_funds = df[df["latest_nav"] > 2]
print(high_nav_funds)
print("\n")

print("--- 筛选3：组合条件（权益投资 AND 净值大于2） ---")
filtered = df[(df["strategy"] == "权益投资") & (df["latest_nav"] > 2)]
print(filtered)
