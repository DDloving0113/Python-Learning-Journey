
import pandas as pd

print("===== 方式1：字典列表（最常用，最自然，和你之前学的一样） =====")
# 每一个字典代表一行，非常直观
fund_info = [
    {"fund_code": "F001", "fund_name": "易方达蓝筹精选", "company": "易方达基金", "strategy": "权益投资"},
    {"fund_code": "F002", "fund_name": "广发双擎升级", "company": "广发基金", "strategy": "权益投资"},
    {"fund_code": "F003", "fund_name": "华夏成长混合", "company": "华夏基金", "strategy": "固收+"},
]
df1 = pd.DataFrame(fund_info)
print(df1)
print("\n")

print("===== 方式2：列字典（按列组织数据，有时候也方便） =====")
# 每一个 key 是列名，value 是这一列的列表
fund_nav = {
    "date": ["2026-07-01", "2026-07-02", "2026-07-03"],
    "F001": [1.523, 1.545, 1.512],
    "F002": [2.123, 2.156, 2.089],
}
df2 = pd.DataFrame(fund_nav)
print(df2)
print("\n")

print("===== 方式3：列表列表（二维列表，加列名） =====")
# 里面每一个小列表代表一行，然后单独给列名
orders = [
    [1, "北京", "手机", 2, 3999],
    [2, "上海", "电脑", 1, 7999],
    [3, "北京", "手机", 1, 3999],
]
df3 = pd.DataFrame(orders, columns=["order_id", "city", "product", "amount", "price"])
print(df3)
print("\n")

print("===== 总结 =====")
print("- 方式1（字典列表）最推荐，和你之前的知识衔接最顺")
print("- 方式2（列字典）适合净值数据这种按产品列开的情况")
print("- 方式3（二维列表）适合纯数字、或者需要从其他系统导过来的情况")
