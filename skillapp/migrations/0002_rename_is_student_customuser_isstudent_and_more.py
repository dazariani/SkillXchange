# Generated by Django 5.1 on 2024-08-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_student',
            new_name='isStudent',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_tutor',
        ),
        migrations.AddField(
            model_name='customuser',
            name='isTutor',
            field=models.BooleanField(default=False),
        ),
    ]
