# Generated by Django 4.2.11 on 2024-11-03 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_department_name_az_remove_department_name_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='profile_picture',
        ),
    ]