from django import forms

class loginform(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

class registerform(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()
	password2 = forms.CharField()