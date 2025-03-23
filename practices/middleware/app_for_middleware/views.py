from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def home(request): 
    request.session['username'] = 'random' 
    if request.method == 'POST': 
        data = request.POST 
        request.session['username'] = data.get('username') 
    return TemplateResponse(request, 'index.html', context={'username': request.session['username']})