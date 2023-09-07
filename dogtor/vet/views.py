from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.

# Models
from vet.models import PetOwner

def list_pet_owners(request):
    """lis"""
    owners = PetOwner.objects.all() 
    
    context = {"owners": owners}
    
    
    template = loader.get_template("vet/owners/list.html")
    
    
    return HttpResponse(template.render(context, request))


class OwnersList (TemplateView):
      # Renderizane esta clasee
    
    template_name = "vet/owners/list.html"
      # Que este template va a tener cierto 'contexto'
    
    def get_context_data(self, **kwargs):
         
        context = super().get_context_data(**kwargs)
         
        context["owners"] = PetOwner.objects.all()
         
        return context          

class Test(View):
    # como funcion el metodo de (get,pats, post, delate)
    
    def get(self, request):
        return HttpResponse("Hello word from a class generation view")
    
    
    