from django.db import models

from helpers.models import MainModel
# Create your models here.

class TrailerCategory(MainModel):
	parent = models.ForeignKey('self', on_delete=models.CASCADE,
		null=True, blank=True, related_name='subcategories')

	class Meta:
		verbose_name_plural = 'Trailer categories'

	def __str__(self):
		return self.name


class TrailerManufacturer(MainModel):
	pass

	def __str__(self):
		return self.name