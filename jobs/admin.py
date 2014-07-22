from django.contrib import admin
from models import *
from sorl.thumbnail import get_thumbnail

class JobAdmin(admin.ModelAdmin):
	list_display = ('empleo','imagen_album')

	def imagen_album(self, obj):
		return '<img src="%s">' % get_thumbnail(obj.image, '100x200', format='PNG').url # , crop='center'
	imagen_album.allow_tags = True 






admin.site.register(Job, JobAdmin)
admin.site.register(Location)
admin.site.register(Contry)
admin.site.register(State)



# Register your models here.
