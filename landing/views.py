from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponse
app_name='landing'
@login_required(login_url="login/")
def home(request):
	if request.user.is_authenticated():
		 return render(request,"home.html")			
	else:
		return redirect('login/')

def home_logout(request):
	logout(request)
	return render(request,'logout.html')
