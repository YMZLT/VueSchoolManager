from django.urls import path
from . import views

urlpatterns = [
    path('<str:teacher_id>', views.Teacher_detail),
]