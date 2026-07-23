---
kind: logging_system
name: 日志系统：无专用框架，仅使用 print 与文本文件分析练习
category: logging_system
scope:
    - '**'
source_files:
    - ex08_log_file_analyzer.py
---

本仓库为 Python 学习练习集合，未引入任何专用日志框架（如 logging、loguru、structlog 等），也未定义统一的日志级别、结构化字段或输出路由策略。代码中的“日志”相关逻辑集中在 `ex08_log_file_analyzer.py`，该脚本仅作为练习题，读取根目录下的 `access.log` 文本文件，按空格分割解析出 date/user/action 三列，并统计用户操作次数与每日独立访客数；其本身并不产生应用日志。

全仓库范围内未发现以下与生产级日志系统相关的要素：
- 无 `logging.getLogger`/`logger.info/debug/error` 调用
- 无日志配置文件（如 `logging.conf`、`loguru.yaml`）
- 无集中式 logger 初始化模块或日志工具包
- 无日志轮转、分级输出到不同 sink 的配置
- 除 `print()` 调试输出外，未见 `sys.stderr`/`sys.stdout` 的定向使用

因此，本项目不存在可抽象的“日志系统”，所有输出均通过裸 `print()` 完成，属于教学示例风格而非工程化日志方案。