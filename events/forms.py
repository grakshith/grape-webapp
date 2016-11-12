from  django import forms
from .models import Event
class DateInput(forms.DateTimeInput):
    input_type = 'date'
class TimeInput(forms.DateTimeInput):
    input_type = 'time'
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['name','date','attending','image']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),
        }
        
