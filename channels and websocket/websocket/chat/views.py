from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request,'chat.html')

def join(request):
    return render(request,'join.html')