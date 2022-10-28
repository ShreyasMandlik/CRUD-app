from django.db import models

# Create your models here.


class ToDoList(models.Model):
    Task_Name=models.CharField(max_length=50)
    deadline=models.DateField()


    def __str__(self):
        return self.Task_Name