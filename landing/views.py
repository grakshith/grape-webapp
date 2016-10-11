from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
app_name='landing'
def home(request):
	return HttpResponse("<center><h1>You successfully landed on the landing page</h1></center>");