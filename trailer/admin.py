from django.contrib import admin

from .models import (
	Trailer,
	TrailerDimensions,
	TrailerCategorySpecific,
	TrailerChassis,
	TrailerInterior,
	TrailerExterior,
	TrailerImage)
# Register your models here.

admin.site.register(Trailer)
admin.site.register(TrailerDimensions)
admin.site.register(TrailerCategorySpecific)
admin.site.register(TrailerChassis)
admin.site.register(TrailerInterior)
admin.site.register(TrailerExterior)
admin.site.register(TrailerImage)