from rest_framework import serializers

from mail.models import (
	TruckMail,
	TruckFriendMail,
	TruckOffer,
	TrailerMail,
	TrailerOffer,
	TrailerFriendMail,
	FriendMail,
	TruckVideoMail,
	TrailerVideoMail,
	SimpleForm)


class TruckMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckMail
		fields = '__all__'


class TruckFriendMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckFriendMail
		fields = '__all__'


class TruckOfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckOffer
		fields = '__all__'


class TrailerMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerMail
		fields = '__all__'


class TrailerOfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerOffer
		fields = '__all__'


class TrailerFriendMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TrailerFriendMail
		fields = '__all__'


class FriendMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = FriendMail
		fields = '__all__'


class TruckVideoMailSerializer(serializers.ModelSerializer):
	start_date = serializers.DateTimeField(input_formats=["%H:%M %Y-%m-%d"])
	end_date = serializers.DateTimeField(input_formats=["%H:%M %Y-%m-%d"])
	class Meta:
		model = TruckVideoMail
		fields = '__all__'


class TrailerVideoMailSerializer(serializers.ModelSerializer):
	start_date = serializers.DateTimeField(input_formats=["%H:%M %Y-%m-%d"])
	end_date = serializers.DateTimeField(input_formats=["%H:%M %Y-%m-%d"])
	class Meta:
		model = TrailerVideoMail
		fields = '__all__'


class SimpleFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = SimpleForm
		fields = '__all__'