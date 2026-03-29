# 题目：Ex20 - 让对象“说话” (Magic Methods: __str__)
#
# 在上一个练习中，我们用 s1.introduce() 来获取信息。
# 但如果我们直接 print(s1)，Python 只会输出一串难看的内存地址：
# <__main__.Student object at 0x000002...>
#
# 这样不仅丑，而且调试时不方便。
# 解决方案：魔法方法 (Magic Method) `__str__`
#
# 只要我们在类里定义了 `__str__` 方法，
# 当我们调用 print(s1) 时，Python 就会自动调用这个方法，
# 并打印它返回的字符串。

class Student:
    def __init__(self, student_id, name, score):
        self.id = student_id
        self.name = name
        self.score = score

    # TODO: 请取消下面代码的注释，并实现它
    def __str__(self):
        """
        返回对象的字符串表示形式。
        """
        # 提示：return f"Student(id='{self.id}', name='{self.name}', score={self.score})"
        return  f"Student(id='{self.id}', name='{self.name}', score={self.score})"

    # 偷懒小技巧：让 repr 直接调用 str
    # 这样打印列表里的对象时，也会变好看！
    __repr__ = __str__

if __name__ == "__main__":
    s1 = Student("001", "Alice", 95)
    s2 = Student("002", "Bob", 59)

    print("--- 直接打印对象 ---")
    # 如果没有实现 __str__，这里会打印内存地址
    # 如果实现了 __str__，这里会打印你返回的字符串
    print(s1)
    print(s2)

    print("\n--- 列表里的对象 ---")
    # 注意：直接打印列表里的对象时，Python 默认调用的是 __repr__ (另一个魔法方法)
    # 所以这里可能还是显示内存地址，这是正常的。
    students = [s1, s2]
    print(students)
