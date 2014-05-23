from jobs.models import Job
from django.shortcuts import render,get_object_or_404
from models import *
from jobs.models import Job
from locations.models import Location
from django.contrib.auth.models import User



def home (request):
	jobs = Job.objects.order_by("-timestamp").all()
	locations = Location.objects.all()
	template = 'empleos.html'
	return render(request, template,{"jobs":jobs, "locations": locations})


def empresa (request, usuario):
	empresas = User.objects.all()
	emp = get_object_or_404(User, username = usuario)
	jobs = Job.objects.filter(usuario = emp)
	template = "empleos.html"
	return render(request,template,locals())


