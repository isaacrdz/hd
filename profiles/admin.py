from django.contrib import admin
from .models import Background
from sorl.thumbnail import get_thumbnail

class BackgroundAdmin(admin.ModelAdmin):
	list_display = ('avatar_imagen', 'first_name','summary')

	def avatar_imagen(self,obj):
		return '<img src="%s">' % get_thumbnail(obj.avatar, '100x200', format='PNG').url
	avatar_imagen.allow_tags = True




admin.site.register(Background,BackgroundAdmin)