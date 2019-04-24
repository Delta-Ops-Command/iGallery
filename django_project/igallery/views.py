from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, HttpResponseBadRequest, JsonResponse
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm 
from .forms import UploadImageForm
from .models import UploadImage 
from django.contrib.auth.models import User
import json # For parsing JSON
from random import sample # For generating a sublist from a list
from django.conf import settings # For discovering media root


def json_access(request):
    # At this stage, a request from client should include only one of these three keys:
    # (Json data stored in this format: {action: "<action>", parameter:"parameter"})
    # (Parameter will be ignored for how_many and _fine)
    # {"delete" : "ImageName"}
    # {"random_pull" : <int>}
    # {"user_pull" : <int>}
    # {"json_data" : }
    # {"im_fine" : }

    try:
        if request.method == 'POST': # If request method is post: start process. Else: return HttpResponesBadRequest
            json_data = json.loads(request.body)
            action = json_data["action"]
            print (action)
            json_data = json.loads(request.body)
            action = json_data["action"]
            parameter = json_data["parameter"]
            if "random_pull" == action: # Request a list of random images
                # Authentication is NOT required
                # Specifies amount of images to be pulled, (default) 5
                requested_size = 5
                if parameter != "":
                    requested_size = int(parameter)
                fullQuery = UploadImage.objects.all()
                requested_size = fullQuery.count() if requested_size > fullQuery.count() else requested_size # If requested_size exceeds query size, scale it down
                fullURLs = list((q.file_field.url for q in fullQuery)) 
                partialURLs = list(sample(fullURLs,requested_size))
                dict_response = {"action": "pull", "result":partialURLs}
                return JsonResponse (dict_response)
            elif "user_pull" == action: # Request a list of URLs from the user
                if not request.user.is_authenticated:
                    return HttpResponse('Unauthorized', status=401)
                # Specifies amount of images to be pulled, (default) 100
                # Urls listed in chronological order
                requested_size = 100
                if parameter != "":
                    requested_size = int(parameter)
                fullQuery = UploadImage.objects.filter(uploader=request.user)
                requested_size = fullQuery.count() if requested_size > fullQuery.count() else requested_size # If requested_size exceeds query size, scale it down
                fullURLs = list((q.file_field.url for q in fullQuery)) 
                partialURLs = fullURLs[0:requested_size]
                dict_response = {"action": "pull", "result":partialURLs}
                return JsonResponse (dict_response)
            elif "how_many" == action: # Retrieve how many image are under user's name
                if not request.user.is_authenticated:
                    return HttpResponse('Unauthorized', status=401)
                session_user = User.objects.get(username=(request.user.username))
                uploaded_images = UploadImage.objects.all().filter (uploader=session_user)
                image_count = uploaded_images.count()
                dict_response = {"action": "how_many", "result":image_count}
                return JsonResponse (dict_response)
            elif "delete" == action: # Delete image with provided URL
                if not request.user.is_authenticated:
                    return HttpResponse('Unauthorized', status=401)
                try:
                    shortenedURL = parameter.strip(settings.MEDIA_URL) # Remove media_url
                    targetImage = UploadImage.objects.get(file_field=shortenedURL)
                    if targetImage.uploader == request.user: # Check if use_is_owner, if so, remove image from database
                        targetImage.delete()
                    dict_response = {"action": "delete", "result": parameter}
                    return JsonResponse (dict_response)
                except Exception:
                    return HttpResponseBadRequest ("Bad delete request: " + parameter)
            elif "im_fine" == action: # Delete user account entirely, alongside images they have uploaded
                if not request.user.is_authenticated:
                    return HttpResponse('Unauthorized', status=401)
                if request.user.is_authenticated:
                    session_user = User.objects.get(username=(request.user.username))
                    uploaded_images = UploadImage.objects.all().filter (uploader=session_user)
                    # delete(). Note that cleanup is automatically completed through django-cleanup
                    session_user.delete()
                    uploaded_images.delete()
                dict_response = {"action": "account_delete", "result": parameter}
                return JsonResponse (dict_response)
            else:
                # then something must be going wrong.
                return HttpResponseBadRequest("Error: Possible data corruption, action key not found") # No corresponding action: found
        else:    
            return HttpResponseBadRequest("Error: Method must be POST")
    except Exception as e:
        print ("A wild exception appeared: ", str(e), type(e))
        return HttpResponseServerError("A wild exception appeared!")
     
        
# list(sample(foo,len(foo)-1))
# /media/cats/Linux_Cheat_Sheet_njT7U0z.png
# UploadImage.objects.filter(file_field="cats/Linux_Cheat_Sheet_njT7U0z.png")

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




