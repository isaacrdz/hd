from django.contrib import admin
from .models import Background
# Register your models here.

class BackgroundAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','summary','experiencie')



admin.site.register(Background,BackgroundAdmin)