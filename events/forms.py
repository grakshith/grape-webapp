from  django import forms
from .models import Event
from django.contrib.admin import widgets as wdgt
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','date','attending','image']
        widgets = {
            'date': wdgt.AdminSplitDateTime()
        }
        
        
