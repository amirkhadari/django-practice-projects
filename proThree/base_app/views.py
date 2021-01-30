from django.shortcuts import render
from .models import User
from . import forms
# Create your views here.


def index(request):
    return render(request, 'base_app/base_app.html')


def create_user(request):
    users = User.objects.order_by('first_name')
    user_list = {'user': users}
    return render(request, 'base_app/user.html', context=user_list)


def contact(request):
    contact_form = forms.ContactUs()

    if request.method == 'POST':
        contact_form = forms.ContactUs(request.POST)

        if contact_form.is_valid():
            print('Validation Success')
            print('Name: ' + contact_form.cleaned_data['name'])
            print('Email: ' + contact_form.cleaned_data['email'])
            print('Queries: ' + contact_form.cleaned_data['queries'])
            # print('Bot: ' + str(len(contact_form.cleaned_data['bot_catcher'])))



    return render(request, 'base_app/contact.html', {'form': contact_form})
