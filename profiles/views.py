from django.shortcuts import render,get_object_or_404
from profiles.models import Background
from locations.models import Location
from jobs.models import Job

# Create your views here.
def profile(request, first_name):
	backgrounds = get_object_or_404(Background, first_name= first_name)
	location = Location.objects.all() 
	template = "profiles.html"
	return render(request,template, {"backgrounds":backgrounds,"request":request} ) 

def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, pk = id_categoria)
    #cat = Categoria.objects.get(pk = id_categoria)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render(request, template,locals())
