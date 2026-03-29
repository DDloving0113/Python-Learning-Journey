# 编写代码判断一个数是正数、负数还是 0
# 根据用户输入的分数（0-100），判断等级（A：90+，B：80-89，C：60-79，D：<60）
import random
def ifzero(x):
    if x == 0:
        print("zero")
    elif x >0:
        print("positive")
    else :
        print("negative")

co1 = ifzero(3)

def grade_level(x):
    if not isinstance(x, (int, float)):
        print("输入错误：请输入数字类型！")
        return
    if x < 0 or x > 100:
        print("输入错误：分数应在0-100之间！")
        return
    if x > 90 :
        print("grade A ")
    elif 80 <= x <= 90 :
        print("grade B")
    elif 60 <= x <=79 :
        print("grade C")
    else:
        print("grade D")

c1 = grade_level(3)

# 嵌套条件：判断用户是否成年（≥18），成年后再判断是否大于 30 岁
def user_age(x):
    if x >= 18:
        if x < 30:
            print("adult but not 30 years yet")
        else:
            print("over 30 years")
    else:
        print("teenager")

for _ in range(10):
    randi = random.randint(0,100)
    user_age(randi)

# 建议项目：编写 “成绩等级评定系统”，接收用户输入的语文、数学、英语分数，计算平均分后评定等级（优秀：90+，良好：80-89，及格：60-79，不及格：<60）

def grade_sys(cny,math,eng):
    scores = [cny,math,eng]
    for score in scores:
        if not isinstance(score, (int, float)):
            return "数据不符合标准请输入正确数值"
    avg_grade = (math+eng+cny)/3
    if avg_grade >= 90:
        print("A")
    elif avg_grade >= 80:
        print("B")
    elif avg_grade >= 60:
        print("C")
    else:
        print("D")
g1 = grade_sys(87,9879,65)