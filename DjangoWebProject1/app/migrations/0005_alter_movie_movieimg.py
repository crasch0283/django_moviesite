# Generated by Django 4.0.4 on 2022-05-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_movie_movieimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieImg',
            field=models.ImageField(unique=True, upload_to='images/<django.db.models.fields.UUIDField>'),
        ),
    ]