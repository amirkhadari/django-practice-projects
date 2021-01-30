from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('others', views.other_pages, name = 'our services'),
    path('sitemap', views.relations_url, name='sitemap')
]
