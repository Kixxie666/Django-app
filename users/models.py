from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users_profile')
    image = models.ImageField(default='media/profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    