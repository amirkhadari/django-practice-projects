from django import forms
from .models import SignUp


class user_register_form(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"
