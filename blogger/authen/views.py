from django.shortcuts import render
from .forms import loginform, registerform

# Create your views here.
def login(request):
	form = loginform(request.POST or None)
	context = {'form':form}
	return render(request, 'authen/form.html', context)

def register(request):
	form = registerform(request.POST or None)
	context = {'form':form}
	return render(request, 'authen/form.html', context)

def logout(request):
	return