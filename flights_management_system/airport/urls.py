from django.urls import path
from . import views

app_name = 'Airports'
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>',views.airport,name='airport')
]

 