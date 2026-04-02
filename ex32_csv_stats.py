"""
题目：员工部门统计 (CSV 文件处理)

任务目标：
1. 读取 `employees.csv` 文件。
2. 按 `department` 进行分组统计。
3. 统计每个部门的：
   - 员工人数
   - 总薪资
   - 平均薪资
4. 将统计结果输出到屏幕。

知识点提示：
- 使用 `csv.DictReader()` 读取 CSV 文件
- 通过字典完成分组统计
- 注意把 `salary` 从字符串转换成整数
- 平均薪资建议在统计完成后再统一计算
"""

import csv


def calculate_department_stats(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        stat = {}
        for row in reader:
            department = row["department"]
            salary = row["salary"]
            department = department.strip()
            salary = salary.strip()
            if department == "" or salary == "":
                continue
            try:
                salary = int(salary)
            except ValueError:
                continue
            if department not in stat:
                stat[department] = {
                    "count": 0,
                    "total_salary": 0
                }
            stat[department]["count"] += 1
            stat[department]["total_salary"] += salary

        for dept in stat:
            stat[dept]["avg_salary"] = stat[dept]["total_salary"] / stat[dept]["count"]
    return stat


if __name__ == "__main__":
    result = calculate_department_stats("./employees.csv")
    print(result)
