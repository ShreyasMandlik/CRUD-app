from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.tasks, name='tasktodone'),
    path('taskdelete/<int:id>', views.taskdelete, name='taskdelete'),
]    