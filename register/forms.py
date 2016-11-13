from  django import forms
from .models import Person
class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','email','roll_no','profession', 'college','image']
        
#    latitude = forms.CharField(label="Latitude", min_length=3)
#    longitude = forms.CharField(label="Longitude", min_length=3)
#    UID = forms.IntegerField()
