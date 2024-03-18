from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def delete_image(self):
        if self.image.name != 'default.jpg':
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        self.image = 'default.jpg'
        self.save()

    def change_password(self,new_password):
        self.user.set_password(new_password)
        self.user.save()










