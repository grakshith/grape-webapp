from __future__ import unicode_literals
import uuid
from django.db import models
from register.models import Person
# Create your models here.
class Event(models.Model):
	def __str__(self):
		return self.name+" "+str(self.id)
	name=models.CharField(max_length=50)
	date=models.DateTimeField()
	attending=models.ManyToManyField(Person)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
