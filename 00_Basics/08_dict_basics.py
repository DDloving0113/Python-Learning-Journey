# 创建字典student = {"name":" 张三", " age":20, "score":{"math":90, "english":85}}
student = {
    "name": "张三",
    "age": 20,
    "score":{
        "math":90,
        "english":85
    }
}
print(student)
# 2. 获取张三的英语成绩（嵌套字典访问），修改年龄为 21，添加 “性别” 字段
print(student["score"])
student["age"] = 21
student["gender"] = "male"
print(student)
# 3. 遍历字典，打印所有键值对
for key in student.keys():
    print(key,end=" ")
print()
for k,v in student.items():
    print(k,v)
for value in student.values():
    print(value)

# 建议项目：编写 “学生信息管理系统（简易版）”，用字典存储 3 个学生的信息（姓名、年龄、成绩 ），实现 “查询所有学生”“根据姓名查询成绩” 功能
student_dict1 = { "bob" : {"age":20,"grade":89},
                "john":{"age":24,"grade":89},
                "david":{"age":25,"grade":89}
                }

def show_student(student):
    i = 0
    for key in student_dict1.keys():
        print(key,end=" ")
        i += 1
        if i == 5:
            print()
            i = 0
def search_grade(name):
    if name in student_dict1.keys():
        print(student_dict1[name]["grade"])
    else:
        print("not exists")

search_grade("bob")
search_grade("john")
search_grade("david")