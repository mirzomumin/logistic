from django.contrib import admin

from .models import (
	Truck,
	TruckEngine,
	TruckPowertrain,
	TruckChassis,
	TruckInterior,
	TruckExterior,
	TruckCapacities,
	TruckDimensions,
	TruckCategorySpecific,
	TruckAttachments,
	TruckImage)
# Register your models here.

admin.site.register(Truck)
admin.site.register(TruckEngine)
admin.site.register(TruckPowertrain)
admin.site.register(TruckChassis)
admin.site.register(TruckInterior)
admin.site.register(TruckExterior)
admin.site.register(TruckCapacities)
admin.site.register(TruckDimensions)
admin.site.register(TruckCategorySpecific)
admin.site.register(TruckAttachments)
admin.site.register(TruckImage)