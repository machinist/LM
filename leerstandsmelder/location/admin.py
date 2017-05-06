from django.contrib import admin
from .models import Location, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'created')
    list_filter = ('region', 'created', 'degree', 'owner', 'empty_since')
    inlines = (PhotoInline,)
