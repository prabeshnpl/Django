from django.shortcuts import render
from .models import PASSENGER
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='users:login')
def index(request):
    passenger = PASSENGER.objects.all()
    return render(request,'passenger/index.html',{'passengers':passenger})
