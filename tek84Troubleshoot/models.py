from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	position = models.CharField(max_length=100)



class InputError(models.Model):

	BAYS = [
		('ELECTRICAL', 'Electrical'),
		('BAY1', 'Bay1'),
		('BAY2', 'Bay2'),
		('BAY3', 'Bay3'),
		('BAY4', 'Bay4'),
		('BAY5', 'Bay5'),
	]


	GENERAL_DESCRIPTION_OF_FAILURE = [
		('AC', 'AC'),
		('CPU', 'CPU'),
		('KIOSK', 'KIOSK'),
		('BASES', 'Bases'),
		('VERTICALS', 'Vertical'),
		('CARM', 'C-Arm'),
		('ATP', 'ATP'),
		('SKINS', 'Skins'),
		('TOPHAT', 'Top Hat')
	]

	
	bays = models.CharField(max_length=10, choices=BAYS)
	general_description_of_failure = models.CharField(max_length=9, 
												   choices=GENERAL_DESCRIPTION_OF_FAILURE)
	title_of_error = models.CharField(max_length=100)
	fix_of_error = models.TextField()
	date_posted = models.DateTimeField(auto_now = True)
	employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



