"""
题目：员工薪资分析 (CSV 文件处理)

任务：
1. 读取 `employees.csv` 文件。
2. 清洗数据：
   - 去除薪资字段的空格。
   - 如果薪资为空，忽略该行。
   - 将薪资转换为整数。
3. 统计分析：
   - 计算所有员工的平均薪资。
   - (进阶) 计算每个部门的平均薪资。
4. 将结果输出到屏幕。

提示：
- 使用 open() 读取文件
- 使用 strip() 去除空格
- 使用 split(',') 分割每一行
"""

def read_employees(filename):
    """
    读取并清洗数据
    返回一个包含员工字典的列表: [{"name": "Alice", "salary": 50000, ...}, ...]
    """
    with open(filename) as f:
        temp_list = []
        lines = f.readlines()
        for line in lines[1:]:
            parts = line.strip().split(",")
            if len(parts)<4:
                continue
            salary_str = parts[3].strip()
            if salary_str == "":
                continue
            salary = int(salary_str)
            temp_list.append({"name": parts[1],"dept":parts[2] ,"salary": salary})
    return temp_list



def calculate_average_salary(employees):
    """
    计算部门平均薪资
    """
    employee_dict = {}
    dept_avg_dict = {}
    for employee in employees:
        dept = employee["dept"]
        if dept not in employee_dict:
            employee_dict[dept] = []
        employee_dict[dept].append(employee["salary"])
    for dept in employee_dict:
        avg_svg = sum(employee_dict[dept])/len(employee_dict[dept])
        dept_avg_dict[dept] = avg_svg
    return dept_avg_dict



if __name__ == "__main__":
    # 1. 读取
    employees = read_employees("employees.csv")
    print(f"员工列表: {employees}")

    # 2. 分析
    avg_salary = calculate_average_salary(employees)
    print(f"平均薪资: {avg_salary}")

