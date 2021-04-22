## 教务管理系统

### 资料参考

#### Django Rest Framework 自动生成接口文档的方法

https://cloud.tencent.com/developer/article/1632466

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

   