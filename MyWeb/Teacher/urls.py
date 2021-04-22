from django.urls import path
from . import views

urlpatterns = [
    path('', views.Teacher_list),
    path('<str:Teacher_id>', views.Teacher_detail),
]