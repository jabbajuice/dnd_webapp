from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
	username = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
	password1 = forms.CharField(required=True, widget=forms.PasswordInput())
	password2 = forms.CharField(required=True, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')



class AuthForm(AuthenticationForm):
	username = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
	password = forms.CharField(required=True, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','password')



class UserProfileForm(forms.ModelForm):
	email = forms.EmailField(required=True, widget=forms.EmailInput)
	username = forms.CharField(required=True, widget =forms.widgets.TextInput)
	telephone = forms.CharField(max_length=255, required=False, widget=forms.TextInput())
	

	class Meta:
		model = UserProfile
		fields = ('email','username','telephone')


class UserAlterationForm(forms.ModelForm):
	first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
	last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
	email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')