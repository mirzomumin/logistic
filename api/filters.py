from django_filters import rest_framework as filters

from truck.models import Truck
from trailer.models import Trailer


class TruckFilter(filters.FilterSet):

	# Ordering of Truck List
	ordering = filters.OrderingFilter(
		choices = (
			('price', 'Price: Low to High'),
			('-price', 'Price: High to Low'),
			('year', 'Year: Low to High'),
			('-year', 'Year: High to Low'),
			('manufacturer', 'Manufacturer'),
			('model', 'Model'),
			('stock_number', 'Stock Number'),
			('-created_at', 'Recently Added'),
			('-updated_at', 'Recently Updated')
		)
	)

	class Meta:
		model = Truck
		fields = ('ordering',)


class TrailerFilter(filters.FilterSet):

	# Ordering of Trailer List
	ordering = filters.OrderingFilter(
		choices = (
			('price', 'Price: Low to High'),
			('-price', 'Price: High to Low'),
			('year', 'Year: Low to High'),
			('-year', 'Year: High to Low'),
			('manufacturer', 'Manufacturer'),
			('model', 'Model'),
			('stock_number', 'Stock Number'),
			('-created_at', 'Recently Added'),
			('-updated_at', 'Recently Updated')
		)
	)

	class Meta:
		model = Trailer
		fields = ('ordering',)