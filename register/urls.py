from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.signup, name='home'),
    url(r'^',views.signup,name='signup'),
]