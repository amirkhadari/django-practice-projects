from django.shortcuts import render
# from django.http import HttpResponse
from . import forms
from base_app.views import index
# Create your views here.


def new_user(request):
    form = forms.user_register_form()

    if request.method == "POST":
        form = forms.user_register_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'authentication/sign.html', {'form': form})
