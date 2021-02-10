from django import forms
from .models import Blog_Model
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
