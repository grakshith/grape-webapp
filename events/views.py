from django.shortcuts import render,redirect
from django.core import serializers
# Create your views here.
from django.http import HttpResponse,JsonResponse
#from .forms import PersonForm
from .models import Event
from register import views
app_name='events'
def home(request):
	return HttpResponse("<center><h1>You successfully landed on the events page</h1></center>")

def signup(request,urlhash):
	e=Event.objects.get(id=urlhash)

	user=views.signup(request)
	json=e.attending.all()
	#print json
	ser=serializers.serialize('json',json,fields=('name','profession', 'college', 'email'))
	e.attending.add(user)
	#print str(ser)
	return JsonResponse({"results":ser},safe=False)
