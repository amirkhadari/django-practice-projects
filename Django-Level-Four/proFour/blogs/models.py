from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Blog_Model(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    image = models.ImageField(upload_to='blog-images/')
    # uploaded_by = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
