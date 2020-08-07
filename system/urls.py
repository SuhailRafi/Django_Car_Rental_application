from django.urls import path
from systems import views

urlpatterns = [
    path ('', views.home, name='home'), #redirects to views.py and searches for home function for functionality
    path ('', views.base, name='base'),
    path ('', views.carList, name='carList'),
    path ('', views.popularCar, name='popularCar'),
    path ('', views.availableCar, name='availableCar'),
    path ('', views.orderCreate, name='orderCreate'),
    path ('', views.orderDetails, name='orderDetails'),
    path ('', views.orderList, name='orderList'),
    path ('', views.forms, name='forms'),
    path ('', views.carCreate, name='carCreate'),
    path ('', views.carDetails, name='carDetails'),
    path ('', views.newCar, name='newCar'),
    path ('', views.adminIndex, name='adminIndex'),
    path ('', views.adminMessage, name='adminMessage'),
    path ('', views.contact, name='contact'),
]