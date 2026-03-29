# 关键技术练习：
# 1. 用双层for循环打印等腰三角形（用*组成，如 3 行)
n = 4
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(1+(i-1)*2):
        print("*",end=" ")
    print()
# 2. 遍历 1-100，打印所有能被 3 整除且不能被 5 整除的数
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        print(i,end=" ")
# 3. 用while嵌套实现 “猜数字游戏进阶”：限制 5 次机会，没猜中提示 “太大” 或 “太小”
i = 1
num = 20
while i <=  5:
    guess_input = input("Guess the number: ")
    try:
         guess_num= int(guess_input)
    except ValueError:
        print("Please enter a number")
        continue
    if num == guess_num:
        print("Correct")
        break
    i += 1
    if i > 5:
        print("Too many times")

# 建议项目：编写 “简易质数判断器”，接收用户输入的整数 n，判断 n 是否为质数（只能被 1 和自身整除，≥2），并打印 1-n 之间的所有质数

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_prime(n):

    if not isinstance(n, int):
        print("Please enter a number")
        return
    prime_list = []
    if n< 2:
        print(f"0-{n}之间没有质数")
        return
    for i in range(2,n+1):
        if isPrime(i):
            prime_list.append(i)
    print(prime_list)
try:
    num = int(input("Enter a number: "))
    find_prime(num)
except ValueError:
    print("Please enter a number")

