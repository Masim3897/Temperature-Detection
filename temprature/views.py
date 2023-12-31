from django .http import HttpResponse
from django.shortcuts import render
from view.models import Temprature
import random

def homepage(request):
        
        #temp=Temprature.objects.all() #queryset(objects)
        temp=Temprature.objects.values_list() #list
        
        cities_names = list(Temprature.objects.values_list('name',flat=True))
        temperature_values = list(Temprature.objects.values_list('value',flat=True))

        new_random_values = generate_random_values(cities_names)
        
        print("new_random_values = " )

        print(new_random_values)
        data = {
         'names':cities_names,
         'temp':temperature_values,
    }

      
        return render(request,"index.html",context=data)


def temp(request):
    return HttpResponse("Well Come")

def tempdetail(request,tempid):
    return HttpResponse(tempid)

def generate_random_values(cities:list()):
     
     number_of_cities = len(cities)
     population = range(0, 100)
     new_values = random.sample(population, number_of_cities)

     return new_values
     pass