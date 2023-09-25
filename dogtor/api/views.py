from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view


# modelos
from vet.models import PetOwner, Pet

# Serializers
from .serializers import OwnersSerializers

# Create your views here.
from .serializers import (
                        PetsSerializer, 
                        OwnersListSerializer,
                        OwnersDetailSerializer,
                        OwnersSerializers, 
                        OwnersCreateSerializer,
                        OwnersUpdateSerializer,
                        OwnersDeleteSerializer,
                        OwnersListCreateView,
                        OwnersRetrieveUpdateDestroyAPIView  )

# list --> GET
#RETRIEVE --> GET
# UPDATE --> PUT
# CREATE --> POST
# DELETE --> DELETE

# TODOS LOS ENDPOINTS DE PETS
# TODOS LOS ENDPOINTS DE PETDATES

class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner."""
    
    
    # 1 qury que se va a reakizar
    
    # obtener todos los owner --> PetOwner.all
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers
    
class PetsViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo Pet."""

    queryset = Pet.objects.all()
    serializer_class = PetsSerializer
    
    
class ListOwnersAPIView(generics.ListAPIView):
    """Lisr Ownes Api View"""
    
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer
    
    
    
class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    """Detail Pet Owner Api View."""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer    
    
class CreateOwnersAPIView(generics.CreateAPIView):
    
    queryset = PetOwner.objects.all()
    serializer_class = OwnersCreateSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    
    
    queryset = PetOwner.objects.all()
    serializer_class = OwnersUpdateSerializer    
        
    
class DeleteOwnersAPIView(generics.DestroyAPIView):
    

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDeleteSerializer
    

class OwnersListCreateView(generics.CreateAPIView):
    queryset =PetOwner.objects.all()
    serializer_class = OwnersListCreateView


class OwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersRetrieveUpdateDestroyAPIView