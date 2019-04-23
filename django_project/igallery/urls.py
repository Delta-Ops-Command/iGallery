from django.urls import include, path, re_path
from . import views
from django.http import HttpResponse
from django.contrib.auth import views as auth_views


 

urlpatterns = [
    re_path(r'^$', views.igallery, name="igallery"), 
    re_path(r'^test/$', views.test, name="test"),
    re_path(r'^jsonaccess/$', views.json_access, name="json_access"),
    re_path(r'^test/jsonimagetest/$', views.json_access, name="json_image_test")
]


