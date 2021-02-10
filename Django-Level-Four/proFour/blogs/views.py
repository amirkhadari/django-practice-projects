from django.shortcuts import render
from .forms import blog_form
from .models import Blog_Model
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
    total_blogs = Blog_Model.objects.all().order_by('-date_created')
    # img = Blog_Model.objects.all()
    blog_dict = {'blogs': total_blogs}
    return render(request, 'blog_templates/blog_listing.html', context=blog_dict)
