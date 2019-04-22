from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm 
from .forms import UploadImageForm
from .models import UploadImage 



def igallery(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                instance = UploadImage(file_field=request.FILES['image'], uploader=request.user)
                instance.save()

                return HttpResponse('Yes, it works!www ' + request.user.username)
            else:
                return HttpResponse ("Please Login First")
        else:
            return HttpResponse ("Corrupted Form")
    else:
        form = UploadImageForm()
    return render(request, 'igallery.html', {'upload_form': form})


"""
def start(request):
    return render(request, 'igallery.html')
"""
def test(request):
   text = """<h1>I am alive!</h1>"""
   return HttpResponse(text)

"""
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm (request.POST, request.FILES)
        if form.is_valid():
            imageModel = ImageModel()
            imageModel.picture = form.cleaned_data["picture"]
            imageModel.save()
            return HttpResponse('Upload Accepted. Have a good day meow.')
        else:
            return HttpResponse ("Form Validation Failed. Meow.")
    else:
        form = UploadImageForm()
    return HttpResponse ("Upload Denied, allowed only via POST") 
"""




