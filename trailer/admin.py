from django.contrib import admin

from .models import (
	Trailer,
	TrailerDimensions,
	TrailerCategorySpecific,
	TrailerChassis,
	TrailerInterior,
	TrailerExterior,
	TrailerImage)

from .forms import TrailerAdminForm
# Register your models here.

# admin.site.register(TrailerDimensions)
# admin.site.register(TrailerCategorySpecific)
# admin.site.register(TrailerChassis)
# admin.site.register(TrailerInterior)
# admin.site.register(TrailerExterior)
# admin.site.register(TrailerImage)

class InlineTrailerChassis(admin.StackedInline):
	model = TrailerChassis


class InlineTrailerInterior(admin.StackedInline):
	model = TrailerInterior


class InlineTrailerExterior(admin.StackedInline):
	model = TrailerExterior


class InlineTrailerDimensions(admin.StackedInline):
	model = TrailerDimensions


class InlineTrailerCategorySpecific(admin.StackedInline):
	model = TrailerCategorySpecific


class InlineTrailerImage(admin.StackedInline):
	model = TrailerImage
	min_num = 1
	extra = 0



@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
	form = TrailerAdminForm
	add_form = TrailerAdminForm
	inlines = (
		InlineTrailerChassis,
		InlineTrailerInterior,
		InlineTrailerExterior,
		InlineTrailerDimensions,
		InlineTrailerCategorySpecific,
		InlineTrailerImage,
	)