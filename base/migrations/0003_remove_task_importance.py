# Generated by Django 3.2.7 on 2021-11-06 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='importance',
        ),
    ]
