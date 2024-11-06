from django.urls import path, include
from . import views  
from users import views as user_views


app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('register/', user_views.register, name='register'),

]