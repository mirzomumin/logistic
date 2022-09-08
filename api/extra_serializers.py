from rest_framework import serializers

from mail.models import TruckMail


class TruckMailSerializer(serializers.ModelSerializer):
	class Meta:
		model = TruckMail
		fields = '__all__'