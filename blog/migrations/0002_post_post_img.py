# Generated by Django 3.2 on 2022-09-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]