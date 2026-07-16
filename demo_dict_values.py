"""演示字典的 .values() 方法"""

# 模拟你的 fund_nav_summary 结构
fund_nav_summary = {
    "F001": {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "last_nav": 1.589},
    "F002": {"fund_code": "F002", "fund_name": "广发双擎升级", "last_nav": 2.234},
    "F003": {"fund_code": "F003", "fund_name": "华夏成长混合", "last_nav": 1.945},
}

print("===== 1. 原始的字典 =====")
print(fund_nav_summary)
print(f"类型: {type(fund_nav_summary)}")
print()

print("===== 2. fund_nav_summary.values() - 只取所有的值 =====")
print(fund_nav_summary.values())
print(f"类型: {type(fund_nav_summary.values())}")
print()

print("===== 3. list(fund_nav_summary.values()) - 转成列表 =====")
result_list = list(fund_nav_summary.values())
print(result_list)
print(f"类型: {type(result_list)}")
print()

print("===== 4. 遍历这个列表 =====")
for fund in result_list:
    print(fund)
