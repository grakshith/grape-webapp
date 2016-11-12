from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^/$',views.home,name='home'),
    url(r'^/register/$',views.register,name='register'),
    url(r'^/(?P<urlhash>.*)/QR$',views.view_QR,name='view_QR'),
    url(r'^/(?P<urlhash>.*)/view$',views.view_attendees,name='view_attendees'),
    url(r'^/(?P<urlhash>.*)/details$',views.view_details,name='view_details'),
    #url(r'^/(?P<urlhash>.*)/$',views.view_QR,name='view_QR'),
    url(r'^/(?P<urlhash>.*)/',views.signup,name='signup'),
]
