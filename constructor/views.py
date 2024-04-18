"""
Views for the 'constructor' app.

This module defines views for handling post-related functionality.

Classes:
    PostUpdate: A view for updating a post.
    PostView: A view for viewing a post.
"""
from django.shortcuts import redirect, render
from django.views import View
from .forms import TestForm
from .models import Post


class PostUpdate(View):
    """
    A view for updating a post.
    """
    def get(self, request, pk):
        """
        Handles GET requests to display the form for updating a post.

        Args:
            request (HttpRequest): The HTTP request.
            pk (int): The primary key of the post to be updated.

        Returns:
            HttpResponse: The HTTP response containing the form for updating the post.
        """
        post = Post.objects.get(id=pk)
        bound_form = TestForm(instance=post)
        return render(request, 'constructor/post_update.html', {'form': bound_form, 'post': post})

    def post(self, request, pk):
        """
        Handles POST requests to update a post.

        Args:
            request (HttpRequest): The HTTP request containing the form data.
            pk (int): The primary key of the post to be updated.

        Returns:
            HttpResponse: The HTTP response redirecting to the updated post on success,
                or re-rendering the form with errors on failure.
        """
        post = Post.objects.get(id=pk)
        bound_form = TestForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'constructor/post_update.html', {'form': bound_form, 'post': post})


class PostView(View):
    """
    A view for viewing a post.
    """
    def get(self, request, pk):
        """
        Handles GET requests to display a post.

        Args:
            request (HttpRequest): The HTTP request.
            pk (int): The primary key of the post to be viewed.

        Returns:
            HttpResponse: The HTTP response containing the details of the post.
        """
        # pylint: disable=E1101
        post = Post.objects.get(id=pk)
        return render(request, 'constructor/post_view.html', {'post': post})
