from django.shortcuts import render,get_object_or_404
from jobs.models import Job
from .models import Area

# Create your views here.




def area(request,id_area):
	areas = Area.objects.all()
	ar = get_object_or_404(Area, pk = id_area)
	jobs = Job.objects.filter(area = ar)
	template = "empleos.html"
	return render(request,template,locals())