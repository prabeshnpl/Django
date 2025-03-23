from django.shortcuts import render,redirect
from .forms import Register
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

@login_required(login_url='users:login')
def index(request):
    return render(request,'users/index.html')

def RegistrationView(request):
    if request.method=='POST':
        form = Register(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('USER:login')

    form = Register()
    return render(request,'users/registration.html',{'form':form})

def LoginView(request):
    message = 'Please fill correct information'
    print(message)
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()        
            login(request,user)
            return redirect('USER:index')
        else : message = 'Invalid credentials'

    form = AuthenticationForm()
    print(message)
    return render(request,'users/login.html',{
        'form':form,
        'message':message,
        })

