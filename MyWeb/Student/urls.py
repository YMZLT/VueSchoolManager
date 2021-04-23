from django.urls import path
from . import views

urlpatterns = [
    path('<str:student_id>', views.Student_detail),
]