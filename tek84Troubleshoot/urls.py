from django.urls import path
from . import views



# URLConf
urlpatterns = [
	path('index/', views.index, name='index'),
	path('errors/', views.errors, name='errors'),
	path('', views.EmployeeLogin.as_view
		(template_name='registration/login.html'), name='login'),
	path('accounts/logout/', views.EmployeeLogout.as_view
		(template_name='registration/logout.html'), name='logout'),
	path('accounts/password_change/', views.EmployeePasswordChange.as_view
		(template_name='registration/password_change_form.html'), name='password_change'),
	path('accounts/password_change/done/', views.EmployeePasswordChangeDone.as_view
		(template_name='registration/password_change_done.html'), name='password_change_done'),
	path('accounts/signup/', views.sign_up, name='signup'),
	path('search_results/', views.SearchResultsView.as_view(), name='search_results'),


# Needs to work on these paths

	path('accounts/password_reset/', views.EmployeePasswordReset.as_view
		(template_name='registration/password_reset_form.html'), name='password_reset'),

	path('accounts/password_reset/done/', views.EmployeePasswordResetDone.as_view
		(template_name='registration/password_reset_done.html'), name='password_reset_done'),

	path('accounts/password_reset_confirm/', views.EmployeePasswordConfirm.as_view
		(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

	path('accounts/password_reset_complete/', views.EmployeePasswordComplete.as_view
		(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),





	


	
# Password Reset Tutorial
# https://learndjango.com/tutorials/django-password-reset-tutorial


# Django Mailer
# https://pypi.org/project/django-mailer/


]