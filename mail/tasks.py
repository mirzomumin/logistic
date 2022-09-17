from django.core.mail import BadHeaderError, send_mail
from rest_framework.response import Response
from django.conf import settings


from .models import (
	TruckMail,
	TruckFriendMail,
	TruckOffer,
	TrailerMail,
	TrailerOffer,
	TrailerFriendMail,
	FriendMail)


def send_truck_email(instance):
	subject = instance.truck
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_truck_friend_email(instance):
	subject = instance.truck
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_truck_offer_email(instance):
	subject = instance.truck
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_trailer_email(instance):
	subject = instance.trailer
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_trailer_friend_email(instance):
	subject = instance.trailer
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_trailer_offer_email(instance):
	subject = instance.trailer
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	if 'recipient_email' in [f.name for f in instance._meta.get_fields()]:
		recipient = instance.recipient_email
	recipient = 'eandatrucksales@gmail.com'
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_friend_email(instance):
	subject = 'Email from Friend'
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	recipient = instance.recipient_email
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})


def send_simple_form(instance):
	subject = 'Simple Form'
	first_name = instance.first_name
	last_name = instance.last_name
	message = instance.message
	from_user = instance.email
	from_email = settings.EMAIL_HOST_USER
	recipient = "eandatrucksales@gmail.com"
	body = f'Subject: {subject}\n \nFrom user: {from_user}\n \nFirst Name: {first_name}\n \nLast Name: {last_name}\n \nMessage: {message}'
	try:
		send_mail(
			subject,
			body,
			from_email,
			recipient_list = [recipient],
			fail_silently=True
		)
	except BadHeaderError:
		return Response({"response": "Invalid header found."})