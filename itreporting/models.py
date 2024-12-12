from django.db import models
from django.contrib.auth.models import User
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
    date_submitted = models.DateTimeField(auto_now_add=True)
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
    
class CouseModule(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length= 100)
    availability= models.CharField(max_length= 100)
    register = models.CharField(max_length= 100)
    
    
class Student1(models.Model):
    dob= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo = models.ImageField(default='default.png', upload_to='profile_pics')

    
class Registration1(models.Model):
    student = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    registerdate= models.CharField(max_length=100)
