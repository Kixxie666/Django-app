from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='itreporting_profile')
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Issue(models.Model):
    type = models.CharField(max_length=100, choices = [('Hardware', 'Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default = False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name = 'issues', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.type} Issue in {self.room}'
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(validators=[EmailValidator()], max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    address = models.CharField(max_length= 100)