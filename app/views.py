from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from config import settings
from .models import Movie
from .forms import MovieForm, UpdateForm

import os


# Create your views here.
def index(request):
    try:
        movies = Movie.objects.all().order_by('-yearReleased')
        if request.method == "POST":
            form = MovieForm(request.POST, request.FILES)
            if form.is_valid():
                movie = Movie(
                    title=form.cleaned_data["title"].lower(),
                    director=form.cleaned_data["director"].lower(),
                    yearReleased=form.cleaned_data["yearReleased"],
                    movieImg=form.cleaned_data["movieImg"]
                )
                movie.save()
                return HttpResponseRedirect("success/")

            else:
                print(form.errors)
                return render(request, "app/createmovie.html", {"forms": form})
        form = MovieForm()
        updateForm = UpdateForm()
        return render(request, "app/index.html", {"movies": movies, "form": form, "updateForm": updateForm})
    except IntegrityError:
        return HttpResponseRedirect("/")


def success(request):
    return render(request, "app/success.html")


def createmovie(request):
    form = MovieForm()
    return render(request, "app/createmovie.html", {"forms": form})


def deletemovie(request, id):
    if request.method == "POST":
        sMovie = Movie.objects.get(pk=id)
        if os.path.exists(settings.MEDIA_ROOT):
            for (dirpath, dirnames, filenames) in os.walk(settings.MEDIA_ROOT + '/images/'):
                for file in filenames:
                    if id in str(file):
                        os.remove(settings.MEDIA_ROOT + '/images/' + file)
        sMovie.delete()
        return HttpResponseRedirect("/")


def searchmovies(request):
    if request.method == "POST":
        try:
            movie = Movie.objects.get(title=request.POST['title'].title())
            return render(request, "app/searchmovies.html", {"movie": movie})
        except ObjectDoesNotExist:
            return render(request, "app/movienotfound.html")


def editmovie(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        mId = request.POST['editId']
        if form.is_valid():
            Movie.objects.filter(id=mId).update(title=form.cleaned_data["title"], director=form.cleaned_data["director"],
                                                yearReleased=form.cleaned_data["yearPublished"])

            return HttpResponseRedirect("/")
        return HttpResponseRedirect("/")


def login_view(request):
    return render(request, "app/login.html")
