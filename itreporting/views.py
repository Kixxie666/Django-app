from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

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


