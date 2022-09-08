from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from helpers.models import MainModel, BaseModel
from truck_utils.models import (TruckCategory,
	TruckManufacturer,
	Condition,
	EngineManufacturer,
	TransmissionManufacturer,
	ListingType,
	Country,
	State,
	City
	)
# Create your models here.

# Validation function
def validate_comma(value):
	if ',' in value:
		raise ValidationError(
			_('"%(value)s" should not have a comma character'),
			params={'value': value},
		)



class Truck(BaseModel):
	'''General info about Truck'''

	mileage = models.PositiveIntegerField(null=True, blank=True)
	odometer = models.CharField(max_length=256, null=True, blank=True)
	operating_condition = models.CharField(max_length=256, null=True, blank=True)

	# dependencies
	category = models.ForeignKey(TruckCategory, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='category_trucks')
	manufacturer = models.ForeignKey(TruckManufacturer, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='manufacturer_trucks')
	condition = models.ForeignKey(Condition, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='condition_trucks')
	listing_type = models.ForeignKey(ListingType, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='listing_trucks')
	country = models.ForeignKey(Country, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='country_trucks')
	state = models.ForeignKey(State, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='state_trucks')
	city = models.ForeignKey(City, on_delete=models.SET_NULL,
		null=True, blank=True, related_name='city_trucks')

	class Meta:
		ordering = ('manufacturer', 'model', 'year', 'price')

	def __str__(self):
		'''Simple representation of model'''
		return f'{self.year}\
		{self.manufacturer}\
		{self.model}'


class TruckEngine(models.Model):
	truck = models.OneToOneField(Truck, on_delete=models.CASCADE,
		null=True, blank=True, related_name='truck_engine')
	engine_manufacturer = models.ForeignKey(EngineManufacturer,
		on_delete=models.CASCADE, null=True, blank=True)
	horsepower = models.PositiveIntegerField(null=True, blank=True)
	engine_displacement = models.DecimalField(max_digits=4, decimal_places=1,
		null=True, blank=True)
	fuel_type = models.CharField(max_length=256, null=True, blank=True)
	engine_model = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.engine_manufacturer.name}\
		{self.engine_model} engine'


class TruckPowertrain(models.Model):
	truck = models.OneToOneField(Truck, on_delete=models.CASCADE,
		null=True, blank=True, related_name='truck_powertrain')
	transmission_manufacturer = models.ForeignKey(TransmissionManufacturer,
		on_delete=models.CASCADE, null=True, blank=True)
	transmission = models.CharField(max_length=256, null=True, blank=True)
	transmission_type = models.CharField(max_length=256, null=True, blank=True)
	number_of_speeds = models.PositiveIntegerField(null=True, blank=True)
	overdrive = models.CharField(max_length=256, null=True, blank=True)
	ratio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.transmission_manufacturer}\
		{self.transmission} {self.transmission_type} transmission\
		with {self.ratio} ratio'


class TruckChassis(models.Model):
	truck = models.OneToOneField(Truck, on_delete=models.CASCADE,
		null=True, blank=True, related_name='truck_chassis')
	drive = models.CharField(max_length=256, null=True, blank=True)
	number_of_rear_axles = models.CharField(max_length=256, null=True, blank=True)
	suspension = models.CharField(max_length=256, null=True, blank=True)
	color = models.CharField(max_length=256, null=True, blank=True)
	wheels = models.CharField(max_length=256, null=True, blank=True)
	wheelbase = models.PositiveIntegerField(null=True, blank=True)
	gvwr = models.CharField(max_length=256, null=True, blank=True)
	gvw = models.PositiveIntegerField(null=True, blank=True)


	class Meta:
		verbose_name_plural = 'Truck chassis'

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} is {self.number_of_rear_axles}\
		and has {self.color} color'


class TruckInterior(models.Model):
	truck = models.OneToOneField(Truck, on_delete=models.CASCADE,
		null=True, blank=True, related_name='truck_interior')
	drive_side = models.CharField(max_length=256, null=True, blank=True)
	power_steering = models.CharField(max_length=256, null=True, blank=True)
	tilt_telescope = models.CharField(max_length=256, null=True, blank=True)
	air_conditioning = models.CharField(max_length=256, null=True, blank=True)
	air_conditioning_condition = models.CharField(max_length=256, null=True, blank=True)
	cruise_control = models.CharField(max_length=256, null=True, blank=True)
	power_locks = models.CharField(max_length=256, null=True, blank=True)
	sleeper = models.CharField(max_length=256, null=True, blank=True)
	sleeper_size = models.PositiveIntegerField(null=True, blank=True)
	number_of_beds = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.number_of_beds} beds,\
		{self.drive_side}'


class TruckExterior(models.Model):
	truck = models.OneToOneField(Truck,
		on_delete=models.CASCADE, null=True, blank=True, related_name='truck_exterior')
	cab = models.CharField(max_length=256, null=True, blank=True)
	doors = models.CharField(max_length=256, null=True, blank=True)
	roof_type = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.cab} cab\
		,{self.doors} doors'


class TruckCapacities(models.Model):
	truck = models.OneToOneField(Truck,
		on_delete=models.CASCADE, null=True, blank=True, related_name='truck_capacities')
	fuel_capacity = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Truck capacities'

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.fuel_capacity} fuel capacity'


class TruckDimensions(models.Model):
	truck = models.OneToOneField(Truck,
		on_delete=models.CASCADE, null=True, blank=True, related_name='truck_dimensions')
	length = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Truck dimensions'

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.length} length'


class TruckCategorySpecific(models.Model):
	truck = models.OneToOneField(Truck,
		on_delete=models.CASCADE, null=True, blank=True, related_name='truck_category_specific')
	lift_and_gate = models.CharField(max_length=256, null=True, blank=True)

	def __str__(self):
		if self.lift_and_gate.lower() == 'yes':
			return f'{self.truck.year} {self.truck.manufacturer}\
			{self.truck.model} has lift and gate'
		elif self.lift_and_gate.lower() == 'no':
			return f'{self.truck.year} {self.truck.manufacturer}\
				{self.truck.model} has not lift and gate'
		return f'{self.truck.year} {self.truck.manufacturer}\
				{self.truck.model} has {self.lift_and_gate} lift and gate'


class TruckAttachments(models.Model):
	truck = models.OneToOneField(Truck,
		on_delete=models.CASCADE, null=True, blank=True, related_name='truck_attachments')
	apu = models.CharField(max_length=256, null=True, blank=True)
	apu_type = models.CharField(max_length=256, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Truck attachments'

	def __str__(self):
		if self.apu.lower() == 'yes':
			return f'{self.truck.year} {self.truck.manufacturer}\
				{self.truck.model} has {self.apu} apu'
		elif self.apu.lower() == 'no':
			return f'{self.truck.year} {self.truck.manufacturer}\
				{self.truck.model} has not apu'
		return f'{self.truck.year} {self.truck.manufacturer}\
			{self.truck.model} has {self.apu} apu'


class TruckImage(models.Model):
	truck = models.ForeignKey(Truck, on_delete=models.CASCADE,
		null=True, blank=True, related_name='truck_images')
	image = models.ImageField(upload_to='truck-images/', null=True, blank=True)

	def __str__(self):
		return f'{self.truck.year} {self.truck.manufacturer}\
		{self.truck.model} has {self.image} image'