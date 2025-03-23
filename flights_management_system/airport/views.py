from django.shortcuts import render,get_object_or_404
from .models import AIRPORT
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='users:login')
def index(request):
    airport = AIRPORT.objects.all()
    return render(request,'airports/index.html',{'airports':airport})


@login_required(login_url='users:login')
def airport(request,pk): 
    airport = get_object_or_404(AIRPORT,pk=pk)
    flights = airport.takeoff.all()
    return render(request,'airports/airport.html',{
        'airport':airport,
        'flights': flights,
    })

 