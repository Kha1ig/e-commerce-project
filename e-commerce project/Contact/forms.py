from django import forms
from django.forms import ModelForm
from Contact.models import Contact
from django.contrib.auth import get_user_model

User=get_user_model()

class ContactForm(ModelForm):
    pass

    class Meta:
        model = Contact
        fields = ('message', 'name', 'email', 'subject')

        widgets = {
            'message': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Message',
                    'cols': '30',
                    'rows': '9',
                }
            ),
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter your name',

                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter email address',
                }
            ),
            'subject': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Enter Subject',

                }
            ),

        }

