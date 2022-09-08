from django.db import models
import datetime

def year_choices():
	return tuple([(r,r) for r in range(1984, datetime.date.today().year+1)])

class BaseModel(models.Model):
	'''Base model for Truck and Trailer'''

	price = models.PositiveIntegerField()
	year = models.PositiveIntegerField(null=True, blank=True, choices=year_choices())
	model = models.CharField(max_length=128, null=True, blank=True)
	vin = models.CharField(unique=True, max_length=256, null=True, blank=True)
	stock_number = models.CharField(unique=True, max_length=256, null=True, blank=True)
	state_dot = models.CharField(max_length=256, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class MainModel(models.Model):
	'''Main model for Truck and Trailer utils'''
	name = models.CharField(max_length=256, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True