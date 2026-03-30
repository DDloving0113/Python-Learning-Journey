"""
实战项目：数据处理大师 - CSV 文件筛选器

任务目标：
从一个包含员工信息的 CSV 文件中读取数据，筛选出月薪大于等于 10000 的员工，
并将这些“高薪员工”的信息保存到一个新的 CSV 文件中。

知识点预习：
在 Python 中处理 CSV，我们通常使用内置的 `csv` 模块。
最常用的两个工具是：
1. `csv.DictReader(f)`：它能把 CSV 文件的每一行变成一个字典。比如第一行会变成：
   {"id": "E001", "name": "Alice", "department": "HR", "salary": "8500"}
   （注意：从 CSV 读出来的数据，无论原本是不是数字，都会变成【字符串】！）

2. `csv.DictWriter(f, fieldnames=[表头列表])`：它能把字典重新写回 CSV 文件中。

要求：
1. 读取 `employees.csv` 文件。
2. 遍历每一行数据，判断 `salary` 是否 >= 10000（记得把字符串转成数字比较）。
3. 如果是，就把这行数据加到一个新的列表 `high_salary_employees` 中。
4. 最后，把这个列表里的所有字典，写入到一个新文件 `high_salary.csv` 中。
"""

import csv

def filter_high_salary(input_file, output_file):
    high_salary_employees = []
    
    # 1. 读取阶段
    print(f"正在读取文件: {input_file} ...")
    with open(input_file, "r", encoding="utf-8") as f:
        # 使用 csv.DictReader 读取
        reader = csv.DictReader(f)
        # TODO: 遍历 reader，判断薪资，把符合条件的行追加到 high_salary_employees 列表中
        for rows in reader:
            if int(rows["salary"]) >= 10000:
                high_salary_employees.append(rows)

    print(f"筛选完毕，共找到 {len(high_salary_employees)} 名高薪员工。")

    # 2. 写入阶段
    # 如果没找到任何人，就不需要写文件了
    if not high_salary_employees:
        return

    print(f"正在将结果保存到: {output_file} ...")
    # 获取表头字段（从列表里的第一个字典的 keys 中提取）
    fieldnames = high_salary_employees[0].keys()
    
    with open(output_file, "w", encoding="utf-8", newline='') as f:
        # 使用 csv.DictWriter 准备写入
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        # TODO: 先写入表头
        writer.writeheader()
        
        # TODO: 再把 high_salary_employees 列表里的数据一行行写进去
        writer.writerows(high_salary_employees)

    print("保存成功！")


if __name__ == "__main__":
    filter_high_salary("employees.csv", "high_salary.csv")
# 测试我自己手动运行 Git 上传流程