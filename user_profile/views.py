"""Views for profile page"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UpdateImageForm
from .models import Page
@login_required
def profile(request):
    """Profile view"""
    user_pages = Page.objects.filter(user=request.user)
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'image_url': request.user.profile.image.url,
        'user_pages':user_pages
    }
    return render(request,'user_profile/profile.html',context)


def change_password(request):
    """change password view"""
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
    """change image view"""
    if request.method == 'POST':
        update_image_form = UpdateImageForm(
            request.POST,request.FILES,instance=request.user.profile)

        if update_image_form.is_valid():
            update_image_form.save()
            messages.success(request,'Your profile image has been updated!')
            return redirect('profile')

    else:
        update_image_form = UpdateImageForm(instance=request.user.profile)
        context = {
            'update_image_form': update_image_form
        }

        return render(request, 'user_profile/change_image.html', context)


def delete_image(request):
    """delete_image view"""
    if request.method == 'POST':
        profile = request.user.profile
        profile.image = 'default.png'
        profile.save()
        return redirect('profile')


def create_page(request):
    """create_page view"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Page.objects.create(title=title, content=content, user=user)
        return redirect('profile')

    return render(request,'user_profile/create_page.html')


def delete_page(request,page_id):
    """delete_page view"""
    page = get_object_or_404(Page,id = page_id)
    if request.method == 'POST':
        page.delete()
    return redirect('profile')