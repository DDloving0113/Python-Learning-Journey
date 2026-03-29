# Python 练习知识库（个人版）

> 这是你在 `PythonProject` 里练习时的“知识库首页”。\
> 建议：每次做完一题/学到一个点，就在这里简单记两句。

***

## 14. 交互式程序的核心：`while True` 主循环

### 14.1 为什么要用 `while True`？

在开发“命令行菜单”、“文字小游戏”或“管理系统”时，如果不用循环，程序执行完一次用户命令后就会直接死亡退出。
使用 `while True:` 可以构建一个\*\*“主循环 (Main Loop)”\*\*，让程序像一个服务生一样：

1. 打印菜单
2. 等待用户输入
3. 执行操作
4. **自动回到第 1 步，等待下一次命令**（不会退出）

### 14.2 如何终结这个死循环？

在 `while True` 内部，必须为用户预留一扇\*\*“逃生门”\*\*。
通常是提供一个“退出”选项，当用户选择该选项时，执行 `break` 语句。
`break` 的作用是：**立刻砸碎并跳出当前所在的循环**，让程序能够自然结束。

**代码模板：**

```python
while True:
    print("1. 记账 | 2. 查账 | 0. 退出")
    choice = input("请选择: ")
    
    if choice == "1":
        print("执行记账逻辑...")
    elif choice == "0":
        print("再见！")
        break  # <--- 逃生门：跳出 while 循环，程序结束
    else:
        print("输入有误，请重试！") # 执行完这句，又会弹回 while 开头重新打印菜单
```

***

## 1. 变量与基本类型

- 变量命名：尽量用有意义的英文单词，不用 a、b、c。
- 常见类型：`int`、`float`、`str`、`bool`、`list`、`dict`、`set`、`tuple`。
- 判断类型：`isinstance(x, (int, float))` 比 `type(x) == int` 更通用。

***

## 2. 条件与循环要点

- 条件判断：
  - 尽量用区间写法：`0 <= score <= 100`。
  - 多个区间用 `if/elif/else`，避免重复判断。
- 循环：
  - 固定次数优先用 `for range(...)`。
  - 不确定次数（直到满足条件才停）用 `while`。
- 提前返回/提前结束：
  - 在函数中，用 `return` 提前结束逻辑。
  - 在循环中，用 `break` 提前跳出。

***

## 3. 数据结构知识点

- 列表 list：
  - 常用：`append`、`insert`、`remove`、列表推导式。
  - 去重：`list(set(lst))`（注意会打乱原来的顺序）。
- 字典 dict：
  - 计数模式：`d[key] = d.get(key, 0) + 1`。
  - 遍历：`for k, v in d.items(): ...`。
  - 合并：Python3.9+ 可用 `d1 | d2`。
- 集合 set：
  - 去重、交集 `&`、并集 `|`、对称差 `^`。
  - 只能存“可哈希”的不可变对象，比如数字、字符串、元组。

***

## 4. 函数与返回值

- 原则：函数“只负责计算结果”，打印交给外面。
- 多个参数需要统一校验时：
  - 可以先打包成元组 `scores = (cn, math, eng)`。
  - 再用 `for` 或 `all()` 统一检查。
- 常见写法：
  - 提前返回错误：`if 不合法: return "错误信息"`。
  - 正常流程写在最后。

***

## 5. 常见易错点（随练随记）

- `int(score)` 会把 50.5 变成 50，如果是字符串会直接报错。
- 在循环中 `for n in ...:`，不要在 `else` 里直接 `return True`，要在循环结束后再 `return True`。
- 在循环体里初始化累加变量或列表，会导致每轮循环都重置，最后只保留最后一次的结果。

***

## 6. 练习题索引（按文件）

### 基础练习 (00\_Basics/)

- `01_print_vars.py` - `15_list_loop_modify.py`：Python 基础语法练习（变量、循环、列表、字典等）。

### 进阶项目 (Root)

- `ex01_calc_safe.py`：安全计算器函数
  - 关键点：运算符分支、除 0 处理、只用 `return` 不在函数里打印。
- `ex02_grade_level.py`：成绩等级评定
  - 关键点：类型和范围校验、区间划分、平均分 + 等级。
- `ex03_prime_tools.py`：质数工具函数
  - 关键点：只需检查到 `sqrt(n)`，在循环外返回 `True`。
- `ex04_cart_checkout.py`：购物车结算升级版
  - 关键点：函数复用（单个商品总价）、循环外初始化累加变量和列表。
- `ex05_log_stats.py`（计划中）：用户日志统计
  - 关键点：字符串拆分、列表转字典、字典计数。
- `ex07_user_clean.py`：数据清洗与去重
  - 关键点：列表推导式、集合去重、lambda 排序。
- `ex08_log_file_analyzer.py`：日志分析（UV统计）
  - 关键点：`split` 解析日志、字典嵌套集合 `set` 进行分组去重。
- `ex09_word_counter_advanced.py`：词频统计进阶
  - 关键点：`lower`、`replace` 预处理、`sorted(d.items())` 字典排序。
- `ex10_filter_lambda.py`：Lambda 与 Filter
  - 关键点：匿名函数语法、列表过滤。
- `ex11_map_reduce.py`：Map 与 Reduce
  - 关键点：函数式编程三剑客、惰性求值。
- `ex12_employee_csv.py`：CSV薪资分析
  - 关键点：`open()` 读取文件、`split(',')` 拆分、分组统计模式（字典存列表）。
- `ex13_csv_robust.py`：健壮的 CSV 解析
  - 关键点：`try-except` 捕获 `ValueError`、`continue` 跳过错误行。

***

## 7. 常用数据结构方法速查 (Cheatsheet)

### 字符串 (str) - 不可变

- `s.lower()` / `s.upper()`: 变大小写（返回新串）。
- `s.strip()`: 去掉首尾空格。

***

## 8. JSON 处理 (json module)

- `json.load(f)`: 读取文件对象 `f`，转为 Python 对象 (dict/list)。
- `json.dump(obj, f, indent=4, ensure_ascii=False)`: 把 Python 对象 `obj` 写入文件 `f`。
  - `indent=4`: 格式化缩进，方便阅读。
  - `ensure_ascii=False`: 允许直接写入中文，不转义。
- `json.loads(s)`: 把 JSON **字符串** 转为 Python 对象。
- `json.dumps(obj)`: 把 Python 对象转为 JSON **字符串**。
- `s.replace(old, new)`: 替换（返回新串）。
- `s.split(sep)`: 拆分成列表（默认按空格）。
- `s.startswith(prefix)` / `s.endswith(suffix)`: 检查开头/结尾。

### 列表 (list) - 可变

- `lst.append(x)`: 加到末尾。
- `lst.extend(iterable)`: 批量加到末尾。
- `lst.sort(key=...)`: 原地排序。
- `sorted(lst, key=...)`: 返回新排序列表。
- `x in lst`: 检查是否存在。

***

## 8. 经典设计模式：分组与统计 (Grouping Pattern)

**场景**：有一堆数据，要把它们按某个字段（比如部门、日期、班级）归类，然后算总和、平均值或计数。

**核心逻辑**：

1. **准备容器**：搞个空字典 `groups = {}`。
2. **遍历数据**：一次拿一条数据 `item`。
3. **提取 Key**：比如 `dept = item["dept"]`。
4. **初始化（防空）**：如果这个 Key 还没在字典里，先给个空列表 `[]`（或者 0）。
5. **追加/累加**：把数据 `append` 进去（或者 `+=`）。

**代码模板**：

```python
# 假设 data 是 [{"dept": "Sales", "salary": 5000}, ...]
groups = {}

# 第一步：分组
for item in data:
    key = item["dept"]
    if key not in groups:
        groups[key] = []  # 第一次遇到，先开个户
    groups[key].append(item["salary"]) # 存进去

# 第二步：统计（可选）
results = {}
for key, values in groups.items():
    results[key] = sum(values) / len(values) # 算平均
```

***

## 9. 文件读取四种姿势 (File Reading Cheatsheet)

| 方法                   | 作用            | 返回类型              | 适用场景                 |
| :------------------- | :------------ | :---------------- | :------------------- |
| **`f.read()`**       | 一口气读完整个文件     | `str` (一个大字符串)    | 文件很小，想直接处理整个文本       |
| **`f.readline()`**   | 只读**一行**      | `str` (单行字符串)     | **跳过标题行**，或者精准控制读每一行 |
| **`f.readlines()`**  | 一口气读完，按行切分    | `list` (列表，每行是元素) | 文件较小，想用列表索引访问某一行     |
| **`for line in f:`** | **(推荐)** 逐行遍历 | `str` (每次循环拿到一行)  | **省内存**！处理大文件首选，最高效  |

### 💡 最佳实践

1. **跳过标题行**：先用一次 `f.readline()`。
2. **处理数据**：接着用 `for line in f:` 循环处理剩下的。

***

## 10. 列表删除技巧（遍历时删除）

### 10.1 `enumerate + del`（找到第一个就删，推荐）

**场景**：遍历列表，命中某个条件后删除该元素，并立刻结束（`return/break`）。

```python
for i, item in enumerate(lst):
    if condition(item):
        del lst[i]
        break
```

要点：

- `enumerate(lst)` 同时拿到索引 `i` 和元素 `item`
- `del lst[i]` 按索引删除
- 删除后一般立刻 `break` / `return`，避免索引位移带来的跳过问题

### 10.2 `remove(value)`（更直观）

**场景**：你已经拿到了“要删的那个对象”，想把它从列表里删掉。

```python
lst.remove(value)
```

要点：

- 只删除第一个匹配
- 如果 `value` 不在列表里会抛 `ValueError`

### 10.3 列表推导式过滤（删除所有匹配，推荐）

**场景**：要删除所有满足条件的元素。

```python
lst = [x for x in lst if not condition(x)]
```

要点：

- 会生成一个新列表（通常没问题）
- 逻辑最清晰、最不容易出错

### 10.4 `pop(index)`（删除并拿到被删元素）

```python
removed = lst.pop(i)
```

要点：

- 需要“删掉并继续使用被删元素”时很方便（比如返回、记录日志）

### 10.5 倒序遍历索引删除（不跳过，适合原地删除多个）

`range(start, stop, step)` 口诀：

- 从 `start` 开始
- 每次加 `step`
- 到 `stop` 为止（不包含 `stop`）

倒序遍历列表索引常用写法：

```python
for i in range(len(lst) - 1, -1, -1):
    if condition(lst[i]):
        del lst[i]
```

解释：

- `start = len(lst) - 1`：最后一个索引
- `stop = -1`：因为 stop 不包含自身，所以写 -1 才能让 0 被遍历到
- `step = -1`：每次减 1，倒着走

### 10.6 `NotImplemented`（比较魔法方法里的“交给系统处理”）

**场景**：在 `__eq__` / `__lt__` 等比较方法里，遇到 `other` 不是同类型对象。

**要点**：

- `NotImplemented` 不是异常，也不是 `False`
- 返回 `NotImplemented` 的意思是：这个比较我不会，让 Python 去尝试“反向比较”或做默认处理
- 常见写法：先判断类型，不匹配就返回 `NotImplemented`，匹配再比较字段

```python
def __eq__(self, other):
    if not isinstance(other, Book):
        return NotImplemented
    return self.title == other.title and self.author == other.author
```

### 10.7 `@property` / `@xxx.setter`（把方法变成“带规则的属性”）

**目的**：对外用 `obj.stock` / `obj.stock = 10` 这种属性写法，但内部仍然能集中做校验规则（比如库存不能为负数）。

**核心概念**：

- `@property`：把一个方法变成“可读属性”（读 `obj.stock` 时会调用这个方法）
- `@stock.setter`：给同一个属性补上“可写入口”（写 `obj.stock = value` 时会调用这个方法）
- 属性名可以换，但 getter 和 setter 必须同名绑定（`stock` 对应 `@stock.setter`，不能乱写成别的名字）

```python
class Book:
    def __init__(self, stock):
        self._stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("stock cannot be negative")
        self._stock = value
```

**内部发生了什么（记住这两条就够）**：

- 读：`obj.stock` 等价于调用 getter（`stock(self)`）
- 写：`obj.stock = x` 等价于调用 setter（`stock(self, x)`）

**为什么要用** **`_stock`（单下划线）**：

- 单下划线是一种约定：表示内部字段
- 避免在 setter 里写 `self.stock = value` 导致无限递归（setter 调 setter）

***

## 11. `print()` 的 `end` 参数（控制结尾与换行）

### 11.1 默认行为

- `print(x)` 等价于 `print(x, end="\n")`
- 也就是打印完会自动换行

### 11.2 自定义结尾

用 `end="..."` 替换默认的换行符：

- `end=" "`：用空格结尾（同一行打印，空格分隔）
- `end=""`：空字符结尾（同一行紧密拼接）
- `end=","`：逗号结尾（类似 CSV 格式）
- `end=" | "`：任意字符串都可以

```python
print("a", end=" ")
print("b", end=" ")
print("c")
# 输出：a b c

print("Hello", end="")
print("World")
# 输出：HelloWorld

print(1, end=",")
print(2, end=",")
print(3)
# 输出：1,2,3
```

### 11.3 易错点

- 连续使用 `end=""` 会导致内容“粘在一行”，需要手动补换行：最后加一个 `print()` 即可

***

## 13. 函数的默认参数 (Default Arguments)

### 13.1 什么是默认参数？

在定义函数时，可以通过 `=` 给参数赋一个初始值。这会让这个参数变成\*\*“选填项”\*\*。

- 如果调用时不传这个参数，它就使用默认值。
- 如果传了，就用传进来的新值覆盖默认值。

```python
def add_expense(date, amount, note=""):
    # note 就是默认参数
    pass

add_expense("10-25", 100)           # 没传 note，note 自动为 ""
add_expense("10-26", 50, "打车")    # 传了 note，note 就是 "打车"
```

### 13.2 ⚠️ 必须遵守的规则：参数排序

在定义函数时，**所有的“默认参数（选填）”必须排在“普通参数（必填）”的后面**。

- **正确写法**：`def func(a, b, c=0):` ✅
- **错误写法**：`def func(a=0, b, c):` ❌（Python 会直接报 SyntaxError 语法错误）

***

### 12.1 今日要点速记

- `@property` 把“方法”变成“可读属性”：读 `obj.x` 会调用 getter
- `@x.setter` 给同一个属性补“可写入口”：写 `obj.x = v` 会调用 setter
- 真正存数据用 `_x`（单下划线内部字段），避免 setter 递归：不要在 setter 里写 `self.x = v`

### 12.2 热身（5 分钟）

把下面 3 句话用自己的话复述一遍（能复述出来就算过关）：

- `obj.x` 不是读变量，它可能在调用代码（getter）
- `obj.x = v` 不是写变量，它可能在做校验（setter）
- 单下划线不是语法限制，是团队约定：外部不要直接改内部字段

### 12.3 练习 A：给 `Book.stock` 加护栏（强制不为负数）

目标文件：`ex23_book_manager.py`

要求：

- 把 `stock` 变成 property
- 允许：`book.stock = 10`
- 禁止：`book.stock = -1`（抛 `ValueError`）
- `sell()` / `restock()` 不用改调用方式，但要确保库存不会被减成负数

自测建议（写完后手动跑）：

```python
b = Book("A", "x", 10, 1)
try:
    b.stock = -1
except ValueError:
    print("ok")
```

### 12.4 练习 B：加一个“只读计算属性”

要求：

- 在 `Book` 里增加一个只读 property：返回本书的库存总价（`price * stock`）
- 这个属性不需要 setter（只读）

自测建议：

```python
b = Book("A", "x", 10, 3)
print(b.value)  # 应该输出 30
```

### 12.5 练习 C：把 `price` 也做成带校验的 property

要求：

- `price` 必须是 `int/float` 且 `>= 0`
- 不合法时抛 `ValueError`
- 内部存 `_price`

自测建议：

```python
b = Book("A", "x", 10, 1)
try:
    b.price = -9
except ValueError:
    print("ok")
```

### 12.6 练习 D：在 `Student` 上做一个“派生属性”

目标文件：`ex24_student_manager_container.py`

要求：

- 增加一个只读 property：根据 `score` 输出等级（例如 A/B/C/D，你自己定规则）
- 不改变 `score` 的存储方式，等级是“读的时候计算出来”的

### 12.7 明日验收标准（你对照自检）

- 能解释：为什么 property 要用 `_x` 存数据
- 能写：读写 property（getter + setter）各 1 个
- 能写：只读 property（只有 getter）1 个
- 能说明：什么时候用 property（需要规则/校验/派生值），什么时候直接用普通属性（纯数据）

