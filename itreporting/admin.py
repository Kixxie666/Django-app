from django.contrib import admin
from .models import Issue
from .models import Profile


admin.site.register(Profile)
admin.site.register(Issue)
