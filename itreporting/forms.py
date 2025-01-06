from django import forms
from .models import Contact, Student1

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'address']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student1
        fields = ['first_name', 'last_name', 'email', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
