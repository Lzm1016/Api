## 初始化数据库
python migrare.py db init

## 自动创建表 脚本
python migrare.py db migrate
## 带提示消息 脚本
python migrare.py db migrate -m 'message'

## 更新(升级)表结构
python migrare.py db upgrade



# Error Code
1000 成功
1001 账号错误/密码错误
1003 参数不能为空
1004 参数格式错误/参数无效