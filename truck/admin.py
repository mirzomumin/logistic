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
from .forms import TruckAdminForm

# Register your models here.
# admin.site.register(Truck)
# admin.site.register(TruckEngine)
# admin.site.register(TruckPowertrain)
# admin.site.register(TruckChassis)
# admin.site.register(TruckInterior)
# admin.site.register(TruckExterior)
# admin.site.register(TruckCapacities)
# admin.site.register(TruckDimensions)
# admin.site.register(TruckCategorySpecific)
# admin.site.register(TruckAttachments)
# admin.site.register(TruckImage)

class InlineTruckEngine(admin.StackedInline):
	model = TruckEngine


class InlineTruckPowertrain(admin.StackedInline):
	model = TruckPowertrain


class InlineTruckChassis(admin.StackedInline):
	model = TruckChassis


class InlineTruckInterior(admin.StackedInline):
	model = TruckInterior


class InlineTruckCategorySpecific(admin.StackedInline):
	model = TruckCategorySpecific


class InlineTruckCapacities(admin.StackedInline):
	model = TruckCapacities


class InlineTruckExterior(admin.StackedInline):
	model = TruckExterior


class InlineTruckDimensions(admin.StackedInline):
	model = TruckDimensions


class InlineTruckAttachments(admin.StackedInline):
	model = TruckAttachments


class InlineTruckImage(admin.StackedInline):
	model = TruckImage
	min_num = 1
	extra = 0





@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
	form = TruckAdminForm
	add_form = TruckAdminForm
	inlines = (
		InlineTruckEngine,
		InlineTruckPowertrain,
		InlineTruckChassis,
		InlineTruckInterior,
		InlineTruckCategorySpecific,
		InlineTruckCapacities,
		InlineTruckExterior,
		InlineTruckDimensions,
		InlineTruckAttachments,
		InlineTruckImage,
	)