from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [

    path('', views.blog_list, name='list-blogs'),
    path('register', views.register, name='register')

]
