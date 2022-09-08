from django.db import models

from helpers.models import MainModel
# Create your models here.


class TruckCategory(MainModel):
	parent = models.ForeignKey('self', on_delete=models.CASCADE,
		null=True, blank=True, related_name='subcategories')

	class Meta:
		verbose_name_plural = 'Truck categories'

	def __str__(self):
		return self.name


class TruckManufacturer(MainModel):
	pass

	def __str__(self):
		return self.name


class Condition(MainModel):
	pass

	def __str__(self):
		return self.name


class EngineManufacturer(MainModel):
	pass

	def __str__(self):
		return self.name


class TransmissionManufacturer(MainModel):
	pass

	def __str__(self):
		return self.name


class ListingType(MainModel):
	pass

	def __str__(self):
		return self.name


class Country(MainModel):
	pass

	class Meta:
		verbose_name_plural = 'countries'

	def __str__(self):
		return self.name


class State(MainModel):
	country = models.ForeignKey(Country, on_delete=models.CASCADE,
		null=True, blank=True, related_name='states')

	def __str__(self):
		return self.name


class City(MainModel):
	state = models.ForeignKey(State, on_delete=models.CASCADE,
		null=True, blank=True, related_name='cities')

	class Meta:
		verbose_name_plural = 'cities'

	def __str__(self):
		return self.name