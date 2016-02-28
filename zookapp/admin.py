from django.contrib import admin
from .models import *
# Register your models here.

class ZookAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(SolarSystem, ZookAdmin)
admin.site.register(Star, ZookAdmin)
admin.site.register(SpectralType, ZookAdmin)
admin.site.register(Planet, ZookAdmin)
admin.site.register(PlanetType, ZookAdmin)
# admin.site.register(StarHasPlanet, ZookAdmin)
admin.site.register(Species, ZookAdmin)
admin.site.register(SpeciesType, ZookAdmin)
admin.site.register(ConservationType, ZookAdmin)
# admin.site.register(PlanetHasSpecies, ZookAdmin)