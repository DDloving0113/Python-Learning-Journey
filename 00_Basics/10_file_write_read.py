# with open("./test.txt","wb") as f:
#     f.write(b"AAABBBCCC")
# with open("./test.txt","rb") as f:
#     for i in range(3):
#         data = f.read(3)
#         print(f'第{i+1}次读取：{data},指针位置：{f.tell()}')


for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}" , end=" ")
    print()

# 用while嵌套实现 “猜数字游戏进阶”：限制 5 次机会，没猜中提示 “太大” 或 “太小”
random_num = 89
cnt = 0
while cnt < 5:
    try:
        guess_num = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a number")
        continue
    if random_num == guess_num:
        print("Correct")
        break
    else:
        print("Try again")
    cnt += 1
    if cnt == 5:
        print("Too many times")
