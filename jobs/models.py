from django.db import models
from django.contrib.auth.models import User
from contries.models import Contry
from states.models import State
from locations.models import Location
from areas.models import Area
from sorl.thumbnail import ImageField


# Create your models here.

class Job(models.Model):
	empleo = models.CharField(max_length = 50)
	area = models.ForeignKey(Area)
	puntos = models.IntegerField(default = 0)
	enlace = models.URLField()
	direccion = models.ForeignKey(Location)
	estado = models.ForeignKey(State)
	pais = models.ForeignKey(Contry)
	descripcion = models.TextField()
	image = models.ImageField(upload_to = 'static')
	usuario = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return  self.empleo