from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, HttpResponseBadRequest
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm 
from .forms import UploadImageForm
from .models import UploadImage 
from django.contrib.auth.models import User
import json # For parsing JSON


def json_access(request):
    # At this stage, a request from client should include only one of these three keys:
    # {"delete" : "ImageName"}
    # {"random_pull" : <int>}
    # {"user_pull" : <int>}
    # {"json_data" : }
    # {"im_fine" : }
    try:
        if request.method == 'POST':
            json_data = json.loads(request.body)
            action = json_data["action"]
            print (action)
            # Specifies nature of the request
            if "delete" == action:
                # If the request contains delete, then:
                # Check if use_is_owner
                # If so, remove image from database
                pass
            elif "random_pull" == action:
                # If the request contains random_pull, then:
                pass
            elif "user_pull" == action:
                # If the request contains user_pull, then:
                pass
            elif "how_many" == action:
                session_user = User.objects.get(username=(request.user.username))
                uploaded_images = UploadImage.objects.all().filter (uploader=session_user)
                image_count = uploaded_images.count()
                return HttpResponse (str(image_count))
            elif "im_fine" == action:
                # Terminates account by deleting user
                if request.user.is_authenticated:
                    # Lookup user with exact username, and images under their name
                    session_user = User.objects.get(username=(request.user.username))
                    uploaded_images = UploadImage.objects.all().filter (uploader=session_user)
                    # Remove them. Note that cleanup is done through django-cleanup
                    session_user.delete()
                    uploaded_images.delete()
                return HttpResponse("account_delete_success")
            else:
                # then something must be going wrong.
                print ("Wait... POSSIBLE DATA CORRUPTION")
            print ("JSON SERVER ERROR")
            return HttpResponseBadRequest("Something is not right: JSON QUERY ERROR")
        else:    
            print ("Wait... Method must be POST")
            return HttpResponseBadRequest("Something is not right: Method must be POST")
    except Exception:
        print ("A wild exception appeared: ")
        return HttpResponseServerError("Wild  Exception: ")

def json_image_test(request):
    print ("data received")
    if request.method == 'POST':
        
        print ("method-post confirmed")
        json_data = json.loads(request.body)
        action = json_data["action"]
        if "delete" == action:
            print ("action: delete")
            # If the request contains delete, then:
            # Check if use_is_owner
            # If so, remove image from database
            return HttpResponse ("detete_success")
        elif "random_pull" == action:
            print ("action: random_pull")
            # If the request contains random_pull, then:
            return HttpResponse ("random_pull_success")
        elif "user_pull" == action:
            print ("action: user_pull")
            # If the request contains user_pull, then:
            return HttpResponse ("user_pull_success")

def igallery(request): # Handles image upload and test formatting
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



def test(request):
   return render(request, 'simpleJSONImage.html')

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




