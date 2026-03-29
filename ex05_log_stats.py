logs = [
    "user1,login,2026-01-01",
    "user2,logout,2026-01-01",
    "user1,login,2026-01-02",
    "user1,view,2026-01-02",
    "user2,login,2026-01-02",
    "user3,login,2026-01-02",
]
# 要求：
# 1.
# 写函数
# `clean_logs(raw_logs)`：
# - 返回“清洗后的日志列表”，每条是形如
# `{"user": "user1", "action": "login", "date": "2026-01-01"}`的字典
def clean_logs(logs):
    result = []
    for log in logs:
        log = log.strip()
        if not log:
            continue
        parts = log.split(",")
        if len(parts) != 3:
            continue
        user,action,date = parts
        one = {"user": user, "action": action, "date": date}
        result.append(one)
    return result
clean_one = clean_logs(logs)
print(clean_one)
# 2.
# 写函数
# - 返回一个字典：`{"user1": 3, "user2": 2, ...}`，表示每个用户的操作次数

def stat_user_actions(log):
    user_count_dict = {}
    for i  in log:
        username = i["user"]
        user_count_dict[username]= user_count_dict.get(username, 0)+1
    return user_count_dict

# 写函数
def stat_action_counts(log):
    action_count_dict = {}
    for i in log:
        action_one = i["action"]
        action_count_dict[action_one] = action_count_dict.get(action_one, 0) + 1
    return action_count_dict
print("--- 用户操作次数统计 ---")
print(stat_user_actions(clean_one))
print("--- 操作类型次数统计 ---")
print(stat_action_counts(clean_one))
# - 返回一个字典：`{"login": 4, "logout": 1, "view": 1}`，表示每种操作的出现次数


