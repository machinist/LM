import requests
import json
import time
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from leerstandsmelder.region.models import Region
from leerstandsmelder.location.models import Location, Photo

REGIONS = 'https://api.leerstandsmelder.de/regions'
LOCATIONS = 'https://api.leerstandsmelder.de/regions/{0}/locations'
LOCATION = 'https://api.leerstandsmelder.de/locations/{0}'
PHOTOS = 'https://api.leerstandsmelder.de/locations/{0}/photos'

# time between requests
NICE = .25

class Command(BaseCommand):
    help = "Initial import via rest api."

    def add_arguments(self, parser):
        parser.add_argument(
            '--photos', '-p', action='store_true', dest='load_photos', default=False,
            help='Download the photos (a lot more requests and data)',
        )
        
    def handle(self, *args, **options):
        # delete existing data
        Location.objects.all().delete()
        Region.objects.all().delete()

        # initialize session
        s = requests.Session()
        s.headers.update({'Content-Type': 'application/json'})

        # get regions
        r = s.get(REGIONS)
        regions = r.json()

        for reg in regions:
            time.sleep(NICE)

            region = Region(title=reg['title'], slug=reg['slug'], lat=reg['lonlat'][1], lon=reg['lonlat'][0])
            region.save()

            print('created region {0}'.format(region))

            locations_url = LOCATIONS.format(reg['uuid'])

            r = s.get(locations_url)
            locations = r.json()['results']
            for _loc in locations:
                time.sleep(NICE)

                location_url = LOCATION.format(_loc['slug'])
                r = s.get(location_url)

                loc = r.json()

                location = Location(region=region, title=loc['title'], slug=loc['slug'], description=loc.get('description', ''), 
                        created=loc['created'], lat=loc['lonlat'][1], lon=loc['lonlat'][0],
                        active=loc['active'], hidden=loc['hidden'], demolished=loc['demolished'], rumor=loc.get('rumor', False))
                        
                location.street = loc.get('buildingType', '') or ''
                location.postcode = loc.get('buildingType', '') or ''
                location.city = loc.get('buildingType', '') or ''
                
                if 'buildingType' in loc:
                    location.building_type = loc['buildingType']

                if 'owner' in loc:
                    location.owner = loc['owner'].split('.')[-1]

                if 'emptySince' in loc:
                    location.empty_since = loc['emptySince'].split('.')[-1]

                if 'degree' in loc:
                    location.degree = loc['degree'].split('.')[-1]
                
                location.save()
                print("  created location {0}".format(location))
		
                # skip photos if parameter not given
                if options['load_photos'] is False:
                    continue

                photos_url = PHOTOS.format(loc['uuid'])
                r = s.get(photos_url)
                photos = r.json()
                for pho in photos:
                    time.sleep(NICE)
                    url = pho['original_url']
                    print("    get photo {0}".format(url))
                    filename = os.path.basename(url)
                    photo = Photo(location=location)

                    r = s.get(url)
                    photo.image.save(filename, ContentFile(r.content))
                    photo.save()


