from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from .forms import ContactForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import EmailMessage
import requests
from .models import CouseModule, Student1, Registration1


# Views for CouseModule
def course_list(request):
    courses = CouseModule.objects.all()
    return render(request, 'itreporting/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(CouseModule, pk=pk)
    return render(request, 'itreporting/course_detail.html', {'course': course})

# Views for Student1
def student_list(request):
    students = Student1.objects.all()
    return render(request, '', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student1, pk=pk)
    return render(request, 'itreporting/student_detail.html', {'student': student})

# Views for Registration1
def registration_list(request):
    registrations = Registration1.objects.all()
    return render(request, 'itreporting/registration_list.html', {'registrations': registrations})

def registration_detail(request, pk):
    registration = get_object_or_404(Registration1, pk=pk)
    return render(request, 'itreporting/registration_detail.html', {'registration': registration})

def home(request):
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Sheffield', 'UK'), ('Melaka', 'Malaysia'), ('Bandung', 'Indonesia')]
    weather_data = []
    api_key = '6e9c2e5749db49381e2789580e8ce734'

    for city in cities:
        # Request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json()

        # Safely create weather dictionary (use .get() for robustness)
        weather = {
            'city': city_weather.get('name', 'N/A') + ', ' + city_weather.get('sys', {}).get('country', 'N/A'),
            'temperature': city_weather.get('main', {}).get('temp', 'N/A'),
            'description': city_weather.get('weather', [{}])[0].get('description', 'No description')
        }

        # Append data for the current city
        weather_data.append(weather)

    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})


def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'profile'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})

from .models import Issue
def report(request):
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
    return render(request, 'itreporting/report.html', daily_report)


class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination


class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'


class PostCreateView(CreateView):

    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 

    model = Issue

    fields = ['type', 'room', 'details']
    
    def test_func(self):

        issue = self.get_object()
        return self.request.user == issue.author

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Issue

    success_url = '/report'
    
    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Get the cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            email_message = EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
                'form-response@example.com',  # Send from your website
                ['test.mailtrap1234@gmail.com'],  # Your admin email
                reply_to=[email],  # Reply to the email from the form
            )
            email_message.send()

            return HttpResponse('Thank you for contacting us. We will respond as soon as possible.')
    else:
        form = ContactForm()  # Create a blank form for GET requests

    return render(request, 'itreporting/contact.html', {'form': form})

