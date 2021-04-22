
from django.urls import include, path
from myWeb import views
from myWeb import jwt
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

# 创建超级用户 python manage.py createsuperuser
# 运行 ：py manage.py runserver 8001

myUrls = [
    path('user/', views.User_list),
    path('user/<str:user_id>/', views.User_detail),
    path('student/', views.Student_list),
    path('student/<str:user_id>/', views.Student_detail),
    path('teacher/', views.Teacher_list),
    path('teacher/<str:user_id>/', views.Teacher_detail),
    path('college/', views.College_list),
    path('college/<str:college_id>/', views.College_detail),
    path('course/', views.Course_list),
    path('course/<str:course_id>/', views.Course_detail),
    path('courseopen/', views.CourseOpen_list),
    path('courseopen/<str:opencourse_id>/', views.CourseOpen_detail),
    path('score/', views.Score_list),
    path('score/<str:college_id>/', views.Score_detail),
]

urlpatterns = [
    # jwt的token认证接口
    path('login/', jwt.obtain_jwt_token),
    path('',include(myUrls)),
    path('docs/', include_docs_urls(title='说明文档')),
]
