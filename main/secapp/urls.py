from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
]
