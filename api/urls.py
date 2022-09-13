from django.urls import path

from . import views
from . import extra_views


urlpatterns = [
	# Truck urls
	path('trucks/', views.TruckListView.as_view(), name='trucks'),
	path('trucks/<int:pk>/', views.TruckDetailView.as_view(), name='truck'),

	# Trailer urls
	path('trailers/', views.TrailerListView.as_view(), name='trailers'),
	path('trailers/<int:pk>/', views.TrailerDetailView.as_view(), name='trailer'),

	# Truck and Trailer filter urls
	path('truck-filter-options/', views.get_truck_filter_options, name='truck-filter-options'),
	path('trailer-filter-options/', views.get_trailer_filter_options, name='trailer-filter-options'),

	# Truck Mail and Offer urls
	path('create-truck-email/', extra_views.create_truck_email, name='create_truck_email'),
	path('create-truck-friend-email/', extra_views.create_truck_friend_email, name='create_truck_friend_email'),
	path('create-truck-offer/', extra_views.create_truck_offer, name='create_truck_offer'),

	# Trailer Mail and Offer urls
	path('create-trailer-email/', extra_views.create_trailer_email, name='create_trailer_email'),
	path('create-trailer-offer/', extra_views.create_trailer_offer, name='create_trailer_offer'),
	path('create-trailer-friend-email/', extra_views.create_trailer_friend_email, name='create_trailer_friend_email'),

	# Common mail url
	path('create-friend-email/', extra_views.create_friend_email, name='create_friend_email'),

	# Video Chat Mail url
	path('create-truck-video-chat-email/', extra_views.create_truck_video_chat_email, name='create_truck_video_chat_email'),
	path('create-trailer-video-chat-email/', extra_views.create_trailer_video_chat_email, name='create_trailer_vidoe_chat_email'),

	# Simple Form
	path('simple-form/', extra_views.create_simple_form, name='simple_form'),

	# PDF downloading
	path('pdf/Pagesfromsandhillsmag.pdf', extra_views.fetch_report_about_company, name='pdf_about'),
	path('pdf/Company_Credit_Application.pdf', extra_views.fetch_report_company_creadit_app, name='pdf_company'),
	path('pdf/Personal_Credit_Application.pdf', extra_views.fetch_report_personal_credit_app, name='pdf_personal'),
]