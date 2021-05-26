from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.Teacher_info.as_view()),
    path('info/student/', views.Student_info.as_view()),
    path('info/edit/', views.Teacher_edit.as_view()),

    path('score/search/', views.Score_search.as_view()),
    path('score/edit/', views.Score_edit.as_view()),

    path('open/search/', views.Open_search.as_view()),

]
