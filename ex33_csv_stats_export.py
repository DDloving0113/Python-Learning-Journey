"""
题目：部门统计结果导出 (CSV 文件处理)

任务目标：
1. 读取 `employees.csv` 文件。
2. 按 `department` 统计每个部门的人数、总薪资、平均薪资。
3. 将统计结果写入新的 `department_stats.csv` 文件。

知识点提示：
- 先用字典完成分组统计
- 再把统计字典整理成“字典列表”
- 使用 `csv.DictWriter()` 写出结果文件
- 写入前要先 `writeheader()`
"""

import csv


def export_department_stats(input_file, output_file):
    with open(input_file,"r",encoding="utf-8")as f:
        reader = csv.DictReader(f)
        stats = {}
        for row in reader:
            salary = row["salary"]
            dept = row["department"]
            if salary == "" or dept == "":
                continue
            salary = salary.strip()
            dept = dept.strip()
            try:
                salary = int(salary)
                if dept not in stats:
                    stats[dept]={
                        "count":0,
                        "total_salary":0
                    }
                stats[dept]["count"]  += 1
                stats[dept]["total_salary"] += salary
            except:
                continue
        for dept in stats:
            stats[dept]["avg_salary"] = stats[dept]["total_salary"]/stats[dept]["count"]
    with open(output_file,"w",encoding = "utf-8",newline="") as f:
        fieldnames = ["department","count","total_salary","avg_salary"]
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        temp_list =[]
        for k,v in stats.items():
            v["department"]=k
            temp_list.append(v)
        writer.writerows(temp_list)
if __name__ == "__main__":
    export_department_stats("employees.csv", "department_stats.csv")
