"""
FOF 投资助理练习：基金数据合并与统计

项目背景：
你是一名 FOF 投资助理，现在需要处理两份数据：
1. fund_nav.csv：基金净值数据（每个基金的每日净值）
2. fund_info.csv：基金基本信息（基金公司、策略类型）

任务目标：
1. 读取这两个文件
2. 把它们合并在一起（按 fund_code 关联）
3. 按 fund_company（基金公司）分组统计：
   - 该公司旗下有多少只基金
   - 该公司基金的最新净值均值
4. 按 strategy_type（策略类型）分组统计：
   - 该策略有多少只基金
5. 计算每只基金的区间收益率
6. 把最终结果写回 fund_analysis_result.csv

知识点提示：
- 先把两个文件都读成字典列表
- 然后用字典做「关联合并」
- 还是用我们之前学的「分组统计模式」
- 收益率 = (最后一天净值 - 第一天净值) / 第一天净值
"""

import csv


def load_csv(filename):
    """读取 CSV 文件，返回字典列表"""
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def main():
    # ========== 第 1 步：读取两个文件 ==========
    nav_data = load_csv("fund_nav.csv")  # 净值数据
    info_data = load_csv("fund_info.csv")  # 基金基本信息

    print(f"读取到 {len(nav_data)} 条净值记录")
    print(f"读取到 {len(info_data)} 只基金的基本信息")

    # ========== 第 2 步：把基金基本信息转成字典，方便关联 ==========
    # key: fund_code, value: 这只基金的完整信息字典
    info_dict = {}
    for info in info_data:
        fund_code = info["fund_code"]
        info_dict[fund_code] = info

    # ========== 第 3 步：先整理每只基金的「第一天净值」和「最后一天净值」 ==========
    # key: fund_code, value: {"first_nav": xxx, "last_nav": xxx, "fund_name": xxx}
    fund_nav_summary = {}

    for nav_row in nav_data:
        fund_code = nav_row["fund_code"]
        nav = float(nav_row["nav"])
        date = nav_row["date"]

        # ========== 你需要写的逻辑开始 ==========
        # 提示：
        # 1. 如果是第一次遇到这只基金，就把 first_nav 和 last_nav 都设为当前 nav
        # 2. 如果不是第一次，就只更新 last_nav
        # 3. 同时把基金基本信息（从 info_dict 里取）也合并进来

        # 你的代码：
        if fund_code not in fund_nav_summary:
            fund_nav_summary[fund_code] =\
                {"fund_code": fund_code,
                 "fund_company":info_dict[fund_code]["fund_company"],
                 "fund_name":info_dict[fund_code]["fund_name"],
                 "strategy_type":info_dict[fund_code]["strategy_type"],
                 "first_nav": nav,
                 "last_nav": nav}
        fund_nav_summary[fund_code]["last_nav"] = nav

        # ========== 你需要写的逻辑结束 ==========

    # ========== 第 4 步：按基金公司分组统计 ==========
    company_stats = {}

    for fund_code in fund_nav_summary:
        fund = fund_nav_summary[fund_code]
        company = fund["fund_company"]
        last_nav = fund["last_nav"]

        # ========== 你需要写的逻辑开始 ==========
        # 提示：用我们之前学的分组统计模式
        if company not in company_stats:
            company_stats[company] = {"count": 1, "total_nav": last_nav}
        else:
            company_stats[company]["count"] += 1
            company_stats[company]["total_nav"] += last_nav


        # ========== 你需要写的逻辑结束 ==========

    # ========== 第 4.5 步：按策略类型分组统计 ==========
    strategy_stats = {}
    for fund_code in fund_nav_summary:
        fund = fund_nav_summary[fund_code]
        strategy = fund["strategy_type"]
        
        if strategy not in strategy_stats:
            strategy_stats[strategy] = {"count": 1}
        else:
            strategy_stats[strategy]["count"] += 1

    # ========== 第 5 步：计算分组平均净值，计算每只基金的收益率 ==========
    # 先处理公司统计
    for company in company_stats:
        stats = company_stats[company]
        stats["avg_nav"] = stats["total_nav"] / stats["count"]

    # 再处理每只基金的收益率
    for fund_code in fund_nav_summary:
        fund = fund_nav_summary[fund_code]
        first_nav = fund["first_nav"]
        last_nav = fund["last_nav"]
        fund["return_rate"] = (last_nav - first_nav) / first_nav  # 计算收益率

    # ========== 第 6 步：导出结果 ==========
    # 先把 fund_nav_summary 转成列表
    result_list = list(fund_nav_summary.values())

    # 写出结果
    if result_list:
        fieldnames = result_list[0].keys()
        with open("fund_analysis_result.csv", "w", encoding="utf-8", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(result_list)

    print("\n===== 基金公司统计 =====")
    for company in company_stats:
        stats = company_stats[company]
        print(f"{company}: {stats['count']} 只基金，平均净值 {stats['avg_nav']:.4f}")

    print("\n===== 策略类型统计 =====")
    for strategy in strategy_stats:
        stats = strategy_stats[strategy]
        print(f"{strategy}: {stats['count']} 只基金")

    print("\n===== 基金收益率统计 =====")
    for fund_code in fund_nav_summary:
        fund = fund_nav_summary[fund_code]
        print(f"{fund['fund_name']}: 收益率 {fund['return_rate']:.2%}")

    print("\n分析结果已保存到 fund_analysis_result.csv")


if __name__ == "__main__":
    main()
