from django.forms import ModelForm, Textarea
from .models import InputError

from django import forms




class InputErrorForm(ModelForm):

	class Meta:
		model = InputError
		fields = '__all__'     # Includes all field in InputError model
		

# Sample code to resize textarea
#		widgets = {
#			'fix_of_error': Textarea(attrs={'cols': 40, 'rows': 20})
#		}

