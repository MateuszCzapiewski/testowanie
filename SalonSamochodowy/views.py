from django.shortcuts import render
from .models import listCars

def car_list(request):
    cars = listCars.objects.all()
    return render(request, 'car_list.html', {'cars': cars})
