from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateImageForm
from PIL import Image

@login_required
def profile(request):

    context = {
        'username': request.user.username,
        'email': request.user.email,
        'image_url': request.user.profile.image.url
    }
    return render(request,'user_profile/profile.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        print("print 1")
        if form.is_valid():
            print("is valid")
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_profile/change_password.html', {
        'form': form
    })


def change_image(request):
    if request.method == 'POST':
        update_image_form = UpdateImageForm(request.POST,request.FILES,instance=request.user.profile)

        if update_image_form.is_valid():
            update_image_form.save()
            messages.success(request,f'Your profile image has been updated!')
            return redirect('profile')

    else:
        update_image_form = UpdateImageForm(instance=request.user.profile)
        context = {
            'update_image_form': update_image_form
        }

        return render(request, 'user_profile/change_image.html', context)





def delete_image(request):
    if request.method == 'POST':
        profile = request.user.profile
        profile.image = 'default.png'
        profile.save()
        return redirect('profile')


