from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.StudentInfo.as_view()),

    path('score/create/', views.ScoreManager.as_view()),
    path('score/search/', views.ScoreManager.as_view()),
    path('score/delete/', views.ScoreManager.as_view()),

    path('open/search/', views.Open_search),
    path('analysis/', views.Score_Analysis.as_view()),
]