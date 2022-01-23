from django.forms import ModelForm, Textarea,TextInput, Select, PasswordInput, EmailField
from .models import InputError, Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class InputErrorForm(ModelForm):
	
	class Meta:
		model = InputError
		fields = '__all__'
		exclude = ["employee"]   # this is vital in displaying the name of reported by in errors page.




# Sample code to resize textarea
		widgets = {
			'bays': Select(attrs={'class':'form-select form-select-sm mt-2'}),
			'general_description_of_failure': Select(attrs={'class':'form-select form-select-sm mt-2'}),
			'title_of_error': TextInput(attrs={'class': 'form-control form-control-sm mt-2'}),
			'fix_of_error': Textarea(attrs={'class': 'form-control mt-2'}),
		}


class EmployeeForm(UserCreationForm):

# Compare to the form at the top, these are declared in here like this so that the REQUIRED_FIELDS will work.


	username = forms.CharField(label="Username",
    	widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mt-2'})
    )

	email = forms.EmailField(label="Email address",
    	widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mt-2'})
    )

	last_name = forms.CharField(label="Last Name",
    	widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mt-2'})
    )

	first_name = forms.CharField(label="First Name",
    	widget=forms.TextInput(attrs={'class': 'form-control form-control-sm mt-2'})
    )
	
	password1 = forms.CharField(label="Password",
    	widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm mt-2', 'type': 'password'})
    )

	password2 = forms.CharField(label=" Confirm Password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm mt-2', 'type':'password'}),
    )


	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

		REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

		


