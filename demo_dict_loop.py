"""演示字典循环"""

# 模拟你的 fund_nav_summary 结构
fund_nav_summary = {
    "F001": {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "last_nav": 1.589},
    "F002": {"fund_code": "F002", "fund_name": "广发双擎升级", "last_nav": 2.234},
    "F003": {"fund_code": "F003", "fund_name": "华夏成长混合", "last_nav": 1.945},
}

print("===== 方式 1：for key in dict - 循环键 =====")
for fund_code in fund_nav_summary:
    print(f"当前 fund_code（键）= {fund_code}")
    fund = fund_nav_summary[fund_code]  # 用键去取对应的值
    print(f"对应的基金信息（值）= {fund}")
    print()

print("\n===== 方式 2：for key, value in dict.items() - 同时循环键和值 =====")
for fund_code, fund in fund_nav_summary.items():
    print(f"fund_code = {fund_code}")
    print(f"fund = {fund}")
    print()
