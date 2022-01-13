from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import InputErrorForm
from .models import InputError


from django.contrib import messages


# Create your views here.
# request -> response
# request handler
# action


def index(request):
	form = InputErrorForm()
	
	

	if request.method == 'POST':
		form = InputErrorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Success!')
			return HttpResponseRedirect('/tek84Troubleshoot/errors')
		else:
			messages.error(request, 'Error!')
			return HttpResponseRedirect('')

	
    
	context = {'form':form}
	return render(request, 'index.html', context)

	


def errors(request):

	querysetBay0 = InputError.objects.all().filter(bays = 'ELECTRICAL').order_by('-date_posted')
	querysetBay1 = InputError.objects.all().filter(bays = 'BAY1').order_by('-date_posted')
	querysetBay2 = InputError.objects.all().filter(bays = 'BAY2').order_by('-date_posted')
	querysetBay3 = InputError.objects.all().filter(bays = 'BAY3').order_by('-date_posted')
	querysetBay4 = InputError.objects.all().filter(bays = 'BAY4').order_by('-date_posted')
	querysetBay5 = InputError.objects.all().filter(bays = 'BAY5').order_by('-date_posted')

	context = {
		'querysetBay0': querysetBay0,
		'querysetBay1': querysetBay1,
		'querysetBay2': querysetBay2,
		'querysetBay3': querysetBay3,
		'querysetBay4': querysetBay4,
		'querysetBay5': querysetBay5,
	}
	

	return render(request, 'errors.html', context)


