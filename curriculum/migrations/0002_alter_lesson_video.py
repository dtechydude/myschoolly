# Generated by Django 3.2 on 2022-09-10 19:57

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]