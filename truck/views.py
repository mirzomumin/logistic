from django.shortcuts import render
from truck_utils.models import Country, State, City

# Create your views here.

def load_cities(request):
	state_id = request.GET.get('state')
	cities = City.objects.filter(state__id=state_id).order_by('name')
	return render(request, 'hr/city_dropdown_list_options.html', {'cities': cities})