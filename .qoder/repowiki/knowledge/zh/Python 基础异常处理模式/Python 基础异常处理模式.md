---
kind: error_handling
name: Python 基础异常处理模式
category: error_handling
scope:
    - '**'
source_files:
    - ex29_exceptions.py
    - ex23_book_manager.py
    - ex13_csv_robust.py
    - 00_Basics/10_file_write_read.py
---

该仓库是一个 Python 学习项目，错误处理主要采用 Python 内置的 try-except 机制，没有自定义的错误类型体系或框架。核心模式包括：

**基本异常捕获**：在 `ex29_exceptions.py` 中展示了标准的 try-except-finally 结构，用于安全除法操作，分别捕获 ValueError（无效数字输入）和 ZeroDivisionError（除零错误），并使用 finally 确保清理代码执行。

**数据验证异常**：在 `ex23_book_manager.py` 中使用 raise ValueError 进行属性验证，如价格不能为负数、库存必须为非负整数等，体现了面向对象设计中的防御性编程。

**健壮的数据处理**：`ex13_csv_robust.py` 展示了在处理脏数据时的异常处理策略，通过 try-except 捕获转换错误并跳过无效记录，保证程序继续运行。

**用户输入验证**：基础语法练习文件（如 `00_Basics/10_file_write_read.py`）广泛使用 try-except 处理用户输入的类型转换错误，提供友好的错误提示而非程序崩溃。

**约定与模式**：
- 优先捕获具体异常类型（ValueError, ZeroDivisionError）而非通用 Exception
- 在数据转换和处理场景中使用异常控制流
- 结合 finally 块进行资源清理
- 面向对象的属性设置器中进行参数验证

该项目作为学习示例，错误处理相对简单直接，未实现复杂的错误码系统、中间件模式或全局异常处理器。