from django.shortcuts import render,get_object_or_404
from profiles.models import Background
from jobs.models import Job

# Create your views here.
def profile(request, first_name):
	backgrounds = get_object_or_404(Background, first_name= first_name)
	template = "profiles.html"
	return render(request,template, {"backgrounds":backgrounds,"request":request} ) 

