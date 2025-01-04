from django.shortcuts import render
from .models import PASSENGER
# Create your views here.
def index(request):
    passenger = PASSENGER.objects.all()
    return render(request,'passenger/index.html',{'passengers':passenger})
