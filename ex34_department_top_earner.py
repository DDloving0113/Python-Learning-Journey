"""
题目：每个部门最高薪员工导出 (CSV 文件处理)

任务目标：
1. 读取 `employees.csv` 文件。
2. 按 `department` 分组。
3. 找出每个部门里薪资最高的员工。
4. 将结果写入新的 `department_top_earners.csv` 文件。

知识点提示：
- 使用 `csv.DictReader()` 读取 CSV 文件
- 使用字典保存每个部门当前最高薪员工
- 注意把 `salary` 从字符串转换成整数
- 使用 `csv.DictWriter()` 写出结果文件
"""

import csv


def export_department_top_earners(input_file, output_file):
    top_earners = {}  # key: 部门名, value: 这个部门当前最高薪的员工（一整行字典）

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            dept = row["department"]
            salary = int(row["salary"])

            # ========== 你需要写的逻辑从这里开始 ==========

            if dept not in top_earners:
                # 情况 1：这个部门第一次出现
                # 把当前这个人存进去
                # 你的代码：
                top_earners[dept] = row

            else:
                # 情况 2：这个部门已经有记录了
                # 拿到已存的那个人的工资
                existing_salary = int(top_earners[dept]["salary"])
                # 比较一下
                if salary > existing_salary:
                    # 如果当前这个人工资更高，就替换掉
                    # 你的代码：
                    top_earners[dept] = row


            # ========== 你需要写的逻辑到这里结束 ==========

    # 接下来要写文件了
    # 先把 top_earners 里的值取出来变成列表
    top_earners_list = list(top_earners.values())

    if not top_earners_list:
        return

    # 获取表头
    fieldnames = top_earners_list[0].keys()

    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(top_earners_list)

    print("每个部门最高薪员工已导出！")
    print(fieldnames)
    print(top_earners_list)


if __name__ == "__main__":
    export_department_top_earners("employees.csv", "department_top_earners.csv")
