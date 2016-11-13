from django.shortcuts import render,redirect
from django.core import serializers
# Create your views here.
from django.http import HttpResponse,JsonResponse
#from .forms import PersonForm
from .models import Event
from .forms import EventForm
from register import views
from django.views.decorators.csrf import csrf_exempt
app_name='events'
def home(request):
	evnts=Event.objects.all()

	return render(request,'events.html',{'querydict':evnts})

def register(request):
	if request.method =='GET':
		form=EventForm()
		return render(request,'event_reg.html',{'form':form})
	elif request.method == 'POST':
		form=EventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request,'event_reg.html',{'form':form})

@csrf_exempt
def signup(request,urlhash):
	e=Event.objects.get(id=urlhash)
	user=views.signup(request)
	#json=e.attending.all()
	#print json
	#ser=serializers.serialize('json',json,fields=('name','profession', 'college', 'email'))
	e.attending.add(user)
	#print str(ser)
	return JsonResponse({"results":"Success"},safe=False)
	
def view_attendees(request,urlhash):
	e=Event.objects.get(id=urlhash)
	json=e.attending.all()
	#print json
	ser=serializers.serialize('json',json,fields=('name','profession', 'college', 'email'))
	return HttpResponse(str({"results":str(ser)}))

def view_QR(request,urlhash):
	evnt=str(Event.objects.get(id=urlhash))
	string="http://grape-webapp.azurewebsites.net/events/"+urlhash+"/"
	return render(request,'QR.html',{'URL':string,'Event':evnt,'urlhash':urlhash})
	
def view_details(request,urlhash):
	e=Event.objects.get(id=urlhash)
	json=e.attending.all()
	count=len(json)
	return render(request,'event_details.html',{'Count':count,'Event':e,'Attending':json})
