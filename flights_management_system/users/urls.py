from django.urls import path
from . import views


app_name = 'USER'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.LoginView,name='login'),
    path('register/',views.RegistrationView,name='registration'),
    path('logout/',views.LoginView,name='logout'),
]