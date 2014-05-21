from jobs.models import Job
from django.shortcuts import render
from models import *
from jobs.models import Job
from locations.models import Location



def home (request):
	jobs = Job.objects.order_by("-timestamp").all()
	locations = Location.objects.all()
	template = 'empleos.html'
	return render(request, template,{"jobs":jobs, "locations": locations})


