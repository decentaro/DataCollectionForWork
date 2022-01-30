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

from django.core.paginator import Paginator

# Display Errors Page
def errors(request):

	querysetBay0 = InputError.objects.all().filter(bays = 'ELECTRICAL').order_by('-date_posted')
	querysetBay1 = InputError.objects.all().filter(bays = 'BAY1').order_by('-date_posted')
	querysetBay2 = InputError.objects.all().filter(bays = 'BAY2').order_by('-date_posted')
	querysetBay3 = InputError.objects.all().filter(bays = 'BAY3').order_by('-date_posted')
	querysetBay4 = InputError.objects.all().filter(bays = 'BAY4').order_by('-date_posted')
	querysetBay5 = InputError.objects.all().filter(bays = 'BAY5').order_by('-date_posted')



	# ELECTRICAL
	paginator0= Paginator(querysetBay0, 2)
	page0 = request.GET.get('page0')
	queryBay0 = paginator0.get_page(page0)


	# BAY 1
	paginator1= Paginator(querysetBay1, 2)
	page1 = request.GET.get('page1')
	queryBay1 = paginator1.get_page(page1)


	# BAY 2
	paginator2 = Paginator(querysetBay2, 2)
	page2 = request.GET.get('page2')
	queryBay2 = paginator2.get_page(page2)


	# BAY 3
	paginator3 = Paginator(querysetBay3, 2)
	page3 = request.GET.get('page3')
	queryBay3 = paginator3.get_page(page3)


	# BAY 4
	paginator4 = Paginator(querysetBay4, 2)
	page4 = request.GET.get('page4')
	queryBay4 = paginator4.get_page(page4)


	# BAY 5
	paginator5 = Paginator(querysetBay5, 2)
	page5 = request.GET.get('page5')
	queryBay5 = paginator5.get_page(page5)


	
	context = {
		#'querysetBay0': querysetBay0,
		#'querysetBay1': querysetBay1,
		#'querysetBay2': querysetBay2,
		#'querysetBay3': querysetBay3,
		#'querysetBay4': querysetBay4,
		#'querysetBay5': querysetBay5,
		'queryBay0': queryBay0,
		'queryBay1': queryBay1,
		'queryBay2': queryBay2,
		'queryBay3': queryBay3,
		'queryBay4': queryBay4,
		'queryBay5': queryBay5,
	}
	
	if not request.user.is_authenticated:
		return redirect('/tek84Troubleshoot/')
	else:
		return render(request, 'errors.html', context)




