# Generated by Django 4.0.3 on 2022-11-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0004_todolist_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]