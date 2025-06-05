from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .models import Movie
from .forms import MovieForm, UpdateForm

import os


# Create your views here.
@login_required
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


@login_required
def success(request):
    return render(request, "app/success.html")


@login_required
def createmovie(request):
    form = MovieForm()
    return render(request, "app/createmovie.html", {"forms": form})


@login_required
def deletemovie(request, id):
    if request.method == "POST":
        sMovie = Movie.objects.get(pk=id)
        if os.path.exists(settings.MEDIA_ROOT):
            for (dirpath, dirnames, filenames) in os.walk(settings.MEDIA_ROOT + '/images/'):
                for file in filenames:
                    if id in str(file):
                        os.remove(settings.MEDIA_ROOT + '/images/' + file)
        sMovie.delete()
        return HttpResponseRedirect("http://127.0.0.1:8000/")


@login_required
def searchmovies(request):
    if request.method == "POST":
        try:
            movie = Movie.objects.get(title=request.POST['title'].title())
            return render(request, "app/searchmovies.html", {"movie": movie})
        except ObjectDoesNotExist:
            return render(request, "app/movienotfound.html")


@login_required
def editmovie(request):
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        mId = request.POST['editId']
        if form.is_valid():
            Movie.objects.filter(id=mId).update(
                title=form.cleaned_data["title"], 
                director=form.cleaned_data["director"],
                yearReleased=form.cleaned_data["yearReleased"]
            )
            return HttpResponseRedirect("/")
        return HttpResponseRedirect("/")


def login_view(request):
    return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


@login_required
def movie_details(request, id):
    try:
        movie = get_object_or_404(Movie, pk=id)
        return render(request, "app/movie_details.html", {"movie": movie})
    except Exception as e:
        print(f"Error in movie_details: {e}")
        return HttpResponseRedirect("/")
