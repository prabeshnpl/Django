from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'Airports'
urlpatterns=[
    path('',views.index,name='index'),
    path('<int:pk>',views.airport,name='airport'),
    path('logout/',LogoutView.as_view(next_page='users:login'),name='logout'),
]

 