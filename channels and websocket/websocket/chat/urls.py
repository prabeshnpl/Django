from django.urls import path
from .views import chat,join
urlpatterns = [
    path('', chat),
    path('join/', join),
]