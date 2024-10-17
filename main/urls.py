from django.urls import path
from .views import main_home

urlpatterns = [
    path('home',main_home,name='main')
]