from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UploadImageForm
from .models import ImageModel 

def start(request):
    return render(request, 'igallery.html')

def test(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm (request.POST, request.FILES)
        if form.is_valid():
            imageModel = ImageModel()
            imageModel.name = form.cleaned_data["name"]
            imageModel.picture = form.cleaned_data["picture"]
            imageModel.save()
            return HttpResponse('You Did It!')
    else:
        form = UploadImageForm()
    return render (request, 'upload.html', {'form':form}) 