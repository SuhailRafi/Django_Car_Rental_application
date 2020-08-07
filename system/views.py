from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse ("This is the home page")
def base (request):
    return HttpResponse ("This is the base page")
def carList (request):
    return HttpResponse ("This is the car list page")
def popularCar (request):
    return HttpResponse ("This is the popular car page")
def availableCar (request):
    return HttpResponse ("This is the available car page")
#def orderCreate (request):
#    return HttpResponse ("This is the order create page")
def orderDetails (request):
    return HttpResponse ("This is the order details page")
def orderList (request):
    return HttpResponse ("This is the order list page")
def forms (request):
    return HttpResponse ("This is the forms page")
#def carCreate (request):
#    return HttpResponse ("This is the car create page")
def carDetails (request):
    return HttpResponse ("This is the car details page")
def newCar (request):
    return HttpResponse ("This is the new car page")
#def adminIndex (request):
#    return HttpResponse ("This is the admin index page")
#def contact (request):
#    return HttpResponse ("Welcome to the home page")
    