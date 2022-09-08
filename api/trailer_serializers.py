from rest_framework import serializers
from collections import OrderedDict
from django.db.models import Count

# from trailer_utils.models import
from trailer.models import (
	Trailer,
	TrailerDimensions,
	TrailerCategorySpecific,
	TrailerChassis,
	TrailerInterior,
	TrailerExterior,
	TrailerImage)
from trailer_utils.models import TrailerCategory, TrailerManufacturer
from truck_utils.models import ListingType, Condition, Country


class TrailerListingTypeSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = ListingType
		fields = ('name', 'count')

	def to_representation(self, instance):
		result = super(TrailerListingTypeSerializer, self).to_representation(instance)
		result['count'] = instance.listing_type_trailers.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in (None, 0, '', [], ()) and result['count'] > 0])


class TrailerConditionSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = Condition
		fields = ('name', 'count')

	def to_representation(self, instance):
		result = super(TrailerConditionSerializer, self).to_representation(instance)
		result['count'] = instance.condition_trailers.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in (None, 0, '', [], ()) and result['count'] > 0])


class TrailerCountrySerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = Country
		fields = ('name', 'count')

	def to_representation(self, instance):
		result = super(TrailerCountrySerializer, self).to_representation(instance)
		result['count'] = instance.country_trailers.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in (None, 0, '', [], ()) and result['count'] > 0])


class TrailerCategorySerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TrailerCategory
		fields = ('name', 'subcategories', 'count')

	def get_fields(self):
		fields = super(TrailerCategorySerializer, self).get_fields()
		fields['subcategories'] = TrailerCategorySerializer(many=True)
		return fields

	def to_representation(self, instance):
		result = super(TrailerCategorySerializer, self).to_representation(instance)
		result['count'] = instance.category_trailers.all().count()
		if result['subcategories']:
			result['count'] = sum([subcategory['count'] for subcategory in result['subcategories']]) + instance.category_trailers.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in (None, 0, '', [], ()) and result['count'] > 0])


class TrailerManufacturerSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TrailerManufacturer
		fields = ('name', 'count')

	def to_representation(self, instance):
		result = super(TrailerManufacturerSerializer, self).to_representation(instance)
		result['count'] = instance.manufacturer_trailers.all().count()
		return OrderedDict([(key, result[key]) for key in result if result[key] not in (None, 0, '', [], ()) and result['count'] > 0])


class TrailerDimensionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerDimensions
		exclude = ('trailer', 'id',)

	def to_representation(self, instance):
		result = super(TrailerDimensionsSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in [None, 0, '', [], ()]])


class TrailerCategorySpecificSerializer(serializers.ModelSerializer):
	count = serializers.IntegerField(default=None)
	class Meta:
		model = TrailerCategorySpecific
		fields = ('lift_and_gate', 'composition', 'logistic_posts', 'logistic_post_spacing', 'scuffliner', 'scuffliner_type', 'two_speed_landing_gear', 'count')

	def to_representation(self, instance):
		result = super(TrailerCategorySpecificSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TrailerChassisSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerChassis
		exclude = ('trailer', 'id',)

	def to_representation(self, instance):
		result = super(TrailerChassisSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TrailerExteriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerExterior
		exclude = ('trailer', 'id',)

	def to_representation(self, instance):
		result = super(TrailerExteriorSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TrailerInteriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerInterior
		exclude = ('trailer', 'id',)

	def to_representation(self, instance):
		result = super(TrailerInteriorSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])


class TrailerImageSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = TrailerImage
		exclude = ('trailer', 'id',)

	def to_representation(self, instance):
		result = super(TrailerImageSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])

	def get_image(self, obj):
		if obj.image:
			return obj.image.url

class TrailerSerializer(serializers.ModelSerializer):
	trailer_images = TrailerImageSerializer(many=True)
	trailer_dimensions = TrailerDimensionsSerializer()
	trailer_category_specific = TrailerCategorySpecificSerializer()
	trailer_chassis = TrailerChassisSerializer()
	trailer_interior = TrailerInteriorSerializer()
	trailer_exterior = TrailerExteriorSerializer()
	condition = serializers.SerializerMethodField()
	category = serializers.SerializerMethodField()
	manufacturer = serializers.SerializerMethodField()
	country = serializers.SerializerMethodField()
	state = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()
	listing_type = serializers.SerializerMethodField()

	class Meta:
		model = Trailer
		fields = '__all__'

	def get_condition(self, obj):
		if obj.condition:
			return obj.condition.name

	def get_category(self, obj):
		if obj.category:
			return obj.category.name

	def get_manufacturer(self, obj):
		if obj.manufacturer:
			return obj.manufacturer.name

	def get_country(self, obj):
		if obj.country:
			return obj.country.name

	def get_state(self, obj):
		if obj.state:
			return obj.state.name

	def get_city(self, obj):
		if obj.city:
			return obj.city.name

	def get_listing_type(self, obj):
		if obj.listing_type:
			return obj.listing_type.name

	def to_representation(self, instance):
		result = super(TrailerSerializer, self).to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in\
			[None, 0, '', [], ()]])