"""Views for profile page"""
import os
from io import BytesIO

import PIL
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from social_django.models import UserSocialAuth  # type: ignore

import numpy
from PIL import Image
from segno import make_qr
from google.cloud import storage as gcs_storage  # type: ignore

from constructor.forms import PageForm
from entry.views import logout
from .forms import UpdateImageForm
from .models import Page


@login_required
def profile(request):
    """Profile view"""
    user_pages = Page.objects.filter(user=request.user)
    # Check if the user logged in via Google OAuth 2
    user_logged_in_with_google = (UserSocialAuth.objects.filter
                                  (user=request.user, provider='google-oauth2').exists())
    context = {
        'username': request.user.username,
        'email': request.user.email,
        # 'image_url': request.user.profile.image.url,
        'user_pages': user_pages,
        'user_logged_in_with_google': user_logged_in_with_google,
        'number_of_pages': user_pages.count(),
    }
    return render(request, 'user_profile/profile.html', context)


@login_required
def delete_account(request):
    """Delete account view"""
    if request.method == 'POST':
        user = request.user
        logout(request)  # Log out the user before deleting the account
        user.delete()  # Delete the user account
        messages.success(request, 'Your account has been deleted successfully.')
    return redirect('profile')


@login_required
def change_password(request):
    """Change password view"""
    # Check if the user logged in via Google OAuth 2
    if request.user.social_auth.filter(provider='google-oauth2').exists():
        messages.error(request, "You cannot change your password because you logged in via Google.")
        return redirect('profile')  # Or wherever you want to redirect

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_profile/change_password.html', {
        'form': form
    })


@login_required
def change_image(request):
    """change image view"""
    if request.method == 'POST':
        update_image_form = UpdateImageForm(
            request.POST, request.FILES, instance=request.user.profile)

        if update_image_form.is_valid():
            update_image_form.save()
            messages.success(request, 'Your profile image has been updated!')
            return redirect('profile')

    else:
        update_image_form = UpdateImageForm(instance=request.user.profile)
        context = {
            'update_image_form': update_image_form
        }

    return render(request, 'user_profile/change_image.html', context)


@login_required
def delete_image(request):
    """delete_image view"""
    if request.method == 'POST':
        profile1 = request.user.profile
        profile1.image = 'default.png'
        profile1.save()

    return redirect('profile')


@login_required
def create_page(request):
    """create_page view"""
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = request.user
            page = Page.objects.create(title=title, content=content, user=user)

            host = os.environ.get("HOST", default="http://localhost:8000/")
            image = make_qr(host + 'profile/view/' + str(page.upid))

            data = []
            for i in image.matrix:
                data.append([])
                for j in i:
                    data[-1].append(j)
            # pylint: disable=no-member
            image = (Image.fromarray(numpy.uint8(numpy.array(data)) * 255).
                     resize((len(image.matrix) * 8, len(image.matrix) * 8), PIL.Image.NONE))
            image_file = BytesIO()
            image.save(image_file, format='WEBP')
            image_file.seek(0)

            client = gcs_storage.Client(credentials=settings.GS_CREDENTIALS)
            bucket = client.bucket(settings.GS_BUCKET_NAME)
            blob = bucket.blob(f"{request.user.username}/{str(page.upid) + '.webp'}")

            blob.upload_from_file(image_file, content_type='image/webp')
            blob.make_public()

            return redirect('profile')
    else:
        form = PageForm()

    return render(request, 'constructor/update.html', {'form': form})


def view_page(request, page_id):
    """view_page view"""
    page = Page.objects.get(upid=page_id)
    return render(request, 'constructor/view.html', {'post': page})


@login_required
def delete_page(request, page_id):
    """delete_page view"""
    page = get_object_or_404(Page, upid=page_id)
    if request.user != page.user:
        messages.warning(request, 'Your are not authorized to delete this page')
        return redirect('profile')
    if request.method == 'POST':
        page.delete()
    return redirect('profile')
