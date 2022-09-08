from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics
from mail.models import Mail

from .extra_serializers import MailSerializer


@api_view(['POST'])
def create_email(request):
	serializer = MailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data)
	return Response(serializer.errors)