from django.shortcuts import render
from .forms import blog_form, UserForm, UserProfileInfoForm
from .models import Blog_Model, UserProfileInfo
from basic_app.views import index
# Create your views here.


def blog_view(request):
    blog_data = blog_form()
    if request.method == 'POST':
        blog_data = blog_form(request.POST, request.FILES)

        if blog_data.is_valid():
            blog_data.save(commit=True)
            return index(request)

    return render(request, 'blog_templates/blog.html', {'form': blog_data})


def blog_list(request):
    total_blogs = Blog_Model.objects.all().order_by('-date_created').filter(blog_status=2)
    # img = Blog_Model.objects.all()
    blog_dict = {'blogs': total_blogs}
    return render(request, 'blog_templates/blog_listing.html', context=blog_dict)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'blog_templates/registration.html',
                            {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})
