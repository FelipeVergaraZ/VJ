from django.urls import path
from .views import home, items


urlpatterns = [
    path('index.html',home,name='home'),
    path('items.html',items,name='items'),
]

