from django.urls import path
from . import views
urlpatterns = [
    path('',views.UserApiView.as_view(),name='user_api'),
    path('login/',views.LoginAPI.as_view(),name='login')
]