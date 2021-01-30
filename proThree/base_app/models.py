from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=14, unique=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
