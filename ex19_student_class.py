# 题目：Ex19 - 面向对象编程入门 (OOP: Classes & Objects)
#
# 到目前为止，我们一直用字典来表示学生：{'name': 'Alice', 'score': 85}
# 但如果有 100 个学生，每个学生都要写一遍字典结构，而且还要单独写函数处理它们，就很麻烦。
#
# 解决方案：类 (Class)
# 类就像一个“模具”，可以批量生产“对象” (Object)。
#
# 任务目标：
# 1. 定义一个 Student 类
# 2. 实现 __init__ 方法 (初始化名字和分数)
# 3. 实现 introduce 方法 (自我介绍)
# 4. 实现 get_grade 方法 (根据分数返回等级)

class Student:
    def __init__(self, student_id, name, score):
        """
        初始化方法 (Constructor)
        当创建新学生对象时，会自动调用这个方法。
        """
        # 1. 这里的 self.id 是对象内部的属性名
        # 2. 这里的 student_id 是外部传进来的参数
        # 它们的名字可以不一样！但为了不把自己绕晕，通常会起一样的名字。
        self.id = student_id 
        
        # 比如这里，如果我写 self.xingming = name 也是合法的，
        # 但以后你就得用 s1.xingming 来访问它。
        self.name = name
        self.score = score
        print(f"DEBUG: 创建了一个新学生 {self.name} (学号: {self.id})")

    def introduce(self):
        """
        让学生自我介绍
        返回字符串： "大家好，我是 [名字] (学号: [学号])，我的分数是 [分数]。"
        """
        # TODO: 请实现
        # 提示：使用 self.name, self.id, self.score
        return f"大家好，我是 {self.name} (学号: {self.id})，我的分数是 {self.score}。"

    def get_grade(self):
        """
        根据分数判断等级
        >= 90: A
        >= 80: B
        >= 60: C
        < 60: D
        """
        # TODO: 请实现
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"

# --- 测试代码 ---
if __name__ == "__main__":
    # 1. 创建对象 (实例化)
    # 注意：现在需要传入学号了
    s1 = Student("001", "Alice", 95)
    s2 = Student("002", "Bob", 59)
    
    # 2. 调用方法
    print(f"\n--- 自我介绍 ---")
    print(s1.introduce())
    print(s2.introduce())
    
    # 3. 获取等级
    print(f"\n--- 成绩等级 ---")
    print(f"{s1.name}: {s1.get_grade()}")
    print(f"{s2.name}: {s2.get_grade()}")

    # 4. 黑科技：查看对象内部所有属性
    print(f"\n--- 对象内部透视 (s1.__dict__) ---")
    # 这就是为什么外部知道有什么属性：虽然看不到代码，但对象自己带着这些信息！
    print(s1.__dict__)
