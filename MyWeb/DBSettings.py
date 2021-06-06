# 数据库配置
import sqlalchemy
import pandas as pd

# 1. pymysql 配置


# sqlite 数据库:
# sqlite://<nohostname>/<path>

sqlite = "sqlite:///db.sqlite3"

# Mysql 数据库:
# mysql+pymysql://<user>:<password>@<hostname>:<port>/<database name>
# 如下所示：
mysql = "mysql+pymysql://root:Forget,88@123.60.31.182:3306/schoolnew"


DBSettings = sqlite


# 2. settings 配置

# sqlite数据库
DATABASES_sqlite = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': './db.sqlite3',
    }
}
# mysql数据库
DATABASES_mysql = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'schoolnew',  # 数据库名称，需要实现建好
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'Forget,88',  # 数据库密码
        'HOST': '123.60.31.182',  # 数据库所在主机地址，如果是本机的话，用localhost
        'PORT': '3306',  # 数据库端口
        'OPTIONS': {
            'init_command': 'SET foreign_key_checks = 0;',  # 初始化外键检查为0
            'charset': 'utf8mb4'
        }
    }
}

DATABASES_settings = DATABASES_sqlite

# 数据库初始化
def init_db(DBSettings):
    engine = sqlalchemy.create_engine(DBSettings)
    # 批量添加 按照依赖关系顺序
    tableMap = [
        {"csv": "user", "table": "User"},
        {"csv": "college", "table": "CollegeTable"},
        {"csv": "student", "table": "StudentTable"},
        {"csv": "teacher", "table": "TeacherTable"},
        {"csv": "course", "table": "CourseTable"},
        {"csv": "open", "table": "OpenTable"},
        {"csv": "score", "table": "ScoreTable"}
    ]
    for tableIndex in tableMap:
        df = pd.read_csv('./data/{0}.csv'.format(tableIndex["csv"]))
        df.to_sql(
            name=tableIndex["table"],
            con=engine,
            index=False,
            if_exists='append'
        )
        print("{0}表初始化成功！".format(tableIndex["table"]))


if __name__ == '__main__':
    init_db(DBSettings)