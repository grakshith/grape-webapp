from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,JsonResponse
from .forms import PersonForm
from .models import Person
app_name='register'
def home(request):
	return HttpResponse("<center><h1>You successfully landed on the registration page</h1></center>")

def signup(request):
	if 'name' and 'email' in request.GET:
		form=PersonForm(request.GET)
		if form.is_valid():
			user=form.save()
		else:

			li=[]
			for items in request.GET:
				li.append(request.GET[items])
			return HttpResponse("<center><h1> Form not validated </h1></center>\n"+str(li)+str(form))
		
		return user
	elif request.method== 'POST' :
		form=PersonForm(request.POST)
		if form.is_valid():
			user=form.save()
		else:
			return render(request,'person_reg.html',{'form':form})	
	else:
		form=PersonForm()
		return render(request,'person_reg.html',{'form':form})