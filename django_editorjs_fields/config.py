"""Configuration module for Editor.js integration in Django.

This module defines various configuration settings for integrating Editor.js,
a block-style editor for rich content creation, into Django projects.

Attributes:
    DEBUG (bool): Indicates whether the application is in debug mode.
    VERSION (str): The version of Editor.js being used.
    EMBED_HOSTNAME_ALLOWED (str): List of allowed hostnames for embedded content.
    IMAGE_UPLOAD_PATH (str): The path where uploaded images are stored.
    IMAGE_UPLOAD_PATH_DATE (str): The format for organizing uploaded images by date.
    IMAGE_NAME_ORIGINAL (bool): Indicates whether to keep the original image name when uploading.
    IMAGE_NAME (function): Function to generate a unique name for uploaded images.
    PLUGINS (tuple): List of default plugins for Editor.js.
    CONFIG_TOOLS (dict): Configuration settings for Editor.js tools.
    PLUGINS_KEYS (dict): Mapping of Editor.js plugin names to their corresponding tool names.

Usage:
- Import the necessary settings from this module to configure
Editor.js integration in your Django project.
- Customize the settings as needed based on your project requirements.

Example:
    from django.conf import settings

    DEBUG = getattr(settings, "DEBUG", False)
    VERSION = getattr(settings, "EDITORJS_VERSION", '2.25.0')
    EMBED_HOSTNAME_ALLOWED = getattr(settings, "EDITORJS_EMBED_HOSTNAME_ALLOWED", (
        'player.vimeo.com',
        'www.youtube.com',
        # Add more allowed hostnames as needed
    ))
    # Configure other settings similarly as needed
"""
from secrets import token_urlsafe
from django.conf import settings
from django.urls import reverse_lazy

DEBUG = getattr(settings, "DEBUG", False)

VERSION = getattr(settings, "EDITORJS_VERSION", '2.25.0')

# ATTACHMENT_REQUIRE_AUTHENTICATION = str(
#     getattr(settings, "EDITORJS_ATTACHMENT_REQUIRE_AUTHENTICATION", True)
# )

EMBED_HOSTNAME_ALLOWED = str(
    getattr(settings, "EDITORJS_EMBED_HOSTNAME_ALLOWED", (
        'player.vimeo.com',
        'www.youtube.com',
        'coub.com',
        'vine.co',
        'imgur.com',
        'gfycat.com',
        'player.twitch.tv',
        'player.twitch.tv',
        'music.yandex.ru',
        'codepen.io',
        'www.instagram.com',
        'twitframe.com',
        'assets.pinterest.com',
        'www.facebook.com',
        'www.aparat.com',
    ))
)

IMAGE_UPLOAD_PATH = str(
    getattr(settings, "EDITORJS_IMAGE_UPLOAD_PATH", 'uploads/images/')
)

IMAGE_UPLOAD_PATH_DATE = getattr(
    settings, "EDITORJS_IMAGE_UPLOAD_PATH_DATE", '%Y/%m/')

IMAGE_NAME_ORIGINAL = getattr(
    settings, "EDITORJS_IMAGE_NAME_ORIGINAL", False)

IMAGE_NAME = getattr(
    settings, "EDITORJS_IMAGE_NAME", lambda **_: token_urlsafe(8))

PLUGINS = getattr(
    settings, "EDITORJS_DEFAULT_PLUGINS", (
        '@editorjs/paragraph',
        '@editorjs/image',
        '@editorjs/header',
        '@editorjs/list',
        '@editorjs/checklist',
        '@editorjs/quote',
        '@editorjs/raw',
        '@editorjs/code',
        '@editorjs/inline-code',
        '@editorjs/embed',
        '@editorjs/delimiter',
        '@editorjs/warning',
        '@editorjs/link',
        '@editorjs/marker',
        '@editorjs/table',
        '@editorjs/underline',
        'editorjs-paragraph-with-alignment',
        'editorjs-header-with-alignment'
    )
)

CONFIG_TOOLS = getattr(
    settings, "EDITORJS_DEFAULT_CONFIG_TOOLS", {
        'Image': {
            'class': 'ImageTool',
            'inlineToolbar': True,
            "config": {
                "endpoints": {
                    "byFile": reverse_lazy('editorjs_image_upload'),
                    "byUrl": reverse_lazy('editorjs_image_by_url')
                }
            },
        },
        'Header': {
            'class': 'Header',
            'inlineToolbar': True,
            'config': {
                'placeholder': 'Enter a header',
                'levels': [1, 2, 3, 4],
                'defaultLevel': 2,
            },
        },
        'paragraph': {
            'class': 'Paragraph',
            'inlineToolbar': True,
        },
        'Checklist': {'class': 'Checklist', 'inlineToolbar': True},
        'List': {'class': 'List', 'inlineToolbar': True},
        'Quote': {'class': 'Quote', 'inlineToolbar': True},
        'Raw': {'class': 'RawTool'},
        'Code': {'class': 'CodeTool'},
        'InlineCode': {'class': 'InlineCode'},
        'Embed': {'class': 'Embed'},
        'Delimiter': {'class': 'Delimiter'},
        'Warning': {'class': 'Warning', 'inlineToolbar': True},
        'LinkTool': {
            'class': 'LinkTool',
            'config': {
                # Backend endpoint for url data fetching
                'endpoint': reverse_lazy('editorjs_linktool'),
            }
        },
        'Marker': {'class': 'Marker', 'inlineToolbar': True},
        'Table': {'class': 'Table', 'inlineToolbar': True},
        'Underline': {'class': 'UnderLine', 'inlineToolbar': True},
    }
)

PLUGINS_KEYS = getattr(
    settings, "EDITORJS_PLUGINS_KEYS", {
        '@editorjs/image': 'Image',
        '@editorjs/header': 'Header',
        '@editorjs/checklist': 'Checklist',
        '@editorjs/list': 'List',
        '@editorjs/quote': 'Quote',
        '@editorjs/raw': 'Raw',
        '@editorjs/code': 'Code',
        '@editorjs/inline-code': 'InlineCode',
        '@editorjs/embed': 'Embed',
        '@editorjs/delimiter': 'Delimiter',
        '@editorjs/warning': 'Warning',
        '@editorjs/link': 'LinkTool',
        '@editorjs/marker': 'Marker',
        '@editorjs/table': 'Table',
    }
)
