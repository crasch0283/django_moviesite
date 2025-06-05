from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, FileInput
from django.utils.translation import gettext as _

from app.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "director", "yearReleased", "movieImg")
        labels = {
            'title': 'Title',
            'yearReleased': 'Year Released',
            'movieImg': 'Movie Image'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'director': TextInput(attrs={'class': 'form-control'}),
            'yearReleased': TextInput(attrs={'class': 'form-control'}),
            'movieImg': FileInput(attrs={'class': 'form-control'}),

        }


class UpdateForm(forms.Form):
    title = forms.CharField(label="Movie Title", max_length=50)
    director = forms.CharField(label="Director", max_length=50)
    yearReleased = forms.CharField(label="Year Released", max_length=4)

    title.widget.attrs.update({'class': 'form-control'})
    director.widget.attrs.update({'class': 'form-control'})
    yearReleased.widget.attrs.update({'class': 'form-control'})
