# Generated by Django 3.2 on 2022-08-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0010_auto_20220830_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='standard_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]