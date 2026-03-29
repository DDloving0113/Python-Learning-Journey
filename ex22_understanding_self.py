# 题目：Ex22 - 理解 `self` (对象的“我”)
#
# 1. 类 (Class) 是图纸。
# 2. 对象 (Object) 是房子。
# 3. self 是什么？
#    self 就是“这栋房子自己”。
#    当我们在类的方法里写代码时，我们不知道房子还没盖好，
#    所以用 `self` 来代指“未来那个被创建出来的对象”。

class Box:
    def __init__(self, color):
        # 这里的 self，就是正在被创建的那个盒子
        # .color = color 意思是：给这个盒子贴上一个标签，上面写着颜色
        self.color = color
        
        # .items = [] 意思是：给这个盒子挂上一个空袋子
        # 以后我们要往袋子里装东西
        self.items = [] 

    def put(self, thing):
        # 这里的 self，就是调用这个方法的那个盒子
        # self.items.append(thing) 意思是：
        # 把 thing 扔进“我自己”的袋子里
        self.items.append(thing)
        print(f"往 {self.color} 色的盒子里放入了 {thing}")

if __name__ == "__main__":
    # 创建两个盒子
    # box1 就是那个“红色的 self”
    box1 = Box("红")
    # box2 就是那个“蓝色的 self”
    box2 = Box("蓝")

    print(f"box1 的袋子: {box1.items}") # 刚开始是空的
    print(f"box2 的袋子: {box2.items}") # 刚开始也是空的

    # 往 box1 里放苹果
    # 这时，put 方法里的 self 就是 box1
    box1.put("苹果")
    box1.put("菠萝")
    
    # 往 box2 里放香蕉
    # 这时，put 方法里的 self 就是 box2
    box2.put("香蕉")

    print(f"box1 的袋子: {box1.items}") # 只有苹果
    print(f"box2 的袋子: {box2.items}") # 只有香蕉
    print(f"{box1.color}")
