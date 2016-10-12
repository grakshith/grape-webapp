from django.conf.urls import url,include
from django.contrib import admin
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^login/',login,{'template_name':'login.html','authentication_form': LoginForm},name='login'),
    url(r'^logout/',views.home_logout,name='logout')
]
