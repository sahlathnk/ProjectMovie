# Generated by Django 3.2.13 on 2022-07-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='detail',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]