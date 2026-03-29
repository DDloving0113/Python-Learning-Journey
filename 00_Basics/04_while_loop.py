# 关键技术练习：
# 1. 用while循环打印 1-10 的数字
i = 1
while i < 11:
    print(i, end=" ")
    i += 1


# 2. 用while循环计算 1-50 的偶数和
x = 0
h = 0
while h < 51:
    if h%2 == 0 :
        x += h
    h += 1
    if h == 51:
        print(x, end=" ")

# while适合未知次数
# 3. 编写 “猜数字游戏雏形”：固定一个数字（如 15），用户反复输入猜测，直到猜中（暂时不限制次数）
import random
num = 10
while x != num:
    try:
        x = int(input("请输入数字"))
    except ValueError:
        print("请输入数值类型")
        continue
    if x < num:
        print("smaller num")
    elif x > num:
        print("bigger num")
print("congratulation")


   # 建议项目：编写 “计数器”，用户输入一个正整数n，用while循环从 1 数到 n，每数 5 个数换行
def calcu_num(x):
    cnt = 1
    idx = 0
    while cnt <= x:
        print(cnt, end=" ")
        idx += 1
        if idx == 5:
            print()
            idx = 0
        cnt += 1
calcu_num(10)






