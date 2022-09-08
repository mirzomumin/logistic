from django.contrib import admin

from .models import (TruckCategory,
	TruckManufacturer,
	Condition,
	EngineManufacturer,
	TransmissionManufacturer,
	ListingType,
	Country,
	State,
	City,)
# Register your models here.

admin.site.register(TruckCategory)
admin.site.register(TruckManufacturer)
admin.site.register(Condition)
admin.site.register(EngineManufacturer)
admin.site.register(TransmissionManufacturer)
admin.site.register(ListingType)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)