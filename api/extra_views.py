from rest_framework.decorators import api_view
from rest_framework.response import Response

from .extra_serializers import (
	TruckMailSerializer,
	TruckFriendMailSerializer,
	TruckOfferSerializer,
	TrailerMailSerializer,
	TrailerOfferSerializer,
	TrailerFriendMailSerializer,
	FriendMailSerializer,
)



@api_view(['POST'])
def create_truck_email(request):
	serializer = TruckMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_truck_friend_email(request):
	serializer = TruckFriendMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_truck_offer(request):
	serializer = TruckOfferSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_trailer_email(request):
	serializer = TrailerMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_trailer_offer(request):
	serializer = TrailerOfferSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_trailer_friend_email(request):
	serializer = TrailerFriendMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_friend_email(request):
	serializer = FriendMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)