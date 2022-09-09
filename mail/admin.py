from django.contrib import admin

from .models import (TruckMail,
	TruckFriendMail,
	TruckOffer,
	TrailerMail,
	TrailerOffer,
	TrailerFriendMail,
	FriendMail,
	TruckVideoMail,
	TrailerVideoMail)
# Register your models here.

admin.site.register(TruckMail)
admin.site.register(TruckFriendMail)
admin.site.register(TruckOffer)
admin.site.register(TrailerMail)
admin.site.register(TrailerOffer)
admin.site.register(TrailerFriendMail)
admin.site.register(FriendMail)
admin.site.register(TruckVideoMail)
admin.site.register(TrailerVideoMail)