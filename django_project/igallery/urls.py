from django.urls import include, path, re_path
from . import views
from django.http import HttpResponse
from django.contrib.auth import views as auth_views




urlpatterns = [
    re_path(r'^$', views.start),
    re_path(r'^test/$', views.test),
]


