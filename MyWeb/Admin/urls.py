from django.urls import path
from . import views

urlpatterns = [
    path('superuser/create/',views.SuperUser_create.as_view()),
    path('superuser/edit/<str:user_id>', views.SuperUser_edit.as_view()),
    path('superuser/search/',views.SuperUser_search.as_view()),

    path('college/create/', views.College_create.as_view()),
    path('college/edit/<str:college_id>', views.College_edit.as_view()),
    path('college/search/', views.College_search.as_view()),

    path('student/create/', views.Student_create.as_view()),
    path('student/edit/<str:student_id>', views.Student_edit.as_view()),
    path('student/search/', views.Student_search.as_view()),

    path('teacher/create/', views.Teacher_create.as_view()),
    path('teacher/edit/<str:teacher_id>', views.Teacher_edit.as_view()),
    path('teacher/search/', views.Teacher_search.as_view()),

    path('course/create/', views.Course_create.as_view()),
    path('course/edit/<str:course_id>', views.Course_edit.as_view()),
    path('course/search/', views.Course_search.as_view()),

    path('open/create/', views.Open_create.as_view()),
    path('open/edit/<str:open_id>', views.Open_edit.as_view()),
    path('open/search/', views.Open_search.as_view()),
    path('open/search_detail/', views.Open_search_detail.as_view()),

    path('score/create/', views.Score_create.as_view()),
    path('score/search/', views.Score_search.as_view()),
    path('score/search_detail/', views.Score_search_detail.as_view()),
    path('score/delete/', views.Score_delete.as_view()),
    path('score/edit/', views.Score_edit.as_view()),

    path('score/analysis/<str:semester>', views.Score_Analysis.as_view()),
]