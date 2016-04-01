from django.db import models
from mezzanine.pages.models import Page
import math

# Create your models here.
class Hof(Page):
    name = models.CharField(max_length=200)
    distance = models.DecimalField(decimal_places=3, max_digits=20)
    reference_point = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Galaxy(models.Model):
    name = models.CharField(max_length=200)
    distance = models.DecimalField(decimal_places=3, max_digits=20)
    reference_point = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('distance',)

class SolarSystem(models.Model):
    name = models.CharField(max_length=200)
    x_coord = models.DecimalField(decimal_places=3, max_digits=20) #decimal_places=3,
    y_coord = models.DecimalField(decimal_places=3, max_digits=20)
    z_coord = models.DecimalField(decimal_places=3, max_digits=20)
    galaxy = models.ForeignKey('Galaxy', on_delete=models.CASCADE, default=1)
    hof = models.ForeignKey('Hof', on_delete=models.CASCADE, default=4)
    security = models.ForeignKey('SystemSecurity', on_delete=models.CASCADE, blank=True, null=True)
    allegiance = models.ForeignKey('SystemAllegiance', on_delete=models.CASCADE, blank=True, null=True)
    faction = models.ForeignKey('StationFaction', on_delete=models.CASCADE, blank=True, null=True)
    permit = models.ForeignKey('SystemPermit',on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/solarsystems/", blank=True, null=True)
    planet_list = []

    def _get_total(self):
       "Returns the total"
       return round(math.sqrt(float(self.x_coord)**2.0 + float(self.y_coord)**2.0 + float(self.z_coord)**2.0),3)
    distance = property(_get_total)

    def __str__(self):
        return self.name

class Spaceship(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey('ShipCreator', on_delete=models.CASCADE, blank=True, null=True)
    cost = models.IntegerField(default=100000)
    size = models.ForeignKey('ShipSize', on_delete=models.CASCADE, blank=True, null=True)
    ship_type = models.ForeignKey('ShipType', on_delete=models.CASCADE, blank=True, null=True)
    agility = models.IntegerField(default=5)
    speed = models.IntegerField(default=200)
    boost = models.IntegerField(default=300)
    jump_range = models.DecimalField(decimal_places=2, max_digits=20, default=10)
    hardpoints = models.CharField(max_length=200, default="1 small")
    compartments = models.CharField(max_length=200, default="2xClass 2, 2xClass 1")
    cargo_space = models.IntegerField(default=8)
    fuel_space = models.IntegerField(default=4)
    image = models.ImageField(upload_to="images/solarsystems/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class ShipSize(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SystemPermit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ShipCreator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ShipType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SpectralType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Star(models.Model):
    name = models.CharField(max_length=200)
    orbital_radius_in_au = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    orbital_period_in_years = models.DecimalField(decimal_places=3, max_digits=20, null=True) # can be calculated - kepler's 3rd law
    solar_radii = models.DecimalField(decimal_places=3, max_digits=7, default=1)
    solar_masses = models.DecimalField(decimal_places=3, max_digits=10, default=1)
    temperature_in_kelvin = models.IntegerField(default=5700)
    solar_system = models.ForeignKey('SolarSystem', on_delete=models.CASCADE, blank=True, null=True)
    spectral_type = models.ForeignKey('SpectralType', on_delete=models.CASCADE, blank=True, null=True)
    visual_magnitude = models.DecimalField(decimal_places=2, max_digits=4, default=5) # can be calculated

    def _get_luminosity(self):
       "Returns the total"
       return round((float(self.solar_radii)**2) * ((float(self.temperature_in_kelvin/5780))**4),4)
    luminosity = property(_get_luminosity)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Planet(models.Model):
    name = models.CharField(max_length=200)
    orbital_radius_in_au = models.DecimalField(decimal_places=3, max_digits=20, default=1)
    earth_radii = models.DecimalField(decimal_places=3, max_digits=7, default=1)
    earth_masses = models.DecimalField(decimal_places=3, max_digits=13, default=1)
    temperature_in_kelvin = models.IntegerField(default=273) # can be calculated
    star = models.ForeignKey('Star', on_delete=models.CASCADE, blank=True, null=True)
    species = models.ManyToManyField('Species')
    percentage_of_water = models.IntegerField(blank=True, null=True)
    planet_type = models.ForeignKey('PlanetType', on_delete=models.CASCADE, blank=True, null=True)
    ring_type = models.ForeignKey('RingType', on_delete=models.CASCADE, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    economy = models.ForeignKey('StationEconomy', on_delete=models.CASCADE, blank=True, null=True)
    faction = models.ForeignKey('StationFaction', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('orbital_radius_in_au',)

class Species(models.Model):
    name = models.CharField(max_length=200)
    genus = models.CharField(max_length=200, null=True)
    species = models.CharField(max_length=200, default='')
    population = models.BigIntegerField(default=1000)
    species_type = models.ForeignKey('SpeciesType', on_delete=models.CASCADE, blank=True, null=True)
    conservation_type = models.ForeignKey('ConservationType', on_delete=models.CASCADE, blank=True, null=True)
    is_it_spacefaring = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=200)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE, blank=True, null=True)
    station_type = models.ForeignKey('StationType', on_delete=models.CASCADE, blank=True, null=True)
    population = models.BigIntegerField(default=1000)
    economy = models.ForeignKey('StationEconomy', on_delete=models.CASCADE, blank=True, null=True)
    faction = models.ForeignKey('StationFaction', on_delete=models.CASCADE, blank=True, null=True)
    services = models.ManyToManyField('StationService')

    class Meta:
        ordering = ('-population',)

    def __str__(self):
        return self.name

class StationType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class SystemAllegiance(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200, default="Independent")
    color = models.CharField(max_length=7, default="df0")
    def __str__(self):
        return self.name

class StationFaction(models.Model):
    name = models.CharField(max_length=200)
    government_type = models.ForeignKey('StationGovernment', on_delete=models.CASCADE, blank=True, null=True)
    popularity = models.IntegerField(default=100)
    def __str__(self):
        return self.name

class SystemSecurity(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StationEconomy(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StationService(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StationGovernment(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class PlanetType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RingType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ConservationType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SpeciesType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
