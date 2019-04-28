Project Report-Project03

Finish date: 2019/4/24

**Git Repo** : [https://github.com/Tan630/iGallery](https://github.com/Tan630/iGallery)

**Note** : This version on git repo is designed to be run on root URL, while my adaption on mac1xa3 server has its settings.py and urls.py modified to accommodate starting from /e/liy443/.

Credits: [https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html](https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html) for sign-up system

[https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/) For user login/logout

An admin account is provided:

Username: admin01,

Password: Cat4LifeFun

### How to use:

cd /mnt/c/Assets/UbuntuWorkspace/iGallery

source bin/activate

cd django\_project/

python3 manage.py runserver localhost:10038

After server starts running, you should be able to access it at [https://mac1xa3.ca/e/liy443](https://mac1xa3.ca/e/liy443)

# Interface

## Main Page




This where you should land upon first accessing [https://mac1xa3.ca/e/liy443/](https://mac1xa3.ca/e/liy443/).

Should be quite self-explanatory. If user was not logged in, the &quot;Welcome&quot; message will be replaced by a Login link.

iGallery leads to the main application page:

## iGallery



- **Clear** :3: Clears carousel slides, resets local storage, and reset iy67546tyd counter. This action will also be performed once all displayed images are deleted via the (#Delete Picture) button
- **Query Size** : Refreshes number displayed at top to reflect number of images contributed under current user&#39;s name.
  - Will be automatically triggered after every action that alters displayed image
- **Delete Account** : Deletes current user account, don&#39;t press that…
  - This is only for testing purposes
- **Delete Picture** : Deletes currently displayed image. The input field underneath displays its **url** for reference.
- **Random Pull** : Pulls a set of random image URLs from the server. Quantity 5(default) or user input
  - Will also be called upon
  - Images could belong to anybody
- **User Pull** : Pulls a set of image URLs from server under current user&#39;s name. Quantity 5(default) or user input
- **UL** allows user to upload an image to server, under their name
- **DL** allows user to download the image that&#39;s being displayed on server

## Admin Page


This page is not meant to be accessible by normal users, but rather directly via url: [https://mac1xa3.ca/e/liy443/admin/](https://mac1xa3.ca/e/liy443/admin/).  Here user and their images can be managed at one place.

# Features

## Program-wise

- User system is managed on project-level
- All user-related functionalities, such as uploading/deletion of images, are authenticated at both server and client side.
- All access URLs are relative/named, thus allowing easy reference and maintenance.
  - During deployment to non-root urls, only urls.py and several URLs in settings.py had to be modified.
- All pages are served through Django&#39;s render() function, which allows for heavy use of tags, csrf\_token, form unpacking and overall greater integrity with the Django framework.
- From client&#39;s perspective, all communications with the server, apart from image, are all in JSON format.
- All JSON-related functionalities are handled (sent/received) via a single function. Easier to read/maintain.

## User Interaction

- Intuitive interface, with foolproof tips (except that big red button which you should definitely never press, ever)
- User is given full authority over their contents, including uploading/downloading/deleting their own images, as well as deleting their entire account in one go if they felt like it.
- Sophisticated user system with redirections allows for everything from signing up to retrieving password. Heart-warming welcome messages included.
- Images already displaying in carousel will not be re-added upon pull requests.
- _Testing teams report a_ **20%** _increase in cat addiction_.

# Space for Improvements

## Lethal

Situations /glitches that may sometimes renders the application unusable:

- With slow connection, some unintended error may come to play:
  - In one test instance, carousel failed to initialize properly, resulting in misplaced starting images. I have since failed to reproduce this glitch
  - In one test instance, login page failed to redirect back. I have since failed to reproduce this glitch.
  - Rapid, successive clicks of the upload\_image button with the intention to upload the same file repeatedly may cause some of them not being uploaded (e.g. 4 uploaded after 10 button clicks)
- Git logs are grammatically inconsistent and (as for the initial commit) incorrect
  - Had to be left this way since last attempt to fix it resulted a bit of trouble.

## Critical

- Debug mode still enabled, with media files directly served from MEDIA\_URL.
- Some codes could be ready for execution before document is fully loaded. Although no problems have arisen so far but I could definitely see errors occurring because of that.
- Carousel nan not accommodate images of all dimensions, resulting inconstancies with pictures of different dimensions.

## Minor

Features that won&#39;t affect user&#39;s overall experience

- Unlike mainstream social platforms, another user with identical username can be created after, possibly allowing impersonation
  - Which is inconsequential since username is used as login credential only, with rest of the site being entirely anonymous.
- User Pull can only retrieve images in chronological order

# Compromises

Compromises made with relation to project objective, outside of the functional scope

- For better integration with Django framework, **JavaScript** is used in favour of **Elm**.
  - This allows for the implementation of additional features such as DTL tags, and better integration with authentication system.
  - as a result, all pages are served through render(), in combination with {% csrf\_token %}, also prevents cross-site forgery

- User authentication pages ( **signup.html** , etc.) are largely &quot;borrowed&quot; from online sources. (also the only case of massive outsourcing)

- After **user deletes an image** , only its database entry will be removed. Corresponsing files stored in server remains untouched. It keeps good logs and prevents unwanted data loss, while at the meantime puts a heavy strain on server-side storage.
  - Better: Missing server-side assets will not cause error
  - Worse: So far server-side assets can only be deleted from bash
- Carousel slides will not be updated after successful image upload, since it could contain either random or user-specific images.
  - User need to decide between performing a random\_pull or user\_pull to update carousel display.
- Page will not refresh after deleting account, allowing user to cherish their last moment with their adorable cats.
