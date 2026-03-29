import json
import pprint
def create_sample_json(filename):
    """创建一个示例的 JSON 文件"""
    data = [
        {"title": "Python Crash Course", "author": "Eric Matthes", "price": 29.99, "in_stock": True},
        {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "price": 25.50, "in_stock": True},
        {"title": "Learning Python", "author": "Mark Lutz", "price": 45.00, "in_stock": False}
    ]
    with open(filename, 'w', encoding='utf-8') as f:
        # indent=4 让输出格式化，ensure_ascii=False 允许中文
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"已生成示例文件: {filename}")

def process_books(filename):
    """读取、处理并保存 JSON 数据"""
    # TODO: 1. 使用 json.load() 读取文件
    # 提示：
    with open(filename, 'r', encoding='utf-8') as f:
        books = json.load(f)
        print("--- 预览数据结构 ---")
        pprint.pprint(books)
        print("-------------------")
    # TODO: 2. 找到价格最高的书并打印标题
    # 提示：可以使用 max() 函数配合 key=lambda...
    most_expensive_book = max(books,key=lambda x:x["price"])
    print(most_expensive_book["title"])
    # TODO: 3. 添加一本新书到列表中
    new_book = {"title": "Fluent Python", "author": "Luciano Ramalho", "price": 39.99, "in_stock": True}
    books.append(new_book)
    # TODO: 4. 将修改后的列表写入 'books_updated.json'
    # 提示：json.dump(books, f, indent=4)
    with open('books_updated.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=1, ensure_ascii=False)
    return most_expensive_book

if __name__ == "__main__":
    filename = "books.json"
    create_sample_json(filename)
    process_books(filename)
    print(process_books(filename))
    
    # 运行后，你会看到生成了 books.json
    # 你的任务是完成 process_books 函数，生成 books_updated.json
