from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.template import loader
from .models import *


# Create your views here.
def star_color_gen(tempk):
    if tempk in range(0,277):
        star_color = "#000"
        text_color = "#fff"
        return star_color, text_color
    elif tempk in range(275,502):
        star_color = "#726"
        text_color = "#fff"
        return star_color, text_color
    elif tempk in range(500,1402):
        star_color = "#a24"
        text_color = "#fff"
        return star_color, text_color
    elif tempk in range(1400,2502):
        star_color = "#e02"
        text_color = "#fff"
        return star_color, text_color
    elif tempk in range(2500, 4002):
        star_color = "#f50"
        text_color = "#fff"
        return star_color, text_color
    elif tempk in range(4000, 5202):
        star_color = "#fa0"
        text_color = "#000"
        return star_color, text_color
    elif tempk in range(5200, 6002):
        star_color = "#ff0"
        text_color = "#000"
        return star_color, text_color
    elif tempk in range(6000, 7202):
        star_color = "#ffd"
        text_color = "#000"
        return star_color, text_color
    elif tempk in range(7200, 10002):
        star_color = "#cde"
        text_color = "#000"
        return star_color, text_color
    elif tempk in range(10000, 25002):
        star_color = "#4be"
        text_color = "#000"
        return star_color, text_color
    elif tempk in range(25000, 150000):
        star_color = "#19f"
        text_color = "#fff"
        return star_color, text_color
    else:
        star_color = "#88f"
        text_color = "#000"
        return star_color, text_color

def index(request):
    star_list = SolarSystem.objects.order_by('distance')
    allegiance_list = SystemAllegiance.objects.order_by('id')
    template = loader.get_template('zookapp/index.html')
    context = {
        'star_list': star_list,
        'allegiance_list': allegiance_list
    }
    return HttpResponse(template.render(context, request))

def spindex(request):
    ship_list = Spaceship.objects.order_by('name')
    template = loader.get_template('zookapp/spindex.html')
    context = {
        'ship_list': ship_list
    }
    return HttpResponse(template.render(context, request))

def solar_system(request, solarsystem_id):
    solar_system = SolarSystem.objects.get(pk=solarsystem_id)
    star_list = solar_system.star_set.all()

    for s in star_list:
        s.solar_luminosities = (float(s.solar_radii)**2) * ((float(s.temperature_in_kelvin/5780))**4)
        s.solar_luminosities = int((s.solar_luminosities * 10000) + 0.5) / 10000.0
        s.star_color = star_color_gen(s.temperature_in_kelvin)[0]
        s.text_color = star_color_gen(s.temperature_in_kelvin)[1]

    return render(request, 'zookapp/solarsystem.html', {'solar_system': solar_system, 'star_list': star_list})

def spaceship(request, ship_id):
    spaceship = Spaceship.objects.get(pk=ship_id)
    return render(request, 'zookapp/spaceship.html', {'spaceship': spaceship})

def star(request, solarsystem_id, star_id):
    return render(request, 'zookapp/star.html')

def planet(request, solarsystem_id, star_id, planet_id):
    return render(request, 'zookapp/planet.html')

def edit_planet(request, solarsystem_id, star_id, planet_id):
    return render(request, 'zookapp/edit_planet.html')
