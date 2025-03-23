from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'FLIGHTS'
urlpatterns=[
    path('',views.flights,name='index'),    
    path('<int:pk>',views.fl_detail,name='fl_detail'),
    path('logout/',LogoutView.as_view(next_page='users:login'),name='logout')
]