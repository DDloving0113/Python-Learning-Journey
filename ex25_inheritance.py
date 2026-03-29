"""
题目：Ex25 - 类的继承与多态 (Inheritance & Polymorphism)

目标：学习如何创建一个“父类”（基类），并让“子类”继承它，同时重写（Override）父类的方法。

场景：公司员工工资计算系统
- 我们有一个通用的 `Employee`（员工）类。
- 我们有两个特殊的员工类型：`Manager`（经理）和 `Developer`（开发人员）。
- 他们都有基本工资，但奖金（Bonus）的计算方式不同。

要求：
1) Employee (父类)
   - 属性：`emp_id` (工号), `name` (姓名), `base_salary` (基本工资)
   - 方法：`calculate_salary()` -> 默认返回基本工资即可。
   - 方法：`__str__()` -> 返回类似 "Employee(id=xxx, name=xxx)"

2) Manager (子类，继承自 Employee)
   - 属性：除了父类的属性，还有一个额外的 `team_size` (团队人数)。
   - 方法：重写 `calculate_salary()` -> 返回 base_salary + (team_size * 1000)

3) Developer (子类，继承自 Employee)
   - 属性：除了父类的属性，还有一个额外的 `projects_completed` (完成项目数)。
   - 方法：重写 `calculate_salary()` -> 返回 base_salary + (projects_completed * 2000)
"""

# 请在这里开始定义 Employee 父类：
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
    def __str__(self):
        return f"Employee(id ={self.emp_id},name={self.name})"
    def calculate_salary(self):
        return self.base_salary


# 请在这里定义 Manager 子类：
class Manager(Employee):
    def __init__(self,emp_id,name,base_salary,team_size):
        super().__init__(emp_id,name,base_salary)
        self.team_size = team_size
    def calculate_salary(self):
        return self.base_salary + self.team_size * 1000




# 请在这里定义 Developer 子类：
class Developer(Employee):
    def __init__(self,emp_id,name,base_salary,projects_completed):
        super().__init__(emp_id,name,base_salary)
        self.projects_completed = projects_completed
    def calculate_salary(self):
        return self.base_salary + self.projects_completed *2000
if __name__ == "__main__":
    # 测试代码 (暂时注释掉，等您写完类之后我们再打开运行)
    emp1 = Employee("E01", "Alice", 5000)
    mgr1 = Manager("M01", "Bob", 8000, team_size=5)
    dev1 = Developer("D01", "Charlie", 6000, projects_completed=3)
    
    print(emp1, "Salary:", emp1.calculate_salary())  # 应输出 5000
    print(mgr1, "Salary:", mgr1.calculate_salary())  # 应输出 8000 + 5000 = 13000
    print(dev1, "Salary:", dev1.calculate_salary())  # 应输出 6000 + 6000 = 12000
    pass
