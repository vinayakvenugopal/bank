from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json as simplejson
from bankapp.models import *


# Create your views here.3
def index(request):
    return render(request,'home.html',)
def login(request):
    if request.method == 'POST':
        return redirect('page')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request,'register.html')
def page(request):
    return render(request,'page.html')


def form(request):
    if request.method == 'POST':
        return render(request,'reply.html')
    else:
        countries = Country.objects.all()
        print(countries)
        return render(request, 'form.html', {'countries': countries})

def getdetails(request):

    #country_name = request.POST['country_name']
    country_name = request.GET['cnt']
    print("ajax " + str(country_name))

    result_set = []
    all_cities = []

    answer = str(country_name[1:-1])
    selected_country = Country.objects.get(name=answer)
    print("selected country name " + str(selected_country))

    all_cities = selected_country.city_set.all()
    for city in all_cities:
        print("city name " + str(city.name))
        result_set.append({'name': city.name})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')