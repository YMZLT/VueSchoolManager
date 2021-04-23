from django.urls import path
from . import views

urlpatterns = [
    path('college', views.College_list),
    path('college/<str:college_id>', views.College_detail),
    path('student', views.Student_list),
    path('student/<str:student_id>', views.Student_detail),
    path('teacher', views.Teacher_list),
    path('teacher/<str:teacher_id>', views.Teacher_detail),
    path('course', views.Course_list),
    path('course/<str:course_id>', views.Course_detail),
    path('open', views.Open_list),
    path('open/<str:open_id>', views.Open_detail),
    path('score', views.Score_list),
    path('score/<str:student_id>', views.Score_detail),
]