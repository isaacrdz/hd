from jobs.models import Job
from django.shortcuts import render,get_object_or_404
from models import *
from jobs.models import Job
from locations.models import Location
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from forms import *






def timeline (request):
	jobs = Job.objects.order_by("-timestamp").all()
	locations = Location.objects.all()
	template = 'timeline.html'
	return render(request, template,{"jobs":jobs, "locations": locations})


def empresa (request, usuario):
	empresas = User.objects.all()
	emp = get_object_or_404(User, username = usuario)
	jobs = Job.objects.filter(usuario = emp)
	template = "empleos.html"
	return render(request,template,locals())


def add(request):
	# if this is a POST request we need to process the form data
	    if request.method == 'POST':
	        # create a form instance and populate it with data from the request:
	        form = PostForm(request.POST)
	        # check whether it's valid:
	        if form.is_valid():
	        	job = form.save(commit = False)
           		job.usuario = request.user
	            # process the data in form.cleaned_data as required
	        	form.save()
	            # redirect to a new URL:
	        return HttpResponseRedirect('/timeline')

	    # if a GET (or any other method) we'll create a blank form
	    else:
	        form = PostForm()
		 

	    return render(request, "form.html", (locals()))