from django.urls import path, include, re_path
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .templates.forms import SignUpForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

# Wasn't able to import these methods, had to leave it here for now...
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/igallery/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def requestMain(request):
    return render(request, 'main/main_view.html')
    
def debugRequestLogout(request):
    return render(request, 'registration/logout.html')

urlpatterns = [
    re_path(r'^$', requestMain, name="index"),
    re_path(r'^admin/', admin.site.urls, name="admin"),
    re_path(r'^signup/', signup, name="signup"),
    re_path(r'^igallery/', include('igallery.urls'), name='igallery'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    #re_path(r'^accounts/logout/$', debugRequestLogout)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Static URLs Enabled

"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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




