from django.db import models
from mezzanine.pages.models import Page


# Create your models here.

class SolarSystem(models.Model):
    name = models.CharField(max_length=200)
    distance = models.DecimalField(decimal_places=3, max_digits=20)
    x_coord = models.DecimalField(decimal_places=3, max_digits=20)
    y_coord = models.DecimalField(decimal_places=3, max_digits=20)
    z_coord = models.DecimalField(decimal_places=3, max_digits=20)
    security = models.ForeignKey('SystemSecurity', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('distance',)

class SpectralType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(max_length=200)
    orbital_radius_in_au = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    orbital_period_in_years = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    solar_radii = models.DecimalField(decimal_places=3, max_digits=7, default=1)
    solar_masses = models.DecimalField(decimal_places=3, max_digits=6, default=1)
    temperature_in_kelvin = models.IntegerField(default=5700)
    solar_luminosities = models.DecimalField(decimal_places=3, max_digits=13, default=1)
    solar_system = models.ForeignKey('SolarSystem', on_delete=models.CASCADE, blank=True, null=True)
    spectral_type = models.ForeignKey('SpectralType', on_delete=models.CASCADE, blank=True, null=True)
    visual_magnitude = models.DecimalField(decimal_places=2, max_digits=4, default=5)
    star_color = ""
    text_color = ""

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Planet(models.Model):
    name = models.CharField(max_length=200)
    orbital_radius_in_au = models.DecimalField(decimal_places=3, max_digits=20, default=1)
    orbital_period_in_years = models.DecimalField(decimal_places=3, max_digits=20, default=1)
    earth_radii = models.DecimalField(decimal_places=3, max_digits=7, default=1)
    earth_masses = models.DecimalField(decimal_places=3, max_digits=13, default=1)
    temperature_in_kelvin = models.IntegerField(default=273)
    star = models.ForeignKey('Star', on_delete=models.CASCADE, blank=True, null=True)
    species = models.ManyToManyField('Species')
    percentage_of_water = models.IntegerField(blank=True, null=True)
    planet_type = models.ForeignKey('PlanetType', on_delete=models.CASCADE, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    economy = models.ForeignKey('StationEconomy', on_delete=models.CASCADE, blank=True, null=True)


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



    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=200)
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE, blank=True, null=True)
    station_type = models.ForeignKey('StationType', on_delete=models.CASCADE, blank=True, null=True)
    population = models.BigIntegerField(default=1000)
    economy = models.ForeignKey('StationEconomy', on_delete=models.CASCADE, blank=True, null=True)
    services = models.ManyToManyField('StationService')

    class Meta:
        ordering = ('-population',)

    def __str__(self):
        return self.name

class StationType(models.Model):
    name = models.CharField(max_length=200)
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

class PlanetType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class StarHasPlanet(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

class ConservationType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SpeciesType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class PlanetHasSpecies(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
