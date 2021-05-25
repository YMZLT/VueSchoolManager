# 教务管理系统

## 技术栈

- 前端：vue3.x

- 后端：Django3.x

## 运行方法

### 下载文件
```
git clone https://gitee.com/wgjmcal/vue-school-manager
```
### 运行后端

#### 进入MyWeb文件夹
```
cd MyWeb
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
## 参考资料

1. [Django 官方中文文档](https://docs.djangoproject.com/zh-hans/3.2/)

2. [Django REST framework 中文文档](https://q1mi.github.io/Django-REST-framework-documentation/)

3. [Django Rest Framework 自动生成接口文档的方法](https://cloud.tencent.com/developer/article/1632466)

4. [后台系统参考](http://gl.timemeetyou.com/#/login)

### 测试工具
postman

下载连接：https://www.postman.com/


### 其他

#### 项目目录生成
https://juejin.cn/post/6844903861254094862#heading-2

