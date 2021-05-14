from django.urls import path,re_path
from . import views

urlpatterns = [
    path('superuser/create/',views.SuperUser_create),
    path('superuser/edit/<str:user_id>', views.SuperUser_edit),
    path('superuser/search/',views.SuperUser_search),

    path('college/create/', views.College_create),
    path('college/edit/<str:college_id>', views.College_edit),
    path('college/search/', views.College_search),

    path('student/create/', views.Student_create),
    path('student/edit/<str:student_id>', views.Student_edit),
    path('student/search/', views.Student_search),

    path('teacher/create/', views.Teacher_create),
    path('teacher/edit/<str:teacher_id>', views.Teacher_edit),
    path('teacher/search/', views.Teacher_search),

    path('course/create/', views.Course_create),
    path('course/edit/<str:course_id>', views.Course_edit),
    path('course/search/', views.Course_search),

    path('open/create/', views.Open_create),
    path('open/edit/<str:open_id>', views.Open_edit),
    path('open/search/', views.Open_search),
    path('open/search_detail/', views.Open_search_detail),

    path('score/create/', views.Score_create),
    path('score/search/', views.Score_search),
    path('score/search_detail/', views.Score_search_detail),
    path('score/delete/', views.Score_delete),
    path('score/edit/', views.Score_edit),
]