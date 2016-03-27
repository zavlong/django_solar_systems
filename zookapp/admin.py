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
admin.site.register(Station, ZookAdmin)
admin.site.register(StationType, ZookAdmin)
admin.site.register(StationEconomy, ZookAdmin)
admin.site.register(StationService, ZookAdmin)
admin.site.register(StationGovernment, ZookAdmin)
admin.site.register(StationFaction, ZookAdmin)
admin.site.register(SystemSecurity, ZookAdmin)
admin.site.register(SystemAllegiance, ZookAdmin)
admin.site.register(RingType, ZookAdmin)
admin.site.register(Spaceship, ZookAdmin)
admin.site.register(ShipType, ZookAdmin)
admin.site.register(ShipSize, ZookAdmin)
admin.site.register(SystemPermit, ZookAdmin)
admin.site.register(ShipCreator, ZookAdmin)
admin.site.register(Galaxy, ZookAdmin)
# admin.site.register(SpeciesSpacefaring, ZookAdmin)
# admin.site.register(PlanetHasSpecies, ZookAdmin)
