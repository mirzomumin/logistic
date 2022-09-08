from django.contrib import admin

from .models import (TrailerCategory,
	TrailerManufacturer)
# Register your models here.

admin.site.register(TrailerCategory)
admin.site.register(TrailerManufacturer)