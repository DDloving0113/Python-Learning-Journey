import pprint
import json

# 原始数据：学生成绩表 (嵌套字典)
# 结构：ID -> { 姓名, 成绩单{语文, 数学} }
students = {
    "001": {"name": "小明", "score": {"语文": 85, "数学": 92}},
    "002": {"name": "小红", "score": {"语文": 90, "数学": 88}},
    "003": {"name": "小刚", "score": {"语文": 78, "数学": 80}},
}

def calculate_total(students_data):
    """
    第一步：给每个学生算总分，并存入 'total' 字段
    提示：遍历字典，取出 'score' 里的语文和数学相加，赋值给 students_data[id]["total"]
    """
    # TODO: 请实现循环逻辑
    for id, info in students_data.items():
        total = info['score']['语文']+info['score']['数学']
        students_data[id]["total"] = total
    return students_data

def find_best_student_pro(students_data):
    """
    第二步：找到总分最高的学生 (使用 max + lambda)
    提示：
    1. students_data.items() 变成列表: [('001', {...}), ('002', {...})]
    2. 这里的 x 是一个元组 (id, info)，分数在 info['total'] 里
    """
    # TODO: 使用 max() 和 lambda 实现，一行代码搞定
    # return max(..., key=lambda x: ...)
    student_list = students_data.items()
    pprint.pprint(student_list)
    max_student_info = max(student_list, key=lambda x: x[1]['total'])
    return max_student_info

def sort_students_pro(students_data, subject):
    """
    第三步：按指定科目分数排序 (使用 sorted + lambda)
    提示：
    1. 这里的 x 是 (id, info)
    2. 分数在 x[1]['score'][subject]
    """
    # TODO: 使用 sorted() 和 lambda 实现 
    student_list = students_data.items() 
    pprint.pprint(student_list) 
    # 注意：reverse=True 表示从大到小排序
    sorted_student_list = sorted(student_list, key=lambda x: x[1]['score'][subject], reverse=True) 
    return sorted_student_list

def save_to_json(students_data, filename):
    """
    第四步：将处理后的数据保存为 JSON 文件
    """
    with open(filename, 'w', encoding='utf-8') as f:
        # indent=4 美化格式，ensure_ascii=False 显示中文
        json.dump(students_data, f, indent=4, ensure_ascii=False)
    print(f"\n[OK] 结果已保存到 {filename}")



if __name__ == "__main__":
    print("--- 原始数据 ---")
    pprint.pprint(students)

    # 1. 计算总分
    calculate_total(students)
    print("\n--- 计算总分后 ---")
    pprint.pprint(students)
    
    # 2. 找第一名 (取消注释来测试)
    best = find_best_student_pro(students)
    print(f"\n--- 第一名 ---")
    print(best)
    
    # 3. 按数学排序 (取消注释来测试)
    sorted_list = sort_students_pro(students, "数学")
    print(f"\n--- 数学排名 (从高到低) ---")
    pprint.pprint(sorted_list)
    
    # 4. 保存为 JSON 文件
    save_to_json(students, "ex15_student_scores.json")
