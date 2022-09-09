from django.db.models.signals import post_save
from django.dispatch import receiver
import asyncio

from .tasks import (
	send_truck_email,
	send_truck_friend_email,
	send_truck_offer_email,
	send_trailer_email,
	send_trailer_friend_email,
	send_trailer_offer_email,
	send_friend_email
)
from .models import (
	TruckMail,
	TruckFriendMail,
	TruckOffer,
	TrailerMail,
	TrailerOffer,
	TrailerFriendMail,
	FriendMail,
	TruckVideoMail,
	TrailerVideoMail
)


@receiver(post_save, sender=TruckMail)
async def create_user_profile(sender, instance, created, **kwargs):
	if created:
		await asyncio.sleep(0.5)
		send_truck_email(instance)


@receiver(post_save, sender=TruckFriendMail)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_truck_friend_email(instance)


@receiver(post_save, sender=TruckOffer)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_truck_offer_email(instance)


@receiver(post_save, sender=TruckVideoMail)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_truck_offer_email(instance)


@receiver(post_save, sender=TrailerMail)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_trailer_email(instance)


@receiver(post_save, sender=TrailerOffer)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_trailer_offer_email(instance)


@receiver(post_save, sender=TrailerFriendMail)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_trailer_friend_email(instance)


@receiver(post_save, sender=TrailerVideoMail)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		send_trailer_offer_email(instance)


@receiver(post_save, sender=FriendMail)
async def create_user_profile(sender, instance, created, **kwargs):
	if created:
		await asyncio.sleep(0.5)
		send_friend_email(instance)