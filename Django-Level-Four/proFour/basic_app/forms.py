from django import forms
from .models import contact
import re

class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"

    def clean_email(self):
        email_details = self.cleaned_data.get('email')
        if "@gmail.com" in email_details:
            raise forms.ValidationError("Please use your official Email Id.")
        return email_details

    def clean_full_name(self):
        name_details = self.cleaned_data.get('full_name')
        if not re.match(r'^[a-zA-Z0-9]*$', name_details):
            raise forms.ValidationError("ONLY ALPHANUMERIC ALLOWED")
        return name_details
