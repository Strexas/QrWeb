"""Database models for profile page"""
import uuid

from django.db import models
from django.contrib.auth import models as auth_models
from django.urls import reverse, reverse_lazy
from PIL import Image
from django_editorjs_fields import EditorJsJSONField


class Profile(models.Model):
    """"Profile model"""
    user: models.OneToOneField = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    image: models.ImageField = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        # pylint: disable=no-member
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Page(models.Model):
    """Page model"""
    user: models.ForeignKey = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    title: models.CharField = models.CharField(max_length=100)
    upid: models.UUIDField = models.UUIDField(default=uuid.uuid4, unique=True)
    objects = models.Manager()
    content = EditorJsJSONField(
        plugins=[
            '@editorjs/paragraph',
            '@editorjs/image',
            '@editorjs/header',
            '@editorjs/list',
            '@editorjs/inline-code',
            '@editorjs/embed',
            '@editorjs/link',
            '@editorjs/marker',
            '@editorjs/table',
            '@editorjs/raw',
            '@editorjs/underline',
            'editorjs-undo',
            'editorjs-text-alignment-blocktune'
        ],
        tools={
            'Image': {
                'class': 'ImageTool',
                'inlineToolbar': True,
                "config": {
                    "endpoints": {
                        "byFile": reverse_lazy('editorjs_image_upload'),
                        "byUrl": reverse_lazy('editorjs_image_by_url')
                    },
                }
            },
            'Header': {
                'class': 'Header',
                'tunes': ['BlockTune'],
                'inlineToolbar': True,
                'config': {
                    'placeholder': 'Enter a header',
                    'defaultLevel': 2,
                    'levels': [2, 3, 4],
                }
            },
            'Raw': {'class': 'RawTool'},
            'Embed': {'class': 'Embed'},
            'LinkTool': {
                'class': 'LinkTool',
                'config': {
                    'endpoint': reverse_lazy('editorjs_linktool'),
                }
            },
            'BlockTune': {
                'class': 'AlignmentBlockTune',
                'config': {
                    'default': "left",
                    'blocks': {
                        'header': 'center',
                        'list': 'right'
                    }
                },
            },
            'paragraph': {
                'class': 'Paragraph',
                'inlineToolbar': True,
                'tunes': ['BlockTune'],
            },
            'underline': {
                'class': 'Underline'
            }
        },
        null=True,
        blank=True,
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    last_updated: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Return the absolute URL of a page detail view.

        Returns:
            str: The absolute URL of a page detail view.
        """
        return reverse('page_detail', kwargs={'page_id': self.upid})
