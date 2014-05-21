from django.db import models
from django.contrib.auth.models import User
from contries.models import Contry
from states.models import State
from locations.models import Location

# Create your models here.

class Job(models.Model):
	empleo = models.CharField(max_length = 50)
	puntos = models.IntegerField(default = 0)
	enlace = models.URLField()
	direccion = models.ForeignKey(Location)
	estado = models.ForeignKey(State)
	pais = models.ForeignKey(Contry)
	descripcion = models.CharField(max_length = 150)
	avatar = models.ImageField(upload_to = 'jobs')
	usuario = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.empleo