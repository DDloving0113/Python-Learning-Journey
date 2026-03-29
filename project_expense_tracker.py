
"""
实战项目：本地记账本管理系统 (Expense Tracker)

项目目标：将前面学过的 OOP、异常处理、JSON 文件读写、模块化全部串联起来，做一个真正能用的小软件。

需求分析（第一阶段：核心逻辑设计）：
我们要设计一个 `ExpenseManager` 类，用来管理账单。
每一笔账单，我们可以用一个字典来表示，比如：
{"id": 1, "date": "2023-10-25", "category": "餐饮", "amount": 45.5, "note": "午饭"}

要求：
请完成下面 `ExpenseManager` 类的基础功能：
1. `__init__`：初始化一个空的列表 `self.expenses = []` 来存账单。
2. `add_expense`：接收金额、分类和备注，构造一个账单字典，加入到列表中。
   - 注意：要有自动生成唯一 ID 的逻辑（比如取当前列表长度 + 1）。
3. `get_total_expense`：计算并返回当前所有账单的总金额。

(注意：这节课我们先不写文件读写和用户输入，先纯写类的核心逻辑，测试跑通了再加新功能)
"""

import json
import os

class ExpenseManager:
    def __init__(self, filename="expenses.json"):
        # 1. 初始化账单列表和文件路径
        self.filename = filename
        self.expenses = []
        # 初始化时自动尝试加载数据
        self.load_data()

    def add_expense(self, date, category, amount, note=""):
        """添加一笔新账单"""
        # 2. 生成新账单的字典，并加入到 self.expenses 中
        id = len(self.expenses)+1
        tem_dict = {
            "id" :id,
            "date":date,
            "category":category,
            "amount":amount,
            "note":note
            
        }
        self.expenses.append(tem_dict)
        self.save_data()
        return True
    def get_total_expense(self):
        """计算总支出"""
        # 3. 遍历 self.expenses，把所有 amount 加起来返回
        total_expense = 0
        for item in self.expenses:
            exp = item["amount"]
            total_expense += exp
        return total_expense

    def delete_expense(self, expense_id):
        """
        删除指定 ID 的账单
        提示：
        1. 遍历 self.expenses 寻找匹配的 ID。
        2. 如果找到了，用 self.expenses.remove(那个账单字典) 删除它。
        3. 删除后，别忘了调用 self.save_data() 保存到硬盘。
        4. 如果删除了，返回 True；如果没找到这个 ID，返回 False。
        """
        for i in self.expenses:
            if i['id'] == expense_id:
                self.expenses.remove(i)
                self.save_data()
                return True
        return False




    # ================== 第二阶段：数据持久化 ==================
    def save_data(self):
        """将 self.expenses 保存到 self.filename 中 (JSON格式)"""
        # 请在这里使用 with open 和 json.dump
        with open(self.filename,"w",encoding="utf-8") as f:
            json.dump(self.expenses,f,ensure_ascii=False,indent =4)

    def load_data(self):
        """从 self.filename 中读取数据到 self.expenses 中"""
        # 提示：需要先检查文件是否存在，不存在就直接 return
        # 请在这里使用 with open 和 json.load
        if not os.path.exists(self.filename):
            return 
            
        with open(self.filename,"r",encoding="utf-8") as f:
            self.expenses = json.load(f)
    






if __name__ == "__main__":
    # ================== 第三阶段：用户交互菜单 ==================
    manager = ExpenseManager()
    
    while True:
        print("\n=== 💰 本地记账本管理系统 ===")
        print("1. 记一笔账")
        print("2. 查看所有账单")
        print("3. 查看总支出")
        print("4. 删除一笔账单")
        print("0. 退出系统")
        
        choice = input("请输入操作编号: ")
        
        if choice == "1":
            # 提示：在这里用 input() 依次让用户输入日期、分类、金额、备注
            try:
                date = input("请输入记账日期")
                class_info = input("请输入记账类型")
                amount = float(input("请输入交易金额"))
                note_info = input("请输入备注详细信息")
                # 然后调用 manager.add_expense(...)
                manager.add_expense(date,class_info,amount,note_info)
            # 注意：input() 拿到的是字符串，金额需要转成 float（可以考虑加上 try...except 防止用户乱输）
            except ValueError:
                print("请输入正确格式的交易金额")
            
        elif choice == "2":
            # 提示：在这里打印出当前有几笔账单，并遍历 manager.expenses 打印详情
            print(f"当前共有 {len(manager.expenses)} 笔账单：")
            for i in manager.expenses:
                print(i)
            
        elif choice == "3":
            # 提示：调用 manager.get_total_expense() 并打印
            print(f"当前总支出：{manager.get_total_expense()} 元")
            
        elif choice == "4":
            # 提示：让用户输入要删除的账单 ID，然后调用 manager.delete_expense(...)
            # 根据返回的 True 或 False 打印相应的提示信息
            try:
                del_id = int(input("请输入需要删除的id编号: "))
                is_deleted = manager.delete_expense(del_id)
                if is_deleted:
                    print(f"成功删除 ID 为 {del_id} 的账单！")
                else:
                    print(f"删除失败：找不到 ID 为 {del_id} 的账单。")
            except ValueError:
                print("错误：ID 必须是数字！")
            
        elif choice == "0":
            print("感谢使用，再见！")
            break
            
        else:
            print("❌ 无效的输入，请重新选择！")
