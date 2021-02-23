from django import forms
from .models import Blog_Model, UserProfileInfo
from django.contrib.auth.models import User
#

class blog_form(forms.ModelForm):
    class Meta:
        model = Blog_Model
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            # 'date_created': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')
