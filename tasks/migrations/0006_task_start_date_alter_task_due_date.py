# Generated by Django 4.1 on 2023-01-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_options_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(default='2023-01-20T22:06:26.187590'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
