
def create_messy_csv(filename):
    """创建包含各种脏数据的CSV文件"""
    data = [
        "id,name,department,salary",
        "1,Alice,Sales,50000",
        "2,Bob,Engineering,80000",
        "3,Charlie,Sales,not_a_number",  # 错误1：薪资不是数字
        "4,David,Engineering,",           # 错误2：薪资缺失
        "5,Eve,HR,45000",
        "6,Frank,Sales,52000",
        "7,Grace,Engineering,82000",
        "8,Heidi,HR,N/A",                 # 错误3：无效标记
        "9,Ivan,Sales,54000",
        "10,Judy,Engineering,bad_data"    # 错误4：乱码
    ]
    
    with open(filename, 'w') as f:
        f.write('\n'.join(data))
    print(f"已生成脏数据文件: {filename}")

def read_employees_robust(filename):
    """
    健壮的读取函数：能处理各种异常情况
    """
    employee_dict = {}
    
    with open(filename, 'r') as f:
        # 跳过标题行
        f.readline()
        
        # 逐行读取（比 readlines 更省内存）
        for line in f:
            line = line.strip()
            if not line: # 跳过空行
                continue
                
            parts = line.split(',')
            
            # 基础格式检查
            if len(parts) != 4:
                continue
                
            try:
                name = parts[1]
                salary_str = parts[3]
                
                # 尝试转换薪资，如果失败会触发 ValueError
                salary = int(salary_str)
                
                employee_dict[name] = salary
                
            except ValueError:
                # 捕获具体的转换错误（如 'N/A', 'bad_data'）
                # print(f"警告: 跳过无效数据 - {line}")
                continue
                
    return employee_dict

if __name__ == "__main__":
    filename = "messy_employees.csv"
    create_messy_csv(filename)
    
    # 你的任务：
    # 1. 运行代码，看看生成了什么文件
    # 2. 完善 read_employees_robust 函数，让它能跳过错误行，只读取正确的数据
    # 3. 打印出读取到的有效员工数量
    print("-" * 30)
    print("开始读取脏数据文件...")
    valid_employees = read_employees_robust(filename)
    
    print(f"读取完成！共找到 {len(valid_employees)} 个有效员工数据：")
    for name, salary in valid_employees.items():
        print(f"  - {name}: {salary}")
        
    print("-" * 30)
    if len(valid_employees) == 6:
        print("✅ 测试通过！成功跳过了所有错误数据。")
    else:
        print(f"❌ 测试失败！预期 6 个有效数据，实际找到 {len(valid_employees)} 个。")
