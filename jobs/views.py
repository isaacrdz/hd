from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.template.context import RequestContext
from forms import *
from jobs.models import Job
from models import *


def enter(request):
    return render(request, 'login.html')

def get_facebook_id(user):
    if user.social_auth.filter(provider='facebook').exists():
        return user.social_auth.first().uid
    return None


@login_required
def home(request):
    setattr(request.user, 'facebook_id', get_facebook_id(request.user))
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)


def log_out(request):
   return redirect('enter')






def welcome(request):
	template  ='welcome.html'
	return render(request, template)

def timeline (request):
	jobs = Job.objects.order_by("-timestamp").all()
	template = 'timeline.html'
	return render(request, template,{"jobs":jobs,})


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
	        form = PostForm(request.POST, request.FILES)
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


def enter(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'index.html', {'username': request.user.username})


def log_out(request):
    logout(request)
    return redirect('enter')