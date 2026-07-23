import pandas as pd

fund_data = [
    {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "company": "易方达基金", "strategy": "权益投资", "latest_nav": 1.589},
    {"fund_code": "F002", "fund_name": "广发双擎升级", "company": "广发基金", "strategy": "权益投资", "latest_nav": 2.234},
    {"fund_code": "F003", "fund_name": "华夏成长混合", "company": "华夏基金", "strategy": "固收+", "latest_nav": 1.945},
    {"fund_code": "F004", "fund_name": "南方优选成长", "company": "南方基金", "strategy": "固收+", "latest_nav": 1.299},
    {"fund_code": "F005", "fund_name": "汇添富创新医药", "company": "汇添富基金", "strategy": "权益投资", "latest_nav": 3.612},
]
df = pd.DataFrame(fund_data)

# 看看这步到底返回了什么
mask = df["strategy"] == "权益投资"
print("布尔 Series：")
print(mask)
print(f"类型：{type(mask)}")

print("\n用这个 mask 去筛选：")
print(df[mask])
