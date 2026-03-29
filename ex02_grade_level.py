# ### 2）成绩等级评定（函数版）
#
# - 题目：
#   参考你之前写过的成绩判断函数，现在要求拆成两个函数：
#   1. `get_level(score)`
#      - 非数字或不在 `0–100` 范围内，返回 `"分数不合法"`
#      - 否则按区间返回 `"A" / "B" / "C" / "D"` 之一
#   2. `avg_level(cn, math, eng)`
#      - 先判断三个分数是否都合法（数字类型，且都在 `0–100` 之间）
#      - 有任何一个不合法时，返回 `"有不合法的分数"`
#      - 否则计算平均分，调用 `get_level` 得到等级，并返回 `(avg, level)` 这样的元组
#   主程序中调用 `avg_level`，把平均分和等级打印出来。

def get_level(score):
    if not isinstance(score,(int,float)) or 0 <= score <= 100:
        return "分数不合法"
    if score <= 60:
        return "D"
    elif score <= 75:
        return "C"
    if score <= 90:
        return "B"
    if score <= 100:
        return "A"
print(get_level(50))

def avg_level(cn,math,eng):
    def is_valid_score(score):
        if not isinstance(score,(int,float)):
            return False
        if not (0 <= score <= 100):
            return False
        return True
    if not is_valid_score(cn) or  is_valid_score(math) or  is_valid_score(eng):
        return "不合法的类型"
    avg_score = (cn+math+eng)/3
    score_level = get_level(avg_score)
    score_tuple = (avg_score,score_level)
    return score_tuple







