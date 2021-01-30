from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


def other_pages(request):
    return render(request, 'basic_app/others.html')


def relations_url(request):
    return render(request, 'basic_app/relative_url_templates.html')
