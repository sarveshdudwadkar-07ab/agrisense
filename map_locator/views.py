from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SoilTestingCenter

@login_required
def map_view(request):
    centers = SoilTestingCenter.objects.all()
    return render(request, 'map_locator/map.html', {'centers': centers})