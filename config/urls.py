"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("oauth/", include('social_django.urls', namespace='social')),
    path("admin/", admin.site.urls),
    path("success/", views.success),
    path("createmovie/", views.createmovie, name="createmovie"),
    path('deletemovie/<str:id>', views.deletemovie, name="deletemovie"),
    path('searchmovies/', views.searchmovies, name="searchmovies"),
    path('editmovie/', views.editmovie, name="editmovie"),
    path('movie/<str:id>/', views.movie_details, name="movie_details"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
