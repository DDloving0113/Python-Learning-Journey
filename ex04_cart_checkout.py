# 给定购物车列表：
cart = [
     {"name": "牛奶", "price": 6, "count": 2, "discount": 0.9},
     {"name": "面包", "price": 4, "count": 3, "discount": 1.0},
     {"name": "鸡蛋", "price": 1, "count": 10, "discount": 0.8},
 ]
# 1.
# 写函数
# ``：返回单个商品的折后总价  price * count * discount`
def calc_item_total(i):
        total = i["price"] * i["count"] * i["discount"]
        return total
# 2.
# 写函数
def checkout(item):
    check_out_dict = {}
    cart_list = []
    grand_total = 0
    for i in item:
        total = calc_item_total(i)
        cart_list.append({"name": i["name"], "total": total})
        grand_total += total
    check_out_dict["item"] = cart_list
    check_out_dict["grand_total"] = grand_total
    return check_out_dict

print(checkout(cart))
# `{"items": [{"name": "牛奶", "total": 10.8}, ...], "grand_total": 23.4}`
# 主程序中调用
# `checkout`，把结果美观地打印出来。