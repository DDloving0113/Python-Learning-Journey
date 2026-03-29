students = {
    "001": {"name": "小明", "score": {"语文": 85, "数学": 92}},
    "002": {"name": "小红", "score": {"语文": 90, "数学": 88}},
    "003": {"name": "小刚", "score": {"语文": 78, "数学": 80}},
}

# 要求：
# 1. 写函数 add_total_score(students)：
#    - 在每个学生字典中增加一个 `total` 键，值为语文和数学总分
def add_total_score(students):
    for key, value in students.items():
        # 计算总分
        total = value["score"]["语文"] + value["score"]["数学"]
        # 增加 total 键 (注意题目要求是 "total"，虽然 "total_score" 更清晰，但我们先按题目来)
        value["total"] = total

# 2. 写函数 best_student(students)：
#    - 返回总分最高的学生信息，例如：{"id": "002", "name": "小红", "total": 178}
def best_student(students):
    max_score = 0
    for key, value in students.items():
        if value["total"] > max_score:
            max_score = value["total"]
            max_dict = {"id":key, "name":value["name"], "total":value["total"]}
    return max_dict

# 3. 写函数 sorted_by_subject(students, subject)：
#    - 按某个科目（"语文" 或 "数学"）分数从高到低排序
#    - 返回一个列表，例如：`[("小红", 90), ("小明", 85), ("小刚", 78)]`
def sorted_by_subject(students, subject):
    temp_list = []
    for key, value in students.items():
        # 1. 获取姓名和分数
        name = value["name"]
        score = value["score"][subject]
        
        # 2. 初始化元组 (姓名, 分数)
        # 元组是用圆括号 () 括起来的，比如 ("小红", 90)
        item = (name, score)
        
        temp_list.append(item)
    # 3. 排序
    # key=lambda x: x[1] 表示按元组的第2个元素（分数）来排序
    # reverse=True 表示从高到低（降序）
    temp_list.sort(key=lambda x: x[1], reverse=True)
    return temp_list


if __name__ == "__main__":
    # 测试 add_total_score
    add_total_score(students)
    print("--- 增加总分后的数据 ---")
    print(students)

    # 打印总分最高的学生
    print("--- 总分最高的学生 ---")
    print(best_student(students))

    # 打印按语文排序的列表
    print("--- 按语文成绩排序 ---")
    print(sorted_by_subject(students, "语文"))
    print("--- 按数学成绩排序 ---")
    print(sorted_by_subject(students, "数学"))
