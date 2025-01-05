from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns=[
    path('',views.index,name='passenger'),
    path('logout/',LogoutView.as_view(next_page='users:login'),name='logout'),

    
]