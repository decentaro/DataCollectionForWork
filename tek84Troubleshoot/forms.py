from django.forms import ModelForm
from .models import InputError

from django import forms




class InputErrorForm(ModelForm):

	class Meta:
		model = InputError
		fields = '__all__'     # Includes all field in InputError model
		

		