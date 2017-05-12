from django.shortcuts import render
from leerstandsmelder.region.models import Region

def region_list(request):
    queryset = Region.objects.all().order_by('title')
    return render(request, 'region/region_list.html', {
        'object_list': queryset
    })

