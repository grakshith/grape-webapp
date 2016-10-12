from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^/(?P<urlhash>.*)/view',views.view_attendees,name='view_attendees'),
    url(r'^/(?P<urlhash>.*)/',views.signup,name='signup'),
]
