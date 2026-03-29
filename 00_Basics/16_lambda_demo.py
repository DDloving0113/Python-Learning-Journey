# 二、练习题（从易到难）
# 基础题
# 用 lambda 函数定义一个 “判断数字是否为奇数” 的函数，调用并验证（如输入 5 返回 True，输入 6 返回 False）。
is_odd = lambda x: x % 2 != 0
print(is_odd(5))
# 用map()+lambda 将列表["a", "b", "c"]中的每个元素转为大写，输出结果。
lst = ["a", "b", "c"]
upper_func = map(lambda x:x.upper(), lst)
print(list(upper_func))
# 进阶题
# 用filter()+lambda 从列表[10, 15, 20, 25, 30]中筛选出能被 15 整除的数。

# 用sorted()+lambda 对列表[{"name":"张三","age":20},{"name":"李四","age":18}]按 “age” 字段升序排序。
# 拓展题
# 用 lambda 函数实现：输入一个列表，返回列表中所有元素的和（提示：结合reduce()，需先导入from functools import reduce）。