from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.Teacher_info),
    path('info/student/', views.Student_info),
    path('info/edit/', views.Teacher_edit),

    path('score/search/', views.Score_search),
    path('score/edit/', views.Score_edit),

    path('open/search/', views.Open_search),

    path('save_pdf/', views.Save_pdf)

]
