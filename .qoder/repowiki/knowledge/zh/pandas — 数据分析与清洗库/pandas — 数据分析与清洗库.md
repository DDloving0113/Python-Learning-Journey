---
kind: external_dependency
name: pandas — 数据分析与清洗库
slug: pandas
category: external_dependency
category_hints:
    - vendor_identity
scope:
    - '**'
---

### pandas
- 角色：本项目唯一引入的第三方库，用于 CSV/JSON 数据读取、筛选、新增列、排序、groupby 聚合以及缺失值/重复值处理等数据清洗任务。
- 集成点：`ex36_pandas_data_cleaning.py`（最新综合练习）及 `pandas_1_read.py` ~ `pandas_4_groupby.py` 系列教程脚本；通过 `import pandas as pd` 使用。
- 使用模型：以 DataFrame/Series 为中心的数据分析工作流，尚未涉及数据库、Web 框架或持久化服务。
- 方向：后续学习重点为多表合并（merge/concat）、时间序列、可视化等进阶能力。