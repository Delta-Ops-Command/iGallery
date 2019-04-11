from django.urls import include, path, re_path
from . import views
from django.http import HttpResponse
from django.contrib.auth import views as auth_views




urlpatterns = [
    re_path(r'^$', views.start, name="default"),
    re_path(r'^test/$', views.test, name="test"),
    re_path(r'^upload/$', views.upload_image, name="upload_image"),
]


