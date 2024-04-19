"""
Views for the 'constructor' app.

This module defines views for handling post-related functionality.

Classes:
    PageUpdate: A view for updating a page.
    PageView: A view for viewing a page.
"""
from django.shortcuts import redirect, render
from django.views import View
from user_profile.models import Page
from .forms import PageForm


class PageUpdate(View):
    """
    A view for updating a page.
    """

    def get(self, request, page_id):
        """
        Handles GET requests to display the form for updating a page.

        Args:
            request (HttpRequest): The HTTP request.
            pk (int): The primary key of the post to be updated.

        Returns:
            HttpResponse: The HTTP response containing the form for updating the page.
        """
        page = Page.objects.get(id=page_id)
        bound_form = PageForm(instance=page)
        return render(request, 'constructor/page_update.html', {'form': bound_form, 'post': page})

    def post(self, request, page_id):
        """
        Handles POST requests to update a page.

        Args:
            request (HttpRequest): The HTTP request containing the form data.
            pk (int): The primary key of the page to be updated.

        Returns:
            HttpResponse: The HTTP response redirecting to the updated page on success,
                or re-rendering the form with errors on failure.
        """
        page = Page.objects.get(id=page_id)
        bound_form = PageForm(request.POST, instance=page)

        if bound_form.is_valid():
            new_page = bound_form.save()
            return redirect(new_page)
        return render(request, 'constructor/page_update.html', {'form': bound_form, 'post': page})


class PageView(View):
    """
    A view for viewing a page.
    """

    def get(self, request, page_id):
        """
        Handles GET requests to display a page.

        Args:
            request (HttpRequest): The HTTP request.
            page_id (int): The primary key of the post to be viewed.

        Returns:
            HttpResponse: The HTTP response containing the details of the page.
        """
        # pylint: disable=E1101
        page = Page.objects.get(id=page_id)
        return render(request, 'constructor/page_view.html', {'post': page})
