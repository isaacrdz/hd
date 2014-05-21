from django.db import models

class State(models.Model):
	estado = models.CharField(max_length  = 30)

	def __unicode__(self):
		return "%s" % (self.estado)

