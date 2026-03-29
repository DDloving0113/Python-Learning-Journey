# 题目：Ex23 - 书店管理员 (Book Manager)
#
# 场景：你是一家小书店的店长。
# 任务：用 OOP 的方式管理你的书籍库存。
#
# -----------------------------------------------------------
#
# 【类 1】 Book (书)
#   - 属性：
#     - title (书名)
#     - author (作者)
#     - price (价格)
#     - stock (库存数量)
#   - 方法：
#     - __str__: 返回 "《书名》- 作者 (¥价格) [库存: X]"
#
# 【类 2】 BookManager (书店管理员)
#   - 属性：
#     - books (存放 Book 对象的列表)
#   - 方法：
#     - add_book(title, author, price, stock): 创建书并添加到列表
#     - show_all_books(): 打印所有书
#     - find_book(keyword): 根据书名搜索 (返回包含 keyword 的书籍列表)
#     - total_value(): 计算库存总价值 (所有书的 price * stock 之和)
#
# -----------------------------------------------------------

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        # TODO: 请实现
        # 目标格式："《Python编程》- Guido (¥99.0) [库存: 10]"
        return f"《{self.title}》- {self.author} (¥{self.price}) [库存: {self.stock}]"

    __repr__ = __str__

    def restock(self, count):
        if count <= 0:
            return False
        self.stock += count
        return True
    def sell(self, count):
        if count <= 0:
            return False
        if self.stock < count:
            return False
        self.stock -= count
        return True
    def __eq__(self,other):
        if not isinstance(other,Book):
            return NotImplemented
        return  self.title == other.title and self.author == other.author

    def __lt__(self,other):
        if not isinstance(other,Book):
            return NotImplemented
        return self.price < other.price
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,value):
        if value < 0:
            raise ValueError
        self._stock = value
    @property
    def value(self):
        return self.price*self.stock
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError
        if value < 0:
            raise ValueError
        self._price = value

class BookManager:
    def __init__(self):
        # TODO: 初始化一个空列表来存书
        self.books = []

    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return iter(self.books)

    def __contains__(self, item):
        return item in self.books

    def add_book(self, title, author, price, stock):
        # TODO: 创建 Book 对象并添加到列表
        for book in self.books:
            if book.title == title and book.author == author:
                return book.restock(stock)
        self.books.append(Book(title, author, price, stock))
        return True

    def show_all_books(self):
        print(f"\n--- 书店库存 ({len(self.books)}本) ---")
        # TODO: 遍历打印
        for bk in self.books:
            print(bk)

    def find_book(self, keyword):
        """搜索书名包含 keyword 的书"""
        # 提示：if keyword in book.title
        # TODO: 返回符合条件的 Book 对象列表
        return [i for i in self.books if keyword in i.title ]

    def total_value(self):
        """计算库存总资产"""
        # 提示：遍历所有书，累加 (price * stock)
        # TODO: 返回总金额
        return sum(bk.value for bk in self.books)
    @property
    def inventory_value(self):
        return sum(bk.value for bk in self.books)

    def sell_book(self, title, count):
        for i, book in enumerate(self.books):
            if book.title == title:
                if not book.sell(count):
                    return False
                if book.stock <= 0:
                    del self.books[i]
                return True
        return False

    def remove_out_of_stock(self):
        before_cnt = len(self.books)
        self.books = [bk for bk in self.books if bk.stock  != 0]
        after_cnt = len(self.books)
        return before_cnt- after_cnt


# --- 测试代码 (不要修改) ---
if __name__ == "__main__":
    manager = BookManager()
    
    # 1. 进货
    manager.add_book("Python编程", "Guido", 88.0, 10)
    manager.add_book("Java入门", "Gosling", 77.0, 5)
    manager.add_book("Python数据分析", "Wes", 99.0, 3)
    manager.add_book("C++精髓", "Stroustrup", 66.0, 2)

    # 2. 展示所有
    manager.show_all_books()
    
    # 3. 搜索测试
    print("\n--- 搜索 'Python' ---")
    results = manager.find_book("Python")
    for book in results:
        print(book)
        
    # 4. 算算多少钱
    print(f"\n库存总价值: ¥{manager.total_value()}")
    print(len(manager.books))
    print("aa" in manager.books)
    print([bk for bk in manager.books])
    b = Book("A", "x", 10, 1)
    b.price = 99
    try:
        b.price = -1
    except ValueError:
        print("ok")
