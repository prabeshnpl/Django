from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListTaskView,name='create_retrieve'),
    path('delete/<int:pk>/<slug:delete>',views.DeleteTaskView,name='delete'),
    path('update/<int:pk>',views.UpdateTaskView,name='update'),
]