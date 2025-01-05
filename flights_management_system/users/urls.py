from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'USER'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.LoginView,name='login'),
    path('register/',views.RegistrationView,name='registration'),
    path('logout/',LogoutView.as_view(next_page='users:login'),name='logout'),
]