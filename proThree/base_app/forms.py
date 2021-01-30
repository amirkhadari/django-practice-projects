from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME SHOULD START WITH Z')

class ContactUs(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify Email', help_text='Enter your email again')
    queries = forms.CharField(widget=forms.Textarea)
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                                 validators=[validators.MaxLengthValidator(0, 'GOTCHA BOT')])


    def clean(self):
        data = super().clean()
        email = data['email']
        vmail = data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Emails are not matching')
