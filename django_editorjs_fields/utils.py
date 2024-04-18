"""Utility functions related to storage and URL parsing."""

import urllib.parse

from django.conf import settings
from django.utils.module_loading import import_string


def get_storage_class():
    """
    Get the storage class specified in settings or default storage.

    Returns:
        class: Storage class instance.
    """
    return import_string(
        getattr(
            settings,
            'EDITORJS_STORAGE_BACKEND',
            'django.core.files.storage.DefaultStorage',
        )
    )()


def get_hostname_from_url(url):
    """
    Extract the hostname from a given URL.

    Args:
        url (str): The URL from which to extract the hostname.

    Returns:
        str: The hostname extracted from the URL.
    """
    obj_url = urllib.parse.urlsplit(url)
    return obj_url.hostname


# Initialize storage class instance
storage = get_storage_class()
