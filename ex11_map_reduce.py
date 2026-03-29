from functools import reduce

# 题目：Python 三剑客 (Map, Filter, Reduce) 实战
# 任务：
# 1. 使用 map 将所有价格打 8 折。
# 2. 使用 filter 过滤出打折后仍然 > 50 的商品。
# 3. 使用 reduce 计算这些商品的总价。

# 数据：商品价格列表
prices = [100, 45, 80, 20, 200, 60]

def apply_discount(price_list):
    """
    1. Map: 所有价格 * 0.8
    提示：map(lambda x: ..., price_list)
    """
    # 请在此处实现代码
    discounted_price_list = map(lambda x : x*0.8, price_list)
    return list(discounted_price_list)

def filter_high_prices(price_list):
    """
    2. Filter: 过滤出 > 50 的价格
    提示：filter(lambda x: ..., price_list)
    """
    # 请在此处实现代码
    high_50 = filter(lambda x: x>50, price_list)
    return list(high_50)

def calculate_total(price_list):
    """
    3. Reduce: 计算总和
    提示：reduce(lambda x, y: x + y, price_list)
    """
    # 请在此处实现代码
    sum_total = reduce(lambda x, y: x + y, price_list)
    return sum_total

if __name__ == "__main__":
    print(f"原价: {prices}")

    # 1. 打折
    discounted = apply_discount(prices) if apply_discount(prices) else []
    print(f"打折后: {discounted}")
    #
    # # 2. 过滤
    filtered = filter_high_prices(discounted) if filter_high_prices(discounted) else []
    print(f"大于50的: {filtered}")
    #
    # 3. 总和
    total = calculate_total(filtered)
    print(f"最终总价: {total}")
