from django.db import models

class Region(models.Model):
    title = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True)
    lat = models.DecimalField(max_digits=12, decimal_places=8)
    lon = models.DecimalField(max_digits=12, decimal_places=8)
    
    def __str__(self):
        return self.title

