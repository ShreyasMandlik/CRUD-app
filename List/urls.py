from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.tasks, name='tasktodone'),
    path('taskdelete/<int:id>', views.taskdelete, name='taskdelete'),
    path('taskupdate/<int:id>', views.taskupdate, name='taskupdate'),
    path('edit/<int:id>', views.edit, name='edit'),
]    