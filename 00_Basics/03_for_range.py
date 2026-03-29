# - **关键技术练习**：
#   1. 用`for`循环打印1-10的数字
#   2. 用`for`循环计算1-100的总和
#   3. 打印1-20中的偶数（用`continue`跳过奇数，或直接用`range(2,21,2)`）


def ins_tance(x):
    return [i for i in range(1,x+1)]
g1 = ins_tance(10)

def add_100(num):
    cnt = 0
    for i in range(1,101):
        cnt += i
    print(cnt)
add_100(100)

# 3. 打印1-20中的偶数（用`continue`跳过奇数，或直接用`range(2,21,2)`）

def double_num(x):
    for i in range(0,21):
        if i%2==1:
            continue
        print(i)

double_num(10)

# - **建议项目**：编写“乘法口诀表生成器”，打印1-9的乘法口诀（如`1×1=1，1×2=2...9×9=81`）
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}" , end=" ")
    print()