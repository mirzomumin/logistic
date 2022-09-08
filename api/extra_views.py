from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics
from mail.models import TruckMail

from .extra_serializers import TruckMailSerializer


@api_view(['POST'])
def create_email(request):
	serializer = TruckMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)