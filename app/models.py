from uuid import uuid4

from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'images/%s.%s' % (instance.id, extension)


class Movie(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(3)])
    director = models.CharField(max_length=50)
    yearReleased = models.CharField(max_length=4)
    movieImg = models.ImageField(upload_to=upload_location, unique=True)
    timeStamp = models.DateTimeField(auto_now=True)
