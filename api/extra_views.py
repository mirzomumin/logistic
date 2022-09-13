from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from .extra_serializers import (
	TruckMailSerializer,
	TruckFriendMailSerializer,
	TruckOfferSerializer,
	TrailerMailSerializer,
	TrailerOfferSerializer,
	TrailerFriendMailSerializer,
	FriendMailSerializer,
	TruckVideoMailSerializer,
	TrailerVideoMailSerializer,
	SimpleFormSerializer
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


@api_view(['POST'])
def create_truck_video_chat_email(request):
	serializer = TruckVideoMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_trailer_video_chat_email(request):
	serializer = TrailerVideoMailSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_simple_form(request):
	serializer = SimpleFormSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

		return Response(serializer.data, status=201)
	return Response(serializer.errors, status=400)



# PDF functions
@action(detail=True, methods=['get'])
def fetch_report_about_company(request, *args, **kwargs):
	short_report = open("static/pdf/Pagesfromsandhillsmag.pdf", 'rb')
	response = HttpResponse(FileWrapper(short_report), content_type='application/pdf')
	return response



@action(detail=True, methods=['get'])
def fetch_report_company_creadit_app(request, *args, **kwargs):
	short_report = open("static/pdf/Company_Credit_Application.pdf", 'rb')
	response = HttpResponse(FileWrapper(short_report), content_type='application/pdf')
	return response


@action(detail=True, methods=['get'])
def fetch_report_personal_credit_app(request, *args, **kwargs):
	short_report = open("static/pdf/Personal_Credit_Application.pdf", 'rb')
	response = HttpResponse(FileWrapper(short_report), content_type='application/pdf')
	return response