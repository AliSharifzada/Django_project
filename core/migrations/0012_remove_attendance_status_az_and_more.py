# Generated by Django 5.1.2 on 2024-11-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_department_options_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='status_az',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='status_en',
        ),
        migrations.RemoveField(
            model_name='compensation',
            name='amount_az',
        ),
        migrations.RemoveField(
            model_name='compensation',
            name='amount_en',
        ),
        migrations.RemoveField(
            model_name='department',
            name='name_az',
        ),
        migrations.RemoveField(
            model_name='department',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file_az',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file_en',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name_az',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='status_az',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='status_en',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname_az',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='surname_en',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content_az',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='offboardingitem',
            name='item_az',
        ),
        migrations.RemoveField(
            model_name='offboardingitem',
            name='item_en',
        ),
        migrations.RemoveField(
            model_name='onboardingitem',
            name='item_az',
        ),
        migrations.RemoveField(
            model_name='onboardingitem',
            name='item_en',
        ),
        migrations.RemoveField(
            model_name='performancereview',
            name='comments_az',
        ),
        migrations.RemoveField(
            model_name='performancereview',
            name='comments_en',
        ),
        migrations.RemoveField(
            model_name='position',
            name='name_az',
        ),
        migrations.RemoveField(
            model_name='position',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='training',
            name='training_name_az',
        ),
        migrations.RemoveField(
            model_name='training',
            name='training_name_en',
        ),
    ]
