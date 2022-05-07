from django.forms import ModelForm
from .models import Comment, Blog
from django import forms
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


class BlogForm(forms.ModelForm):

    # title = forms.CharField(max_length=50, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Title'}))

    # short_description = forms.CharField(max_length=500, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Short Description'}))
    # short_description_1 = forms.CharField(max_length=500, widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Short Description-1'}))
    # short_description_2 = forms.CharField(max_length=500, widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Short Description-2'}))
    # short_description_3 = forms.CharField(max_length=500, widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Short Description-3'}))
    # short_description_4 = forms.CharField(max_length=500, widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Short Description-4'}))
    # short_description_5 = forms.CharField(max_length=150, widget=forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Short Description-5'}))

    class Meta:
        model = Blog
        fields = ('title', 'short_description', 'short_description_1', 'short_description_2', 'short_description_3', 'short_description_4', 'short_description_5')