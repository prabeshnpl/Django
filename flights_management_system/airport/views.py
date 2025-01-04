from django.shortcuts import render,get_object_or_404
from .models import AIRPORT
from flights.models import FLIGHTS
# Create your views here.
def index(request):
    airport = AIRPORT.objects.all()
    return render(request,'airports/index.html',{'airports':airport})

def airport(request,pk): 
    airport = get_object_or_404(AIRPORT,pk=pk)
    flights = airport.takeoff.all()
    return render(request,'airports/airport.html',{
        'airport':airport,
        'flights': flights,
    })

 