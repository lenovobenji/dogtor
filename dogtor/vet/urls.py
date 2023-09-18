# 1. path
# 2. urlpatterns

from django.urls import path

# Views
# PascalCase -> clases -> modelos o vistas clase
# snake_case -> para todo lo demas
from .views import list_pet_owners, Test, OwnersList, OwnerDetail, PetsList, PetsDetail, OwnerCreate, OwnerUpdate

# alias (reversed urls) -> rutas de una app en especifico
# alias (reversed urls) -> rutas del proyecto

# si no tienes include -> reversed url se pone como 3er parametro ejemplo -> name="owners_list"
# si SI tienes include -> reversed url se pone como 2do parametro DENTRO del include() -> include(("vet.urls", "vet"))

# SINTAXIS de como acceder
# "vet:owners_list"
# "vet:owners_detail"
# "reversed_url_app: reversed_url_singular"
urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDetail.as_view(), name="owners_detail"),
    
    path("owners/add/", OwnerCreate.as_view(), name="owners_Create"),
    path("owners/<int:pk>/edit/", OwnerUpdate.as_view(), name="owners_edit"),
    
    path("pets/", PetsList.as_view(), name="Pets_list"),
    path("pets/<int:pk>/", PetsDetail.as_view(), name="Pets_datail"),
    
    #path("pets/add/", PetsCreate.as_view(), name="Pets_Create"),
    #path("pets/<int:pk>/", PetsUpdate.as_view(), name="Pets_edit"), 
    
    path("test/", Test.as_view()),
]