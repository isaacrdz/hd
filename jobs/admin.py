from django.contrib import admin
from .models import Job
from sorl.thumbnail import get_thumbnail

class JobAdmin(admin.ModelAdmin):
	list_display = ('empleo','imagen_album')

	def imagen_album(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.image, '100x200', format='PNG').url # , crop='center'
	imagen_album.allow_tags = True 






admin.site.register(Job, JobAdmin)



# Register your models here.
