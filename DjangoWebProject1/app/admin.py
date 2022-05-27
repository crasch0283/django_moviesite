from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "director", "yearReleased"]


# Register your models here.
admin.site.register(Movie, MovieAdmin)
