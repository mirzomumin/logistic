from django.urls import path

from . import views
from . import extra_views


urlpatterns = [
	# path('trucks/?ordering=&country=&state=&city=', views.TruckListView.as_view(), name='trucks'),
	path('trucks/', views.TruckListView.as_view(), name='trucks'),
	path('trucks/<int:pk>/', views.TruckDetailView.as_view(), name='truck'),
	path('trailers/', views.TrailerListView.as_view(), name='trailers'),
	path('trailers/<int:pk>/', views.TrailerDetailView.as_view(), name='trailer'),
	path('truck-filter-options/', views.get_truck_filter_options, name='truck-filter-options'),
	path('trailer-filter-options/', views.get_trailer_filter_options, name='trailer-filter-options'),
	path('create-email/', extra_views.create_email, name='create-email'),
]