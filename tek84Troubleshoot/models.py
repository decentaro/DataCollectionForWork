from django.db import models
from django.utils import timezone

from django import forms

# Create your models here.


class InputError(models.Model):

	ELECTRICAL = 'Electrical'
	BAY1 = 'B1'
	BAY2 = 'B2'
	BAY3 = 'B3'
	BAY4 = 'B4'
	BAY5 = 'B5'

	BAYS = [
		('ELECTRICAL', 'Electrical'),
		('BAY1', 'Bay1'),
		('BAY2', 'Bay2'),
		('BAY3', 'Bay3'),
		('BAY4', 'Bay4'),
		('BAY5', 'Bay5'),
	]


	AC = 'AC'
	CPU = 'CPU'
	BASES = 'BS'
	VERTICALS = 'VR'
	CARM = 'CA'
	ATP = 'AP'
	SKINS = 'SK'
	TOPHAT = 'TP'

	GENERAL_DESCRIPTION_OF_FAILURE = [
		('AC', 'AC'),
		('CPU', 'CPU'),
		('BASES', 'Bases'),
		('VERTICALS', 'Vertical'),
		('CARM', 'C-Arm'),
		('ATP', 'ATP'),
		('SKINS', 'Skins'),
		('TOPHAT', 'Top Hat')
	]

	bays = models.CharField(max_length=10, choices=BAYS, default=BAY1)
	general_description_of_failure = models.CharField(max_length=9, 
												   choices=GENERAL_DESCRIPTION_OF_FAILURE, 
												   default=BASES)
	title_of_error = models.CharField(max_length=100)
	fix_of_error = models.TextField()
	date_posted = models.DateTimeField(auto_now = True)

