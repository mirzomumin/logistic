from django.db import models

from helpers.models import BaseModel
from truck_utils.models import Condition, ListingType, Country, State, City
from trailer_utils.models import TrailerCategory, TrailerManufacturer
# Create your models here.

class Trailer(BaseModel):
	'''Trailer model'''
	qty = models.PositiveIntegerField(null=True, blank=True)
	condition = models.ForeignKey(Condition, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='condition_trailers')
	category = models.ForeignKey(TrailerCategory, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='category_trailers')
	manufacturer = models.ForeignKey(TrailerManufacturer, on_delete=models.SET_NULL,null=True, blank=True, related_name='manufacturer_trailers')
	listing_type = models.ForeignKey(ListingType, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='listing_type_trailers')
	country = models.ForeignKey(Country, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='country_trailers')
	state = models.ForeignKey(State, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='country_trailers')
	city = models.ForeignKey(City, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='country_trailers')

	class Meta:
		ordering = ('manufacturer', 'model', 'year', 'price')

	def __str__(self):
		return f'{self.year} {self.model} {self.manufacturer}'


class TrailerDimensions(models.Model):
	trailer = models.OneToOneField(Trailer, on_delete=models.CASCADE,
		null=True, blank=True, related_name='trailer_dimensions')
	width = models.PositiveIntegerField(null=True, blank=True)
	length = models.PositiveIntegerField(null=True, blank=True)
	height = models.CharField(max_length=64, null=True, blank=True)
	internal_height = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Trailer dimensions'

	def __str__(self):
		return f'{self.trailer.year}\
		{self.trailer.manufacturer}\
		{self.trailer.model} has {self.width} width,\
		{self.length} length, {self.height} height'


class TrailerCategorySpecific(models.Model):
	tariler = models.OneToOneField(Trailer, on_delete=models.CASCADE,
		null=True, blank=True, related_name='trailer_category_specific')
	lift_and_gate = models.CharField(max_length=256, null=True, blank=True)
	composition = models.CharField(max_length=256, null=True, blank=True)
	logistic_posts = models.CharField(max_length=256, null=True, blank=True)
	logistic_post_spacing = models.PositiveIntegerField(null=True, blank=True)
	scuffliner = models.CharField(max_length=256, null=True, blank=True)
	scuffliner_type = models.CharField(max_length=256, null=True, blank=True)
	two_speed_landing_gear = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		if self.lift_and_gate.lower() == 'yes':
			return f'{self.tariler.year} {self.tariler.manufacturer}\
			{self.tariler.model} has lift and gate'
		elif self.lift_and_gate.lower() == 'no':
			return f'{self.tariler.year} {self.tariler.manufacturer}\
				{self.tariler.model} has not lift and gate'
		return f'{self.tariler.year} {self.tariler.manufacturer}\
				{self.tariler.model} has {self.lift_and_gate} lift and gate'


class TrailerChassis(models.Model):
	trailer = models.OneToOneField(Trailer, on_delete=models.CASCADE,
		related_name='trailer_chassis', null=True, blank=True)
	suspension = models.CharField(max_length=256, null=True, blank=True)
	wheels = models.CharField(max_length=256, null=True, blank=True)
	color = models.CharField(max_length=256, null=True, blank=True)
	number_of_rear_axles = models.CharField(max_length=256, null=True, blank=True)
	axle_type = models.CharField(max_length=256, null=True, blank=True)
	floor_type = models.CharField(max_length=256, null=True, blank=True)
	gvw = models.PositiveIntegerField(null=True, blank=True)
	mud_flaps = models.CharField(max_length=256, null=True, blank=True)
	tires = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	tire_percent_remaining = models.PositiveIntegerField(null=True, blank=True)
	brake_percent_remaining = models.PositiveIntegerField(null=True, blank=True)
	skirts = models.CharField(max_length=256, null=True, blank=True)
	skirt_type = models.CharField(max_length=256, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Trailer chassis'

	def __str__(self):
		return f'{self.trailer.year} {self.trailer.manufacturer}\
		{self.trailer.model} is {self.number_of_rear_axles}\
		and has {self.color} color'


class TrailerInterior(models.Model):
	trailer = models.OneToOneField(Trailer, on_delete=models.CASCADE,
		related_name='trailer_interior', null=True, blank=True)
	lining_type = models.CharField(max_length=256, null=True, blank=True)
	treshold_plate = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		return f'{self.trailer.year} {self.trailer.manufacturer}\
		{self.trailer.model}\'s listing type is {self.lining_type}'


class TrailerExterior(models.Model):
	trailer = models.OneToOneField(Trailer, on_delete=models.CASCADE,
		related_name='trailer_exterior', null=True, blank=True)
	doors = models.CharField(max_length=256, null=True, blank=True)
	roof_type = models.CharField(max_length=256, null=True, blank=True)
	insulated = models.CharField(max_length=256, null=True, blank=True)
	lock_rods_number = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return f'{self.trailer.year} {self.trailer.manufacturer}\
		{self.trailer.model} has {self.roof_type} roof type\
		and {self.doors} doors'


class TrailerImage(models.Model):
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE,
		null=True, blank=True, related_name='trailer_images')
	image = models.ImageField(upload_to='trailer-images/', null=True, blank=True)

	def __str__(self):
		return f'{self.trailer.year} {self.trailer.manufacturer}\
		{self.trailer.model} has {self.image} image'