from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.Student_info),
    path('info/edit/', views.Student_edit),

    path('score/create/', views.Score_create),
    path('score/search/', views.Score_search),
    path('score/delete/', views.Score_delete),

    path('course/search/', views.Course_search),
]