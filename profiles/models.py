from django.db import models

class Background(models.Model):
	first_name = models.CharField(max_length = 20) 
	last_name = models.CharField(max_length = 20) 
	summary = models.TextField(blank = True)
	experiencie = models.TextField(blank = True)

	def __unicode__(self):
		return self.summary