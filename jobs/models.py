from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from contries.models import Contry
from states.models import State
from areas.models import Area


# Create your models here.

class Job(models.Model):
	empleo = models.CharField(max_length = 50)
	area = models.ForeignKey(Area)
	puntos = models.IntegerField(default = 0, blank=True)
	descripcion = models.TextField()
	calle = models.CharField(max_length  = 50)
	numero = models.IntegerField(default = 0)
	colonia = models.CharField (max_length = 50)
	ciudad = models.CharField(max_length=50)
	estado = models.ForeignKey(State)
	pais = models.ForeignKey(Contry)
	codigoPostal = models.IntegerField(default = 0)
	web = models.URLField()
	timestamp = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User)	
	image = models.ImageField(upload_to = 'static', null=True, )

	def __unicode__(self):
		return  self.empleo