from django.urls import path
from . import views

app_name = 'FLIGHTS'
urlpatterns=[
    path('',views.flights,name='index'),    
    path('<int:pk>',views.fl_detail,name='fl_detail'),
]