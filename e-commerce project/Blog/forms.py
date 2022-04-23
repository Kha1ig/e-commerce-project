from django.forms import ModelForm
from .models import Comment
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class CommentForm(ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ('letter', 'user')

        widgets = {
            'letter': forms.Textarea(
                attrs = {
                'class': 'form-control',
                'cols': '30',
                'rows':   "9",
                'placeholder': 'Write Comment',
                }
            ),

            
            }