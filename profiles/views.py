from django.shortcuts import render,get_object_or_404
from profiles.models import Background
from locations.models import Location

# Create your views here.
def profile(request, first_name):

	backgrounds = get_object_or_404(Background, first_name= first_name)
	location = Location.objects.all() 
	template = "profiles.html"
	return render(request,template, {"backgrounds":backgrounds, "request":request} ) 

	
