from django.db import models

# Create your models here.
class Area(models.Model):
	nombre = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.nombre
