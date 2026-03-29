print("chenille")
print("Hello,Python")

# 定义 5 个不同类型的变量，打印其类型（type()）；
# 用 f-string 格式化输出："我的名字是 XXX，今年 XX 岁，目标 30 天掌握 Python 基础"；
# 编写脚本：接收用户输入的两个数字，计算并打印它们的和、差、积、商。

# name = "dyc"
# age = 20
# height = 18.2
# female = True
# info_list = [name, age, height, female ]
# print( [type(i) for i in info_list])
#
# print(f"我的名字是{name},今年{age}岁，目标30天掌握Python基础")



def calculate1():
    cnt = 0
    while cnt < 2 :
        calcu1 = input("请输入你的数字A ： ")
        try :
            calcu1 = float(calcu1)
        except ValueError:
            print("请输入数值类型数据")
            continue
        calcu2 = input("请输入你的数字B ： ")
        try :
            calcu2 = float(calcu2)
        except ValueError:
            print("请输入数值类型数据")
            continue
        print(calcu1+calcu2,calcu1-calcu2,calcu1*calcu2,calcu1/calcu2)
        cnt += 1

cal = calculate1()


