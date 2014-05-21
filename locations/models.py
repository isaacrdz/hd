from django.db import models
from states.models import State
from contries.models import Contry

class Location(models.Model):
	calle = models.CharField(max_length  = 50)
	numero = models.IntegerField(default = 0)
	colonia = models.CharField (max_length = 50)
	codigoPostal = models.IntegerField(default = 0)
	estado = models.ForeignKey(State)
	pais = models.ForeignKey(Contry) 

	def __unicode__(self):
		
		  return "%s  %s  %s " % (self.calle,self.numero, self.colonia)