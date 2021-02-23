from django.contrib import admin
from .models import Author, Blog_Model, UserProfileInfo
# Register your models here.

admin.site.register(Author)
# admin.site.register(Blog_Model)
class Blog_ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'blog_status')
    list_filter = ('blog_status', )
    search_fields = ('title', )

admin.site.register(Blog_Model, Blog_ModelAdmin)

admin.site.register(UserProfileInfo)
