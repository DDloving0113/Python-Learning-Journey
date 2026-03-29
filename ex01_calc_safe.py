# 1）安全计算器函数
# - 要求：写一个函数 calc(a, b, op) ，支持四种运算： + - * /
# - 行为规则：
#   - 如果 op 是 "+" 、 "-" 、 "*" 、 "/" 之一，返回运算结果
#   - 如果 op 是其他字符串，返回 "未知运算符"
#   - 如果是除法且 b 为 0，返回 "除数不能为 0"
# - 只用 return 返回结果，不在函数里 print
# - 再写一小段代码，调用这个函数，针对几组输入，把返回值 print 出来

def calc(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0:
            return "除数不能为0"
        else:
            return a/b
    else:
        return "unknown operator"

a1 = calc(1,8,"+")
a2 = calc(1,8,"-")
a3 = calc(1,8,"/")
a4 = calc(1,8,"===")
print(a1,a2,a3,a4)

def calc(a, b, op):
    if op == "/":
        if b == 0:
            return "除数不能为 0"
        return a / b

    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
    }

    if op in ops:
        return ops[op]
    return "未知运算符"


