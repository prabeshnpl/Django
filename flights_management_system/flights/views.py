from django.shortcuts import render,redirect
from . import models
from passenger.models import PASSENGER
# Create your views here.
def flights(request):
    f = models.FLIGHTS.objects.all()
    return render(request,'flights/index.html',{'flights':f})


def fl_detail(request,pk):
    
    f = models.FLIGHTS.objects.get(pk=pk)
    p = PASSENGER.objects.all()
    p_of_f = f.passenger.all()
    total_passenger = p.count() 

    if request.method == 'POST':
        new_passenger_id = request.POST.get('new_passenger')
        new_passenger = PASSENGER.objects.get(id=new_passenger_id)
        PASSENGER.objects.create(first=new_passenger.first,last=new_passenger.last,flight=f)
        return redirect('FLIGHTS:fl_detail',pk)

    return render(request,'flights/fl_detail.html',{
        'flight':f,
        'passengers':p_of_f,
        'all_passenger':p,
        'max_passenger':30,
        'total_passenger':total_passenger,
        })  