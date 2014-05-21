from django.db import models

class Contry(models.Model):
	pais = models.CharField(max_length  = 30)

	def __unicode__(self):
		return "%s" % (self.pais)

