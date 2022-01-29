from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from .forms import InputErrorForm, EmployeeForm
from .models import InputError, Employee
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from django.contrib.auth.models import User


from django.db.models import Q   # SEARCH BAR




# Sign Up Page
def sign_up(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			messages.success(request, 'User account was created successfully!')
			login(request, user)
			return redirect('/tek84Troubleshoot/')
	else:
		form = EmployeeForm()
	return render(request, 'registration/signup.html', {'form': form})



# Login Page
class EmployeeLogin(LoginView):
	template_name = 'registration/login.html'



# Logout Page
class EmployeeLogout(LogoutView):
	template_name = 'registration/logout.html'



# Password Change Page
class EmployeePasswordChange(PasswordChangeView):
	template_name = 'accounts/password_change_form.html'




# Password Change Done Page
class EmployeePasswordChangeDone(PasswordChangeDoneView):
	template_name = 'registration/password_change_done.html'



# Password Reset Page
class EmployeePasswordReset(PasswordResetView):
	template_name = 'accounts/password_reset_form.html'



# Password Reset Done Page
class EmployeePasswordResetDone(PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'



# Password Reset Confirm Page
class EmployeePasswordConfirm(PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'



# Password Reset Complete Page
class EmployeePasswordComplete(PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'



# Search Results Page
class SearchResultsView(ListView):
	model = InputError
	template_name = 'search_results.html'
	

	def get_queryset(self):
		query = self.request.GET.get('q') # q --> id name of the search input
		object_list = InputError.objects.filter(Q(title_of_error__contains=query)) 
		return object_list



# Input Error Page
def index(request):
	form = InputErrorForm()

	if not request.user.is_authenticated:
		return redirect('/tek84Troubleshoot/')
	else:
		if request.method == 'POST':
			form = InputErrorForm(request.POST) # this is vital in displaying the name of reported by in errors page.
			if form.is_valid():
				instance = form.save(commit=False)
				instance.employee = request.user
				instance.save()
				messages.success(request, 'Success!')
				return redirect('/tek84Troubleshoot/errors')
			else:
				messages.error(request, 'Error!')
				return redirect('/tek84Troubleshoot/index')

	context = {'form':form}
	return render(request, 'index.html', context)




# Display Errors Page
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
	
	if not request.user.is_authenticated:
		return redirect('/tek84Troubleshoot/')
	else:
		return render(request, 'errors.html', context)




