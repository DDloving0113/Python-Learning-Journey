# 1. 创建列表[1,3,5,7,9]，添加元素 11（append）、在索引 2 插入 6
temp = [1, 3, 5, 7, 9, 11]
print(temp)
temp.insert(2, 6)
print(temp)

# 2. 删除列表中的 5（remove）删除最后一个元素
temp.remove(5)
print(temp)
temp.pop()
print(temp)


# 3. 用列表推导式创建 1-10 的平方列表（ [1,4,9,...,100]）
sqt_list = [i**2 for i in range(1,11)]
print(sqt_list)

# 建议项目：编写 “购物车管理”，创建购物车列表，实现 “添加商品”“删除商品”“查看购物车”功能（固定商品名称，如["苹果", "香蕉"]）
# 固定商品池（练习用，限定只能加这些）
fixed_goods = ["苹果", "香蕉", "橙子"]
# 购物车初始化为空列表（核心操作对象）
shopping_cart = []
# 功能 1：查看购物车（纯列表查操作）
def show_shopping_cart():
    if not shopping_cart:
        print("购物车为空")
    print("购物车包含：",shopping_cart)
# 功能 2：添加商品（练 list 的 append）
def add_shopping_cart(x):
    if x in fixed_goods:
        shopping_cart.append(x)
    else:
        print("不在商品列表内")

# 功能 3：删除商品（练 list 的 remove/pop）
def del_shopping_cart(x):
    if shopping_cart:
        shopping_cart.remove(x)
    else:
        print("购物车为空")

# 统计购物车中各商品的数量（用列表推导式实现）
# 练列表推导式：统计购物车中每个固定商品的数量
def count_goods():
    # 列表推导式：遍历固定商品，统计每个在购物车中的出现次数
    count_list = [(goods, shopping_cart.count(goods)) for goods in fixed_goods]
    print("商品数量统计：", count_list)

# 测试
add_shopping_cart("苹果")
add_shopping_cart("苹果")
add_shopping_cart("香蕉")
count_goods()  # 输出：[('苹果', 2), ('香蕉', 1), ('橙子', 0)]

# 要统计购物车中不重复的水果数量，核心是先对购物车列表做「去重」，再统计去重后的元素个数
def unique_goods():
    unique_list = [g for g in shopping_cart if g  in fixed_goods]
    set_list = set(unique_list)
    print(len(set_list))
unique_goods()