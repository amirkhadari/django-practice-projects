from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=14, unique=True)
    country = CountryField()

    RELATIONSHIPS = [
    ('Customer (potential/existing)', (
            ('request', 'Request for Services'),
        )
    ),
    ('Other Queries', (
                    ('analyst', 'Analysts (Industry and Financial)'),
                    ('investor', 'Investors'),
                    ('media', 'Media and Journalists'),
                    ('global', 'Global Procurement Services'),
                    ('security', 'Report a Security Incident'),
        )
    ),
    ]

#     MEDIA_CHOICES = [
#     ('Audio', (
#             ('vinyl', 'Vinyl'),
#             ('cd', 'CD'),
#         )
#     ),
#     ('Video', (
#             ('vhs', 'VHS Tape'),
#             ('dvd', 'DVD'),
#         )
#     ),
#     ('unknown', 'Unknown'),
# ]

    Investors = models.CharField(max_length=50, choices=RELATIONSHIPS)
    Queries = models.TextField(max_length=10000)
    upload_file = models.FileField(upload_to='contact/')

    def __str__(self):
        return self.full_name
