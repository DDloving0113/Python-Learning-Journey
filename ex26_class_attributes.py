"""
题目：Ex26 - 类属性与类方法 (Class Attributes & Class Methods)

目标：理解“类共享的数据”与“对象独立的数据”之间的区别。

场景：银行账户开户系统
要求创建一个 `BankAccount`（银行账户）类。

1) 类属性 (Class Attributes) - 全局共享：
   - `bank_name` = "Python Bank" (所有账户共用的银行名称)
   - `total_accounts` = 0 (用于记录总共创建了多少个账户)

2) 实例属性 (Instance Attributes) - 每个对象独立：
   - `account_id` (账号，每次创建对象时由外部传入)
   - `balance` (余额，默认为 0)

3) 方法：
   - `__init__(self, account_id)`: 
     初始化时，将传入的账号保存为实例属性，并将 `total_accounts` 这个“类属性”的值加 1。
   
   - 普通方法 `deposit(self, amount)`:
     存款，让余额增加。

4) 类方法 (Class Methods)：
   - 使用 `@classmethod` 装饰器定义一个方法 `get_bank_info(cls)`:
     返回一个字符串，包含银行的名称和目前总开户数。
     例如："Welcome to Python Bank! Total accounts: 2"
"""

from functools import total_ordering


class BankAccount:
    # 1. 在这里定义类属性 (直接写在类里面，不要写在 __init__ 里)
    bank_name = "Python Bank"
    total_accounts = 0



    def __init__(self, account_id):
        # 2. 在这里定义实例属性，并更新类属性 total_accounts
        self.account_id = account_id
        self.balance = 0
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance +=  amount
        return True


    # 3. 在这里定义类方法
    @classmethod
    def get_bank_info(cls):
        return f"Welcome to {cls.bank_name}! Total accounts: {cls.total_accounts}"


if __name__ == "__main__":
    # 测试代码（等您写完后我们解除注释）
    
    print(BankAccount.get_bank_info())  # 还没开户，应该显示 Total accounts: 0
    
    acc1 = BankAccount("1001")
              
    acc2 = BankAccount("1002")
    acc1.deposit(500)
    
    print(BankAccount.get_bank_info())  # 开了两个户，应该显示 Total accounts: 2
    print(f"Acc1 Bank: {acc1.bank_name}, Balance: {acc1.balance}") # Python Bank, 500