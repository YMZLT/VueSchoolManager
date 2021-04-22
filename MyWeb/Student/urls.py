from django.urls import path
from . import views

urlpatterns = [
    path('', views.Student_list),
    path('<str:Student_id>', views.Student_detail),
]