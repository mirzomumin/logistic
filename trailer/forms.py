from django import forms

from .models import Trailer
from truck_utils.models import Country, State, City


class TrailerAdminForm(forms.ModelForm):
	class Meta:
		model = Trailer
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['city'].queryset = City.objects.none()

		if 'state' in self.data:
			try:
				state_id = int(self.data.get('state'))
				self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
				print(self.fields['city'].queryset.count())
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['city'].queryset = self.instance.state.cities.order_by('name')