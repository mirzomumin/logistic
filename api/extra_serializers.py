from rest_framework import serializers

from mail.models import (
	TruckMail,
	TruckFriendMail,
	TruckOffer,
	TrailerMail,
	TrailerOffer,
	TrailerFriendMail,
	FriendMail)


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