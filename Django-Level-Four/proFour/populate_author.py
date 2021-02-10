import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proFour.settings')

import django
django.setup()

from blogs.models import Author
from faker import Faker

fakegen = Faker()

def add_author(N=5):
    for entry in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        birth = fakegen.date_of_birth(minimum_age=20, maximum_age=80)
        death = fakegen.date_object()

        Author.objects.get_or_create(first_name=first_name, last_name=last_name,
                                date_of_birth=birth, date_of_death=death)


if __name__ == "__main__":
    print("Adding Authors")
    add_author(20)
    print("Created Authors")
