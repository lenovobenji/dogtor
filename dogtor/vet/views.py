from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy


# Models
from vet.models import PetOwner, Pet, PetDate
# forms
from .forms import OwnerForm
from django.db.models import ProtectedError


# Create your views here.
def list_pet_owners(request):
    # por defecto -> metodo GET
    print("REQUEST --->", request.__dict__)

    """List owners."""

    # Agarrar informacion de nuestra bd
    owners = PetOwner.objects.all()

    # Hacemos el contexto
    context = {"owners": owners}

    # Agarrar template
    template = loader.get_template("vet/owners/list.html")

    # Retornar respuesta HTTP con el template pasandole el contexto y el request
    return HttpResponse(template.render(context, request))


# CRUD


# Ctrl + /
# Cmd + /
class OwnersList(TemplateView):
    # Renderizame este template
    template_name = "vet/owners/list.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["owners"] = PetOwner.objects.all()
        return context


class PetsList(TemplateView):
    # Renderizame este template
    template_name = "vet/pets/list.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'
        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["pets"] = Pet.objects.all()
        return context


class PetsDetail(TemplateView):
    # Renderizame este template
    template_name = "vet/pets/detail.html"

    # Que este template va a tener cierto 'contexto'
    def get_context_data(self, **kwargs):
        # Agarrar el contexto que ya creo 'TemplateView'

        context = super().get_context_data(**kwargs)

        # Le agregamos nuestro custom context
        context["pet"] = Pet.objects.get(pk=kwargs["pk"])
        return context


class OwnersList(ListView):
    """Render all Pet Owners."""

    # 1. Modelo que estamos manipulando
    # 2. Template con el que vamos renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner  # 1
    template_name = "vet/owners/list.html"  # 2
    context_object_name = "owners"  # 3


class OwnerDetail(LoginRequiredMixin,DetailView):
    """Render a specific Pet Owner with their pk."""

    # 1. Modelo
    # 2. Template a renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class PetsList(ListView):
    """Render all Pet Owners."""

    # 1. Modelo que estamos manipulando
    # 2. Template con el que vamos renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner  # 1
    template_name = "vet/pest/list.html"  # 2
    context_object_name = "pets"  # 3


class PetsDetail(DetailView):
    """Render a specific Pet Owner with their pk."""

    # 1. Modelo
    # 2. Template a renderizar
    # 3. El contexto que va a tener ese template
    model = PetOwner
    template_name = "vet/pets/detail.html"
    context_object_name = "pets"
class OwnerCreate(CreateView):
    """View used to create a PeaOwners"""
     # modelo
     # template a renderizar
     # 3. el formulario con el qye se va a crear
     # 4 la urls si la requiere fue exitosa ->
     
    model =PetOwner # 1
    template_name ="vet/owners/create.html"
    form_class = OwnerForm #3
     
     # Url donde se va a rediricional si fue 
     
    success_url = reverse_lazy("vet:owners_list")
    
    
class OwnerUpdate(PermissionRequiredMixin,UpdateView):  
    # modelo
     # template a renderizar
     # 3. el formulario con el qye se va a crear
     # 4 la urls si la requiere fue exitosa ->
    permission_required = "vet.change_petowner" #app.how is it named on admin in the group section on permission assigned, just the user with this permission can access to this view
    raise_exception = True  # Raise exception when you do not have permission
    login_url = "/admin/login"
    redirect_field_name = "next"
    
    model =PetOwner
    template_name = "vet/owners/Update.html"
    form_class = OwnerForm
    
    # Url donde se va a rediricional si fue
    success_url = reverse_lazy("vet:owners_list")  
     

          





class Test(View):
    # Como funcion el metodo(GET,PATCH,POST,DELETE,PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")