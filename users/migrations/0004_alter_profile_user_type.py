# Generated by Django 3.2 on 2022-02-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220221_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('parent', 'parent')], default='student', max_length=15),
        ),
    ]