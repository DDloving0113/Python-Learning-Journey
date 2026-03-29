# 题目：
# 在项目根目录下创建一个文本文件（例如 access.log），内容类似：
# 2026-02-21 user1 login
# 2026-02-21 user2 login
# 2026-02-21 user1 view
# 2026-02-22 user1 logout
# 2026-02-22 user3 login


# 要求编写脚本（Python 文件中完成以下逻辑）：
# 1. 逐行读取日志文件内容
# 2. 解析出 date、user、action 三部分
# 3. 统计每个用户的总操作次数，并按次数从多到少打印结果
# 4. 统计每一天有多少“不同用户”访问（用集合去重），按日期从小到大打印结果

def parse_log_file(filename):
    """
    读取文件，逐行解析，返回字典列表
    例如：[{"date": "...", "user": "...", "action": "..."}, ...]
    """
    # 请在此处实现代码
    with open(filename,"r",encoding="utf-8") as f:
        temp_list = []
        for line in f:
            line = line.strip()
            line = line.split()
            temp_dict = {
                "date": line[0],
                "user": line[1],
                "action": line[2],
            }
            temp_list.append(temp_dict)
        return temp_list

def stat_user_activity(logs):
    """
    统计每个用户的总操作次数
    返回：[('user1', 3), ('user2', 1), ...] (按次数从多到少排序)
    """
    log_dict = {}
    for log in logs:
        log_dict[log["user"]] = log_dict.get(log["user"],0)+1
    
    # 使用 sorted + lambda 按次数排序 (从多到少)
    return sorted(log_dict.items(), key=lambda x: x[1], reverse=True)

def stat_daily_unique_visitors(logs):
    """
    统计每一天有多少“不同用户”访问
    返回：[('2026-02-21', 2), ('2026-02-22', 2)] (按日期从早到晚排序)
    """
    log_dict = {}
    output_dict = {}
    for i in logs:
       if i["date"] not in log_dict:
           log_dict[i["date"]] = set()
       log_dict[i["date"]].add(i["user"])
    for i,j in log_dict.items():
        output_dict[i] = len(j)
    
    # 使用 sorted + lambda 按日期排序 (从早到晚)
    # 日期字符串可以直接比较，所以 key 选日期 x[0]
    return sorted(output_dict.items(), key=lambda x: x[0])


if __name__ == "__main__":
    # 1. 读取日志
    logs = parse_log_file("access.log")
    print(logs)
    
    # 2. 打印解析后的前3条数据，检查是否正确
    print("--- 解析结果 ---")
    print(logs[:3])
    
    # 3. 统计并打印用户操作次数
    user_counts = stat_user_activity(logs)
    print("--- 用户操作次数 ---")
    print(user_counts)
    
    # 4. 统计并打印每天独立访客数
    daily_uv = stat_daily_unique_visitors(logs)
    print("--- 每日独立访客 ---")
    print(daily_uv)
    pass
