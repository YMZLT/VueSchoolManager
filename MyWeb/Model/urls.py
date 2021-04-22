from django.urls import path
from . import views

urlpatterns = [
    path('', views.College_list),
    path('<str:college_id>', views.College_detail),
]