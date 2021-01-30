from django.db import models

# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
