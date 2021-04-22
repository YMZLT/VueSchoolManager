# 教务管理系统

## 技术栈

- 前端：vue3.x

- 后端：Django3.x

## 参考资料

1. [Django 官方中文文档](https://docs.djangoproject.com/zh-hans/3.2/)

2. [Django REST framework 中文文档](https://q1mi.github.io/Django-REST-framework-documentation/)

3. [Django Rest Framework 自动生成接口文档的方法](https://cloud.tencent.com/developer/article/1632466)

4. [后台系统参考](http://gl.timemeetyou.com/#/login)

## 文件说明
```
├─.gitignore----------------------------------git忽略文件
├─.prettierrc---------------------------------配置文件
├─babel.config.js-----------------------------配置文件
├─package-lock.json---------------------------配置文件
├─package.json--------------------------------配置文件
├─postcss.config.js---------------------------配置文件
├─README.md-----------------------------------说明文档
├─vue.config.js-------------------------------配置文件
├─src-----------------------------------------前端主要项目文件
|  ├─App.vue----------------------------------项目全局配置文件
|  ├─main.js----------------------------------项目入口文件
|  ├─router.js--------------------------------设置路由
|  ├─plugins----------------------------------UI文件
|  |    └element.js---------------------------引入UI组件
|  ├─components-------------------------------前端页面文件
|  |     ├─Home.vue---------------------------首页
|  |     ├─Login.vue--------------------------登录页面
|  |     ├─Welcome.vue------------------------首页中的main页面
|  |     ├─user-------------------------------用户管理
|  |     |  ├─Students.vue--------------------学生页面
|  |     |  ├─Teachers.vue--------------------教师页面
|  |     |  └ Users.vue-----------------------管理员页面
|  |     ├─course-----------------------------课程管理
|  |     |   └─Courses.vue--------------------课程页面
|  └─assets-----------------------------------资源文件，存放图片等
├─SchoolManagerApi----------------------------后端文件
|        ├─db.sqlite3-------------------------本地数据库
|        ├─manage.py--------------------------主程序入口
|        ├─requirements.txt-------------------依赖文件
|        ├─SchoolManagerApi-------------------项目主文件
|        |        ├─asgi.py-------------------忽略
|        |        ├─settings.py---------------全局设置文件，包括数据库、app设置等
|        |        ├─urls.py-------------------路由设置文件
|        |        └─wsgi.py-------------------忽略
|        └─myWeb------------------------------主要app文件
|            ├─admin.py-----------------------忽略
|            ├─apps.py------------------------忽略
|            ├─jwt.py-------------------------登录验证jwt
|            ├─models.py----------------------数据库模型设定
|            ├─serializers.py-----------------序列化器：转换json数据和python原生数据
|            ├─tests.py-----------------------忽略
|            ├─views.py-----------------------api接口
|            └─migrations---------------------数据库迁移文件
├─public--------------------------------------公共资源文件
└─MyWeb---------------------------------------后端v2(待完成)
````
## 运行方法

### 下载文件
```
git clone https://gitee.com/wgjmcal/vue-school-manager
```
### 运行后端

#### 进入SchoolManagerApi文件夹
```
cd SchoolManagerApi
```
#### 安装依赖

```
pip install -r requirements.txt
```
#### 运行

```
py manage.py runserver 8001
```
> 此处的端口8001需要与前端一致

#### 查看API

浏览器打开：http://127.0.0.1:8001/docs/


### 运行前端

**确保本地已经有node.js环境**

#### 安装依赖
```
npm install
```

#### 编译
```
npm run serve
```

#### 构建运行
```
npm run build
```

### 测试工具
postman

下载连接：https://www.postman.com/

###  测试数据

1. 用户数据

   ```json
   [
       {
           "user_id": "12345678",
           "user_name": "test",
           "user_type": "S",
           "password": "12345678",
           "is_admin": false,
           "college_id": "02",
           "English_class": "C",
           "position": ""
       },
       {
           "user_id": "12345670",
           "user_name": "test0",
           "user_type": "S",
           "password": "pbkdf2_sha256$216000$1OGAs3ZY8nPO$lGOrCkqHRsE6wgx/sc/ADlQBNlkghDLpNMGmj3Ok7kA=",
           "is_admin": false,
           "college_id": "02",
           "English_class": "C",
           "position": ""
       },
       {
           "user_id": "12345671",
           "user_name": "test1",
           "user_type": "S",
           "password": "pbkdf2_sha256$216000$IQioJOf4fBIg$kVBbWLWrlvQE9+c7O7WmRimy7tQotus9eKWR0MA9AkI=",
           "is_admin": false,
           "college_id": "01",
           "English_class": "A",
           "position": ""
       },
       {
           "user_id": "12345672",
           "user_name": "teacher2",
           "user_type": "T",
           "password": "pbkdf2_sha256$216000$uA1ViZhl5s8T$yAx1ixuTSLOJuRUhEoL7Y50fVNFSRq5MLThGV8Cl5HQ=",
           "is_admin": false,
           "college_id": "01",
           "English_class": "",
           "position": "教授"
       },
       {
           "user_id": "12345673",
           "user_name": "teacher3",
           "user_type": "T",
           "password": "pbkdf2_sha256$216000$z0DJjr2I1E3a$1nVveURNonqUngieUiwFM4IOtXP36pxWtETCoWg3BF4=",
           "is_admin": true,
           "college_id": "01",
           "English_class": "",
           "position": "教授"
       }
   ]
   ```

   

2. 学院数据

   ```json
   [
       {
           "college_id": "01",
           "college_name": "计算机学院"
       },
       {
           "college_id": "02",
           "college_name": "材料学院"
       },
       {
           "college_id": "03",
           "college_name": "环化学院"
       },
       {
           "college_id": "04",
           "college_name": "马克思主义学院"
       }
   ]
   ```


3. 课程数据

   ```json
   [
       {
       "course_id":"01",
       "course_name":"数据库原理",
       "credict":6,
       "credit_hour":60,
       "teacher_id":"12345672"
   	},
       {
       "course_id":"02",
       "course_name":"编译原理",
       "credict":4,
       "credit_hour":60,
       "teacher_id":"12345672"
   	},
       {
       "course_id":"03",
       "course_name":"计算机组成原理",
       "credict":5,
       "credit_hour":60,
       "teacher_id":"12345673"
   	},
   ]
   ```

   

4. 开课数据

   ```json
   [
       {
       "opencourse_id":"01",
       "course_id":"01",
       "semaster":"202001",
       "course_time":"星期三5-6"
   	},
       {
       "opencourse_id":"02",
       "course_id":"01",
       "semaster":"202001",
       "course_time":"星期一7-8"
   	},
       {
       "opencourse_id":"03",
       "course_id":"02",
       "semaster":"202002",
       "course_time":"星期一9-10"
   	},
       {
       "opencourse_id":"04",
       "course_id":"03",
       "semaster":"202002",
       "course_time":"星期四3-4"
   	},
       
   ]
   ```

   

5. 选课/成绩数据

   ```json
   [
       {
           "student_id":"12345671",
       	"opencourse_id":"01",
       	"score":90.0
       },
        {
           "student_id":"12345671",
       	"opencourse_id":"02",
       	"score":0
       },
        {
           "student_id":"12345671",
       	"opencourse_id":"03",
       	"score":0
       },
        {
           "student_id":"12345671",
       	"opencourse_id":"04",
       	"score":0
       },
   ]
   ```

   
### 其他

#### 项目目录生成
https://juejin.cn/post/6844903861254094862#heading-2

