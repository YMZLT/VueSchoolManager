# 1.安装依赖包

# pip3 install PyMySQL
# pip3 install sqlalchemy

# 2.连接数据库
import pandas as pd
import sqlalchemy
# 连接 Mysql 数据库:
# engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/express')
# 连接 sqlite 数据库:
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
df = pd.read_sql_table('users', engine)
df


