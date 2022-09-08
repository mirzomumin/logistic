from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _
import phonenumbers

from helpers.models import MainModel
# Create your models here.


class Mail(MainModel):
	name = None
	first_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=256)
	email = models.EmailField()
	phone = PhoneNumberField()
	postal_code = models.PositiveIntegerField(
		validators=[RegexValidator('^[0-9]{6}$', _('Invalid postal code'))],)
	message = models.TextField()

	def __str__(self):
		return f'{self.first_name} -\
		{self.last_name} - {self.email} -\
		{self.phone} - {self.message}'