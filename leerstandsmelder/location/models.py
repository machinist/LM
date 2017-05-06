import os
from django.db import models
from django.utils import timezone

class Location(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    building_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    street = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=255)

    active = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)
    demolished = models.BooleanField(default=False)
    rumor = models.BooleanField(default=False)
    owner = models.CharField(max_length=30)
    empty_since = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)

    region = models.ForeignKey('region.Region')

    lat = models.DecimalField(max_digits=12, decimal_places=8)
    lon = models.DecimalField(max_digits=12, decimal_places=8)
    
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

def photo_upload(instance, filename):
    base, ext = os.path.splitext(filename.lower())
    return 'location/{0}{1}'.format(instance.location.slug, ext)

class Photo(models.Model):
    location = models.ForeignKey(Location)
    image = models.ImageField(upload_to=photo_upload)

