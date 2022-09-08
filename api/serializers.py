from rest_framework import serializers
from collections import OrderedDict


# Import models
from truck_utils.models import (
	TruckCategory,
	TruckManufacturer,
	Condition,
	EngineManufacturer,
	ListingType,
	Country,
	State,
	City)

from truck.models import (Truck,
	TruckEngine,
	TruckPowertrain,
	TruckChassis,
	TruckInterior,
	TruckExterior,
	TruckCapacities,
	TruckDimensions,
	TruckCategorySpecific,
	TruckAttachments,
	TruckImage)

# Serializers of models related to Truck utils/serializers for filtering
class TruckCategorySerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TruckCategory
		fields = ('id', 'name', 'count', 'subcategories')
		read_only_fields = fields

	def get_fields(self):
		fields = super(TruckCategorySerializer, self).get_fields()
		fields['subcategories'] = TruckCategorySerializer(many=True)
		return fields

	def to_representation(self, instance):
		result = super(TruckCategorySerializer, self).to_representation(instance)
		result['count'] = instance.category_trucks.all().count()
		if result['subcategories']:
			result['count'] = sum([subcategory['count'] for subcategory in result['subcategories']]) + instance.category_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class ListingTypeSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = ListingType
		fields = ('id', 'name', 'count')
		read_only_fields = fields

	def to_representation(self, instance):
		result = super(ListingTypeSerializer, self).to_representation(instance)
		result['count'] = instance.listing_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class TruckManufacturerSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=False)
	class Meta:
		model = TruckManufacturer
		fields = ('id', 'name', 'count')
		read_only_fields = fields

	def to_representation(self, instance):
		result = super(TruckManufacturerSerializer, self).to_representation(instance)
		result['count'] = instance.manufacturer_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class ConditionSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = Condition
		fields = ('id', 'name', 'count')
		read_only_fields = fields

	def to_representation(self, instance):
		result = super(ConditionSerializer, self).to_representation(instance)
		result['count'] = instance.condition_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class CountrySerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = Country
		fields = ('id', 'name', 'count')

	def to_representation(self, instance):
		result = super(CountrySerializer, self).to_representation(instance)
		result['count'] = instance.country_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class StateSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = State
		fields = ('id', 'name', 'count')

	def to_representation(self, instance):
		result = super(StateSerializer, self).to_representation(instance)
		result['count'] = instance.state_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class CitySerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = City
		fields = ('id', 'name', 'count')

	def to_representation(self, instance):
		result = super(CitySerializer, self).to_representation(instance)
		result['count'] = instance.city_trucks.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


# Serializers of models related to Truck
class TruckEngineSerializer(serializers.ModelSerializer):
	engine_manufacturer = serializers.SerializerMethodField()
	class Meta:
		model = TruckEngine
		exclude = ('truck', 'id')

	def get_engine_manufacturer(self, obj):
		if obj.engine_manufacturer is not None:
			return obj.engine_manufacturer.name

	def to_representation(self, instance):
		result = super(TruckEngineSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class FuelTypeSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TruckEngine
		fields = ('fuel_type', 'count')

	def to_representation(self, instance):
		result = super(FuelTypeSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckEngineManufacturerSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = EngineManufacturer
		fields = ('name', 'count',)

	def to_representation(self, instance):
		result = super(TruckEngineManufacturerSerializer, self).to_representation(instance)
		result['count'] = instance.truckengine_set.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()] and result['count'] > 0])


class TruckPowertrainSerializer(serializers.ModelSerializer):
	transmission_manufacturer = serializers.SerializerMethodField()
	class Meta:
		model = TruckPowertrain
		exclude = ('truck', 'id')

	def get_transmission_manufacturer(self, obj):
		if obj.transmission_manufacturer:
			return obj.transmission_manufacturer.name

	def to_representation(self, instance):
		result = super(TruckPowertrainSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TransmissionSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TruckPowertrain
		fields = ('transmission', 'transmission_type', 'number_of_speeds', 'count')

	def to_representation(self, instance):
		result = super(TransmissionSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TruckChassisSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TruckChassis
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckChassisSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TruckInteriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckInterior
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckInteriorSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckExteriorSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TruckExterior
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckExteriorSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckCapacitiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckCapacities
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckCapacitiesSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckDimensionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckDimensions
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckDimensionsSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckCategorySpecificSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckCategorySpecific
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckCategorySpecificSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckAttachmentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckAttachments
		exclude = ('truck', 'id')

	def to_representation(self, instance):
		result = super(TruckAttachmentsSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckImageSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = TruckImage
		exclude = ('truck', 'id')

	def get_image(self, obj):
		return obj.image.url

	def to_representation(self, instance):
		result = super(TruckImageSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])


class TruckSerializer(serializers.ModelSerializer):
	truck_engine = TruckEngineSerializer()
	truck_powertrain = TruckPowertrainSerializer()
	truck_chassis = TruckChassisSerializer()
	truck_interior = TruckInteriorSerializer()
	truck_exterior = TruckExteriorSerializer()
	truck_capacities = TruckCapacitiesSerializer()
	truck_dimensions = TruckDimensionsSerializer()
	truck_category_specific = TruckCategorySpecificSerializer()
	truck_attachments = TruckAttachmentsSerializer()
	truck_images = TruckImageSerializer(many=True)
	category = serializers.SerializerMethodField()
	manufacturer = serializers.SerializerMethodField()
	condition = serializers.SerializerMethodField()
	listing_type = serializers.SerializerMethodField()
	country = serializers.SerializerMethodField()
	state = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()
	class Meta:
		model = Truck
		fields = '__all__'

	def get_category(self, obj):
		if obj.category:
			return obj.category.name

	def get_manufacturer(self, obj):
		if obj.manufacturer:
			return obj.manufacturer.name

	def get_condition(self, obj):
		if obj.condition:
			return obj.condition.name

	def get_listing_type(self, obj):
		if obj.listing_type:
			return obj.listing_type.name

	def get_country(self, obj):
		if obj.country:
			return obj.country.name

	def get_state(self, obj):
		if obj.state:
			return obj.state.name

	def get_city(self, obj):
		if obj.city:
			return obj.city.name

	def to_representation(self, instance):
		result = super(TruckSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, '', [], ()]])