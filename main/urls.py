from django.urls import path
from .views import main_home, portfolio_view,team_view,service_view

urlpatterns = [
    path('',main_home,name='main'),
    path('portfolio_view/<int:pk>',portfolio_view,name = 'portfolio_view'),
    path('team_detail/<int:pk>',team_view,name = 'team_detail'),
    path('service',service_view,name = 'service')
]