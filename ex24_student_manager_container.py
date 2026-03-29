"""
题目：Ex24 - 学生容器管理器（Student + StudentManager）

目标：练习 OOP 的“容器协议”（len / for / in）以及“对象相等规则”（__eq__）。

要求：
1) Student
   - 字段：student_id, name, score
   - 相等规则：只要 student_id 相同，就认为是同一个学生（name/score 不参与比较）

2) StudentManager
   - 内部用一个列表存 Student 对象（例如：self.students）
   - 支持：
     - len(manager)
     - for s in manager:
     - student in manager
   - add(student):
     - 如果已存在相同 student_id 的学生：更新该学生的 score 为新值
     - 否则：追加到列表
   - top(n):
     - 返回分数最高的 n 个学生（返回新列表）
     - 不能改变原列表的顺序（不能对 self.students 原地 sort）
"""


class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student(id={self.student_id}, name={self.name}, score={self.score})"

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other,Student):
            return NotImplemented
        return self.student_id == other.student_id

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError
        if value < 0 or value > 100:
            raise ValueError
        self._score = value

    @property
    def grade(self):
        if self.score >= 90:
            return "A"
        if self.score >= 80:
            return "B"
        if self.score >= 70:
            return "C"
        if self.score >= 60:
            return "D"
        return "F"

class StudentManager:
    def __init__(self):
        self.students = []
        self.index = {}

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def __contains__(self, item):
        return   item in self.students

    def add(self, student):
        if not isinstance(student,Student):
            return False
        existing = self.get(student.student_id)
        if existing is not None:
            existing.score = student.score
            return True
        else:
            self.students.append(student)
            self.index[student.student_id] = student
            return True

    def top(self, n):
        if n <= 0:
            return []
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)
        return sorted_students[:n]
        
    @property
    def average_score(self):
        if not self.students:
            return 0
        return sum(s.score for s in self.students) / len(self.students)

    def get(self, student_id):
        return self.index.get(student_id)   # 不存在就返回 None



if __name__ == "__main__":
    manager = StudentManager()

    s1 = Student("S001", "Alice", 95)
    s2 = Student("S002", "Bob", 88)
    s3 = Student("S003", "Carol", 92)

    manager.add(s1)
    manager.add(s2)
    manager.add(s3)

    manager.add(Student("S002", "Bob", 99))

    print("len:", len(manager))
    print("all:", [s for s in manager])
    print("contains:", Student("S001", "AnyName", 0) in manager)
    print("top2:", manager.top(2))
    print(s1.grade)
    print(manager.add("not a student"))
    print(manager.add(Student("S999","Z",60)))