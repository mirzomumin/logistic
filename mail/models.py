from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _
import phonenumbers

from helpers.models import BaseMail
from truck.models import Truck
from trailer.models import Trailer
# Create your models here.


class TruckMail(BaseMail):
	truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
	phone = PhoneNumberField()
	postal_code = models.PositiveIntegerField(
		validators=[RegexValidator('^[0-9]{4,6}$', _('Invalid postal code'))],)

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.phone} - {self.truck} - {self.message}'


class TruckFriendMail(BaseMail):
	truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
	recipient_email = models.EmailField()

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.recipient_email} - {self.truck} - {self.message}'


class TruckOffer(BaseMail):
	truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
	phone = PhoneNumberField()
	postal_code = models.PositiveIntegerField(
		validators=[RegexValidator('^[0-9]{4,6}$', _('Invalid postal code'))],)
	offer_amount = models.PositiveIntegerField()
	currency = models.CharField(max_length=64)

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.phone} - {self.truck} - {self.message}'


class TrailerMail(BaseMail):
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
	phone = PhoneNumberField()
	postal_code = models.PositiveIntegerField(
		validators=[RegexValidator('^[0-9]{4,6}$', _('Invalid postal code'))],)

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.phone}- {self.trailer} - {self.message}'


class TrailerOffer(BaseMail):
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
	phone = PhoneNumberField()
	postal_code = models.PositiveIntegerField(
		validators=[RegexValidator('^[0-9]{4,6}$', _('Invalid postal code'))],)
	offer_amount = models.PositiveIntegerField()
	currency = models.CharField(max_length=64)

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.phone} - {self.trailer} - {self.message}'


class TrailerFriendMail(BaseMail):
	trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
	recipient_email = models.EmailField()

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.recipient_email} - {self.trailer} - {self.message}'


class FriendMail(BaseMail):
	recipient_email = models.EmailField()

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.recipient_email} - {self.message}'