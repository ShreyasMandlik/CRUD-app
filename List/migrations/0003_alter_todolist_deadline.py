# Generated by Django 4.1.2 on 2022-10-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0002_alter_todolist_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='deadline',
            field=models.DateField(),
        ),
    ]
