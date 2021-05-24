from django.urls import path
from .views import home, items 

urlpatterns = [
    path('',home,name='home'),
    path('/items',items,name='items'),
]