from django.db import models
from sorl.thumbnail import ImageField


class Background(models.Model):
	avatar = models.ImageField(upload_to = 'static')
	first_name = models.CharField(max_length = 20) 
	last_name = models.CharField(max_length = 20) 
	summary = models.TextField(blank = True)
	experiencie = models.TextField(blank = True)
	skills = models.TextField(blank=True)

	def __unicode__(self):
		return self.summary