from . import views
from django.urls import path


urlpatterns = [
    path('',views.ItemAPI.as_view(),name='Item_List'),
    path('<int:pk>/',views.ItemAPI.as_view(),name='Item_detail'),
]