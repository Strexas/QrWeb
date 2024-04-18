"""Database models for profile page"""
from django.db import models
from django.contrib.auth import models as auth_models
from django.urls import reverse
from django_editorjs_fields import EditorJsJSONField
from PIL import Image


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
    objects = models.Manager()
    content = EditorJsJSONField(
        plugins=[
            '@editorjs/paragraph',
            '@editorjs/image',
            '@editorjs/header',
            '@editorjs/list',
            '@editorjs/code',
            '@editorjs/inline-code',
            '@editorjs/embed',
            '@editorjs/link',
            '@editorjs/marker',
            '@editorjs/table',
            'header-with-alignment',
        ],
        tools={
            "Image": {
                'class': 'ImageTool',
                "config": {
                    "endpoints": {
                        "byFile": "/editorjs/image_upload/"
                    }
                }
            },
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
        return reverse('page_detail', kwargs={'page_id': self.id})
