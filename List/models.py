from django.db import models

# Create your models here.


class ToDoList(models.Model):
    Task_Name=models.CharField(max_length=50)
    start_date=models.DateField(null=True)
    deadline=models.DateField()
    status=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.Task_Name