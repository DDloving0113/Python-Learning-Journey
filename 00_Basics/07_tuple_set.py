# 关键技术练习：
# 1. 创建元组 (10,20,30)，尝试修改元素（观察报错），用索引获取第二个元素
t = (10, 20, 30)
print(t[1])
# 2. 用集合给列表[1,2,2,3,3,3]去重，计算两个集合{1,2,3}和{3,4,5}的交集、并集
lst = [1,2,2,3,3,3]
s = list(set(lst))
print(s)
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1 | s2
s4 = s1 & s2
# 3. 判断集合中是否存在某个元素（in）
print(2 in s3)

# 建议项目：编写 “数据去重工具”，接收用户输入的 5 个数字（可能重复），用集合去重后，转换为列表并排序输出
num_list = []
for _ in range(5):
    num = input("Enter a number: ")
    try:
        num = int(num)
        num_list.append(num)
    except ValueError:
        print("Please enter a valid integer.")
        continue

def sort_num(num_list):
    s1 = list(set(num_list))
    s1.sort()
    print(s1)
sort_num(num_list)
