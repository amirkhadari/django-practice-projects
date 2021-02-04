from django.shortcuts import render
from .forms import contact_us_form

# Create your views here.


def index(request):
    context_dict = {'text': 'the web framework for perfectionists with deadlines',
                    'digit': 100}
    return render(request, 'basic_app/index.html', context_dict)


def other_pages(request):
    return render(request, 'basic_app/others.html')


def relations_url(request):
    return render(request, 'basic_app/relative_url_templates.html')


def form_contact(request):
    user_data = contact_us_form()

    if request.method == "POST":
        user_data = contact_us_form(request.POST, request.FILES)

        if user_data.is_valid():
            # print('VALIDATION SUCCESS')
            # print('NAME: ' + user_data.cleaned_data['full_name'])
            # print('EMAIL: ' + user_data.cleaned_data['email'])
            user_data.save(commit=True)
            return index(request)

    return render(request, 'basic_app/contact.html', {'form': user_data})
