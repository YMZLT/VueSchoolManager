# 教务管理系统

## 技术栈

- 前端：vue3.x

- 后端：Django3.x

## 运行方法

### 1. 下载文件
```
git clone https://gitee.com/wgjmcal/vue-school-manager
```
### 2. 运行后端

#### 进入MyWeb文件夹
```
cd MyWeb
```
#### 安装依赖

```
pip install -r requirements.txt
```
#### 数据库

这里默认使用django自带的sqlite数据库，使用mysql数据库请看下面[配置mysql数据库](#anchor)

- 数据库迁移

  执行以下数据库迁移命令，会自动创建好在Model/models.py 文件中已定义的表。

  ```shell
  python manage.py makemigrations
  python manage.py migrate
  ```

<img src="./images/image-20210527202446606.png" alt="image-20210527202446606" style="zoom:67%;" />

- 数据库初始化

  ```shell
  python DBSettings.py
  ```

<img src="./images/image-20210527202800704.png" alt="image-20210527202800704" style="zoom:67%;" />

#### 运行后端

```
py manage.py runserver 8001
```
> 此处的端口8001需要与前端一致

<img src="./images/image-20210527203004547.png" alt="image-20210527203004547" style="zoom:67%;" />

#### 查看API

[文档地址](https://documenter.getpostman.com/view/14310338/TzXwGeZ5)


### 3. 运行前端

**确保本地已经有node.js环境**

返回项目文件夹

#### 安装依赖
```
npm install
```

#### 运行
```
npm run serve
```

#### 账号说明

- 管理员账号：
    - user_id : 9001
    - password: admin123

- 教师账号：
    - user_id : 1001
    - password: 12345678

- 学生账号：
    - user_id : 18122801
    - password: 12345678

#### 效果截图

<img src="./images/login.jpg" alt="login" style="zoom:67%;" />

<img src="./images/student_1.jpg" alt="student_1" style="zoom:67%;" />

<img src="./images/student_2.jpg" alt="student_2" style="zoom:67%;" />

<img src="./images/student_3.jpg" alt="student_3" style="zoom:67%;" />

<img src="./images/student_4.jpg" alt="student_4" style="zoom:67%;" />

<img src="./images/teacher_2.jpg" alt="teacher_2" style="zoom:67%;" />

<img src="./images/teacher_3.jpg" alt="teacher_3" style="zoom:67%;" />

<img src="./images/teacher_4.jpg" alt="teacher_4" style="zoom:67%;" />

<img src="./images/teacher_5.jpg" alt="teacher_5" style="zoom:67%;" />

<img src="./images/admin_1.jpg" alt="admin_1" style="zoom:67%;" />

<img src="./images/admin_2.jpg" alt="admin_2" style="zoom:67%;" />

<img src="./images/admin_3.jpg" alt="admin_3" style="zoom:67%;" />

<img src="./images/admin_4.jpg" alt="admin_4" style="zoom:67%;" />

<img src="./images/admin_5.jpg" alt="admin_5" style="zoom:67%;" />

## 其他

### 配置mysql数据库

<span id = "anchor"></span>

默认使用的是自带的sqlite数据库，使用mysql数据库需要重新配置一下。

进入后端文件夹：`./MyWeb/MyWeb/`

找到seetings.py文件，将数据库配置修改一下:

```python
mysql = "mysql+pymysql://root:Forget,88@123.60.31.182:3306/schoolnew"
DBSettings = mysql
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
DATABASES_settings = DATABASES_mysql
```

### 文件说明

```
├─.gitignore----------------------------------git忽略文件
├─.prettierrc---------------------------------配置文件
├─babel.config.js-----------------------------配置文件
├─package-lock.json---------------------------配置文件
├─package.json--------------------------------配置文件
├─postcss.config.js---------------------------配置文件
├─README.md-----------------------------------说明文档
├─vue.config.js-------------------------------配置文件
├─images--------------------------------------效果截图
├─src-----------------------------------------前端主要项目文件
|  ├─App.vue----------------------------------项目全局配置文件
|  ├─main.js----------------------------------项目入口文件
|  ├─router.js--------------------------------设置路由
|  ├─plugins----------------------------------UI文件
|  |    └element.js---------------------------引入UI组件
|  ├─components-------------------------------前端页面文件
|  |     ├─Login.vue--------------------------登录页面 管理员、教师、学生共享页面
|  |     |-admin------------------------------管理员页面文件夹
|  |     |-student----------------------------学生页面文件夹
|  |     |-teacher----------------------------教师页面文件夹
|  └─assets-----------------------------------资源文件，存放图片等
├─MyWeb---------------------------------------后端文件
|        ├─db.sqlite3-------------------------本地数据库
|        ├─manage.py--------------------------主程序入口
|        ├─requirements.txt-------------------依赖文件
|        └─MyWeb------------------------------项目主文件
└─public--------------------------------------公共资源文件
````
### 测试工具

postman

下载连接：https://www.postman.com/

## 参考资料

1. [Django 官方中文文档](https://docs.djangoproject.com/zh-hans/3.2/)

2. [Django REST framework 中文文档](https://q1mi.github.io/Django-REST-framework-documentation/)

3. [Django Rest Framework 自动生成接口文档的方法](https://cloud.tencent.com/developer/article/1632466)

4. [后台系统参考](http://gl.timemeetyou.com/#/login)



