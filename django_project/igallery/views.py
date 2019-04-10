from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def start(request):
    return render(request, 'igallery.html')

def test(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

