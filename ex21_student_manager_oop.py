# 题目：Ex21 - 面向对象版学生管理系统
#
# 之前的做法：
# students = [
#     {'id': '001', 'name': 'Alice', 'score': 95},
#     {'id': '002', 'name': 'Bob', 'score': 59}
# ]
#
# 现在的做法 (OOP)：
# 1. Student 类：负责单个学生的数据和行为 (自我介绍、算等级)
# 2. StudentManager 类：负责管理“一群”学生 (添加、展示、统计)
#
# 这就是 OOP 的核心思想：各司其职。

class Student:
    """单个学生：只管自己的事"""
    def __init__(self, student_id, name, score):
        self.id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"[{self.id}] {self.name}: {self.score}分"

    def get_grade(self):
        if self.score >= 90: return "A"
        elif self.score >= 60: return "C"
        else: return "D"

class StudentManager:
    """班主任：管理所有学生"""
    def __init__(self):
        # 这里的 students 是一个列表，用来存 Student 对象
        self.students = []

    def add_student(self, name, score):
        """
        1. 生成一个新的 ID (比如列表长度+1)
        2. 创建 Student 对象
        3. 存入 self.students 列表
        """
        # 简单的 ID 生成逻辑：当前人数 + 1
        new_id = str(len(self.students) + 1).zfill(3)
        
        # 核心：Manager 创建并拥有 Student 对象 (组合关系)
        new_student = Student(new_id, name, score)
        self.students.append(new_student)
        
        print(f"系统: 已添加学生 {name}")

    def show_all(self):
        """遍历打印所有学生"""
        print(f"\n--- 全班名单 ({len(self.students)}人) ---")
        # 核心：Manager 指挥 Student 对象干活
        for s in self.students:
            # 这里自动调用了 Student 的 __str__ 方法
            print(s)

    def get_failed_students(self):
        # self.students 是名单（名词），不带括号
        # s.score 是分数（名词），不带括号
        return [s for s in self.students if s.score < 60]
# --- 测试代码 ---
if __name__ == "__main__":
    manager = StudentManager()
    
    # 招收新学生
    manager.add_student("Alice", 95)
    manager.add_student("Bob", 59)
    manager.add_student("Charlie", 88)
    
    # 展示全班
    manager.show_all()
