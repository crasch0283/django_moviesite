# Generated by Django 4.0.4 on 2022-05-26 09:27

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_movie_movieimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieImg',
            field=models.ImageField(unique=True, upload_to=app.models.upload_location),
        ),
    ]
