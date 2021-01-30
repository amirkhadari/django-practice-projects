import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proThree.settings')

import django
django.setup()

from base_app.models import User
from faker import Faker

fake = Faker()

def populate_user(N=5):

    for entry in range(N):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.ascii_safe_email()
        phone = fake.phone_number()


        User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, phone=phone)[0]


if __name__ == "__main__":
    print("Generating fake data")
    populate_user(N=20)
    print("Fake data Generated successfully")
