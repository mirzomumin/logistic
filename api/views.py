from rest_framework import generics
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta, datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from truck.models import (
	Truck,
	TruckEngine,
	TruckExterior,
	TruckPowertrain,
	TruckChassis)

from truck_utils.models import (
	TruckCategory,
	ListingType,
	TruckManufacturer,
	Condition,
	EngineManufacturer,
	Country,
	State,
	City)

from .serializers import (
	TruckSerializer,
	TruckCategorySerializer,
	ListingTypeSerializer,
	TruckManufacturerSerializer,
	ConditionSerializer,
	TruckChassisSerializer,
	TruckEngineSerializer,
	FuelTypeSerializer,
	TruckExteriorSerializer,
	TransmissionSerializer,
	TruckEngineManufacturerSerializer,
	CountrySerializer,
	StateSerializer,
	CitySerializer)

from trailer.models import Trailer
from .trailer_serializers import (
	TrailerSerializer,
	TrailerCategorySerializer,
	TrailerManufacturerSerializer,
	TrailerListingTypeSerializer,
	TrailerConditionSerializer,
	TrailerCountrySerializer,
)
from trailer_utils.models import (
	TrailerCategory,
	TrailerManufacturer
)


from .filters import TruckFilter, TrailerFilter
# Create your views here.


class TruckListView(generics.ListAPIView):
	serializer_class = TruckSerializer
	filterset_class = TruckFilter

	def get_queryset(self):
		queryset = Truck.objects.all()
		city = self.request.query_params.get('city')
		listing_type = self.request.query_params.get('listing-type')
		category = self.request.query_params.get('category')
		manufacturer = self.request.query_params.get('manufacturer')
		start_year = self.request.query_params.get('start-year')
		end_year = self.request.query_params.get('end-year')
		min_price = self.request.query_params.get('min-price')
		max_price = self.request.query_params.get('max-price')
		condition = self.request.query_params.get('condition')
		state = self.request.query_params.get('state')
		country = self.request.query_params.get('country')
		start_date = self.request.query_params.get('start-date')
		end_date = self.request.query_params.get('end-date')
		last_days = self.request.query_params.get('last-days')
		drive = self.request.query_params.get('drive')
		min_horsepower = self.request.query_params.get('min-horsepower')
		max_horsepower = self.request.query_params.get('max-horsepower')
		serial = self.request.query_params.get('serial')
		min_mileage = self.request.query_params.get('min-mileage')
		max_mileage = self.request.query_params.get('max-mileage')
		min_gvw = self.request.query_params.get('min-gvw')
		max_gvw = self.request.query_params.get('max-gvw')
		fuel_type = self.request.query_params.get('fuel-type')
		cab = self.request.query_params.get('cab')
		transmission = self.request.query_params.get('transmission')
		gvwr = self.request.query_params.get('gvwr')
		engine_manufacturer = self.request.query_params.get('engine-manufacturer')
		number_of_speed = self.request.query_params.get('number-of-speed')
		min_sleeper_size = self.request.query_params.get('min-sleeper-size')
		max_sleeper_size = self.request.query_params.get('max-sleeper-size')
		transmission_type = self.request.query_params.get('transmission-type')
		stock_number = self.request.query_params.get('stock')

		if listing_type:
			listing_types = listing_type.split('^^')
			queryset = queryset.filter(listing_type__name__in=listing_types)
		if category:
			categories = category.split('^^')
			queryset = queryset.filter(category__name__in=categories)
		if manufacturer:
			manufacturers = manufacturer.split('^^')
			queryset = queryset.filter(manufacturer__name__in=manufacturers)
		if start_year and end_year:
			queryset = queryset.filter(year__gte=start_year, year__lte=end_year)
		if min_price and max_price:
			queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
		if condition:
			conditons = condition.split('^^')
			queryset = queryset.filter(condition__name__in=conditons)
		if state:
			states = state.split('^^')
			queryset = queryset.filter(state__name__in=states)
		if city:
			cities = city.split('^^')
			queryset = queryset.filter(city__name__in=cities)
		if country:
			countries = country.split('^^')
			queryset = queryset.filter(country__name__in=countries)
		if (start_date and end_date) and not last_days:
			queryset = queryset.filter(created_at__gte=start_date, created_at__lte=end_date)
		if last_days and not (start_date or end_date):
			day_treshold = datetime.now() - timedelta(days=int(last_days))
			queryset = queryset.filter(created_at__gte=day_treshold)
		if drive:
			drives = drive.split('^^')
			queryset = queryset.filter(truck_chassis__drive__in=drives)
		if min_horsepower and max_horsepower:
			queryset = queryset.filter(truck_engine__horsepower__gte=min_horsepower,
				truck_engine__horsepower__lte=max_horsepower)
		if serial:
			queryset = queryset.filter(vin__exact=serial)
		if min_mileage and max_mileage:
			queryset = queryset.filter(mileage__gte=min_mileage, mileage__lte=max_mileage)
		if min_gvw and max_gvw:
			queryset = queryset.filter(truck_chassis__gvw__gte=min_gvw, truck_chassis__gvw__lte=max_gvw)
		if fuel_type:
			fuel_types = fuel_type.split('^^')
			queryset = queryset.filter(truck_engine__fuel_type__in=fuel_types)
		if cab:
			cabs = cab.split('^^')
			queryset = queryset.filter(truck_exterior__cab__in=cabs)
		if transmission:
			transmissions = transmission.split('^^')
			queryset = queryset.filter(truck_powertrain__transmission__in=transmissions)
		if gvwr:
			gvwrs = gvwr.split('^^')
			queryset = queryset.filter(truck_chassis__gvwr__in=gvwrs)
		if engine_manufacturer:
			engine_manufacturers = engine_manufacturer.split('^^')
			queryset = queryset.filter(truck_engine__engine_manufacturer__name__in=engine_manufacturers)
		if number_of_speed:
			number_of_speeds = number_of_speed.split('^^')
			queryset = queryset.filter(truck_powertrain__number_of_speeds__in=number_of_speeds)
		if min_sleeper_size and max_sleeper_size:
			queryset = queryset.filter(truck_interior__sleeper_size__gte=min_sleeper_size, truck_interior__sleeper_size__lte=max_sleeper_size)
		if transmission_type:
			transmission_types = transmission_type.split('^^')
			queryset = queryset.filter(truck_powertrain__transmission_type__in=transmission_types)
		if stock_number:
			queryset = queryset.filter(stock_number__exact=stock_number)


		return queryset


class TruckDetailView(generics.RetrieveAPIView):
	serializer_class = TruckSerializer
	queryset = Truck.objects.all()


class TrailerListView(generics.ListAPIView):
	serializer_class = TrailerSerializer
	filterset_class = TrailerFilter

	def get_queryset(self):
		queryset = Trailer.objects.all()
		serial = self.request.query_params.get('serial')
		min_gvw = self.request.query_params.get('min-gvw')
		max_gvw = self.request.query_params.get('max-gvw')
		stock = self.request.query_params.get('stock')
		listing_type = self.request.query_params.get('listing-type')
		category = self.request.query_params.get('category')
		manufacturer = self.request.query_params.get('manufacturer')
		condition = self.request.query_params.get('condition')
		start_date = self.request.query_params.get('start-date')
		end_date = self.request.query_params.get('end-date')
		last_days = self.request.query_params.get('last-days')

		if serial:
			queryset = queryset.filter(vin__exact=serial)
		if min_gvw and max_gvw:
			queryset = queryset.filter(trailer_chassis__gte=min_gvw,
				trailer_chassis__lte=max_gvw)
		if stock:
			queryset = queryset.filter(stock_number__exact=stock)
		if listing_type:
			listing_types = listing_type.split('^^')
			queryset = queryset.filter(listing_type__name__in=listing_types)
		if category:
			categories = category.split('^^')
			queryset = queryset.filter(category__name__in=categories)
		if manufacturer:
			manufacturers = manufacturer.split('^^')
			queryset = queryset.filter(manufacturer__name__in=manufacturers)
		if condition:
			conditions = condition.split('^^')
			queryset = queryset.filter(condition__name__in=conditions)
		if last_days and not (start_date or end_date):
			days_treshold = datetime.now() - timedelta(days=int(last_days))
			queryset = queryset.filter(created_at__gte=days_treshold)
		if (start_date and end_date) and not last_days:
			queryset = queryset.filter(created_at__gte=start_date, created_at__lte=end_date)
		return queryset


class TrailerDetailView(generics.RetrieveAPIView):
	queryset = Trailer.objects.all()
	serializer_class = TrailerSerializer


@api_view(['GET'])
def get_truck_filter_options(request):
	data = {}

	# Category options
	categories_values = TruckCategory.objects.filter(~Q(subcategories=None), parent=None)
	category_serializer = TruckCategorySerializer(categories_values, many=True)
	data['category_options'] = category_serializer.data

	# Listing Type options
	listing_types_values = ListingType.objects.filter(~Q(listing_trucks=None))
	listing_type_serializer = ListingTypeSerializer(listing_types_values, many=True)
	data['listing_type_options'] = listing_type_serializer.data

	# Truck manufacturer
	manufacturer_values = TruckManufacturer.objects.filter(~Q(manufacturer_trucks=None))
	manufacturer_serializer = TruckManufacturerSerializer(manufacturer_values, many=True)
	data['manufacturer_options'] = manufacturer_serializer.data

	# Truck condition
	condition_values = Condition.objects.filter(~Q(condition_trucks=None)).annotate(
		count = Count('condition_trucks', distinct=True)
	)
	condition_serializer = ConditionSerializer(condition_values, many=True)
	data['condition_options'] = condition_serializer.data

	# Truck drive
	drive_values = TruckChassis.objects.values('drive').annotate(
		count = Count('drive')
	)
	drive_serializer = TruckChassisSerializer(drive_values, many=True)
	data['drive_options'] = drive_serializer.data

	# Fuel Type
	fuel_type_values = TruckEngine.objects.values('fuel_type').annotate(
		count = Count('fuel_type')
	)
	fuel_type_serializer = FuelTypeSerializer(fuel_type_values, many=True)
	data['fuel_type_options'] = fuel_type_serializer.data

	# Cab
	cab_values = TruckExterior.objects.values('cab').annotate(
		count = Count('cab')
	)
	cab_serializer = TruckExteriorSerializer(cab_values, many=True)
	data['cab_options'] = cab_serializer.data

	# Transmission
	transmission_values = TruckPowertrain.objects.values('transmission').annotate(
		count = Count('transmission')
	)
	transmission_serializer = TransmissionSerializer(transmission_values, many=True)
	data['transmission_options'] = transmission_serializer.data

	# Gross Vehicle Weight Rating
	gvwr_values = TruckChassis.objects.values('gvwr').annotate(
		count = Count('gvwr')
	)
	gvwr_serializer = TruckChassisSerializer(gvwr_values, many=True)
	data['gvwr_options'] = gvwr_serializer.data

	# Engine Manufacturer
	engine_manufacturer_values = EngineManufacturer.objects.filter(~Q(truckengine=None))
	engine_manufacturer_serializer = TruckEngineManufacturerSerializer(engine_manufacturer_values, many=True)
	options = {'engine_manufacturer_options': engine_manufacturer_serializer.data}
	data['engine_manufacturer_options'] = engine_manufacturer_serializer.data

	# Number of Speeds
	speed_values = TruckPowertrain.objects.filter(~Q(number_of_speeds=None)).values('number_of_speeds').annotate(count=Count('number_of_speeds'))
	speed_serializer = TransmissionSerializer(speed_values, many=True)
	data['number_of_speeds'] = speed_serializer.data

	# Suspension
	suspension_values = TruckChassis.objects.filter(~Q(suspension=None)).values('suspension').annotate(
		count = Count('suspension')
	)
	suspension_serializer = TruckChassisSerializer(suspension_values, many=True)
	data['suspension'] = suspension_serializer.data

	# Transmission Type
	transmission_type_values = TruckPowertrain.objects.filter(~Q(transmission_type=None)).values('transmission_type').annotate(
		count = Count('transmission_type', )
	)
	transmission_type_serializer = TransmissionSerializer(transmission_type_values, many=True)
	data['transmission_type'] = transmission_type_serializer.data

	# Country
	country_values = Country.objects.filter(~Q(country_trucks=None))
	country_serializer = CountrySerializer(country_values, many=True)
	data['country_options'] = country_serializer.data

	# State
	state_values = State.objects.filter(~Q(state_trucks=None))
	state_serializer = StateSerializer(state_values, many=True)
	data['state_options'] = state_serializer.data

	# City
	city_values = City.objects.filter(~Q(city_trucks=None))
	city_serializer = CitySerializer(city_values, many=True)
	data['city_options'] = city_serializer.data

	return Response(data)


@api_view(['GET'])
def get_trailer_filter_options(request):
	data = {}

	# Listing Type
	listing_type_values = ListingType.objects.all()
	listing_type_serializer = TrailerListingTypeSerializer(listing_type_values, many=True)
	data['listing_type_options'] = listing_type_serializer.data

	# Trailer Category
	trailer_category_values = TrailerCategory.objects.filter(~Q(subcategories=None), parent=None)
	trailer_category_serializer = TrailerCategorySerializer(trailer_category_values, many=True)
	data['category_options'] = trailer_category_serializer.data

	# Trailer Manufacturer
	trailer_manufacturer_values = TrailerManufacturer.objects.all()
	trailer_manufacturer_serializer = TrailerManufacturerSerializer(trailer_manufacturer_values, many=True)
	data['manufacturer_options'] = trailer_manufacturer_serializer.data

	# Trailer Condition
	condition_values = Condition.objects.all()
	condition_serializer = TrailerConditionSerializer(condition_values, many=True)
	data['condition_options'] = condition_serializer.data

	# Trailer Country
	country_values = Country.objects.all()
	trailer_country_serializer = TrailerCountrySerializer(country_values, many=True)
	data['country_options'] = trailer_country_serializer.data

	return Response(data)