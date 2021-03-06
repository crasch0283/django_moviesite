# Generated by Django 4.0.4 on 2022-05-26 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_movie_movieimg_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieImg',
            field=models.ImageField(unique=True, upload_to='images', verbose_name=uuid.uuid4),
        ),
    ]
