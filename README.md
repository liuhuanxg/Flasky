## 项目功能

1. 目录功能
2. 子目录
3. 表单定制
4. 通用接口
5. 权限配置
6. 缓存配置
7. 历史记录

## 表设计

1、目录表

| 字段名称       | 类型     | 描述       |
| -------------- | -------- | ---------- |
| id             | int      | 自增主键id |
| directory_name | varchar  | 名称       |
| add_time       | Datetime | 添加时间   |
| update_time    | datetime | 更新时间   |
| sort           | int      | 排序       |
| status         | boolean  | 是否在用   |

2、子目录

| 字段名称          | 类型 | 描述       |
| ----------------- | ---- | ---------- |
| id                | int  | 自增主键id |
| subdirectory_name |      |            |
|                   |      |            |
|                   |      |            |

