from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'text': 'the web framework for perfectionists with deadlines',
                    'digit': 100}
    return render(request, 'basic_app/index.html', context_dict)


def other_pages(request):
    return render(request, 'basic_app/others.html')


def relations_url(request):
    return render(request, 'basic_app/relative_url_templates.html')
